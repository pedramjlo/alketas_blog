import React from 'react';

import Navbar from '../navbar.jsx';
import '../../style/blog/feed.css';



const FeedPage = () => {
    return(
        <div className='home-container'>
            <Navbar />

            <div class="container">
                <div class="left">Left</div>
                <div class="middle">Middle</div>
                <div class="right">Right</div>
            </div>

        </div>
    );
};

export default FeedPage;

