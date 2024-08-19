import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import HomePage from './components/home';
import FeedPage from './components/blog/feed';


import { AuthProvider } from './components/auth/authContext';

function App() {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/feed" element={<FeedPage />} />
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;
