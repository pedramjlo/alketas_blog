import React, { useState } from 'react';
import Navbar from '../navbar';
import '../../style/user_account/signup.css';


const SignupPage = () => {
    const [username, setUsername] = useState('');
    const [first_name, setFirst_name] = useState('');
    const [last_name, setLast_name] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const[error, setError] = useState('');

    const handleSignup = async (event) => {
        event.preventDefault();
        setError(null);

        try {
            const response = await fetch('http://localhost:3000/api/register', {
                method: 'Post',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username, first_name, last_name, email, password}),
            })

            //unsuccessful register handle
            if (!response.status == 201) {
                throw new Error(response.data.message)
            }

            const data = await response.json()
            console.log('created successfully, logging you in...')
        }

        catch (error) {
            setError(error.message)
        }
    };

    return (
        <div className='signup-form-page'>
            <Navbar />
            <div className='signup-body'>
                <div className='form-container'>
                    <h2>عضویت</h2>
                    <form onSubmit={handleSignup}>

                        <div className='form-username'>
                            <label>نام کاربری</label>
                            <input 
                                type="text"
                                value={username}
                                onChange={(e) => setUsername(e.target.value)}
                            />
                        </div>

                        <div className='form-firstname'>
                            <label>نام کوچک</label>
                            <input 
                                type="text"
                                value={first_name}
                                onChange={(e) => setFirst_name(e.target.value)}
                            />
                        </div>

                        <div className='form-lastname'>
                            <label>نام خانوادگی</label>
                            <input 
                                type="text"
                                value={last_name}
                                onChange={(e) => setLast_name(e.target.value)}
                            />
                        </div>
                        
                        <div className='form-email'>
                            <label>ایمیل</label>
                            <input 
                                type="text"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                            />
                        </div>

                        <div className='form-username'>
                            <label> گذرواژه</label>
                            <input 
                                type="password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                            />
                        </div>

                        <button type='submit'>عضویت</button>
                    
                        {error && <p>{error}</p>}  

                        <div className='have-account'>
                        <span>حساب کاربری دارید؟ <a href="/">وارد شوید</a></span>
                        </div>

                    </form>
                </div>
            </div>
        </div>
    );

};


export default SignupPage;