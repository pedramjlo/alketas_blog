import React from 'react';
import { useAuth } from './auth/authContext';



const Navbar = () => {

    const { isAuthenticated, logout } = useAuth();

    return (
        <nav className='navbar'>

            { isAuthenticated ? (
                <>

                </>
            ) : (
                <>
                    <div className='alketas-logo'><a href="/">آلکتاس</a></div>
                    <div className='buttons-div'>
                        <button id='signup-btn'>عضویت</button>
                        <button id='login-btn'>ورود</button>
                    </div>
                </>
            ) }

        </nav>
    );
};


export default Navbar;