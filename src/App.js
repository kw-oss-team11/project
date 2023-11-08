import React, { useState } from "react";
import { Routes, Route, BrowserRouter } from "react-router-dom";
import PostList from "./PostList";
import LoginPage from "./LoginPage";
import PostForm from "./PostForm";
import SignupPage from "./SignupPage";
import { UserProvider } from "./UserContext";
import Chat from "./Chat";
import MyMapcomponent from "./MyMapcomponent";

function App() {
  const [posts, setPosts] = useState([
    { id: 1, title: "첫 번째 게시물", item: "포스틱", content: "게시물 내용" },
    {
      id: 2,
      title: "두 번째 게시물",
      item: "바나나킥",
      content: "게시물 내용",
    },
  ]);

  const addPost = (newPost) => {
    setPosts([...posts, newPost]);
  };

  const deletePost = (postId) => {
    const updatedPosts = posts.filter((post) => post.id !== postId);
    setPosts(updatedPosts);
  };
  return (
    <BrowserRouter>
      <UserProvider>
        <Routes>
          <Route path="/" element={<LoginPage />} />
          <Route
            path="/postlist"
            element={<PostList posts={posts} deletePost={deletePost} />}
          />
          <Route path="/postform" element={<PostForm addPost={addPost} />} />
          <Route path="/signup" element={<SignupPage />} />
          <Route path="/chatroom" element={<Chat />} />
          <Route path="/map" element={<MyMapcomponent />} />
          {/* 다른 페이지 라우팅 정보도 추가할 수 있습니다. */}
        </Routes>
      </UserProvider>
    </BrowserRouter>
  );
}

export default App;
