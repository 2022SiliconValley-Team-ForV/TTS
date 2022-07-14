import React from 'react'
import style from '../Styles/Detail.module.css';
import profile from '../Images/images.jpg';

function Detail() {

  const name = "김혜진";
  const birth = "2000/02/17";

  return (
    <div>

      <div id={style.wrap}>
        <div className={style.logo}>TFV</div>
        <hr className={style.hr}/>

        <div id={style.profilewrap}>
          <div className={style.bigprofile}>
            <img src={profile} alt="profile"></img>
          </div>

          <div className={style.info}>
            <div>이름 : {name}</div>
            <div>생년 월일 : {birth}</div>
            <input placeholder="적고 싶은 말을 적으세요" className={style.write}/>
          </div>

        </div>

      </div>

    </div>
  )
}

export default Detail
