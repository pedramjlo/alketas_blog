import logo from './logo.svg';
import './App.css';

import HomePage from './components/home';
import FeedPage from './components/blog/feed';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/feed" element={<FeedPage />} />
        <Route path="/" element={<HomePage />} />
      </Routes>
    </Router>
  );
}

export default App;
