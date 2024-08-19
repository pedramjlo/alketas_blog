import React, { useState } from 'react';


const SelectAvatar = () => {
    const [avatar, setAvatar] = useState(null);

    const hadleAvatarSelection = async (event) => {
        event.preventDefault();


    const response = await fetch('http://127.0.0.1:8000/api/select-avatar/', {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ avatar }),
    });

    // handle response 
    if (response.ok){
        window.location.href = '/'
    }

    else {
        alert("لظفا یک آواتار را انتخاب کنید!")
    }

    return (
        <div className='select-avatar'>
            <div className='avatar-container'>
                <form onSubmit={hadleAvatarSelection}>
                    <input type="file" onChange={(e) => setAvatar(e.target.files[0])} required />
                    <button type="submit">انتخاب آواتار</button>
                </form>
            </div>
        </div>
    );

}}; 


export default SelectAvatar;
