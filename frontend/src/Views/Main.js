import React, { useState, useEffect } from 'react'
import Style from '../Styles/Main.module.css'
import Profile from './Profile';
import { Link } from 'react-router-dom';
import axios from "axios";
// import datas from './data.json';


function Main() {

  // DB에 받아온 데이터들을 넣는 곳
  const [member, setMember] = useState([]);

  //url에서 데이터를 한번만 받아온다.
  useEffect(()=>{
    axios.get("http://127.0.0.1:8000/members/")
    .then((response)=>{
      setMember([...response.data]);
    })
    .catch(function(error){
      console.log(error);
    });
  },[])

  // map를 사용해서 Profile 컴포넌트에 하나씩 넣어준다.
  const profile = member.map((m)=>(
      <Profile 
        key={m.id} id={m.id} name={m.name} birth={m.birth}
        img={m.image_link} info={m.tmi}
        
      />
    ));

  return (
      <div id={Style.wrap}>
        <div id={Style.wraplogo}>
            <div className={Style.logo}>TFV</div>
            <div className={Style.member}>Member</div>
          
            <hr/>
        </div>


        <div className={Style.wrapmiddle}>
          <div className={Style.profiletts}>
            <div className={Style.profiles}>{profile}</div>

            <div className={Style.tts}>
              <div className={Style.maketext}>내 목소리로 TTS를 만들고 싶다면</div>
                <Link to="/maketts">
                  <button className={Style.maketts}>
                    만들어 보기
                  </button>
                </Link>
            </div> 

          </div>


        </div>
 


        <div id={Style.wrapcopyright}>


          <hr/>
          <div>
            TUKorea 237, Sangideahakro, Sihungsi, Kungido, Republic of Korea TEL. 031-8041-1000
            <br/>Copyright © 2022 Team ForV.All Right Reserved.
          </div>
        </div>


      </div>

  )
}

export default Main;
