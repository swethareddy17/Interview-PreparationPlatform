🚀 Interview-PreparationPlatform

A Flask-based web application designed to help students and job seekers prepare for technical interviews through automated question generation, answer evaluation, and feedback.

📌 Project Overview

The Interview-PreparationPlatform simulates real interview scenarios by generating role-based questions and evaluating user responses using structured text-processing techniques. It provides instant scoring and feedback, helping users improve their performance effectively.

🎯 Features
✅ Role-based interview question generation
✅ Automated answer evaluation using keyword matching
✅ Instant score calculation
✅ Structured feedback for improvement
✅ Simple and user-friendly interface
✅ Fully offline (no external APIs required)
✅ Modular and scalable architecture
🛠️ Tech Stack
Backend: Python, Flask
Frontend: HTML, CSS
Data Storage: JSON
Text Processing: Regex, Keyword Matching
Architecture: Modular / MVC-style
📂 Project Structure
AI/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── config.py
│
├── core/
│   ├── __init__.py
│   ├── question_generator.py
│   ├── evaluator.py
│   ├── feedback.py
│   └── text_processing.py
│
├── data/
│   └── role_questions.json
│
├── storage/
│   ├── __init__.py
│   └── results.py
│
├── templates/
│   ├── index.html
│   ├── interview.html
│   └── result.html
│
├── static/
│   └── style.css
│
└── run.py
⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/sure-trust/K.NAGASWETHA-g30-fsd.git
cd K.NAGASWETHA-g30-fsd
2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate   # On Windows
3️⃣ Install Dependencies
pip install flask
▶️ Run the Application
python run.py

Now open your browser and go to:

http://127.0.0.1:5000
🧠 How It Works
User selects a job role
System fetches relevant interview questions
User submits answer
System processes text and evaluates using keywords
Score and feedback are displayed instantly
📸 Sample Output
Interview question displayed
User submits answer
Score and feedback shown
🌟 Advantages
Works completely offline
Provides consistent evaluation
Easy to use and lightweight
Suitable for academic and portfolio projects
🔮 Future Enhancements
NLP-based semantic evaluation (TF-IDF, cosine similarity)
User login and performance tracking
Admin dashboard
Integration with AI/LLM models
Cloud deployment
👩‍💻 Author

Kamana Naga Swetha
B.Tech (Computer Science)
Final Year Student

🔗 Repository Link

👉 https://github.com/sure-trust/K.NAGASWETHA-g30-fsd.git

⭐ Support

If you like this project, give it a ⭐ on GitHub!
