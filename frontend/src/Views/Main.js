import React from 'react'
import Style from '../Styles/Main.module.css'
import { Link } from 'react-router-dom';
import profile from '../Images/bomb.png';


function Main() {
  
  const onClick=()=>{
    console.log("clicked!");
  };

  return (
    <div id={Style.master}>

      <div id={Style.wrap}>

        <div className={Style.member}>Member</div>
        <div className={Style.logo}>TFV</div>
        
        <hr/>

        <div className={Style.profiles}>

          <Link to = "/Detail/1">
            <div id={Style.first} className={Style.profile}>
              <img className={Style.circle}
              src={profile} alt="profile"/>
              <div className={Style.name}>구지혜</div>
            </div>    
          </Link> 

          <Link to = "/Detail/2">
            <div id={Style.second} >
              <img className={Style.circle}
              src={profile} alt="profile"/>
              <div className={Style.name}>김혜진</div>
            </div>    
          </Link>  

          <Link to = "/Detail/3">
            <div id={Style.third} >
              <img className={Style.circle}
              src={profile} alt="profile"/>
              <div className={Style.name}>배준일</div>
            </div>    
          </Link>  

          <Link to = "/Detail/4">
            <div id={Style.fourth} >
              <img className={Style.circle}
              src={profile} alt="profile"/>
              <div className={Style.name}>최준혁</div>
            </div>    
          </Link>  

          <Link to = "/Detail/5">
            <div id={Style.fifth} >
              <img className={Style.circle}
              src={profile} alt="profile"/>
              <div className={Style.name}>이수현</div>
            </div>    
          </Link>  

                  

           {/*<Link to = "/Detail/2">
            <div id={Style.second} className={Style.circle}>
              <div className={Style.name}>김혜진</div>
            </div>          
          </Link>           

          <Link to = "/Detail/3">
            <div id={Style.third} className={Style.circle}>
              <div className={Style.name}>배준일</div>
            </div>
          </Link>

          <Link to = "/Detail/4">
            <div id={Style.fourth} className={Style.circle}>
              <div className={Style.name}>최준혁</div>
            </div>          
          </Link>

          <Link to = "/Detail/5">
            <div id={Style.fifth} className={Style.circle}>
              <div className={Style.name}>이수현</div>
            </div>          
          </Link>    */}
        </div>


        <div className={Style.tts}>
          <div className={Style.maketext}>내 목소리로 TTS를 만들고 싶다면</div>
            <Link to="/maketts">
              <button
              className={Style.maketts}
              onClick={onClick}>
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

    </div>
  )
}

export default Main
