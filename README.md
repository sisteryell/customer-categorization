# Customer Segmentation and Categorization

This project implements a customer categorization system using both **Clustering** and **Classification** techniques, with a FastAPI-based web application for real-time predictions.

## Project Overview

The goal of this project is to segment customers into distinct categories based on various features, and then build a machine learning model to predict the customer's category based on new input data. The project uses:
- **Clustering** to identify patterns in customer data and create meaningful customer segments.
- **Classification** to predict the customer segment for new data.
- **FastAPI** to deploy the machine learning models in a web application for real-time predictions.

- ## Project Structure

```plaintext
.
├── model/                                             # Folder for machine learning models
│   └── catboost_best_model.cbm                        # Code to train and save models
├── notebooks/                                         # Jupyter notebooks
│   ├── Exploratory_Data_Analysis.ipynb                # exploratory data analysis
│   ├── Feature_engineering_and_clustering.ipynb       # feature engineering and clustering
│   ├── Feature_selection_and_Classification.ipynb     # feature selection and classification
│   └── marketing_campaign.csv                         # datasets
├── static/                                            # Static files (images, CSS for the web app)
├── templates/                                         # HTML templates for FastAPI front-end
├── .dockerignore                                      # Docker ignore file
├── .gitignore                                         # Git ignore file
├── README.md                                          # Project documentation
├── app.py                                             # FastAPI application for real-time model predictions
├── Dockerfile                                         # Dockerfile for containerizing the app
└── requirements.txt                                   # List of Python dependencies

```

## Setup

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

### 2. Run Locally with Python (optional)

#### Create and activate a virtual environment:

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

#### Install required dependencies:

```bash
pip install -r requirements.txt
```

#### Start the FastAPI app:

```bash
uvicorn app:app --reload
```

The app will be available at http://127.0.0.1:8000.

### 3. Run with Docker (recommended)

#### Build docker image:

```bash
docker build -t customer-categorization-app .
```

#### Run the Docker container:

```bash
docker run -d -p 8000:8000 customer-categorization-app
```

#### Access the app:

Open your browser and go to http://localhost:8000.

#### Stop the container when done:

Find the container ID with:

```bash
docker ps
````

Then stop it with:

```bash
docker stop <container_id>
```

## Future Improvements
-  Add Docker Compose support for easier multi-service orchestration
-  CI/CD pipeline integration to automate tests and deployments
-  Deploy the app to a cloud platform (e.g., AWS, Azure, or DigitalOcean) for production use
