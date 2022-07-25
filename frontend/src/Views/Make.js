import React, { useRef } from 'react';
import Style from '../Styles/Make.module.css';
import { AiOutlineCloudUpload, AiFillCheckCircle } from "react-icons/ai";
import{useState}from 'react';
import { Link } from 'react-router-dom';
import Loading from './Loading';
import Header from './Header';
	

	

	function Make() {
	 
	const[uploadClick,setuploadClick]=useState("Browser to upload");
	const[files,setfiles]=useState(null);
	

	const [iconsUpload,seticonsUpload ]=useState({display:"block"});
	const [iconsReady,  seticonsReady ]=useState({display:"none"});
	const [loading, setLoading] = useState(false);
	

	const fileInputInfo = useRef(null);

	  const onConvert=(e)=>{
	    if(files==null){
	      alert("음성파일을 업로드 해주세요");
	    }
	    else{
	      setLoading(!loading);
	    }
	   }
	
	  const onAudioBtnClick = (event) =>{
	    fileInputInfo.current.click();
	  }
	  const onAudioGet =(e)=>{
	

	  const  file = e.target.files;
	  console.log(file);
	  setfiles(file);
	  setuploadClick("Click the convert button");
	 
	  seticonsUpload({display:"none"});
	  seticonsReady({ display:"block"});

	  }
	

	  return (
	    
	    <div id={Style.wrap}>
	      <Link to="/" style={{textDecoration:'none'}}>
	        <Header/>
	      </Link>
	      <div className={Style.upload_big_area}>    
	

          <input 
            ref={fileInputInfo}
            type="file"
            id="avatar" 
            name="avatar"
            style={{display:"none"}}
            accept="audio/*"
            onChange={onAudioGet}>

          </input>
            
      
          <div className={Style.upload_area} onClick={onAudioBtnClick}>
            <AiOutlineCloudUpload  
			  style={iconsUpload}
			  size ="70" 
			  color="#2F2E6F"
             
            />
    

              <AiFillCheckCircle  
                   size ="70" 
	               color="#2F2E6F"
	               style={iconsReady}
	               />

              <br/><header>{uploadClick}</header> 
              <div>upload file and click button</div>    
                    
            </div>
		

		   <div className={Style.loadingArea}>{ loading && <Loading />}
		   </div>

      
          <button className={Style.convert} onClick={onConvert}>convert</button> 
	      </div>
	

	      <div className={Style.convertEnd} style={{display:"none"}}>   
	        <h className={Style.readyMakeTTS}>Ready To TTS !</h>
	        <div className={Style.playbar}>
	          <input placeholder=" 적고 싶은 말을 적으세요" className={Style.write}/>
	          <button className={Style.play}></button>
	        </div>
	      </div>

	    </div>
		
	  )
	}
	

	export default Make