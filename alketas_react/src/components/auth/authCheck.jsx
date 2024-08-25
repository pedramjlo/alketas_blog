// AuthCheck.js
import React from 'react';
import { useAuth } from '../authConfig/authConfig';

const AuthCheck = ({ children }) => {
  const { isAuthenticated } = useAuth();

  return isAuthenticated ? children : <p>You are not authenticated.</p>;
};

export default AuthCheck;
