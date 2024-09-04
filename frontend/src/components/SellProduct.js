import React, { useState } from 'react';
import { createProduct } from '../services/productService';

function SellProduct() {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [price, setPrice] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await createProduct({ name, description, price });
      alert('Product listed successfully!');
    } catch (error) {
      console.error('Error listing product:', error);
    }
  };

  return (
    <div className="container">
      <h1>Sell a Product</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Name:</label>
          <input type="text" value={name} onChange={(e) => setName(e.target.value)} required />
        </div>
        <div>
          <label>Description:</label>
          <textarea value={description} onChange={(e) => setDescription(e.target.value)} required />
        </div>
        <div>
          <label>Price:</label>
          <input type="number" value={price} onChange={(e) => setPrice(e.target.value)} required />
        </div>
        <button type="submit">List Product</button>
      </form>
    </div>
  );
}

export default SellProduct;

