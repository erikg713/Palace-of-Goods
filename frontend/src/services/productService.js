import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL;

export const getProducts = async () => {
  return await axios.get(`${API_URL}/marketplace/`);
};

export const getProductById = async (id) => {
  return await axios.get(`${API_URL}/marketplace/product/${id}`);
};

export const createProduct = async (product) => {
  return await axios.post(`${API_URL}/marketplace/sell`, product);
};

