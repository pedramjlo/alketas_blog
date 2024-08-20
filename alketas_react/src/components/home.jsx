import React from 'react';
import Navbar from './navbar';
import Icons from './icons';


import '../styles/home.css';



const HomePage = () => {
    return (
        <div className='home-container'>
            <Navbar />
            <div className='home-content'>

                <div className='home-content-parent'>
                    <div className='home-visuals'>
                        <img src="/images/idea.svg" alt="idea-illustration" />
                        <button id='visitor-button'>ورود به عنوان ویزیتور</button>
                    </div>

                    <div className='home-description'>
                        <p>به پروژه ی فول استک من خوش آمدید. من پدرام جلالی این وب اپلیکیشن فول اسنک نوشته شده با جنگو و ری اکت را صرفا برای رزومه شخصی خودم درست کرده ام. آلکتاس یک اب CRUD است که ری اکت از طریق متود fetch با اند پوینت های ویوهای DRF ارتباط برقرار میکند</p>
                        <Icons />
                    </div>
                </div>


            </div>
        </div>
    );
};

export default HomePage;    