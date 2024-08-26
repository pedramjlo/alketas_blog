import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Navbar from '../navbar';

import '../../styles/user_account/login.css';

const LoginPage = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleLogin = async (event) => {
        event.preventDefault(); // Prevent the default form submission

        try {
            const response = await fetch('http://localhost:8000/api/login/', {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ username, password })
            });

            const data = await response.json();

            if (data.success) {
                navigate('/');
            } else {
                setError('Invalid Credentials!');
            }
        } catch (error) {
            setError('An error occurred. Please try again.');
        }
    };

    return (
        <div className='login-page'>
            <Navbar />
                <div className='form-container'>
                    <div className='form'>

                    <form onSubmit={handleLogin}>
                        <h2>ورود</h2>
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
                                type="password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                required
                            />
                        </div>
                        <button type="submit">ورود</button>
                        <a href="/register">حساب کاربری ندارید؟</a>
                        {error && <p>{error}</p>}
                    </form>
                    
                    </div>
                </div>
        </div>
    );
};

export default LoginPage;
