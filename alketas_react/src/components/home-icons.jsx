import React from "react";
import '../styles/home-icons.css';



const HomeIcons = () => {
    return (
        <div className="container">
            <div className="label">Technologies used in this project</div>
            <div className="icons">
                <img src="/icons/django.svg" alt="Django" />
                <img src="/icons/python.svg" alt="Python" />
                <img src="/icons/react.svg" alt="React" />
                <img src="/icons/bootstrap.svg" alt="Bootstrap" />
            </div>
        </div>
    );
};


export default HomeIcons;