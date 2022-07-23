import React from 'react'
import {Link} from "react-router-dom";
import Style from '../Styles/Make.module.css'
import Header from './Header'
import { AiOutlineCloudUpload } from "react-icons/ai";


function Make() {

  

  return (
    
  // <div id={Style.master}>
    <div id={Style.wrap}>
      
      {/* //로고 누르면 홈으로 돌아가게 구현 */}
      <Link to="/" style={{textDecoration:'none'}}>
        <Header/>
      </Link>

      <div className={Style.upload_big_area}>
   
       <div className={Style.upload_area}>
             <AiOutlineCloudUpload 
               size ="80" 
               color="#2F2E6F"/><br/>

            <header >Browser to upload</header> 
            <div>upload file and click button</div>
       </div>

       <button className={Style.convert}>Upload</button>
       
      </ div>

         <div className={Style.convertEnd}>
            <div className={Style.readyMakeTTS}>Ready To TTS !</div>
              <div className={Style.playbar}>
                 <input placeholder=" 적고 싶은 말을 적으세요" className={Style.write}/>
                 <button className={Style.play}>Play</button>
              </div>
              
         </div>

    </div>
//  </div>
   
  )
}

export default Make