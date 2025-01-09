# Importing Libraries
import tkinter as tk
from tkinter import filedialog, messagebox
from tensorflow.keras.models import model_from_json
import numpy as np
import cv2
from PIL import Image, ImageTk


# Function to load the model
def animal_detection_model(json_file, weights_file):
    with open(json_file, "r") as file:
        loaded_model = file.read()
    model = model_from_json(loaded_model)
    model.load_weights(weights_file)
    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
    return model


# Function to load animal list
def load_animal_list(txt_file):
    with open(txt_file, "r") as file:
        animals = [line.strip() for line in file]
    return animals

def preprocess_image(file_path):
    image = cv2.imread(file_path)
    if image is None:
        raise ValueError("Unable to read the image file.")
    resized_image = cv2.resize(image, (128, 128))
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    normalized_image = gray_image / 255.0
    input_image = normalized_image[..., np.newaxis]
    input_image = np.expand_dims(input_image, axis=0)
    return input_image

# Detect function
def Detect(file_path):
    print(f"Detect function triggered with file_path: {file_path}")
    if not file_path:
        print("No file selected!")
        messagebox.showerror("Error", "Please upload an image first!")
        return

    try:
        # Preprocess the image
        input_image = preprocess_image(file_path)

        print("Making prediction...")
        pred = model.predict(input_image)
        print(f"Prediction: {pred}")
        predicted_animal = Animals[np.argmax(pred)]
        print(f"Predicted Animal: {predicted_animal}")

        # Determine label color based on carnivorous/non-carnivorous
        if predicted_animal.lower() in [animal.lower() for animal in carnivorous_animals]:
            color = "red"
        else:
            color = "green"

        # Update GUI with the result
        label1.configure(foreground=color, text=predicted_animal)
        print("Label updated successfully.")
    except Exception as e:
        print(f"Error during detection: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")



# Show the Detect button
def show_detect_button(file_path):
    detect_b = tk.Button(top, text="Detect Animals", command=lambda: Detect(file_path), padx=10, pady=5)
    detect_b.configure(background="#364156", foreground="white", font=("arial", 10, "bold"))
    detect_b.place(relx=0.79, rely=0.46)


# Upload image function
def upload_image():
    try:
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
        if file_path:
            uploaded = Image.open(file_path)
            uploaded.thumbnail(((top.winfo_width() / 2.3), (top.winfo_height() / 2.3)))
            im = ImageTk.PhotoImage(uploaded)
            sign_image.configure(image=im)
            sign_image.image = im
            label1.configure(text="")
            show_detect_button(file_path)
    except Exception as e:
        messagebox.showerror("Error", f"Error uploading image: {e}")

# Initialize the GUI
top = tk.Tk()
top.geometry("800x600")
top.title("Animal Detection")
top.configure(background="#6699CC")

# Heading
heading = tk.Label(top, text="Animal Detector", pady=20, font=("arial", 25, "bold"))
heading.configure(background="#CDCDCD", foreground="#364156")
heading.pack()

# Label for result
label1 = tk.Label(top, background="#CDCDCD", font=("arial", 15, "bold"))
label1.pack(side="bottom", expand="True")

# Image display area
sign_image = tk.Label(top)
sign_image.pack(side="bottom", expand="True")

# Upload button
upload = tk.Button(top, text="Upload Image", command=upload_image, padx=10, pady=5)
upload.configure(background="#364156", foreground="white", font=("arial", 20, "bold"))
upload.pack(side="bottom", pady=50)

# Load model and animal list
model = animal_detection_model(
    r"C:\Users\admin\PycharmProjects\NullClass\Task2_Animal_detection_model\model_a.json",
    r"C:\Users\admin\PycharmProjects\NullClass\Task2_Animal_detection_model\model.weights.h5",
)
Animals = load_animal_list(
    r"C:\Users\admin\PycharmProjects\NullClass\Task2_Animal_detection_model\name of the animals.txt"
)

# Define carnivorous animals
carnivorous_animals = [
    "Badger",
    "Bat",
    "Bear",
    "Coyote",
    "Crab",
    "Crow",
    "Dolphin",
    "Eagle",
    "Fox",
    "Hyena",
    "Jellyfish",
    "Leopard",
    "Lion",
    "Lizard",
    "Octopus",
    "Orangutan",
    "Otter",
    "Owl",
    "Penguin",
    "Raccoon",
    "Rat",
    "Seal",
    "Shark",
    "Snake",
    "Tiger",
    "Whale",
    "Wolf",
    "Woodpecker"
]


# Run the GUI
top.mainloop()
