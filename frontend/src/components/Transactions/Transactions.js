import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Transactions = () => {
    const [transactions, setTransactions] = useState([]);

    useEffect(() => {
        const fetchTransactions = async () => {
            const response = await axios.get('/api/transactions?user_id=1'); // Replace with dynamic user ID
            setTransactions(response.data.transactions);
        };
        fetchTransactions();
    }, []);

    return (
        <div>
            <h1>Transactions</h1>
            <ul>
                {transactions.map(transaction => (
                    <li key={transaction.id}>{transaction.amount} from {transaction.sender.username} to {transaction.receiver.username}</li>
                ))}
            </ul>
        </div>
    );
};

export default Transactions;
