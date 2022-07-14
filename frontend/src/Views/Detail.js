import React from 'react'
import style from '../Styles/Detail.module.css';
import profile from '../Images/images.jpg';

function Detail() {
  const name = "김혜진"
  return (
    <div>
      <div id={style.wrap}>
        <div id={style.profilewrap}>
          <div className={style.bigprofile}>
            <img src={profile} alt="profile"></img>
          </div>

          <div className={style.info}>
            <div>이름 : </div>
            <div>생년 월일</div>
            <input placeholder="적고 싶은 말을 적으세요" className={style.write}/>
          </div>
        </div>

      </div>

    </div>
  )
}

export default Detail
