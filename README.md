# Animal Detection and Activation Maps

This repository contains code and resources for two tasks:

1. **Activation Maps (Task 1)**: Visualize activation maps to understand model predictions better.
2. **Animal Detection Model (Task 2)**: Detect animals in images using a pre-trained deep learning model via a GUI application.

## Task 1: Activation Maps

### Objective
To visualize activation maps from a trained convolutional neural network (CNN) to understand which regions of an input image contribute most to the model's predictions.

### Files
- **`model_training.ipynb`**: Contains the code for training the model and visualizing activation maps.

### Features
- Generate activation maps for individual convolutional layers.
- Visualize the regions in the input image contributing to predictions.

### Usage
1. Open the `model_training.ipynb` file in Jupyter Notebook.
2. Run the cells to train the model and generate activation maps.
3. Modify the image path and layer names as needed to visualize specific results.

## Task 2: Animal Detection Model

### Objective
To build a GUI application that detects animals in uploaded images and provides predictions using a pre-trained deep learning model.

### Files
- **`gui.py`**: The Python script for the GUI-based animal detection application.
- **`model_training.ipynb`**: Code for training the animal detection model.
- **`requirements.txt`**: List of all required Python libraries.

### Features
- Upload an image via the GUI.
- Predict the animal in the image using a trained model.
- Display predictions with color-coded results (e.g., carnivorous animals in red).

### Pre-trained Model
The application uses a pre-trained model (`model.h5`) and its corresponding architecture (`model.json`). You can download these files from the following link:

[Download model files from Google Drive](https://drive.google.com/drive/folders/1ZOdua3rOPBKO02t5996-JXVAltrq6hHR?usp=sharing)

Once downloaded, place the files in the appropriate directory as specified in `gui.py`.

### Usage
1. Run the GUI application:
   ```bash
   python gui.py
   ```
2. Use the "Upload Image" button to select an image file.
3. Click "Detect Animals" to get the prediction.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Dhanyavarthini/NullClass.git
   cd your-repository-folder
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Dependencies

The project relies on the following libraries:
- `tensorflow`
- `keras`
- `numpy`
- `opencv-python`
- `matplotlib`
- `Pillow`
- `tkinter`

Ensure you have Python 3.8+ installed.

## How It Works

### Task 1: Activation Maps
1. **Model Training**: The model is trained on image data.
2. **Activation Map Generation**: Specific convolutional layers are analyzed to highlight important regions in input images.

### Task 2: Animal Detection
1. **Model Training**: The animal detection model is trained using the `model_training.ipynb` notebook on a dataset of animal images.
2. **Image Preprocessing**: Images are resized, converted to grayscale, and normalized before prediction.
3. **Animal Detection**: The trained model predicts the animal in the image and determines if it's carnivorous or not.
4. **GUI**: The result is displayed in a user-friendly graphical interface.

## Contributing
Feel free to contribute to this project by opening issues or submitting pull requests.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
