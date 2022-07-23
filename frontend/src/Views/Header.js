import React from 'react'
import Style from '../Styles/Header.module.css'

function Header() {
  return (

    <div id={Style.wrap_logo}>
        <div className={Style.logo}>TFV</div>
        <div className={Style.member}>Member</div>
          
        <hr/>
    </div>

  )
}

export default Header
