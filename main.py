import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np
import cv2

from util import classify, set_background


set_background('./bgs/spidy.jpg')

# set title
st.title('Spider Classifier')

# set header
st.header('Upload a spider image:')
# upload file
file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

# load classifier
model = load_model('./model/web_9090.h5')

# load class names
with open('./model/labels.txt', 'r') as f:
    class_names = [line.strip().split(' ', 1)[1] for line in f]
    #class_names = [a[:-1].split(' ')[1] for a in f.readlines()]
    f.close()

# display image
if file is not None:
    image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    ###
    #image = Image.open(file).convert('RGB')
    st.image(image, use_column_width=True)

    # classify image
    class_name, conf_score, index = classify(image, model, class_names)

    # write classification
    st.write("## Bites from this spider species are considered {}".format(class_name))
    #st.write("### score: {}%".format(int(conf_score * 1000) / 10))
    
    