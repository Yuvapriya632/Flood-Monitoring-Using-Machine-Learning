## Flood Monitoring Using Machine Learning

A web-based flood monitoring and prediction application built with **Python, Django, and Machine Learning**. The project uses a trained K-Nearest Neighbors (KNN) model to generate predictions from user-provided input through a web interface.

## Project Demo

▶️ **YouTube Demo:** [Watch the project demonstration](https://youtu.be/yL9WzXNX0S8?si=mWsyY7VJs3m2cw6W)

## Application Screenshot

![Flood Monitoring Using Machine Learning application screenshot](frontend/static/images/flood-prediction.png)

> If the screenshot does not appear on GitHub, confirm that `flood-prediction.png` is committed at `frontend/static/images/flood-prediction.png`.

## Dataset

📊 **Kaggle Dataset:** [Flood Monitoring Using Machine Learning](https://www.kaggle.com/datasets/yuvashrisankar/flood-monitoring-using-machine-learning)

The project dataset is also included locally as `backend/data.csv`.

## Project Overview

This project combines a machine learning model with a Django web application. Users can open the website, enter the required information, and view the prediction result.

## Features

- Flood prediction using a saved K-Nearest Neighbors (KNN) model.
- Django backend for application logic and request handling.
- HTML templates for the web interface.
- Static CSS and image assets.
- Pages for sign-up, login, logout, home, and prediction results, as represented in the project structure.

## Technologies Used

- **Programming language:** Python
- **Web framework:** Django
- **Machine learning:** scikit-learn
- **Frontend:** HTML and CSS
- **Database:** SQLite
- **Dataset:** `data.csv`
- **Trained model:** `KNN.pkl`
- **Jupyter notebook:** `Flood.ipynb`

## Project Structure

```text
Flood/
├── backend/
│   ├── data.csv
│   ├── Flood.ipynb
│   └── KNN.pkl
└── frontend/
    ├── base/
    │   ├── migrations/
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── Flood/
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── static/
    │   ├── css/
    │   └── images/
    │       └── flood-prediction.png
    ├── templates/
    │   ├── base.html
    │   ├── home.html
    │   ├── index.html
    │   ├── login.html
    │   ├── logout.html
    │   ├── result.html
    │   └── signup.html
    ├── db.sqlite3
    ├── KNN.pkl
    ├── manage.py
    └── requirements.txt
```

## Getting Started

### 1. Prerequisites

- Python installed on your computer
- pip (Python package installer)
- Git (optional, for cloning the repository)

Use a Python version supported by the project's dependencies. Creating a virtual environment is recommended.

### 2. Clone or download the project

If the project is hosted on GitHub, clone it and enter the project folder:

```bash
git clone <YOUR_REPOSITORY_URL>
cd Flood
```

Alternatively, download and extract the project ZIP file.

### 3. Create and activate a virtual environment

From the main `Flood` folder, run these commands in Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell does not allow activation, you can use Command Prompt:

```bat
.venv\Scripts\activate.bat
```

### 4. Install dependencies

The `requirements.txt` file is inside the `frontend` folder. Run:

```powershell
cd frontend
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If you encounter `ModuleNotFoundError: No module named 'sklearn'`, install scikit-learn in the same active environment:

```powershell
python -m pip install scikit-learn
```

### 5. Apply database migrations

Make sure the terminal is in the `frontend` directory (the directory containing `manage.py`):

```powershell
python manage.py migrate
```

### 6. Run the application

```powershell
python manage.py runserver
```

Open the local URL in your browser:

**http://127.0.0.1:8000/**

Press `Ctrl + C` in the terminal to stop the development server.

## How to Use

1. Start the Django development server.
2. Open the application in your browser.
3. Navigate to the available pages.
4. Enter the required prediction inputs.
5. Submit the form to view the result.

The exact input fields and prediction interpretation depend on the implementation in `frontend/base/views.py` and the HTML templates.

## Machine Learning Model

The project contains a trained model named `KNN.pkl` and a Jupyter notebook named `Flood.ipynb`.

- **Algorithm:** K-Nearest Neighbors (KNN)
- **Dataset file:** `data.csv`
- **Saved model:** `KNN.pkl`

For consistent predictions, the input features, feature order, data types, and preprocessing in the web application must match those used when training the model. Model accuracy should be reported only after verifying it against the notebook or evaluation results.

## Troubleshooting

### `No module named 'sklearn'`

Activate the virtual environment and install scikit-learn:

```powershell
python -m pip install scikit-learn
```

### `Could not open requirements.txt`

Ensure that your terminal is in the `frontend` folder before installing dependencies:

```powershell
cd path\to\Flood\frontend
python -m pip install -r requirements.txt
```

### Model file not found

Check that `KNN.pkl` exists at the location expected by the Django code. Review the model-loading path in `views.py` and update it if necessary.

### Port 8000 is already in use

Run the application on another port:

```powershell
python manage.py runserver 8001
```

Then open **http://127.0.0.1:8001/**.

## Future Improvements

- Improve input validation and error messages.
- Evaluate the model on held-out data and document verified performance metrics.
- Improve responsive design and accessibility.
- Add automated tests for prediction and form handling.
- Document the dataset's source, features, and limitations.

## Disclaimer

This project is intended for educational and demonstration purposes. Its predictions should **not** be used as the sole basis for flood warnings, evacuation decisions, or other safety-critical actions.

## Author

**Yuvapriya S**

## License

No license is specified. Add a `LICENSE` file if you plan to distribute or allow reuse of this project.
"""

