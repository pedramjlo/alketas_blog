import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import HomePage from './components/home';
import FeedPage from './components/blog/feed';
import LoginPage from './components/user_account/login';
import SignupPage from './components/user_account/signup';


import { AuthProvider } from './components/auth/authContext';

function App() {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route path="/register" element={<SignupPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/" element={<HomePage />} />
          <Route path="/feed" element={<FeedPage />} />
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;
