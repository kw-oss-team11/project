import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";
import './PostForm.css'
import './GlobalStyles.css';

const PostForm = ({ addPost }) => {
  const [newPost, setNewPost] = useState({ id: 0, title: '', content: '', item: '' });

  const navigate = useNavigate();

  const goToList = () => {
      navigate("/postlist");
  }

  const handleAddPost = () => {
    addPost(newPost);
    setNewPost({ id: 0, title: '', content: '', item: '' });
  };

  return (
    <div className="post-form">
      <h1>새 게시물 추가</h1>
      <input
        type="text"
        placeholder="제목"
        value={newPost.title}
        onChange={(e) => setNewPost({ ...newPost, title: e.target.value })}
      />
      <input
        type="text"
        placeholder="원하는 상품"
        value={newPost.item}
        onChange={(e) => setNewPost({ ...newPost, item: e.target.value })}
      />
      <textarea
        placeholder="내용"
        value={newPost.content}
        onChange={(e) => setNewPost({ ...newPost, content: e.target.value })}
      />
      <button onClick={() => {
      handleAddPost();
      goToList();
    }}>추가</button>
    </div>
  );
}

export default PostForm;
