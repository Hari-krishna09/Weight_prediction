
# Weight Prediction Using Simple Linear Regression

## Project Overview

This project predicts a person's weight (in kilograms) based on their height (in feet) using **Simple Linear Regression**, a supervised machine learning algorithm.

The project uses Python for model development and Flask to build a web application where users can enter their height and receive a predicted weight.

## Technologies Used

- **Python** – Programming language
- **Pandas** – Data manipulation
- **NumPy** – Numerical computations
- **Matplotlib** – Data visualization
- **Scikit-learn** – Machine learning model
- **Flask** – Backend web framework
- **HTML & CSS** – Frontend development
- **Pickle** – Model serialization

## Machine Learning Algorithm

**Simple Linear Regression**

Simple Linear Regression is used to identify the relationship between one independent variable (height) and one dependent variable (weight).

### Mathematical Equation

\[
y = mx + c
\]

Where:

- `y` = Predicted weight
- `x` = Height in feet
- `m` = Slope (coefficient)
- `c` = Intercept

## Dataset Description

The dataset contains two columns:

| Feature | Description |
|---|---|
| Height (feet) | Independent variable |
| Weight (kg) | Dependent variable / Target |

The project uses a synthetic dataset containing 100 records for practice.

## Project Structure

```text
Weight-Prediction/
│
├── app.py
├── LR.pkl
├── height_weight_dataset.csv
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── README.md
```

## Installation and Setup


### 2. Navigate to the Project Folder

```bash
cd Weight-Prediction


### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate Virtual Environment

.venv\Scripts\Activate.ps1
```


### 5. Install Required Libraries

```bash
pip install numpy pandas matplotlib scikit-learn flask
```

### 6. Run the Flask Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## Application Workflow

1. User enters their height in feet.
2. Flask receives the input through an HTML form.
3. Input is converted into a NumPy array.
4. The trained Linear Regression model predicts weight.
5. Flask sends the prediction back to the frontend.
6. The predicted weight is displayed in kilograms.

## Features

- Predicts weight based on height.
- Uses a trained Simple Linear Regression model.
- Interactive web interface.
- Flask-based backend integration.
- Responsive frontend design.
- Real-time prediction after form submission.

## Future Improvements

- Add more input features such as age and gender, with an appropriately trained model.
- Improve prediction accuracy using a larger real-world dataset.
- Display actual vs predicted values.
- Add model evaluation metrics such as R², MAE and MSE.
- Deploy the application online.

## Important Note

This project is developed for educational purposes. The dataset contains synthetic practice data, and predictions should not be considered actual body-weight measurements or medical recommendations.

## Author

**Hari Krishna**

Machine Learning | Python | Flask | Data Science
