
# CSC 805 Project
**Exploring Breast Tumor Data**
Made By Darshil Dhameliya and Vishal Sharma
In Fall 2022 at San Francisco State University

# System Architecture

 **Frontend**
 

 - Made with [React.JS](https://reactjs.org/) and [TypeScript](https://www.typescriptlang.org/)
 - We are also leveraging the UI Components from [Antd](https://ant.design/)


 **Backend**
 - The Backend is developed using [Python](https://www.python.org/) and leverages the [Flask](https://flask.palletsprojects.com/en/2.2.x/) Framework
 - The charts are generated using Python Library [Seaborn](https://seaborn.pydata.org/)
 - For obtaining predictions we use [XGBoost ML Model](https://xgboost.readthedocs.io/en/stable/)
 
 **Dataset Description**
 - Our target data is sourced from [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29) called the "Breast Cancer Wisconsin (Diagnostic) Data Set"
 - This data set includes calculated measurements of a digitized image of a fine needle aspirate (FNA) of a breast mass, i.e., radius, smoothness, fractal dimension, etc
 - They describe the characteristics of the cell nuclei present in the images
 
 ## Local Development Prerequisites
 You will need the following prerequisites
 - [Node.JS](https://nodejs.org/en/download/)
 - [Python3](https://www.python.org/)
 
 ## Local Development
 -	Clone the repository using   `git clone https://github.com/vishals9711/CSC_805_Project`
 ### Frontend Developement
 -	`cd frontend`
 -	`npm install`
 -	`npm start`
 -	`Navigate to http://localhost:3000/`

### Backend Development
- `cd flask_server`
- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python3 app.py`

## Demo Video Link
[Video Link](https://drive.google.com/drive/folders/1aYsNOaUvoMwixa2avbxU5kIbU3Cw8Btf?usp=sharing)