import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getProductById } from '../services/productService';
import { purchaseProduct } from '../services/transactionService';

function ProductDetail() {
  const { id } = useParams();
  const [product, setProduct] = useState(null);

  useEffect(() => {
    const fetchProduct = async () => {
      try {
        const response = await getProductById(id);
        setProduct(response.data);
      } catch (error) {
        console.error('Error fetching product:', error);
      }
    };

    fetchProduct();
  }, [id]);

  const handlePurchase = async () => {
    try {
      await purchaseProduct(id);
      alert('Purchase successful!');
    } catch (error) {
      console.error('Error purchasing product:', error);
    }
  };

  return product ? (
    <div className="container">
      <h1>{product.name}</h1>
      <p>{product.description}</p>
      <p>Price: {product.price} Pi</p>
      <button onClick={handlePurchase}>Purchase</button>
    </div>
  ) : (
    <div className="container">Loading...</div>
  );
}

export default ProductDetail;

