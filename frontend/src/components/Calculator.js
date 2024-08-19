import React, { useState } from 'react';
import axios from 'axios';
import './Calculator.css';

const Calculator = () => {
    const [a, setA] = useState('');
    const [b, setB] = useState('');
    const [result, setResult] = useState(null);
    const [error, setError] = useState(null);

    const calculate = async (operation) => {
        try {
            const response = await axios.post(`http://127.0.0.1:8000/api/${operation}/`, { a, b });
            setResult(response.data.result);
            setError(null);
        } catch (error) {
            setError(error.response?.data?.error || "An error occurred");
            setResult(null);
        }
    };

    return (
        <div className="container">
            <h2>Simple Calculator</h2>
            <input
                type="number"
                value={a}
                onChange={(e) => setA(e.target.value)}
                placeholder="Enter number a"
            />
            <input
                type="number"
                value={b}
                onChange={(e) => setB(e.target.value)}
                placeholder="Enter number b"
            />
            <div>
                <button onClick={() => calculate('add')}>Add</button>
                <button onClick={() => calculate('subtract')}>Subtract</button>
                <button onClick={() => calculate('multiply')}>Multiply</button>
                <button onClick={() => calculate('divide')}>Divide</button>
            </div>
            {result !== null && <div className="result">Result: {result}</div>}
            {error && <div className="error">Error: {error}</div>}
        </div>
    );
};

export default Calculator;
