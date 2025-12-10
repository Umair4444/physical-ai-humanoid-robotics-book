import React, { useState, useEffect } from 'react';
import styles from './Chatbot.module.css'; // Assuming a CSS module for styling

interface ChatMessage {
  id: number;
  sender: 'user' | 'bot';
  text: string;
  source?: {
    chapter: string;
    url: string;
  };
}

const Chatbot: React.FC = () => {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(false);
  const [isTextSelectionMode, setIsTextSelectionMode] = useState<boolean>(false);
  const [selectedText, setSelectedText] = useState<string>('');

  useEffect(() => {
    const handleSelectionChange = () => {
      if (isTextSelectionMode) {
        const selection = window.getSelection();
        if (selection && selection.toString().length > 0) {
          setSelectedText(selection.toString());
        } else {
          setSelectedText('');
        }
      }
    };

    document.addEventListener('selectionchange', handleSelectionChange);
    return () => {
      document.removeEventListener('selectionchange', handleSelectionChange);
    };
  }, [isTextSelectionMode]);

  const handleSendMessage = async () => {
    if (input.trim() === '') return;
    if (isTextSelectionMode && selectedText.trim() === '') {
      alert('Please select some text in the document or switch off text selection mode.');
      return;
    }

    const newUserMessage: ChatMessage = { id: messages.length + 1, sender: 'user', text: input };
    setMessages((prevMessages) => [...prevMessages, newUserMessage]);
    setInput('');
    setLoading(true);

    try {
      const mode = isTextSelectionMode && selectedText.trim() !== '' ? 'selected-text' : 'full-book';
      const body: any = { query: input, mode: mode };

      if (mode === 'selected-text') {
        body.selected_text = selectedText;
      }

      const response = await fetch('/api/rag/query', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(body),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      const newBotMessage: ChatMessage = {
        id: messages.length + 2,
        sender: 'bot',
        text: data.answer || 'No answer received.',
        source: data.source,
      };
      setMessages((prevMessages) => [...prevMessages, newBotMessage]);
    } catch (error) {
      console.error('Error sending message:', error);
      const errorMessage: ChatMessage = {
        id: messages.length + 2,
        sender: 'bot',
        text: 'Sorry, I am having trouble connecting to the service. Please try again later.',
      };
      setMessages((prevMessages) => [...prevMessages, errorMessage]);
    } finally {
      setLoading(false);
      setSelectedText(''); // Clear selected text after sending
    }
  };

  const handleKeyPress = (event: React.KeyboardEvent<HTMLInputElement>) => {
    if (event.key === 'Enter' && !loading) {
      handleSendMessage();
    }
  };

  const toggleTextSelectionMode = () => {
    setIsTextSelectionMode((prev) => !prev);
    setSelectedText(''); // Clear selected text when toggling mode
    if (!isTextSelectionMode) {
      alert('Text selection mode enabled. Now select text in the document and ask a question.');
    } else {
      alert('Text selection mode disabled.');
    }
  };

  return (
    <div className={styles.chatbotContainer}>
      <div className={styles.messagesContainer}>
        {messages.length === 0 && <p className={styles.welcomeMessage}>Ask me anything about the book!</p>}
        {messages.map((msg) => (
          <div key={msg.id} className={`${styles.chatMessage} ${styles[msg.sender]}`}>
            <p>{msg.text}</p>
            {msg.source && (
              <a href={msg.source.url} target="_blank" rel="noopener noreferrer" className={styles.sourceLink}>
                Source: {msg.source.chapter}
              </a>
            )}
          </div>
        ))}
        {loading && <div className={styles.loadingMessage}>Thinking...</div>}
      </div>
      <div className={styles.inputContainer}>
        <button
          onClick={toggleTextSelectionMode}
          className={`${styles.toggleButton} ${isTextSelectionMode ? styles.active : ''}`}
          title="Toggle text selection mode"
          disabled={loading}
        >
          {isTextSelectionMode ? 'Disable Text Select' : 'Enable Text Select'}
        </button>
        {isTextSelectionMode && selectedText && (
          <span className={styles.selectedTextIndicator} title={selectedText}>
            Selected: {selectedText.substring(0, 30)}...
          </span>
        )}
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Type your question here..."
          disabled={loading}
        />
        <button onClick={handleSendMessage} disabled={loading}>
          Send
        </button>
      </div>
    </div>
  );
};

export default Chatbot;
