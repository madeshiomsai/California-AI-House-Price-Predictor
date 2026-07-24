# 🏠 California House Price Prediction

A Machine Learning web application built with **Flask** that predicts California house prices based on housing-related features. The application provides a simple and user-friendly interface where users can enter housing details and receive an estimated house value.

---

## 📌 Features

- Predict California house prices using a trained Machine Learning model.
- Clean and responsive web interface.
- Flask-based backend.
- Joblib model loading.
- Fast and lightweight application.

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- NumPy
- Joblib

---

## 📂 Project Structure

```
CaliforniaHousePrice/
│
├── app.py
├── california_info.joblib
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    └── style.css
```

---

## 📊 Input Features

The model predicts house prices using the following features:

| Feature | Description |
|----------|-------------|
| Median Income | Median income of households |
| House Age | Average age of houses |
| Average Rooms | Average number of rooms |
| Average Bedrooms | Average number of bedrooms |
| Population | Population of the area |
| Average Occupancy | Average occupants per household |

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/California-House-Price-Prediction.git
```

### 2. Navigate to the project directory

```bash
cd California-House-Price-Prediction
```

### 3. Create a virtual environment (Optional)

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Run the application

```bash
python app.py
```

---

### 6. Open your browser

```
http://127.0.0.1:5000/
```

---

## 📷 Application Preview

### Home Page

- Enter housing information.
- Click **Predict Price**.

### Result Page

- Displays the predicted California house value.

---

## 📦 Requirements

```
Flask
NumPy
Scikit-learn
Joblib
```

or install using

```bash
pip install -r requirements.txt
```

---

## 💡 Future Improvements

- Interactive charts
- Better UI/UX
- Deployment on Render or Railway
- User authentication
- Database integration
- Model comparison
- Prediction history

---

## 👨‍💻 Author

**Madeshi Om Sai**

- GitHub: https://github.com/madeshiomsai

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

---

## 📄 License

This project is open-source and available under the MIT License.
