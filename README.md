# Street Safe

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Flutter](https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging_Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-0db7ed?style=for-the-badge&logo=docker&logoColor=white)

> Automated road damage assessment powered by Vision Transformers, built for field teams, deployable anywhere.

---

## Overview

StreetSafe takes a road image and returns a structured damage report: defect type, severity level, and repair recommendation. The ML backbone is `google/vit-base-patch16-224` served via a FastAPI backend. Field teams access it through a Flutter mobile app; internal teams use a Streamlit dashboard. The whole backend ships as a Docker container.

---

## Features

| Feature | Description |
|---|---|
| ViT Classification | Classifies road damage (Potholes, Cracks, Surface Wear) using `google/vit-base-patch16-224` |
| Severity Mapping | Maps each defect class to High, Medium, or Low severity automatically |
| Repair Recommendations | Returns material requirements and estimated labor scope per defect type |
| Confidence Scoring | Includes match confidence in the JSON response for every prediction |
| Dual Frontend | Streamlit dashboard for internal use; Flutter app for field teams |
| Containerized Backend | Docker-ready — single command to spin up the API server |

---

## Tech Stack

```
ML Engine      : Hugging Face Transformers, PyTorch, PIL
Backend        : Python 3.13, FastAPI, Uvicorn
Web Dashboard  : Streamlit
Mobile         : Flutter (Dart)
DevOps         : Docker, Git LFS
```

---

## Author

[Gummadi Likith](https://github.com/glikith)
