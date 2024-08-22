import React from 'react';

import '../styles/icons/icons.css';


const Icons = () => {
    return (
        <div className='project-icons'>
            <h3>Technologies used in this project</h3>
            <div className='icons'>
                <img src="./django.svg" alt="Django"/>
                <img src="/python.svg" alt="Python"/>
                <img src="/bootstrap.svg" alt="Bootstrap"/>
                <img src="/react.svg" alt="React"/>
            </div>
        </div>
    );
};


export default Icons;