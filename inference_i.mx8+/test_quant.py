from keras_retinanet.keras_retinanet.models import load_model
import numpy as np
from keras_retinanet.keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image
import cv2
model = load_model('GHL_Models/resnet50_csv_26.h5', backbone_name='resnet50')
image = read_image_bgr('PyAVE_cmu_fall2023/cmu_fall2023/images/validation_image_cmu/10.6.3.9 Flat margin.jpg')

# copy to draw on
draw = image.copy()
draw = cv2.cvtColor(draw, cv2.COLOR_BGR2RGB)

# preprocess image for network
image = preprocess_image(image)
image, scale = resize_image(image)

boxes, scores = model.predict_on_batch(np.expand_dims(image, axis=0))
print(boxes, scores)