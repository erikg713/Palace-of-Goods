// src/components/RecursionLevel.js
import React, { useState } from 'react';
import axios from 'axios';

const RecursionLevel = () => {
  const [code, setCode] = useState('');
  const [output, setOutput] = useState('');

  const runCode = () => {
    axios.post('/api/levels/recursion', { code })
      .then(response => setOutput(response.data.message))
      .catch(error => console.error(error));
  };

  return (
    <div>
      <h1>Recursion Ridge</h1>
      <textarea value={code} onChange={e => setCode(e.target.value)} />
      <button onClick={runCode}>Run Code</button>
      <p>{output}</p>
    </div>
  );
};

export default RecursionLevel;

