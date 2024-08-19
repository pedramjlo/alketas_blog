import React, { useState, useEffect } from 'react';

import Navbar from '../navbar';

import '../../style/user_account/login.css';



const LoginPage = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');


    const handleLogin = async (event) => {
        event.preventDefault();
        setError(null);

        try {
            const response = await fetch('http://127.0.0.1:8000/api/login', {
                method: 'Post',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username, password}),
            });

            // handle unsuccessful login
            if (!response.status == 202) {
                throw new Error(response.data.message);
            }

            const data = await response.json();
            console.log('successful login')

        } catch (error) {
            setError(error.message)
        }

    };
    
    return (
        <div className='form-page'>  
            <Navbar />
           <div className='form-body'>
            <div className='form-container'>
                <h2>ورود</h2>
                <form onSubmit={handleLogin}>

                    <div className='form-username'>
                        <label>نام کاربری</label>
                        <input 
                            type="text"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            required
                        />
                    </div>
                    
                    <div className='form-password'>
                        <label>گذرواژه</label>
                        <input 
                            type="text"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            required
                        /> 
                    </div> 


                    <button type='submit'>ورود</button>
                    
                    <div className='no-account'>
                        <span>حساب کاربری ندارید؟ <a href="/">عضو شوید</a></span>
                        <a href="/" style={{ color: '#13274F' }}>گذرواژه را فراموش کردم</a>
                    </div>

                    {error && <p>{error}</p>}
                </form>

            </div>
           </div>
        </div>
    );
};  



export default LoginPage;