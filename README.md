# Project Title: Big Data Taxi Fare Predictor

# Description:

The "Big Data Taxi Fare Predictor" is a data science project aimed at predicting taxi fares using a large-scale dataset consisting of 8.4 crore rows and 18 columns. The first step of the project involved converting the massive 12GB SQLite file into an HDF5 file format using the efficient Vaex library. This conversion allowed for easier data loading and handling, significantly speeding up the overall data processing.

After loading the data into a Vaex dataframe, thorough preprocessing was performed. This included removing unnecessary columns, detecting and addressing NaN values in each column, and identifying and handling outliers to reveal the underlying patterns between the features and the target variable (fare_amount). Notably, a linear relationship was discovered between certain features and the target.

To prepare the data for training, normalization/scaling was performed using the standard scaler. For the actual training and prediction, the Incremental Stochastic Gradient Descent (SGD) model was employed. The model yielded promising results, achieving an R-squared score of 0.89 and a mean absolute error of 0.18.

Finally, the trained model was saved as a pickle file for future use, and a Streamlit app was deployed for users to interactively predict taxi fares based on their inputs.
