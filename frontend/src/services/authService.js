import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL;

export const login = async (email, password) => {
  return await axios.post(`${API_URL}/auth/login`, { email, password });
};

export const register = async (email, password) => {
  return await axios.post(`${API_URL}/auth/register`, { email, password });
};

export const getProfile = async () => {
  return await axios.get(`${API_URL}/auth/profile`);
};

