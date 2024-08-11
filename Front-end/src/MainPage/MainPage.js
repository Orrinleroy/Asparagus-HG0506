import React from 'react';
import { useNavigate } from 'react-router-dom';
import './MainPage.css';
import { FaQrcode, FaMoneyBillWave, FaWallet, FaQuestionCircle, FaCog, FaUser } from 'react-icons/fa';

const MainPage = () => {
  const navigate = useNavigate(); // Hook for navigation

  return (
    <div className="main-container">
      <h1 className="header">Payment App</h1>

      <div className="top-utilities-row">
        <UtilityButton 
          icon={<FaQrcode />} 
          label="QR Generator" 
          large 
          onClick={() => navigate('/qr-generator')} // Navigate to QR Generator page
        />
        <UtilityButton 
          icon={<FaMoneyBillWave />} 
          label="Pay via UPI" 
          large 
          onClick={() => navigate('/pay-via-upi')} // Navigate to Pay via UPI page
        />
      </div>

      <div className="utilities-grid">
        <UtilityButton icon={<FaWallet />} label="Wallet" />
        <UtilityButton icon={<FaUser />} label="Profile" />
        <UtilityButton icon={<FaQuestionCircle />} label="Help" />
        <UtilityButton icon={<FaCog />} label="Settings" />
      </div>
    </div>
  );
};

const UtilityButton = ({ icon, label, large, onClick }) => (
  <div className={`utility-button ${large ? 'large' : ''}`} onClick={onClick}>
    <div className="icon">{icon}</div>
    <div className="label">{label}</div>
  </div>
);

export default MainPage;
