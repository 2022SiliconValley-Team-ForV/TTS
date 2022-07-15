import React from 'react'
import style from '../Styles/Detail.module.css';
import profile from '../Images/images.jpg';

function Detail() {

// 데이터 베이스에서 받아온다.
//나중에 Detail 함수에 변수 넣을 거임
//지금은 테스트

  const name = "김혜진";
  const birth = "2000/02/17";
  const tmi = "asdkjfalksdfj";

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
            <div>tmi={tmi}</div>

            <div className={style.playbar}>
              {/* input button 수평 안맞음 */}
              <input placeholder="적고 싶은 말을 적으세요" className={style.write}/>
              <button className={style.play}></button>
            </div>

          </div>

        </div>

      </div>

    </div>
  )
}

export default Detail
