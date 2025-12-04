
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model



# Function to preprocess an image
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array / 255.

# Function to make predictions
def predict_image( img_path):
    # # Load the trained model
    model = load_model('ecg_model_vgg16_.h5')
    print("*"*100)
    print("img_pathssss : ",img_path)
    preprocessed_img = preprocess_image(img_path)
    prediction = model.predict(preprocessed_img)
    predicted_class = np.argmax(prediction)
    class_map = {
        0: 'building',
        1: 'flooded',
        2: 'forest',
        3: 'mountains',
        4: 'sea',
        5: 'street'
    }
    predicted_label = class_map[predicted_class]
    confidence = prediction[0][predicted_class]
    return predicted_label, confidence
def setpath():
    # # Example usage
    img_path = 'static/img.jpg'  # Replace with the path to your new ECG image
    predicted_label, confidence = predict_image( img_path)
    print(f'Predicted Label: {predicted_label}')
    print(f'Confidence: {confidence}')
    return predicted_label, confidence 

# setpath()