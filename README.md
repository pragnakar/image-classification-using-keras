# image-classification-using-keras
using keras ,image classification is performed on  STL-10 data-set. 

I have used pretrained model of vgg16, that model was created to win image net competition. I made few changes on my own hoping to to increase the predction accuracy of the model.  

This repository contains following files 

1) A jupyter notebook, contains everything I have done. 
2) A hdf5 file containing the weights obtained after training my  model.(saved model)
3) A python file to visualzie all the images. 


link to the data set:
https://cs.stanford.edu/~acoates/stl10/

download the data set and extract the file. make sure the names of the files extracted match those mentioned in the code. 

there is an issue with loading saved model in keras it has to do with load_model(), I have mentioned about a fix to that problem in the notebook. 
