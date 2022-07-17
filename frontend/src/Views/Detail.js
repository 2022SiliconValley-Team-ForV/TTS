import React,  {useState} from 'react'
import { Link } from 'react-router-dom';
import style from '../Styles/Detail.module.css';
import profile from '../Images/bomb.png';

function Detail() {

// 데이터 베이스에서 받아온다.
//나중에 Detail 함수에 변수 넣을 거임
//지금은 테스트

  const name = "김혜진";
  const birth = "2000/02/17";
  const tmi = "포켓몬이랑 오구랑 커비 좋아함";
  const position = "FRONTEND";

  const [sentence, setSentence]=useState();
  
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
            <div class={style.position}>{position}</div>
            <div id={style.wrapdetail}>

              <div className={style.bigprofile}>
                <img src={profile} alt="profile"></img>
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
                  <div style={{fontSize: '1.6rem', fontWeight:'bold'}}>{name}</div>
                  <div>{birth}</div>
                  <br/>
                  <div><br/> {tmi}</div>
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
