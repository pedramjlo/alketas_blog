import './App.css';

import HomePage from './components/home';
import FeedPage from './components/blog/feed';
import LoginPage from './components/user_account/login';
import SignupPage from './components/user_account/signup';

import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/register" element={<SignupPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/feed" element={<FeedPage />} />
      </Routes>
    </Router>
  );
}

export default App;
