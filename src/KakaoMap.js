import React, { useEffect } from "react";

const KakaoMap = () => {
  useEffect(() => {
    const { kakao } = window;

    if (kakao && kakao.maps) {
      // Kakao 맵 초기화 코드를 실행합니다.
      // eslint-disable-next-line
      const map = new kakao.maps.Map(document.getElementById("map"), {
        center: new kakao.maps.LatLng(37.566826, 126.978656), // 예시 좌표
        level: 3, // 지도 확대 레벨
      });
    } else {
      console.error("Kakao maps 객체를 찾을 수 없습니다.");
    }
  }, []); // 빈 배열을 두 번째 인수로 전달하여 컴포넌트가 마운트될 때 한 번만 실행되도록 합니다.

  return <div id="map" style={{ width: "100%", height: "400px" }}></div>;
};

export default KakaoMap;
