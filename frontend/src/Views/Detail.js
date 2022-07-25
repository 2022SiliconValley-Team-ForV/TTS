import React,  { useState,useEffect } from 'react'
import { Link,useParams } from 'react-router-dom';
import style from '../Styles/Detail.module.css';
import axios from "axios";
import Header from './Header'

function Detail() {

  //loading 다 되면 setLoading에 false를 넣어서 보이게 해준다.
  const [loading, setLoading] = useState(true);

  // input태그에 넣을거
  const [sentence, setSentence]=useState();

  // id값 받아서 DB에서 가져온 데이터 넣는곳
  const [getinfo, setGetinfo]=useState([]);

  //사이트 :id에서 id값 가져오기
  let { id } = useParams([]);

  //url 한번만 부르기
  useEffect(()=>{
    axios.get(`http://127.0.0.1:8000/api/members/${id}`)
    .then((response)=>{
      setGetinfo(response.data);
      setLoading(false);
    })
    .catch(function(error){
      console.log(error);
    });
  },[])

  //input 태그에 적힌 글 sentence에 저장
  const onChange=(e)=>{
    const value=e.target.value
    setSentence(value);
  }

  //playbutton 이벤트
  const onClick=(e)=>{
    //버튼 누르면 서버로 글씨 올리기 구현 해야함
    if(sentence==null || sentence ===""){
      alert("문장을 적어주세요.");
    }
    else{
      console.log(sentence);
    }
    
  }

  return (

    <div>
      {loading ? <></>:
      <div id={style.wrap}>
        <Link to="/" style={{textDecoration:'none'}}>
          <Header/>
        </Link>
      

        <div id={style.profilewrap}>
          <div class={style.position}>FRONTEND</div>
          <div id={style.wrapdetail}>

            <div className={style.bigprofile}>
              <img src={getinfo.image_link} alt="profile"></img>
            </div>

            <div className={style.info}> 
           
              <div className={style.deco}></div>  
              <div className={style.gitinfo}>
                <div className={style.wrapinfo}>
                  <div style={{fontSize: '1.6rem', fontWeight:'bold'}}>{getinfo.name}</div>
                  <br/>
                  <div>{getinfo.birth}</div>
                  <div>{getinfo.tmi}.</div> 
                </div> 

                <div class={style.buttons}>
                  <button id={style.github} className={style.botton}></button>
                </div>
              </div>
              
               

              <div className={style.playbar}>
                <input placeholder=" 적고 싶은 말을 적으세요" className={style.write}
                  onChange={onChange}></input>
                <button onClick={onClick} className={style.play}></button>
              </div>
               
                
            </div>
          </div>
        </div>
      </div>}
    </div>
     
  )
}

export default Detail