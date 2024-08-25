import logo from './logo.svg';
import './App.css';

import HomePage from './components/home';
import FeedPage from './components/blog/feed';
import LoginPage from './components/user_account/login';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/feed" element={<FeedPage />} />
        <Route path="/" element={<HomePage />} />
      </Routes>
    </Router>
  );
}

export default App;
