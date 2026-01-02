# inference.py
from transformers import pipeline
from PIL import Image

_classifier = None

def load_model():
    global _classifier
    if _classifier is None:
        _classifier = pipeline(
            "image-classification",
            model="google/vit-base-patch16-224"
        )
    return _classifier


def map_to_damage(label: str):
    label = label.lower()

    if "hole" in label or "pothole" in label:
        return "Pothole", "High", "Immediate"
    elif "crack" in label or "asphalt" in label:
        return "Crack", "Medium", "Scheduled"
    else:
        return "Surface Wear", "Low", "Monitor"


def analyze_image(image: Image.Image):
    classifier = load_model()
    result = classifier(image)[0]

    label = result["label"]
    score = float(result["score"])

    damage, severity, priority = map_to_damage(label)

    return {
        "damage": damage,
        "severity": severity,
        "priority": priority,
        "confidence": round(score, 2)
    }
