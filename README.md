\# 🌾 Smart Crop Recommendation System



A \*\*machine learning-based crop recommendation system\*\* that suggests the best crop to grow based on soil and weather parameters. The system is deployed using \*\*Streamlit\*\* for an interactive user interface.



---



\## 📁 Project Structure





---



\## ⚙️ Features



\- Takes \*\*soil nutrients\*\* (N, P, K), \*\*temperature\*\*, \*\*humidity\*\*, \*\*pH\*\*, and \*\*rainfall\*\* as input.

\- Uses \*\*Random Forest Classifier\*\* to predict the most suitable crop.

\- Interactive \*\*Streamlit interface\*\* with sliders for easy input.

\- Ready for deployment on \*\*local machine or cloud\*\*.



---



\## 🛠 Setup Instructions



1\. \*\*Clone the repository\*\*:

&nbsp;  ```bash

&nbsp;  git clone <your-repo-url>

&nbsp;  cd suggestion

suggestion/

│

├── app/

│ └── streamlit\_app.py # Streamlit interface

│

├── data/

│ └── SmartCrop-Dataset.csv # Dataset with soil and weather data

│

├── models/

│ └── crop\_model.pkl # Saved trained ML model

│

├── src/

│ ├── data\_processing.py # Load \& preprocess dataset

│ ├── model\_training.py # Train and save ML model

│ └── predict.py # Load model \& make predictions

│

├── requirements.txt # Python dependencies

└── README.md # Project description



