import React, { useEffect } from "react";

function MyMapComponent() {
  const newScript = (src) => {
    return new Promise((resolve, reject) => {
      const script = document.createElement("script");
      script.src = src;
      script.addEventListener("load", () => {
        resolve();
      });
      script.addEventListener("error", (e) => {
        reject(e);
      });
      document.head.appendChild(script);
    });
  };

  useEffect(() => {
    const myScript = newScript(
      "https://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=c8ba5cea9a2e465594e024fd6b506ea2"
    );

    myScript.then(() => {
      const kakao = window.kakao;
      kakao.maps.load(() => {
        const mapContainer = document.getElementById("map");
        const options = {
          center: new kakao.maps.LatLng(37.56000302825312, 126.97540593203321), // 중심 좌표 설정 (예시 좌표)
          level: 3,
        };
        const map = new kakao.maps.Map(mapContainer, options);

        // 편의점 위치 정보 (예시)
        const convenienceStoreLocations = [
          { name: "편의점 1", lat: 37.561, lng: 126.975 },
          { name: "편의점 2", lat: 37.562, lng: 126.976 },
          // 다른 편의점들의 위치도 추가
        ];

        // 현재 위치 정보 (예시)
        const currentLocation = new kakao.maps.LatLng(
          37.56200302825312,
          126.97740593203321
        );

        // 사용자 이미지 설정
        const userMarkerImage = new kakao.maps.MarkerImage(
          `${process.env.PUBLIC_URL}/user.jpeg`, // 사용자 아이콘 이미지 파일 경로
          new kakao.maps.Size(32, 37),
          { offset: new kakao.maps.Point(16, 37) }
        );

        // 편의점 이미지 설정
        const convenienceStoreMarkerImage = new kakao.maps.MarkerImage(
          `${process.env.PUBLIC_URL}/conve.jpeg`, // 편의점 아이콘 이미지 파일 경로
          new kakao.maps.Size(32, 37),
          { offset: new kakao.maps.Point(16, 37) }
        );

        // 사용자 위치 마커 생성
        const userMarker = new kakao.maps.Marker({
          position: currentLocation,
          image: userMarkerImage,
        });
        userMarker.setMap(map);

        // 편의점 위치 마커 생성
        convenienceStoreLocations.forEach((location) => {
          const markerPosition = new kakao.maps.LatLng(
            location.lat,
            location.lng
          );
          const convenienceStoreMarker = new kakao.maps.Marker({
            position: markerPosition,
            image: convenienceStoreMarkerImage,
          });
          convenienceStoreMarker.setMap(map);
        });
      });
    });
  }, []);

  return (
    <div className="App">
      <div
        id="map"
        className="map"
        style={{ width: "100%", height: "300px", margin: "auto" }}
      ></div>
    </div>
  );
}

export default MyMapComponent;
