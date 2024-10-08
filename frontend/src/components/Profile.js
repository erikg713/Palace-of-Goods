import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Profile = () => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    // Fetch user data from Pi Network or your backend
    axios.get('/api/user/profile')
      .then(response => setUser(response.data))
      .catch(error => console.error('Error fetching user profile:', error));
  }, []);

  if (!user) return <div>Loading...</div>;

  return (
    <div className="profile-page">
      <h1>{user.username}'s Profile</h1>
      <p>Email: {user.email}</p>
      <p>Pi Balance: {user.piBalance}</p>
      {/* Add functionality to update user info */}
    </div>
  );
};

export default Profile;
