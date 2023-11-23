# 구매대행 - by. 백색 태양의 일격(팀 11)

---

## 📚 Project Overview

- Project Period: 2023.10.20 ~ 2023.11.23

- Project Presentation File: [최종발표자료.pdf](여기에 업로드 후 주소 넣기)

- Project Wrap-up Report: [최종보고서.pdf](여기에 업로드 후 주소 넣기)

## 🏪 편의점 구매대행 😊

**구매** **대**량으로 같이 해서 **행**복해요

프로젝트 시연.gif(완성 후에 추가)

### 😎 Members

**광운대학교**
| [이동호](https://github.com/malchaa) | [이준석](https://github.com/hansanlee1208) | [장기현](https://github.com/Janggihyeon) | [최진우](https://github.com/wlsgudy3) | [황정묵](https://github.com/hwangjello) |
| --- | --- | --- | --- | --- |
| 소프트웨어학부 | 수학과 | 소프트웨어학부 | 소프트웨어학부 | 수학과 |

### 🤗 Contribution

- 이동호: 로그인 및 회원가입, 행사 물품 목록 확인, 회원 이름으로 QR 생성
- 이준석: 사용자 간 채팅
- 장기현: 주변 편의점 확인
- 최진우: 포스트 기능
- 황정묵: 챗봇 시스템

## **❓ About This Project**
- 로그인 및 회원가입 기능
- 주변 편의점 확인
- 행사 물품 목록 확인
- 챗봇 시스템
- 포스트 기능
- 회원 이름으로 QR 생성
- 사용자 간 채팅
  
### Purpose

- 편의점 1+1, 2+1 상품들을 공동 구매하여 원하는 양만, 값싸게 살 수 있도록 한다.

### Objective

- 공동 구매를 원하는 사람을 모집할 수 있는 웹페이지
- 모집한 공동 구매원 간의 채팅 기능
- 지도 API를 이용하여 근처 편의점을 확인하는 기능
- 크롤링을 이용하여 편의점 브랜드별 행사정보를 모아보는 기능
- 구매 물품을 추천해주는 챗봇 기능

## 🗺 Service Architecture

![Service Architecture](링크는 지워두기)

## 💾 Datasets

크롤링에 사용한 페이지

- CU 편의점 ([Link](https://cu.bgfretail.com/event/plus.do?category=event&depth2=1&sf=N))
- GS25 편의점 ([Link](http://gs25.gsretail.com/gscvs/ko/products/event-goods))
- 세븐일레븐 편의점 ([Link](https://www.7-eleven.co.kr/product/presentList.asp))

## 💻 **Development Environment**

- windows 10, 11
- Python 3.10.9

## 📁 Project Structure (Main branch)

(다 완성한 후에 수정)

```markdown
final-project-level3-cv-16
├─ api_folder
│ ├─ .streamlit
| | └─ config.toml
│ ├─ backend
| | ├─ epillid_benchmark(cloned from Link)
| | ├─ Dockerfile
| | ├─ Backend.py
| | └─ requirements.txt
│ ├─ frontend
| | ├─ Dockerfile
| | ├─ frontend.py
| | └─ requirements.txt
│ └─ Docker
| └─ docker-compose.yml  
└─ image_classification
├─ data_preprocessing
| ├─ download_pill_data.py
| └─ normalize_pill_data.py
├─ image_concatenation
| └─ concatenation_images.py
├─ kaggle_pill_data_preprocessing
| ├─ 1_annotation_file_name_to_txt.py
| ├─ 2_edit_xml_path.py
| └─ 3_xml_to_json.py
├─ pill_excel_data
| └─ README.md
├─ .gitignore
├─ data.py
├─ dataset.py
├─ log.py
└─ train.py
```

## 🚀 How to Start

1. python 환경 설치

2. 실행에 필요한 모듈 설치
   
   ```
   pip install -r requirements.txt
   ```
   *관리자 권한으로 실행해서 설치하는 것을 권장합니다.

   2.1 chatting을 위해서는 docker를 설치해야한다.
   [docker 설치](https://www.docker.com/get-started/)
   설치한 후에 쉘을 다시 실행하고, 아래 명령으로 설치 확인

   ```
   docker -v
   ```

   2.2 docker 실행

   ```
   docker run -p 6379:6379 -d redis:5
   ```

   참고 : 아래 명령은 순서대로 실행중인 컨테이너 확인, 중지, 중지된 컨테이너 확인, 삭제이다
   
   ```
   docker ps
   docker stop [컨테이너 이름 또는 ID]
   docker ps -a
   docker rm [컨테이너 이름 또는 ID]
   ```

3. crawling 폴더로 이동해 크롤링을 실시한다.
   ```python
   cd ./crawling # 크롤링 폴더로 이동
   python crawling_CU.py
   python crawling_GS.py
   python crawling_SE.py
   ```
   위와 같이 실행한다면 CSV파일이 생성된다. 이를 토대로 이미지를 다운받는다.
   ```python
   python CU_Images.py
   python GS_Images.py
   python SE_Images.py
   ```
4. 다시 project 폴더로 돌아가서 서버 실행
   ```
   cd .. # project 폴더로 이동
   python manage.py runserver
   ```
5. 서버를 실행했을 때 나오는 주소로 이동하면 로컬 환경에서 실행해볼 수 있다. [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 🔎 Future Research

이것도 완성하고 따져봅시다

- 모델의 정확도 향상 및 inference time 단축
- Mobile Application 제작
- 실용성 향상
- OCR 적용

## 📎 Appendix

📄 [Experiments & Submission Report](링크는 지워두기)

## 📜 Reference

- ePillID Dataset: A Low-Shot Fine-Grained Benchmark for Pill Identification ([Link]링크는 지워두기)
- YOLACT: Real-time Instance Segmentation ([Link]링크는 지워두기)
