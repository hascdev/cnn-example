import numpy as np
from tensorflow.python.keras.preprocessing.image import load_img, img_to_array
from tensorflow.python.keras.models import load_model

longitud, altura = 224, 224
modelo = './modelo/modelo2.h5'
pesos_modelo = './modelo/pesos2.h5'
cnn = load_model(modelo)
cnn.load_weights(pesos_modelo)

def predict(file):
  x = load_img(file, target_size=(longitud, altura))
  x = img_to_array(x)
  x = np.expand_dims(x, axis=0)
  array = cnn.predict(x)
  result = array[0]
  answer = np.argmax(result)
  if answer == 0:
    print("pred: Perro")
  elif answer == 1:
    print("pred: Gato")
  elif answer == 2:
    print("pred: Gorila")

  return answer

predict('images.jpg')