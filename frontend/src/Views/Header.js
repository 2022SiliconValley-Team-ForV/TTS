import React from 'react'
import {Link} from "react-router-dom";
import Style from '../Styles/Header.module.css'

function Header() {

  return (
    
    <div id={Style.wrap_logo}>
      <Link to='/'>
        <div className={Style.logo}>TFV</div>
      </Link>
      <div className={Style.member}>Member</div>
      <hr/>
    </div>

  )
}

export default Header