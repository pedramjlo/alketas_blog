import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Navbar from '../navbar';
import Cookies from 'js-cookie'; 
import '../../styles/user_account/login.css';


const getCSRFToken = () => {
    return Cookies.get('csrftoken');
};


const fetchCSRFToken = async () => {
    try {
        const response = await fetch('http://localhost:8000/api/csrf/', {
            method: 'GET',
            credentials: 'include',  
        });
        if (response.ok) {
            console.log('CSRF token fetched successfully.');
        } else {
            console.error('Failed to fetch CSRF token.');
        }
    } catch (error) {
        console.error('Error fetching CSRF token:', error);
    }
};

const LoginPage = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();

    // Fetch CSRF token when component mounts
    useEffect(() => {
        fetchCSRFToken();
    }, []);

    const handleLogin = async (event) => {
        event.preventDefault(); // Prevent the default form submission
        const csrfToken = getCSRFToken(); // Get CSRF token from cookies

        try {
            const response = await fetch('http://localhost:8000/api/login/', {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken,  // Include the CSRF token in headers
                },
                credentials: 'include',  // Correct placement of credentials
                body: JSON.stringify({ username, password })  // Use state variables
            });

            if (response.ok) {  // Check if response is OK
                const data = await response.json();
                if (data.success) {
                    navigate('/');
                } else {
                    setError(data.message || 'Invalid Credentials!');
                }
            } else {
                const errorData = await response.json();
                console.error('Error response data:', errorData);
                setError(errorData.message || 'An error occurred. Please try again.');
            }
        } catch (error) {
            console.error('Fetch error:', error);
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
