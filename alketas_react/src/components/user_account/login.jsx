import React, { useState, useEffect } from 'react';

import Navbar from '../navbar';

import '../../style/user_account/login.css';



const LoginPage = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [errors, setErrors] = useState('');


    const handleLogin = async (event) => {
        event.preventDefault();
        setErrors(null);

        try {
            const response = await fetch('http://127.0.0.1:8000/login', {
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
            setErrors(error.message)
        }

    };
    
    return (
        <div className='form-page'>  
           <div className='form-container'>
                <h2>ورود</h2>
                <form onSubmit={handleLogin}>
                    <label>نام کاربری</label>
                    <input 
                        type="text"
                        value={username}
                        required
                    />
                    <label>گذرواژه</label>
                    <input 
                        type="text"
                        value={password}
                        required
                    />  
                    <button type='submit'>ورود</button>
                    {error && <p>{error}</p>}
                </form>

           </div>
        </div>
    );
};  



export default LoginPage;