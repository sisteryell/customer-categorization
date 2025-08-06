# Customer Segmentation and Categorization

This project implements a customer categorization system using both **Clustering** and **Classification** techniques, with a FastAPI-based web application for real-time predictions.

## Project Overview

The goal of this project is to segment customers into distinct categories based on various features, and then build a machine learning model to predict the customer's category based on new input data. The project uses:
- **Clustering (Unsupervised Learning)** to identify patterns in customer data and create meaningful customer segments.
- **Classification (Supervised Learning)** to predict the customer segment for new data.
- **FastAPI** to deploy the machine learning models in a web application for real-time predictions.

- ## Project Structure

```plaintext
.
├── model/                                             # Folder for machine learning models
│   └── catboost_best_model.cbm                        # Code to train and save models
├── notebooks/                                         # Jupyter notebooks
│   └── Exploratory_Data_Analysis.ipynb                # exploratory data analysi
│   └── Feature_engineering_and_clustering.ipynb       # feature engineering and clustering
│   └── Feature_selection_and_Classification.ipynb     # feature selection andd classification
│   └── marketing_campaign.csv                         # datasets
├── static/                                            # Static files (images, CSS for the web app)
├── templates/                                         # HTML templates for FastAPI front-end
├── .gitignore                                         # Git ignore file
├── README.md                                          # Project documentation
├── app.py                                             # FastAPI application for real-time model predictions
└── requirements.txt                                   # List of Python dependencies
```

## 🚀 Setup

### Prerequisites

Ensure you have Python 3.7 or above installed. You can check your Python version by running:

```bash
python --version
```

### 1. Clone the repository
First, clone the repository to your local machine:
```bash
git clone https://github.com/sisteryell/customer-categorization.git
cd customer-categorization
```

### 2. Create and activate a virtual environment

🔹 On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

🔹 On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install required dependencies

```bash
pip install -r requirements.txt
```

### 4. Running the FastAPI App
After installing the dependencies, you can start the FastAPI application.

To start the FastAPI server locally, run:
```bash
uvicorn app:app --reload
```

The FastAPI app will be available at http://127.0.0.1:8000.


## 🚧 Future Improvements
-  Add Docker support to containerize the application for easier deployment and portability across environments
-  CI/CD pipeline integration to automate tests and deployments
-  Deploy the app to a cloud platform (e.g., AWS, Heroku, or DigitalOcean) for production use
