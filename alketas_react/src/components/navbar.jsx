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
                    <div id='alketas-logo'><a href="/">آلکتاس</a></div>

                    <div className='buttons-div'>
                        <button>ورود</button>
                        <button>عضویت</button>
                    </div>

                </nav>
            )}
        </div>
    );
};


export default Navbar;