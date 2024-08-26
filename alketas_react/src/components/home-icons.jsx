import React from "react";
import '../styles/home-icons.css';

import Django from '../icons/django.svg';
import Python from '../icons/python.svg';
import Bootstrap from '../icons/bootstrap.svg';
import Reacti from '../icons/react.svg';
import MySQl from '../icons/mysql.svg';



const HomeIcons = () => {
    return (
        <div className="container">
            <div className="label">Technologies used in this project</div>
            <div className="icons">
                <img src={Django} alt="Django" />
                <img src={Python} alt="Python" />
                <img src={Bootstrap} alt="React" />
                <img src={Reacti} alt="Bootstrap" />
                <img src={MySQl} alt="Bootstrap" />
            </div>
        </div>
    );
};


export default HomeIcons;