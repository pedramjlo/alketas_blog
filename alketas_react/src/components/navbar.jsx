import React from 'react';
import { useAuth } from './authConfig/authConfig';


const Navbar = () => {
    const auth = useAuth();
    console.log(auth); // Debugging line
    const { isAuthenticated } = auth || {};
  
    return (
      <div>

        {isAuthenticated ? (
          <nav className='navbar'>
          </nav>
        ) : (
          <nav className='navbar'>
            <div className='buttons-div'>
              <a href='/login' id='login-btn'>ورود</a>
              <a href='/' id='signup-btn'>عضویت</a>
            </div>
            <div className='alketas-logo'><a href="/">آلکتاس</a></div>
        </nav>
        )}

      </div>
    );
  };
  
export default Navbar;