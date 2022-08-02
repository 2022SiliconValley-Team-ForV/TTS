import React,  { useState,useEffect } from 'react'
import { useParams } from 'react-router-dom';
import style from '../Styles/Detail.module.css';
import axios from "axios";
import Header from './Header';
import { v4 as uuid } from 'uuid';



function Detail() {
  //loading 다 되면 setLoading에 false를 넣어서 보이게 해줌
  const [loading, setLoading] = useState(true);

  // input태그 value값 저장
  const [sentence, setSentence]=useState();

  // id값 받아서 DB에서 가져온 데이터 저장
  const [getinfo, setGetinfo]=useState([]);

  // uuid값 저장
  const [userid, setUserid]=useState();

  // flask에서 받은 response 값 저장
  const [geturl, setGeturl]=useState();

  //사이트 :id에서 id값 가져오기
  let { id } = useParams([]);
  
  function notShowsend(){
    const show = document.getElementsByClassName('send');
    if(show.style.display == 'none'){
      show.style.display='inline-block';
    }
  }
  function showPlay(){
    const notshow=document.getElementsByClassName('playbutton');
    if(notshow.style.display == 'inline-block'){
      notshow.style.display='none';
    }
  }


  //url 한번만 부르기
  useEffect(()=>{
    axios.get(`http://127.0.0.1:8000/api/members/${id}`)
    .then((response)=>{
      setGetinfo(response.data);
      setLoading(false);
      setUserid(uuid());
    })
    .catch(function(error){
      console.log(error);
    });
  },[]);

  // uuid 가져오기
  useEffect(()=>{setUserid(uuid());}, []);

  //input 태그에 적힌 글 sentence에 저장
  const onChange=(e)=>{
    const value=e.target.value
    setSentence(value);
  }

  //sendbutton 이벤트
  const onClick=(e)=>{ 
    // audio1.play();
    if(sentence==null || sentence ===""){
      alert("문장을 적어주세요.");
    }
    else{
      // e.preventDefatul();
      const time = new Date();
      const date = time.getFullYear()+'-'+time.getMonth()+'-'+time.getDate()+'-'+
                  time.getHours()+':'+time.getMinutes()+':'+time.getSeconds();
      
      console.log(sentence, date);
      // const data={uuid: userid, member_id:`${id}`, text:sentence};
      const data={uuid: userid, member_id:`${id}`, text:sentence, created_at:date};
      
      axios.post(`http://127.0.0.1:8000/api/texts/`, data)
      .then((response)=>{
        console.log(response);
        console.log(data);
      })
      .catch((error)=>{
        console.log(error);
      })

      axios.post(`http://127.0.0.1:5000/api/texts`, data)
      .then((response)=>{
        console.log(response);
        console.log(data);
        setGeturl(`https://storage.googleapis.com/forv_bucket/wav_files/${response.data.member_id}/${response.data.uuid}_${response.data.created_at}_voice.wav`);
        alert("변환이 완료되었습니다.");
        showPlay();
        
      })
      .catch((error)=>{
        console.log(error);
      })
      
    }
  }
  const onClickplay=()=>{
    const audio = new Audio(geturl);
    audio.play();

  }


  //깃허브 링크 이동
  const onClickGit=(e) =>{
    window.open(`https://github.com/${getinfo.githubID}`, '_blank');
  }


  return (

    <div>
      {loading ? <div></div>:
      <div id={style.wrap}>
    
        <Header/>

        <div id={style.profilewrap}>
          <div className={style.position}>FRONTEND</div>
          <div id={style.wrapdetail}>

            <div className={style.bigprofile}>
              <img src={getinfo.image_link} alt="profile"></img>
            </div>

            <div className={style.info}> 
            
              <div className={style.deco}></div>  
              <div className={style.wrapinfo}>
                <div className={style.info_name} style={{fontSize: '1.6rem', fontWeight:'bold'}}> 
                    {getinfo.name} 
                    <button onClick={onClickGit} id={style.github} className={style.botton}></button>
                   
                </div>
                <div>{getinfo.birth}</div>
                <br/>
                <br/>
                  
                <div className={style.tmi_txt} style={{wordBreak:"keep-all"}}>{getinfo.tmi}.</div> 
              </div> 
              
               

              <div className={style.playbar}>
                <input placeholder=" 적고 싶은 말을 적으세요" className={style.write}
                  onChange={onChange}></input>
                <button onClick={onClick} className={style.send}>send</button>
                <button className={style.playbutton} onClick={onClickplay}>play</button>
              </div>
               
                
            </div>
          </div>
        </div>

        <div className={style.play_wrap}>
          
        </div>
      </div>}
    </div>
     
  )
}

export default Detail