import React from 'react'
import style from '../Styles/Detail.module.css';
import profile from '../Images/images.jpg';

function Detail() {
  return (
    <div>
      <div id={style.wrap}>
        <div className={style.bigprofile}>
          {/* <img src={profile} alt="profile"></img> */}
          <input className={style.write}/>
        </div>
        <div className={style.info}></div>
      </div>
    </div>
  )
}

export default Detail
