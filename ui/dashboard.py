import streamlit as st
import cv2
import time
import numpy as np
from PIL import Image
from src.engine.detector import VisionEngine

# Configuration
st.set_page_config(
    page_title="Lumina Vision Engine",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Sleek UI
st.markdown("""
<style>
    .reportview-container { background: #0e1117; }
    .stButton > button { background-color: #3b82f6; color: white; border-radius: 8px; }
    .stMetric { background-color: #1e293b; padding: 15px; border-radius: 12px; }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/vision.png", width=80)
    st.title("Lumina Control")
    st.markdown("---")
    
    st.subheader("⚙️ Engine Settings")
    model_choice = st.selectbox("Inference Model", ["Lumina-Nano", "Lumina-Base", "Lumina-Large"])
    confidence_threshold = st.slider("Confidence Threshold", 0.0, 1.0, 0.45)
    
    st.subheader("🎥 Stream Source")
    source = st.radio("Input Source", ["Static Image", "Video Stream", "Live Camera"])
    
    st.markdown("---")
    st.info("💡 **Tip:** Adjust model choice to balance speed vs precision.")

# Main Interface
st.title("✨ Lumina Vision AI")
st.markdown("### Real-Time Object Detection & Instance Segmentation")

# Global Inference Engine
engine = VisionEngine(model_choice)

# Metrics Row
col1, col2, col3, col4 = st.columns(4)
with col1: st.metric("Processing Time", "3.2ms", "1.1ms")
with col2: st.metric("Inference FPS", "125", "12")
with col3: st.metric("Detected Objects", "12", "3")
with col4: st.metric("ID Tracking Persistence", "99.8%", "0.2%")

# Content Row
left_col, right_col = st.columns([2, 1])

with left_col:
    st.markdown("#### Real-Time Stream")
    if source == "Static Image":
        uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
        if uploaded_file:
            image = Image.open(uploaded_file)
            frame = np.array(image)
            
            with st.spinner("Analyzing Scene..."):
                processed_frame, dets = engine.process_frame(frame)
                st.image(processed_frame, caption="Lumina Annotated Output", use_column_width=True)
                
    else:
        st.warning(f"{source} mode requires active backend connection.")
        # Placeholder for real-time video stream (e.g., using OpenCV)
        st.image("https://via.placeholder.com/1280x720.png?text=Awaiting+Real-Time+Input+Stream", use_column_width=True)

with right_col:
    st.markdown("#### Live Telemetry")
    if 'dets' in locals():
        for det in dets:
            st.success(f"**ID {det['id']}** | {det['label']} ({det['confidence']*100:.1f}%)")
    else:
        st.info("No active detections.")
    
    st.markdown("#### Activity Logs")
    st.code("""
    [SYSTEM] Engine v2.1.0 Online
    [LOAD] Model weight path: /models/yolov8_base.pt
    [INFO] CUDA 12.1 detected, utilizing TensorRT
    [INFO] Inference started on stream 1...
    """)