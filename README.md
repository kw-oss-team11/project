# 구매대행 - by. 백색 태양의 일격(팀 11)

---

## 📚 Project Overview

- Project Period: 2023.10.00 ~ 2023.11.00

- Project Presentation File: [최종발표자료.pdf](여기에 업로드 후 주소 넣기)

- Project Wrap-up Report: [최종보고서.pdf](여기에 업로드 후 주소 넣기)

## 🏪 편의점 구매대행 😊

**구매** **대**량으로 같이 해서 **행**복해요

프로젝트 시연.gif(완성 후에 추가)

### 😎 Members

**광운대학교**
| [이동호](https://github.com/malchaa) | [이준석](https://github.com/hansanlee1208) | [장기현](https://github.com/Janggihyeon) | [최진우](https://github.com/wlsgudy3) | [황정묵](https://github.com/hwangjello) |
| --- | --- | --- | --- | --- |
| 소프트웨어학부 | 2019603016 | 소프트웨어학부 | 소프트웨어학부 | 2019603016 |

### 🤗 Contribution

- 이동호: 크롤링
- 이준석: 채팅
- 장기현: 지도
- 최진우: 게시물
- 황정묵: 챗봇

## **❓ About This Project**

### Purpose

- 편의점 1+1, 2+1 상품들을 공동 구매하여 원하는 양만, 싸게 살 수 있게 한다.

### Objective

- 공동 구매를 원하는 사람을 모집할 수 있는 웹페이지
- 모집한 공동 구매원 간의 채팅 기능
- 지도 API를 이용하여 근처 편의점을 확인하는 기능
- 크롤링을 이용하여 편의점 브랜드별 행사정보를 모아보는 기능
- 구매 물품을 추천해주는 챗봇 기능

### Target Audience

- 1+1, 2+1 제품을 구매했을 때, 쉽게 소비하기 어려운 사람, 대학교 자취생
- 가격에 대한 부담으로 더 싸게 구매하고 싶은 사람

### Background Information

- 1인 가구의 수는 점점 증가하고 있다.
- 물가의 상승으로 식비에 대한 부담이 커져가고 있다. 행사 상품 구매로 부담을 줄일 수 있다.

## 🗺 Service Architecture

![Service Architecture](링크는 지워두기)

## 💾 Datasets

크롤링에 사용한 페이지

- CU 편의점 ([Link](https://cu.bgfretail.com/event/plus.do?category=event&depth2=1&sf=N))
- GS25 편의점 ([Link](http://gs25.gsretail.com/gscvs/ko/products/event-goods))
- 세븐일레븐 편의점 ([Link](https://www.7-eleven.co.kr/product/presentList.asp))

## 💻 **Development Environment**

- window 환경
- Python (버전은 모르겠음)

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

## ✏️ Evaluation

평가도 일단 다 완성하고 작성

- Top-1 accuracy: 43%
- Top-5 accuracy: 80%

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

3. project/crawling 폴더에 있는 crwaling.py 실행
   ```python
   python crwaling.py
   ```
4. 다시 project 폴더로 돌아가서 서버 실행
   ```
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
