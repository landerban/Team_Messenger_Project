import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import Home from './pages/Home';
import Chats from './pages/Chats';
import About from './pages/About';
import Login from './pages/Login';
import NotFound from './pages/NotFound';
import Register from './pages/Register';

const AppRoutes = ({ isDark, isAuthenticated }) => {
  return (
    <Routes>
      <Route path='/' element={<Home isDark={isDark} />} />
      <Route path='/login' element={<Login />} />
      
      {/* Protected route for /chats */}
      <Route 
        path='/chats' 
        element={isAuthenticated ? <Chats isDark={isDark} /> : <Navigate to="/register" />} 
      />

      <Route path='/about' element={<About isDark={isDark} />} />
      <Route path='/register' element={<Register isDark={isDark} />} />
      <Route path='*' element={<NotFound isDark={isDark} />} />
    </Routes>
  );
};

export default AppRoutes;
