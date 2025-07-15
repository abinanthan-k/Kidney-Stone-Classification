from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware  
from io import BytesIO
from PIL import Image
import numpy as np
import cv2
import keras

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

model = keras.models.load_model("stone_classif.keras")
print("Model Loaded successfully")

def predict_image(img_array):
    try:   
        prediction = model.predict(img_array)
        prediction = float(prediction[0][0])
        if prediction >= 0.9:
            prediction = 1
        else:
            prediction = 0
    except Exception as e:
        return f"Error: {e}"
    print(prediction)
    return prediction

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    img = Image.open(BytesIO(image_bytes)).convert("RGB")
    img_np = np.array(img)
    img_np = cv2.resize(img_np, (180, 180))
    img_np = img_np / 255.0
    img_np = img_np.astype("float32")
    img_np = np.expand_dims(img_np, axis=0) 
    print("Input shape to model:", img_np.shape)
    result = predict_image(img_np)
    diagnosis = ""
    if result == 0:
        diagnosis = "Healthy Kidney"
    else:
        diagnosis = "Kidney has stone"

    return {"prediction": diagnosis}
