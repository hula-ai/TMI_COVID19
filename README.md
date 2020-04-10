# TMI_COVID19
The COVID-CT can be downloaded from: https://github.com/UCSD-AI4H/COVID-CT/tree/master/Images-processed
- Use the code 'covid_seperation.py' to split Train, Test, and Validation sets. It needs '.csv' files and CT-images to be run.
- The code 'covid_preprocess' copies all images to a folder and make labels.The output is a compressed file containing 
  image names and labels (0 for NonCovid Cases and 1 for Covid Cases). 

# UPDATE: Standardized Dataset
The CT and X-ray Dataset can be downloaded from: https://drive.google.com/open?id=1cmujE0e3vu2CgIbGoIxPkfVHVs5C988o
You may change the training data, but test sets should not be changed.

CT folder:

  CT_COVID.zip: all CT images for COVID cases.
  
  CT_NonCOVID.zip: all CT images for Non-COVID cases.
  
  CT_DATA.zip: all CT images seperated for training, testing, and validation. 
 
  
 X-ray folder:
 
  X_DATA.zip: all x-ray images seperated for training and testing.
  
 Alpha-test set:
 
  The images that were sent to radiologists and the name mappings can be found here:
  
  https://drive.google.com/open?id=1AQRrpRUzGhyTTc28ODlpZqqrG3V4kDx4
  
  - The results recieved from radiologists are added to: https://drive.google.com/open?id=1HM9L2t1jg_KTfGsofzScEKzl0X4lZ28R
  
    CT Radiologist.zip: CT images that each radiologist could classify + .xlsx file including actual name of each image,
  predicted and actual class. 0 is for Non-COVID and 1 for COVID class.
    Xray Radiologist.zip: Xray images + .xlsx file including actual name of each image, predicted and actual class. 0 is for normal,
  1 for COVID, and 2 for pneumonia  class.
 
 
