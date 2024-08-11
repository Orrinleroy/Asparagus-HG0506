import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import SideNav from './Components/SideNav';
import Home from './Components/Home';
import Help from './Components/Help';
import Settings from './Components/Settings';
import MainPage from './MainPage/MainPage';
import QRGenerator from './Components/Qr';
import PayViaUpi from './Components/PayViaUpi';

function App() {
  return (
    <Router>
      <div>
        <SideNav />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/help" element={<Help />} />
          <Route path="/settings" element={<Settings />} />
          <Route path="/main" element={<MainPage />} />
          <Route path="/qr-generator" element={<QRGenerator />} />
          <Route path="/pay-via-upi" element={<PayViaUpi />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
