
from PIL import Image, ImageFile
import tensorflow as tf
import numpy as np

def reading(name):
        model = tf.keras.models.load_model('final_model.h5',compile=False)
        img1=name
        image = Image.open(img1)
        image=image.resize((224,224))
        img_arr = np.array(image)
        img_arr = np.expand_dims(img_arr, axis=0)
        img_arr = img_arr.astype('float32')
        img_arr /= 255
        prediction=model.predict(img_arr)
        label=np.argmax(prediction)
        label_dict={0:"Acne",1:"Eczema",2:"hives",3:"rosacea",4:"shingles"}
        prediction=label_dict[label]
        return prediction

def main():
        reading("uploads/2.png")

if __name__=='__main__':
        main()