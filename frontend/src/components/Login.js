import React from 'react';
import { PiAuth } from 'pi-network-sdk'; // Assuming you have the Pi SDK setup

const Login = () => {
  const handleLogin = async () => {
    try {
      const user = await PiAuth.login(); // Login with Pi Network
      console.log('Logged in user:', user);
      // Handle user authentication, save token, etc.
    } catch (error) {
      console.error('Login failed:', error);
    }
  };

  return (
    <div className="login-page">
      <h1>Login</h1>
      <button onClick={handleLogin}>Login with Pi Network</button>
    </div>
  );
};

export default Login;
