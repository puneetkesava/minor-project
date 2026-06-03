import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import os
from openai import OpenAI

# ===== CONFIG =====
API_KEY = "*****"  # ⛔ Replace with your real key
client = OpenAI(api_key=API_KEY)

class_names = ['landscape', 'object', 'passport', 'selfie']
dataset_base = "/content/drive/MyDrive/clean_dataset"

# ===== Load CNN Model =====
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("/content/drive/MyDrive/smart_photo_organizer_model.h5")

model = load_model()

# ===== Call OpenAI GPT =====
def call_openai_chat(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ OpenAI API error: {str(e)}"

# ===== Streamlit Page Config =====
st.set_page_config(page_title="Photo Organizer + Chatbot", layout="wide")
st.title("📁 Smart Photo Organizer + Chatbot 🤖")

# ===== Upload Image Section =====
st.subheader("🖼️ Upload an Image for Classification")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess
    img_resized = image.resize((128, 128))
    img_array = np.array(img_resized) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array)
    class_index = np.argmax(prediction)
    predicted_label = class_names[class_index]

    # Save image to folder
    save_dir = os.path.join(dataset_base, str(class_index))
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, uploaded_file.name)
    image.save(save_path)

    st.success(f"🧠 Predicted Category: {predicted_label}")
    st.info(f"✅ Saved to folder: {save_dir}")

# ===== Chatbot Section =====
st.subheader("💬 Talk to the Bot")
user_prompt = st.text_input("You:", "")

def show_images_for_class(class_keyword):
    matched = None
    for label in class_names:
        if label in class_keyword.lower():
            matched = str(class_names.index(label))
            break
    if matched:
        folder_path = os.path.join(dataset_base, matched)
        if os.path.exists(folder_path):
            image_files = os.listdir(folder_path)
            st.subheader(f"🖼️ Showing images for: {class_names[int(matched)]}")
            for img_name in image_files[:5]:
                st.image(os.path.join(folder_path, img_name), width=200)
        else:
            st.warning("📂 No images found in that folder.")
    else:
        st.info("🤖 No matching image category detected.")

if st.button("Send"):
    if user_prompt:
        if any(label in user_prompt.lower() for label in class_names):
            show_images_for_class(user_prompt)
        else:
            bot_reply = call_openai_chat(user_prompt)
            st.success(f"🤖 Bot: {bot_reply}")
