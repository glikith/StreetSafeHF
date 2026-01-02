import streamlit as st
from PIL import Image
from transformers import pipeline

st.set_page_config(page_title="SafeStreet", layout="centered")

st.title("🚧 SafeStreet – Road Damage Detection")
st.write("Upload a road image to analyze damage severity and priority.")

@st.cache_resource
def load_model():
    return pipeline(
        "image-classification",
        model="google/vit-base-patch16-224"
    )

classifier = load_model()

def map_to_damage(label):
    label = label.lower()

    if "hole" in label or "pothole" in label:
        return "Pothole", "High", "Immediate"
    elif "crack" in label or "asphalt" in label:
        return "Crack", "Medium", "Scheduled"
    else:
        return "Surface Wear", "Low", "Monitor"

uploaded_file = st.file_uploader(
    "Upload road image",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Analyze Damage"):
        result = classifier(image)

        label = result[0]["label"]
        score = result[0]["score"]

        damage, severity, priority = map_to_damage(label)

        st.subheader("📝 SafeStreet Report")
        
        st.write(f"**Damage Type:** {damage}")
        st.write(f"**Severity Level:** {severity}")
        st.write(f"**Repair Priority:** {priority}")
        st.write(f"**Model Confidence:** {score:.2f}")

