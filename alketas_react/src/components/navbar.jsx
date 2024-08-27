import React from 'react';
import { useAuth } from './authConfig/authConfig';


const Navbar = () => {
    const auth = useAuth();
    console.log(auth); // Debugging line
    const { isAuthenticated } = auth || {};
  
    return (
      <div>

        {isAuthenticated ? (
          <nav className='navbar auth'>
            <div className='logo-auth'><a href="/">آلکتاس</a></div>
          </nav>
        ) : (
          <nav className='navbar unauth'>
            {/* <div className='buttons-div'>
              <a href='/login' id='login-btn'>ورود</a>
              <a href='/register' id='signup-btn'>عضویت</a>
            </div>
            */}
            <div className='alketas-logo'><a href="/">آلکتاس</a></div>
        </nav>
        )}

      </div>
    );
  };
  
export default Navbar;