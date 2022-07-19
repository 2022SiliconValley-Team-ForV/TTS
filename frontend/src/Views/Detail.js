import React,  { useState,useEffect } from 'react'
import { Link,useParams } from 'react-router-dom';
import style from '../Styles/Detail.module.css';
import axios from "axios";

function Detail({_id, name, position, birth, info}) {

  // input태그에 넣을거
  const [sentence, setSentence]=useState();
  const [getinfo, setGetinfo]=useState([]);

  let { id } = useParams([]);

  useEffect(()=>{
    axios.get(`http://127.0.0.1:8000/members/${id}`)
    .then((response)=>{
      setGetinfo(response.data);
      console.log(response.data);
    })
    .catch(function(error){
      console.log(error);
    });
  },[])

  console.log(getinfo);


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

      <div id={style.wrap}>

        {/* //로고 누르면 홈으로 돌아가게 구현 */}
        <Link to="/" style={{textDecoration:'none'}}>
          <div className={style.logo}>TFV</div>
        </Link>
        <hr/>

          <div id={style.profilewrap}>
            <div class={style.position}>FRONTEND</div>
            <div id={style.wrapdetail}>

              <div className={style.bigprofile}>
                <img src={getinfo.image_link} alt="profile"></img>
                <br/>
                <div class={style.buttons}>
                  <button id={style.github} className={style.botton}></button>
                  <button id={style.instar} className={style.botton}></button>
                  <button id={style.blog} className={style.botton}></button>
                </div>

              </div>

              <div className={style.info}>
                <div className={style.deco}/>
                <div className={style.wrapinfo}>
                  <div style={{fontSize: '1.6rem', fontWeight:'bold'}}>{getinfo.name}</div>
                  <div>{getinfo.birth}</div>
                  <br/>
                  <div><br/>{getinfo.tmi}.</div>
                </div>


                <div className={style.playbar}>

                  <input placeholder=" 적고 싶은 말을 적으세요" className={style.write}
                  onChange={onChange}></input>
                  <button onClick={onClick} className={style.play}></button>

                </div>

              </div>

            </div>

          </div>

      </div>

    </div>
  )
}

export default Detail
