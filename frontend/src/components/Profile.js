import React, { useState, useEffect } from 'react';
import { getProfile } from '../services/authService';

function Profile() {
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const response = await getProfile();
        setProfile(response.data);
      } catch (error) {
        console.error('Error fetching profile:', error);
      }
    };

    fetchProfile();
  }, []);

  return profile ? (
    <div className="container">
      <h1>Profile</h1>
      <p>Email: {profile.email}</p>
      <p>Wallet Address: {profile.wallet_address}</p>
    </div>
  ) : (
    <div className="container">Loading...</div>
  );
}

export default Profile;

