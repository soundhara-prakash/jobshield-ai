# JobShield – AI-Powered Fake Job Detection System

JobShield is an AI-based system designed to detect fraudulent job listings circulating across **online job ecosystems**, including professional networking platforms, social media channels, and digital job communities.

The system analyzes job descriptions using **Natural Language Processing (NLP)** and classifies them as **Real** or **Scam**.

---

## Problem Statement

Fraudulent job opportunities are increasingly spread across online job ecosystems.  
Scammers often advertise unrealistic earnings, request registration fees, or redirect applicants to external communication channels.

Because such listings appear across multiple digital platforms, it becomes difficult for users to manually identify fraudulent posts.

This creates the need for **automated AI-based detection systems** that can analyze job descriptions and flag suspicious listings.

---

## Proposed Solution

JobShield uses **NLP-based text classification** to analyze job descriptions and detect fraudulent patterns.

The system processes job text through a machine learning pipeline and returns:

- Prediction (**Real / Scam**)
- Model **Confidence**
- **Flagged suspicious patterns** explaining the prediction

---

## System Architecture


User Input (Job Description)
↓
Frontend Interface (HTML + JavaScript)
↓
Flask Backend API
↓
NLP Model (TF-IDF + Logistic Regression)
↓
Prediction Output


---

## Technology Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python Flask

### Machine Learning
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression

---

## Features

- AI-based job scam detection
- Confidence score for prediction
- Explainable AI output showing flagged patterns
- Simple web interface for demonstration

---

## Example Output

### Input Job Description


Earn ₹30000 daily work from home
Registration fee required
Contact WhatsApp immediately


### Output


Prediction: SCAM
Confidence: 0.91

Flagged Patterns:
• Registration Fee
• External Contact
• Unrealistic Earnings


---

## Project Structure


jobshield-ai
│
├── dataset # Training dataset
├── model # ML model training code
├── backend # Flask API for predictions
├── frontend # Web interface
├── demo # Demo assets
└── README.md


---

## Demo Video

Demo Video Link:  https://youtu.be/kTPhvfMggwo

---

## Hackathon

Project developed for **AI4Dev '26 – AI-Enabled Transformative Technologies for Global Development Hackathon**.

Hosted by the Coding Club at PSG College of Technology.

---

## Future Improvements

- Train the model on larger real-world datasets
- Integrate with live digital job platforms
- Add advanced NLP models (BERT / Transformer architectures)
- Develop a browser extension for scam detection

---

## License

This project is developed for educational and hackathon purposes.
