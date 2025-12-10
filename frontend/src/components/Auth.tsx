import React, { useState } from 'react';

const Auth: React.FC = () => {
  const [isSignIn, setIsSignIn] = useState(true);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [fullName, setFullName] = useState('');
  const [background, setBackground] = useState(''); // For signup
  const [message, setMessage] = useState<string | null>(null); // For user messages

  const handleAuthSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    setMessage(null); // Clear previous messages
    const endpoint = isSignIn ? '/api/auth/signin' : '/api/auth/signup';
    const body = isSignIn
      ? { email, password }
      : { email, password, full_name: fullName, background };

    try {
      const response = await fetch(endpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(body),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Authentication failed');
      }

      const data = await response.json();
      console.log('Auth successful:', data);
      // Handle successful sign-in/sign-up (e.g., store token, redirect)
      if (isSignIn && data.access_token) {
        localStorage.setItem('access_token', data.access_token);
        setMessage('Signed in successfully!');
      } else if (!isSignIn && data.user_id) {
        setMessage('Signed up successfully! Please sign in.');
        setIsSignIn(true); // Switch to sign-in after successful signup
      }
    } catch (error: any) {
      setMessage(`Error: ${error.message}`);
      console.error('Auth error:', error);
    }
  };

  return (
    <div style={{ maxWidth: '400px', margin: '50px auto', padding: '20px', border: '1px solid #ccc', borderRadius: '8px' }}>
      <h2>{isSignIn ? 'Sign In' : 'Sign Up'}</h2>
      <form onSubmit={handleAuthSubmit}>
        {message && (
          <div style={{ marginBottom: '15px', padding: '10px', backgroundColor: message.startsWith('Error') ? '#ffe0e0' : '#e0ffe0', border: `1px solid ${message.startsWith('Error') ? 'red' : 'green'}`, borderRadius: '4px', color: message.startsWith('Error') ? 'red' : 'green' }}>
            {message}
          </div>
        )}
        <div style={{ marginBottom: '15px' }}>
          <label htmlFor="email" style={{ display: 'block', marginBottom: '5px' }}>Email:</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            style={{ width: '100%', padding: '8px', boxSizing: 'border-box' }}
          />
        </div>
        <div style={{ marginBottom: '15px' }}>
          <label htmlFor="password" style={{ display: 'block', marginBottom: '5px' }}>Password:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            style={{ width: '100%', padding: '8px', boxSizing: 'border-box' }}
          />
        </div>
        {!isSignIn && (
          <>
            <div style={{ marginBottom: '15px' }}>
              <label htmlFor="fullName" style={{ display: 'block', marginBottom: '5px' }}>Full Name (Optional):</label>
              <input
                type="text"
                id="fullName"
                value={fullName}
                onChange={(e) => setFullName(e.target.value)}
                style={{ width: '100%', padding: '8px', boxSizing: 'border-box' }}
              />
            </div>
            <div style={{ marginBottom: '15px' }}>
              <label htmlFor="background" style={{ display: 'block', marginBottom: '5px' }}>Background (e.g., student):</label>
              <input
                type="text"
                id="background"
                value={background}
                onChange={(e) => setBackground(e.target.value)}
                style={{ width: '100%', padding: '8px', boxSizing: 'border-box' }}
              />
            </div>
          </>
        )}
        <button type="submit" style={{ width: '100%', padding: '10px', backgroundColor: '#007bff', color: 'white', border: 'none', borderRadius: '5px', cursor: 'pointer' }}>
          {isSignIn ? 'Sign In' : 'Sign Up'}
        </button>
      </form>
      <p style={{ textAlign: 'center', marginTop: '20px' }}>
        {isSignIn ? "Don't have an account?" : "Already have an account?"}{' '}
        <button
          onClick={() => setIsSignIn(!isSignIn)}
          style={{ background: 'none', border: 'none', color: '#007bff', cursor: 'pointer', textDecoration: 'underline' }}
        >
          {isSignIn ? 'Sign Up' : 'Sign In'}
        </button>
      </p>
    </div>
  );
};

export default Auth;
