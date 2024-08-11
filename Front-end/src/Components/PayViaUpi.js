import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import '../CompoCss/PayViaUpi.css';

const PayViaUpi = () => {
  const navigate = useNavigate();
  const [upiId, setUpiId] = useState('');
  const [amount, setAmount] = useState('');

  const handlePay = () => {
    // Implement payment processing logic here
    alert(`Processing payment of ₹${amount} to UPI ID: ${upiId}`);
  };

  return (
    <div className="upi-container">
      <h2 className="upi-header">UPI Payment</h2>
      
      <input
        type="text"
        className="upi-input"
        placeholder="Enter User UPI ID"
        value={upiId}
        onChange={(e) => setUpiId(e.target.value)}
      />
      
      <input
        type="number"
        className="upi-input"
        placeholder="Enter Amount"
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
      />
      
      <div className="upi-buttons">
        <button className="google-button pay-button" onClick={handlePay}>
          Pay
        </button>
        <button className="google-button cancel-button" onClick={() => navigate('/main')}>
          Cancel
        </button>
      </div>
    </div>
  );
};

export default PayViaUpi;
