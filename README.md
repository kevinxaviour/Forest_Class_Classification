# End to End Forest Cover Classification ML Mini Project
- Predict or test model @ https://forestclassclassification.streamlit.app/

## Work Flow
### 1) Data Insertion and Preparation: (https://github.com/kevinxaviour/Forest_Class_Classification/blob/eea945dac294e644aed91d944c0d36661f856181/Data%20Insertion%20and%20Preparation.ipynb)
- Understanding of features with Definitions.
- Creating Pickle files for One hot Encoded and Label Encoded Features.
- Preparing and Exporting the Dataset for Exploratory Data Analysis.

### 2) Exploratory Data Analysis: (https://github.com/kevinxaviour/Forest_Class_Classification/blob/eea945dac294e644aed91d944c0d36661f856181/EDA.ipynb)
- Understanding the data.
- Finding out if the data is imbalanced.
- Outliers detection.
- Skewness and Kurtosis Detection.
- Univariate and Bivariate Analysis
- Making the data features normally distributed.

### 3) Model training: (https://github.com/kevinxaviour/Forest_Class_Classification/blob/eea945dac294e644aed91d944c0d36661f856181/modeltraining.ipynb)
-  Training With different Classification Model
   - Logistic Regression
   - KNN Classifier
   - Decision Tree
   - Random Forest Classifier
   - Balanced Random Forest Classifier
   - Xtreme Gradient Boost Classifier
- Hypertuning Each algo to get the best fit.
- Saving the best model into a pickle file and using for future predictions

### 4) Saving all pickle files in AWS S3
- This process is done because github file size restriction is 25MB.
- But the Model here was more than 25MB.

### 5) Streamlit Application: (https://github.com/kevinxaviour/Forest_Class_Classification/blob/580610e677847f0420b071bb62f787adcef474b3/streamlit.py)
- Reading Pickle Files from AWS S3
- The credentials will not be initialized in streamlit.py file but in streamlit environment for data security.
- Creating Manual Input and also Slider drag drop input for entering feature values
- Inputing data and getting the predictions in the application.

# THE END


