import axios from 'axios';

const api = axios.create({
  baseURL: 'https://your-backend-url.com/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

export const fetchProducts = () => api.get('/products');
export const fetchProductById = (id) => api.get(`/products/${id}`);

export default api;
