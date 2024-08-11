import React from 'react';
import { Link } from 'react-router-dom';
import '../CompoCss/Sidenav.css';
import { FaHome, FaQuestionCircle, FaCog, FaMoneyBillWave } from 'react-icons/fa';

const SideNav = () => {
  return (
    <div className="sidenav">
      <Link to="/" className="nav-link">
        <FaHome className="icon" />
        <span>Home</span>
      </Link>
      <Link to="/main" className="nav-link">
        <FaMoneyBillWave className="icon" />
        <span>Payments</span> {/* This link now points to MainPage */}
      </Link>
      <Link to="/help" className="nav-link">
        <FaQuestionCircle className="icon" />
        <span>Help</span>
      </Link>
      
      <Link to="/settings" className="nav-link">
        <FaCog className="icon" />
        <span>Settings</span>
      </Link>
      
    </div>
  );
};

export default SideNav;
