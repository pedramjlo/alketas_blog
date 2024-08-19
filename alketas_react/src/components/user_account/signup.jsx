import React, { useState } from 'react';



const SignupPage = () => {
    const [username, setUsername] = useState('');
    const [firstName, setFirstName] = useState('');
    const [lastName, setLasttName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const[error, setError] = useState('');

    const handleSignup = async (event) => {
        event.preventDefault();
        setError(null);

        try {
            const response = await fetch('http://localhost:3000/api/register', {
                
            })
        }
    }

}