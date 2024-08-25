import React from 'react';
import Navbar from './navbar';
import '../styles/home.css';
import HomeIcons from './home-icons';



const HomePage = () => {
    return(
        <div >
            <Navbar />
            <main className='home-main'>

                <div className='visuals'>
                    <img src="/images/idea.svg" alt="idea illustration" />
                    <button id='visitor-btn'>ورود به عنوان ویزیتور</button>
                </div>
                
                <div className='descriptions'>
                    <p>
                        آلکتاس به معنای پسر جوان و جسما قدرتمند. این بلاگ اپ با استفاده از ری اکت برای سمت کاربر و فریمورک جنگو برای سمت سرور. شامل قابلیت هایی از قبیل احراز هویت کاربر، ساخت پروفایل بعد از ثبت نام، اختصاص اجازه به پروفایل برای ساخت پست.
                    </p>

                    <div id='personal-info'></div>

                    <HomeIcons />
                </div>

            </main>
        </div>

    );
};


export default HomePage;