# AI Recommendation System

An Artificial Intelligence based Recommendation System developed using Python and Flask.

## Project Overview

This project recommends movies based on user preferences using similarity matching logic.

The system analyzes selected genres and recommends movies with the highest matching score.

## Features

- User preference input
- Similarity matching
- Recommendation engine
- Match score calculation
- Flask web interface
- Clean UI design

## Technologies Used

- Python
- Flask
- HTML
- CSS

## Project Structure

AI-Recommendation-System/
│
├── app.py
├── recommender.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css

## Installation

Install dependencies:

```bash
pip install -r requirements.txt

Run the application:
python app.py

Open in browser:
http://127.0.0.1:5000

Recommendation Logic

The recommendation engine compares user-selected genres with movie genres and calculates a similarity score.

Higher score = better recommendation.
