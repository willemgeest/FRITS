import beer_classification
from PIL import Image
import object_detection
import beer_classification
from datetime import datetime
import connection

#load model
obj_det_model = object_detection.get_obj_det_model(local=True)

class_names = beer_classification.get_classes()

n_beers = 0
beerbrand = 'N.A.'

conn = connection.connect_with_pi()

photo_id = datetime.now().strftime("%Y%m%d%H%M%S")
picture_name = 'pictures/latest_picture.jpg'

latest_image = Image.open(picture_name).rotate(180, expand=True)

#object detection
boxes, n_beers, _, preds = object_detection.find_bottles(image=latest_image,
                                                         model=obj_det_model,
                                                         detection_threshold=0.8, GPU=False)


#image classification
if n_beers>0:
    beer_nr = 0
    image_cropped = latest_image.crop(tuple(boxes[beer_nr]))
    beerbrand, probabilities, heatmap = beer_classification.beer_classification(img=image_cropped)

# if probability < 90% and there are other beers on image, check brand of other beer
while max(probabilities).item() <= 0.90 and n_beers > beer_nr+1:
    beer_nr = beer_nr+1
    image_cropped = latest_image.crop(tuple(boxes[beer_nr]))
    beerbrand, probabilities, heatmap = beer_classification.beer_classification(img=image_cropped)

print(f'Detected beerbrand is {beerbrand} with {max(probabilities).tolist()*100:.1f}% certainty')

