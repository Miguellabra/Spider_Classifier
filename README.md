# Spider Classifier


### The Problem
It is widely recognized that among the approximately 50,000 known spider species, not all possess venomous bites that pose a mortal threat to humans. In general, there are two well-documented spider species of significant medical concern due to their bites. Without proper treatment or observation, these bites can potentially lead to fatal consequences. This highlights the importance of distinguishing whether a spider belongs to one of these species. 

The primary objective of this project is to differentiate between spider species of medical importance and those without medical significance using computer vision techniques, particularly through **convolutional neural networks**. The project utilizes a dataset sourced from Kaggle [repository](https://www.kaggle.com/datasets/gpiosenka/yikes-spiders-15-species/data), containing a total of 15 spider species, with 2186 images for training, 75 for testing, and an additional 75 images for model validation. The ambition of this project extends further, as it also includes the task of developing an app that allows users to upload spider images and receive predictions from the model.

Please note that this project acknowledges the existence of other spider species that are not included in the current dataset. A future enhancement will prioritize expanding the dataset to encompass a more comprehensive range of spider species.

### Data
The spider spieces considered are the following:

* Black Widow
* Blue Tarantula
* Bold Jumper
* Brown Grass Spider
* Brown Recluse Spider
* Deinopis Spider
* GoldenOrbWeaver
* Hobo Spider
* Huntsman Spider
* Ladybird Mimic Spider
* Peacock Spider
* Red Knee Tarantula
* Spiny Backed-OrbWeaver
* White Tarantula
* Yellow Garden Spider

As mentioned previously, the training set consists of 2186 images, while the test set comprises 75 images. While this number might seem insufficient for building a robust model, I employed a **data augmentation** technique to generate additional images for each original one. This technique was applied twice: once before feeding the data to the model using the ImageDataGenerator() function, and another during training by adding a layer to the model with the RandomFlip() function.

### Model and Results
The initial convolutional neural network achieved a final accuracy of 90%, with a validation accuracy of 90%. This model was trained over 55 epochs, using a batch size of 20, and the 'Adamax' optimizer. In addition, both MaxPooling2D() and Dropout() functions were integrated into some layers of the model.
### The App
The app was developed using the Streamlit library and will be hosted through the community cloud of Streamlit once the last details of the app are finalized. In this repository, you can find the architecture of the app.
