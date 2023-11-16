# 구매대행 - by. 백색 태양의 일격(팀 11)

---

## 📚 Project Overview

- Project Period: 2023.10.00 ~ 2023.11.00

- Project Presentation File: [최종발표자료.pdf](여기에 업로드 후 주소 넣기)

- Project Wrap-up Report: [최종보고서.pdf](여기에 업로드 후 주소 넣기)


## 👀 너의 알약이 보여 💊

- Metric Learning을 활용한 Reverse Pill Image Search
- streamlit 실행 예시

![프로젝트 시연.gif](링크는 지워두기)

### 😎 Members

| [이동호](https://github.com/malchaa) | [이준석](https://github.com/hansanlee1208) | [장기현](https://github.com/Janggihyeon) | [최진우](https://github.com/wlsgudy3) | [황정묵](https://github.com/hwangjello) |
| --- | --- | --- | --- | --- |
| ![이동호](얼굴사진 링크인데) | ![이준석](필요없을듯?) | ![장기현](이하생략) | ![최진우](깔쌈하게넣기?) | ![황정묵](고민) |

### 🤗 Contribution

- 이동호: FastAPI, BentoML, streamlit, GCP, OCR, Text Recognition
- 이준석: FastAPI, streamlit, OCR, Text Recognition
- 장기현: Data EDA, Data Pre-processing, Image Classification, Custom Dataset Production
- 최진우: Metric learning, Segmentation, Database, Docker
- 황정묵: Data EDA, Data Pre-processing, Data Annotation, OCR, Text Recognition

## **❓ About This Project**

### Purpose

- 구매 대량으로 해서 함께 행복해져용

### Objective

- 사용자의 **알약 이미지**로부터 **성상, 제형, 색상**을 식별 후 조건에 맞는 알약을 검색하여 알약의 **종류**를 식별한다.

### Target Audience

- 지리적, 물리적 한계로 약국이나 병원을 방문하기 어려운 사람
- 알약은 있지만 알약을 구분할 수 없는 사람

### Background Information

- 종종 일어나는 처방 실수, 및 착각으로 인한 약물사고를 예방하고자 하였다.
- 실제 보건 계열 종사자에 따르면 노년 층의 경우 어떤 알약인지 병원에 방문하여 알약을 찾는 경우가 존재한다고 하며, 한국의 통계를 보았을 때도 약물 오복용에 의한 사고는 줄지 않고 계속 유지되고 있는 추세이다.

## 🗺 Service Architecture

![Service Architecture](링크는 지워두기)

## 💾 Datasets

- 의약품 안전나라 데이터 ([Link](링크는 지워두기)
- ePillID Benchmark ([Link](링크는 지워두기)
- 기타 이미지 데이터 ([Link](링크는 지워두기)
    - Classification 및 Object Detection을 위해 직접 촬영 및 수집한, 라이센스가 없는 이미지들

## 💻 **Development Environment**

- GPU: Tesla V100
- OS: Ubuntu 18.04.5LTS
- CPU: Intel Xeon
- Python : 3.8.5 / 3.9.13

## 📁 Project Structure (Main branch)

```markdown
final-project-level3-cv-16
├─ api_folder
│   ├─ .streamlit
|   |   └─ config.toml
│   ├─ backend
|   |   ├─ epillid_benchmark(cloned from Link)
|   |   ├─ Dockerfile
|   |   ├─ Backend.py
|   |   └─ requirements.txt
│   ├─ frontend
|   |   ├─ Dockerfile
|   |   ├─ frontend.py
|   |   └─ requirements.txt
│   └─ Docker
|       └─ docker-compose.yml  
└─ image_classification
    ├─ data_preprocessing
    |   ├─ download_pill_data.py 
    |   └─ normalize_pill_data.py
    ├─ image_concatenation
    |   └─ concatenation_images.py
    ├─ kaggle_pill_data_preprocessing
    |   ├─ 1_annotation_file_name_to_txt.py
    |   ├─ 2_edit_xml_path.py
    |   └─ 3_xml_to_json.py
    ├─ pill_excel_data
    |   └─ README.md
    ├─ .gitignore
    ├─ data.py
    ├─ dataset.py
    ├─ log.py
    └─ train.py
```

## ✏️ Evaluation

- Top-1 accuracy: 43%
- Top-5 accuracy: 80%

## 🚀 How to Start

1. Image Classification: [Link](링크는 지워두기)
    
2. OCR: [Link](링크는 지워두기)
    
3. Object Detection (yolov5): [Link](링크는 지워두기)

4. Metric learning: [Link](링크는 지워두기)

## 🔎 Future Research

- 모델의 정확도 향상 및 inference time 단축
- Mobile Application 제작
- 실용성 향상
- OCR 적용

## 📎 Appendix

📄 [Experiments & Submission Report](링크는 지워두기)

## 📜 Reference

- ePillID Dataset: A Low-Shot Fine-Grained Benchmark for Pill Identification ([Link]링크는 지워두기)
- YOLACT: Real-time Instance Segmentation ([Link]링크는 지워두기)

