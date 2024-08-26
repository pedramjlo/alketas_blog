import React, { useState } from 'react';
import Navbar from '../navbar';
import '../../styles/user_account/signup.css';
import { useNavigate } from 'react-router-dom';

const SignupPage = () => {
    const [username, setUsername] = useState('');
    const [first_name, setFirst_name] = useState('');
    const [last_name, setLast_name] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleRegister = async (event) => {
        event.preventDefault();
        const csrfToken = Cookies.get('csrftoken');
        try {
            const response = await fetch('http://127.0.0.1:8000/api/register/', {
                method: "POST",
                headers: {
                    "Content-Type": 'application/json',
                    'X-CSRFToken': csrfToken,
                },
                body: JSON.stringify({ username, first_name, last_name, email, password })
            });

            const data = await response.json();

            if (data.success) {
                navigate('/feed');
            } else {
                setError('Invalid credentials');
            }
        } catch (error) {
            setError('An error occurred while creating the account!');
        }
    };

    return (
        <div className='signup-page'>
            <Navbar />
            <div className='form-container'>
                <div className='form'>
                    <form onSubmit={handleRegister}>
                        <h2>عضویت</h2>
                        
                        <div className='form-username'>
                            <label>نام کاربری</label>
                            <input 
                                type="text" 
                                value={username}
                                onChange={(e) => setUsername(e.target.value)}
                                required
                            />
                        </div>

                        <div className='form-firstname'>
                            <label> نام</label>
                            <input 
                                type="text" 
                                value={first_name}
                                onChange={(e) => setFirst_name(e.target.value)}
                                required
                            />
                        </div>

                        <div className='form-lastname'>
                            <label>نام خانوادگی</label>
                            <input 
                                type="text" 
                                value={last_name}
                                onChange={(e) => setLast_name(e.target.value)}
                                required
                            />
                        </div>

                        <div className='form-email'>
                            <label>ایمیل </label>
                            <input 
                                type="text" 
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                                required
                            />
                        </div>

                        <div className='form-password'>
                            <label>گذرواژه </label>
                            <input 
                                type="password" 
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                required
                            />
                        </div>
                        <button type='submit'>عضویت</button>
                        {error && <p>{error}</p>}
                        <a id='have-account' href="/login">حساب کاربری دارید؟</a>
                    </form>
                </div>
            </div>
        </div>
    );
};

export default SignupPage;
