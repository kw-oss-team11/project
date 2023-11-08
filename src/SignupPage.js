import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";
import { useUser } from './UserContext';
import './GlobalStyles.css';
import './LoginPage.css'

function SignupPage() {
  const { setUser } = useUser(); // 사용자 정보를 설정할 수 있는 setUser 함수
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const goToLogin = () => {
      navigate("/");
  }

  const handleSignup = () => {
    // 사용자 정보를 설정
    setUser({ email, password });
  };

  return (
    <div className="login-page">
      <h1>회원가입</h1>
      <div className="login-form">
      <input
        type="email"
        placeholder="아이디"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />
      <input
        type="password"
        placeholder="비밀번호"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button onClick={() => {
      handleSignup();
      goToLogin();
      
    }}>가입하기</button>
    </div>
    </div>
  );
}

export default SignupPage;
