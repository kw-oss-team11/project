import React from 'react';
import { useNavigate } from "react-router-dom";
import './PostList.css';
import './GlobalStyles.css';

function PostList({ posts, deletePost }) {

  const navigate = useNavigate();

  const goToForm = () => {
      navigate("/postform");
  }

  const goToChat = () => {
    navigate("/chatroom");
  }

  return (
    <div className="post-list">
      <h1><a href="/">구매대행 웹사이트</a></h1>
      <h2>게시물 목록</h2>
      <button onClick={goToForm}>게시물 만들기</button>
      <button onClick={goToChat}>채팅방</button>
      <ul>
        {posts.map((post) => (
          <li key={post.id} className="post">
            <h2>{post.title}</h2>
            <p>원하는 상품 : {post.item}</p>
            <p>내용 : {post.content}</p>
            <button onClick={() => deletePost(post.id)}>삭제</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default PostList;
