import React, { useState, useEffect } from 'react';
import Layout from '@theme/Layout';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

interface UserProfileData {
  user_id: string;
  email: string;
  full_name?: string;
  profile_data?: {
    background_sw?: string;
    background_hw?: string;
    preferences?: {
      translation_language?: string;
      chapter_order?: string[];
      hidden_chapters?: string[];
      highlighted_chapters?: string[];
    };
  };
}

const Profile: React.FC = () => {
  const { siteConfig } = useDocusaurusContext();
  const [userProfile, setUserProfile] = useState<UserProfileData | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [message, setMessage] = useState<string | null>(null); // For user messages

  const [fullName, setFullName] = useState('');
  const [backgroundSw, setBackgroundSw] = useState('');
  const [backgroundHw, setBackgroundHw] = useState('');
  const [translationLanguage, setTranslationLanguage] = useState('en');

  useEffect(() => {
    fetchUserProfile();
  }, []);

  const fetchUserProfile = async () => {
    const token = localStorage.getItem('access_token');
    if (!token) {
      setError('You are not logged in.');
      setLoading(false);
      return;
    }

    try {
      const response = await fetch('/api/users/me', {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Failed to fetch user profile');
      }

      const data: UserProfileData = await response.json();
      setUserProfile(data);
      setFullName(data.full_name || '');
      setBackgroundSw(data.profile_data?.background_sw || '');
      setBackgroundHw(data.profile_data?.background_hw || '');
      setTranslationLanguage(data.profile_data?.preferences?.translation_language || 'en');
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleProfileUpdate = async (event: React.FormEvent) => {
    event.preventDefault();
    const token = localStorage.getItem('access_token');
    if (!token) {
      setError('You are not logged in.');
      return;
    }

    const updatePayload = {
      full_name: fullName,
      profile_data: {
        background_sw: backgroundSw,
        background_hw: backgroundHw,
        preferences: {
          translation_language: translationLanguage,
          // chapter_order, hidden_chapters, highlighted_chapters can be added here
        },
      },
    };

    try {
      const response = await fetch('/api/users/me', {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
        body: JSON.stringify(updatePayload),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'Failed to update user profile');
      }

      const data: UserProfileData = await response.json();
      setUserProfile(data);
      setMessage('Profile updated successfully!');
    } catch (err: any) {
      setMessage(`Error updating profile: ${err.message}`);
      console.error('Profile update error:', err);
    }
  };

  if (loading) {
    return (
      <Layout title={`Profile | ${siteConfig.title}`}>
        <main>
          <div style={{ padding: '20px', textAlign: 'center' }}>Loading profile...</div>
        </main>
      </Layout>
    );
  }

  if (error) {
    return (
      <Layout title={`Profile | ${siteConfig.title}`}>
        <main>
          <div style={{ padding: '20px', textAlign: 'center', color: 'red' }}>Error: {error}</div>
        </main>
      </Layout>
    );
  }

  return (
    <Layout title={`Profile | ${siteConfig.title}`} description="User Profile Page">
      <main style={{ maxWidth: '800px', margin: '50px auto', padding: '20px', border: '1px solid #eee', borderRadius: '8px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)' }}>
        <h1 style={{ textAlign: 'center', marginBottom: '30px' }}>Your Profile</h1>

        {message && (
          <div style={{ marginBottom: '15px', padding: '10px', backgroundColor: message.startsWith('Error') ? '#ffe0e0' : '#e0ffe0', border: `1px solid ${message.startsWith('Error') ? 'red' : 'green'}`, borderRadius: '4px', color: message.startsWith('Error') ? 'red' : 'green' }}>
            {message}
          </div>
        )}
        {userProfile && (
          <form onSubmit={handleProfileUpdate}>
            <div style={{ marginBottom: '15px' }}>
              <label htmlFor="emailDisplay" style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>Email:</label>
              <input type="text" id="emailDisplay" value={userProfile.email} readOnly style={{ width: '100%', padding: '8px', boxSizing: 'border-box', backgroundColor: '#f0f0f0' }} />
            </div>

            <div style={{ marginBottom: '15px' }}>
              <label htmlFor="fullName" style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>Full Name:</label>
              <input
                type="text"
                id="fullName"
                value={fullName}
                onChange={(e) => setFullName(e.target.value)}
                style={{ width: '100%', padding: '8px', boxSizing: 'border-box' }}
              />
            </div>

            <div style={{ marginBottom: '15px' }}>
              <label htmlFor="backgroundSw" style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>Software Background:</label>
              <input
                type="text"
                id="backgroundSw"
                value={backgroundSw}
                onChange={(e) => setBackgroundSw(e.target.value)}
                placeholder="e.g., Student, Professional"
                style={{ width: '100%', padding: '8px', boxSizing: 'border-box' }}
              />
            </div>

            <div style={{ marginBottom: '15px' }}>
              <label htmlFor="backgroundHw" style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>Hardware Background:</label>
              <input
                type="text"
                id="backgroundHw"
                value={backgroundHw}
                onChange={(e) => setBackgroundHw(e.target.value)}
                placeholder="e.g., Beginner, Expert"
                style={{ width: '100%', padding: '8px', boxSizing: 'border-box' }}
              />
            </div>

            <div style={{ marginBottom: '25px' }}>
              <label htmlFor="translationLanguage" style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>Translation Language:</label>
              <select
                id="translationLanguage"
                value={translationLanguage}
                onChange={(e) => setTranslationLanguage(e.target.value)}
                style={{ width: '100%', padding: '8px', boxSizing: 'border-box' }}
              >
                <option value="en">English</option>
                <option value="ur">Urdu</option>
              </select>
            </div>

            <button type="submit" style={{ width: '100%', padding: '12px', backgroundColor: '#28a745', color: 'white', border: 'none', borderRadius: '5px', cursor: 'pointer', fontSize: '16px' }}>
              Update Profile
            </button>
          </form>
        )}
      </main>
    </Layout>
  );
};

export default Profile;
