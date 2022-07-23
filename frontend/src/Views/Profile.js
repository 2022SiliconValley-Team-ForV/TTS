import React from 'react';
import style from '../Styles/Profile.module.css'
import {Link} from "react-router-dom";

function Profile({id, name, img}) {

  const PHOTO = img;
  
  return (
    <Link to={{
      pathname: `/detail/${id}`,
      state:{id:id}
    }} style={{textDecoration:'none'}}>
      <div id={style.wrapprofile}>
        <img src={PHOTO} alt="profile" className={style.photo}></img>
        <p>{name}</p>
      </div>
    </Link>



  )
}

export default Profile
