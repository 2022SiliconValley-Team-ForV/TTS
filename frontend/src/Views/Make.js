import React from 'react'
import {Link} from "react-router-dom";
import Style from '../Styles/Make.module.css'
import { AiOutlineCloudUpload } from "react-icons/ai";


function Make() {



  return (
    
  <div id={Style.master}>
    <div id={Style.wrap}>
      {/* //로고 누르면 홈으로 돌아가게 구현 */}
      <Link to="/" style={{textDecoration:'none'}}>
        <div className={Style.logo}>TFV</div>
      </Link>
      <hr/>

      <div className={Style.upload_big_area}>
   
       <div className={Style.upload_area}>
             <AiOutlineCloudUpload 
               size ="80" 
               color="#2F2E6F"/><br/>

            <header >Browser to upload</header> 
            <div>upload file and click button</div>
       </div>

       <button className={Style.convert}>convert</button>
       
      </ div>

         <div className={Style.convertEnd}>
            <h className={Style.readyMakeTTS}>Ready To TTS !</h>
              <div className={Style.playbar}>
                 <input placeholder=" 적고 싶은 말을 적으세요" className={Style.write}/>
                 <button className={Style.play}></button>
              </div>
         </div>

    </div>
 </div>
   
  )
}

export default Make