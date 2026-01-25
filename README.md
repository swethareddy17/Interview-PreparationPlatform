
# AI Interview Preparation Platform (Flask Web Application)

## Abstract
The AI Interview Preparation Platform is a Flask-based web application designed to help students and job seekers prepare for technical interviews. The system generates role-specific interview questions, evaluates user responses using structured text-processing logic, and provides automated scoring and qualitative feedback. The application is built using a modular and scalable architecture suitable for academic evaluation and future AI enhancements.

---

## Problem Statement
Traditional interview preparation relies on static question banks and self-assessment, which lacks objectivity and structured feedback. Candidates often struggle to evaluate the quality of their answers and identify gaps in conceptual understanding. This project addresses the need for an automated interview preparation system that simulates interview scenarios and provides consistent, logic-based evaluation.

---

## Objectives
- To design a role-based interview question generation system  
- To evaluate candidate answers using text-processing techniques  
- To provide automated scoring and structured feedback  
- To implement a scalable Flask-based web architecture  
- To ensure modularity and maintainability for future enhancements  

---

## System Architecture
The application follows a layered architecture:

User Interface (HTML Templates)  
→ Flask Routes (Controller Layer)  
→ Core Logic Modules (Question Generation, Evaluation, Feedback)  
→ Data Layer (JSON Storage)

---

## Project Structure
```

AI/
│
├── app/
│   ├── **init**.py
│   ├── routes.py
│   └── config.py
│
├── core/
│   ├── **init**.py
│   ├── question_generator.py
│   ├── evaluator.py
│   ├── feedback.py
│   └── text_processing.py
│
├── data/
│   └── role_questions.json
│
├── storage/
│   ├── **init**.py
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

````

---

## Technologies Used
- Programming Language: Python  
- Web Framework: Flask  
- Text Processing: Regex, Keyword Matching  
- Frontend: HTML, CSS  
- Data Storage: JSON  
- Architecture Pattern: Modular / MVC-style  

---

## Module Description

### Question Generation Module
Selects interview questions based on the chosen job role from a structured dataset.

### Text Processing Module
Normalizes user input by converting text to lowercase, removing special characters, and tokenizing input.

### Answer Evaluation Module
Evaluates answers by matching predefined keywords and calculates a percentage score based on coverage.

### Feedback Module
Generates qualitative feedback based on the computed score to guide improvement.

### Storage Module
Stores interview results locally for future analysis.

---

## How to Run the Application

### Prerequisites
- Python 3.8 or higher
- Flask installed

### Installation
```bash
pip install flask
````

### Execution

```bash
python run.py
```

Open browser and navigate to:

```
http://127.0.0.1:5000
```

---

## Sample Output

* Role-based interview question displayed on screen
* User submits answer through web interface
* System displays score and feedback instantly

---

## Advantages

* Fully offline system (no external APIs required)
* Consistent and unbiased evaluation
* Modular and scalable design
* Suitable for academic and placement portfolios

---

## Future Enhancements

* Semantic answer evaluation using NLP techniques (TF-IDF, cosine similarity)
* User authentication and performance tracking
* Admin dashboard for question management
* Integration with AI/LLM models
* Deployment on cloud platforms

---

## Conclusion

The AI Interview Preparation Platform provides an effective and automated solution for interview practice. Its modular Flask-based design ensures maintainability, scalability, and suitability for final-year academic evaluation as well as real-world extension.

---

## Author

Pre Final Year B.Tech (Information Technology)
Project: AI Interview Preparation Platform


