# SnapClass – AI-Based Smart Attendance System

### Making Attendance Faster Using AI

## About the Project

SnapClass is a smart attendance management system developed to make the traditional classroom attendance process easier and faster. The main idea behind this project is to reduce manual attendance work by using AI-based facial and voice recognition.

The application provides separate interfaces for teachers and students, where teachers can create subjects and manage attendance, while students can enroll in subjects and mark their attendance.

## Features

- **Face Recognition:** Identifies students using facial recognition.
- **Voice Attendance:** Allows attendance to be recorded using voice recognition.
- **Teacher Dashboard:** Teachers can create subjects and manage their classes.
- **Student Dashboard:** Students can join subjects and manage their enrollment.
- **QR Code Sharing:** Teachers can generate QR codes to share subject joining links.
- **Attendance Management:** Attendance records are stored and managed digitally.
- **Database Integration:** Uses Supabase to store application data.

## Technologies Used

- Python
- Streamlit
- OpenCV
- Face Recognition
- NumPy
- Pandas
- Librosa
- Resemblyzer
- Supabase
- Bcrypt
- Segno

## How the Project Works

1. Teachers create an account and log in.
2. Teachers create subjects and share them with students using QR codes or links.
3. Students join the subjects and complete their enrollment.
4. The system uses facial recognition to identify students.
5. Voice-based attendance is also available.
6. Attendance information is saved in the database.

## Project Structure

```text
snap_class/
│
├── app.py
├── requirements.txt
│
├── src/
│   ├── components/
│   ├── database/
│   ├── pipelines/
│   ├── screens/
│   └── ui/
│
└── .streamlit/
```

## Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/Xyphorax018/snapclass-main-bornisha.git
```

**2. Move into the project folder**

```bash
cd snapclass-main-bornisha
```

**3. Create a virtual environment**

```bash
python -m venv venv
```

**4. Activate the environment**

For Windows:

```bash
venv\Scripts\activate
```

**5. Install the required packages**

```bash
pip install -r requirements.txt
```

**6. Configure Supabase**

Create a `.streamlit/secrets.toml` file and add your Supabase project credentials.

```toml
SUPABASE_URL = "your_supabase_url"
SUPABASE_KEY = "your_supabase_key"
```

**7. Run the application**

```bash
streamlit run app.py
```

## Future Improvements

There are several areas where I would like to improve SnapClass in the future:

- Improve face and voice recognition accuracy.
- Add attendance reports and analytics.
- Improve the application interface.
- Add more features to make attendance management easier.

## Author

**Bornisha Saha**

BCA Student | Developer in Progress


© 2026 Bornisha Saha. All rights reserved.

This project is created for educational and portfolio purposes. Unauthorized copying, redistribution, or commercial use of this code is not permitted without the author's permission.
