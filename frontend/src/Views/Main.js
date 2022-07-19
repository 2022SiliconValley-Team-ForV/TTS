import React, { Component, useState, useEffect } from 'react'
import Style from '../Styles/Main.module.css'
import Profile from './Profile';
import { Link } from 'react-router-dom';
import profile from '../Images/bomb.png';
import axios from "axios";
// import datas from './data.json';


function Main() {

  const [member, setMember] = useState([]);
  useEffect(()=>{
    axios.get("http://127.0.0.1:8000/members/")
    .then((response)=>{
      setMember([...response.data]);

    })
    .catch(function(error){
      console.log(error);
    });
  },[])

 const profile = member.map((m)=>(
      <Profile 
        key={m.id} id={m.id} name={m.name} birth={m.birth}
        img={m.image_link} info={m.tmi}
        
      />
    ));

  return (
      <div id={Style.wrap}>
        <div className={Style.logo}>TFV</div>
        <div className={Style.member}>Member</div>
        
        
        <hr/>

        <div className={Style.profiles}>
            {profile}
        </div>


        <div className={Style.tts}>
          <div className={Style.maketext}>내 목소리로 TTS를 만들고 싶다면</div>
            
            <Link to="/maketts">
              <button className={Style.maketts}>
              만들어 보기
              </button>
            </Link>
            
        </div>

        <div className={Style.copyright}>
          <hr/>
          <footer>
            TUKorea 237, Sangideahakro, Sihungsi, Kungido, Republic of Korea TEL. 031-8041-1000<br/>
            Copyright © 2022 Team ForV.All Right Reserved.
          </footer>
        </div>

      </div>
  )
}

export default Main;
