# Emotion Prediction using NLP

## Overview

This project uses machine learning and natural language processing techniques to classify the emotion expressed in text.

The pipeline performs text preprocessing, converts the processed text into numerical features using TF-IDF, and uses a Logistic Regression model to predict the emotion category.

## Approach

The project follows this workflow:

1. Text preprocessing
2. Stopword removal
3. TF-IDF feature extraction
4. Logistic Regression model training
5. Emotion classification
6. Interactive prediction through a Streamlit application

## Technologies

- Python
- NLTK
- Pandas
- NumPy
- scikit-learn
- Joblib
- Streamlit

## Model

The project uses:

- **TF-IDF** for converting text into numerical features.
- **Logistic Regression** for emotion classification.

The trained model and supporting preprocessing artifacts are saved using Joblib and loaded by the Streamlit application for prediction.

## Interactive Demo

A Streamlit application allows users to enter text and receive an emotion prediction using the trained model.

## Repository

GitHub: https://github.com/Abhinandan2023/emotion-prediction-ml

## Atlas Integration

This project is registered in AI Project Atlas as `ml-002`.
