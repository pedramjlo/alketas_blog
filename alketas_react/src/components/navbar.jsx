import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from './auth/authContext.jsx';




const Navbar = () => {
    const { isAuthenticated, login, logout } = useAuth();

    return(
        <div>
            {isAuthenticated ? (
                <nav className='navbar auth'>
                </nav>
            ) : (
                <nav className='navbar unauth'> 
                    <div className='buttons-div'>
                        <button id='signup-btn'>عضویت</button>
                        <button id='login-btn'>ورود</button>
                    </div>

                    <div id='alketas-logo'><a href="/">آلکتاس</a></div>

                </nav>
            )}
        </div>
    );
};


export default Navbar;