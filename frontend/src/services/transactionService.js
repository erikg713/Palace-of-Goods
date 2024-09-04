import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL;

export const purchaseProduct = async (productId) => {
  return await axios.post(`${API_URL}/transaction/purchase`, { product_id: productId });
};

