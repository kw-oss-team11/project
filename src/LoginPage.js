import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useUser } from "./UserContext";
import "./GlobalStyles.css";
import "./LoginPage.css";

function LoginPage() {
  const { user } = useUser(); // 사용자 정보 읽어옴
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loggedIn, setLoggedIn] = useState(false);
  const navigate = useNavigate();

  const goToPost = () => {
    navigate("/postlist");
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter") {
      handleLogin();
    }
  };

  const handleLogin = async () => {
    try {
      if (user && user.email === email && user.password === password) {
        setLoggedIn(true);
        goToPost();
      } else alert("로그인 실패");
    } catch (error) {
      console.error("로그인 실패", error);
    }
  };

  return (
    <div className="login-page">
      <h1>구매대행 사이트</h1>
      {loggedIn ? (
        <p>로그인 성공!</p>
      ) : (
        <div className="login-form">
          <input
            type="email"
            placeholder="아이디"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            onKeyPress={handleKeyPress}
          />
          <input
            type="password"
            placeholder="비밀번호"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            onKeyPress={handleKeyPress}
          />
          <button onClick={handleLogin}>로그인</button>
        </div>
      )}
      <br />
      <a href="/signup">회원가입</a>
    </div>
  );
}

export default LoginPage;
