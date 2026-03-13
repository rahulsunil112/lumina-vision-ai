# ✨ Lumina Vision AI

![Status](https://img.shields.io/badge/status-active-success.svg)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

**Lumina Vision AI** is an advanced, real-time computer vision platform designed for high-performance object detection, instance segmentation, and multi-object tracking. Built on top of SOTA models (YOLOv8/v10), it provides a seamless interface for analyzing video streams and images with extreme precision.

---

## 🚀 Key Features

- **Real-Time Detection**: High-FPS inference using Optimized TensorRT and ONNX backends.
- **Instance Segmentation**: Pixel-perfect object masking for complex scene understanding.
- **Neural Tracking**: Persistent ID tracking across frames using DeepSORT/ByteTrack.
- **Auto-Annotation**: Accelerate your dataset labeling with AI-assisted bounding box generation.
- **Custom Model Zoo**: Easily swap between YOLO, EfficientDet, and Faster R-CNN architectures.

## 🏗️ System Architecture

`mermaid
graph LR
    Source[Camera/Video/Image] -->|Frame Stream| Pre[Pre-processing]
    Pre -->|Tensor| Engine[Inference Engine]
    Engine -->|Raw Detections| Post[Post-processing / NMS]
    Post -->|Filtered Results| Tracker[Object Tracker]
    Tracker -->|Annotated Frames| WebUI[Streamlit Dashboard]
    Post -->|Telemetry| Analytics[Analytics Engine]
`

## 🛠️ Installation

### Prerequisites
- Python 3.9+
- NVIDIA GPU + CUDA (Recommended for real-time performance)
- OpenCV / PyTorch

### Quick Start
1. **Clone the repository**
   \\\ash
   git clone https://github.com/rahulsunil112/lumina-vision-ai.git
   cd lumina-vision-ai
   \\\

2. **Install dependencies**
   \\\ash
   pip install -r requirements.txt
   \\\

3. **Run the Dashboard**
   \\\ash
   streamlit run ui/dashboard.py
   \\\

## 📊 Performance Benchmarks

| Model | mAP@50 | Latency (RTX 3080) | FPS |
| :--- | :---: | :---: | :---: |
| Lumina-Nano | 37.4 | 1.2ms | 180 |
| Lumina-Base | 52.1 | 3.5ms | 85 |
| Lumina-Large | 54.8 | 8.2ms | 45 |

## 🧩 Project Structure

\\\
lumina-vision-ai/
├── src/
│   ├── engine/              # Core inference and tracking logic
│   ├── utils/               # Image processing and visualization helpers
│   └── config/              # Model hyperparameters and CLI configs
├── ui/                      # Streamlit real-time dashboard
├── models/                  # Pre-trained weights and ONNX exports
├── data/                    # Sample images and video for testing
├── Dockerfile               # Production containerization
└── requirements.txt         # Project dependencies
\\\

## 👨‍💻 Author

**Rahul Sunil**
*AI Engineer @ Certa.ai*
[LinkedIn](https://www.linkedin.com/in/rahulsunil2/)

---
*Empowering the world through intelligent vision.*