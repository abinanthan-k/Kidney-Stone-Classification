# Kidney-Stone-Classification

## Overview

Kidney-Stone-Classification is a Python-based project for detecting kidney stones from medical images using deep learning. The project exposes a REST API (using FastAPI) that receives an image upload and returns a prediction: "Healthy Kidney" or "Kidney has stone". The model is loaded from a pre-trained Keras file (`stone_classif.keras`).

## Features

- **Image Classification:** Predicts whether a kidney image is healthy or has stones using a trained neural network.
- **REST API:** Easily integrates with other applications or frontends via HTTP POST requests.
- **FastAPI Backend:** Modern, async Python web framework for high performance.
- **CORS Support:** Enables requests from any origin.

## Usage

### Running the API Server

1. **Install dependencies:**  
   Make sure to install the required Python packages (see below).

2. **Start the server:**  
   ```bash
   uvicorn app:app --reload
   ```
   This will run the FastAPI server locally.

3. **Make predictions:**  
   Send a POST request to `/predict/` with an image file. Example using `curl`:
   ```bash
   curl -F "file=@kidney_image.jpg" http://localhost:8000/predict/
   ```
   The response will be a JSON object like:
   ```json
   {"prediction": "Healthy Kidney"}
   ```

### API Endpoint

- **POST /predict/**
  - **Body:** Image file upload (e.g., JPEG, PNG).
  - **Response:** `{ "prediction": "Healthy Kidney" }` or `{ "prediction": "Kidney has stone" }`

## Installation

### Requirements

- Python 3.8+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/) (for running server)
- [Keras](https://keras.io/) and its backend (TensorFlow)
- [Pillow (PIL)](https://pillow.readthedocs.io/)
- [OpenCV](https://opencv.org/) (`cv2`)
- `stone_classif.keras` model file (must be present in the repo root)

Install dependencies:
```bash
pip install fastapi uvicorn keras pillow opencv-python
```

## How it Works

- The server loads a Keras model (`stone_classif.keras`) at startup.
- When an image is uploaded, it is resized to 180x180 pixels and normalized.
- The processed image is sent to the model for prediction.
- If the prediction score is >= 0.9, it is classified as "Kidney has stone", otherwise "Healthy Kidney".

## File Structure

- `app.py` – FastAPI server and API logic
- `stone_classif.keras` – Pretrained model file (not included)
- `README.md` – Project documentation

## Contributing

Please open issues or pull requests if you find bugs or have suggestions.

## License

_(No license file detected. Please add one if required.)_

## Author

[abinanthan-k](https://github.com/abinanthan-k)
