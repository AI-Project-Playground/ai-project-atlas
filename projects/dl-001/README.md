# AI Quote Generator using LSTM

A category-conditioned quote generation project using a Long Short-Term Memory (LSTM) neural network.

## Overview

This project uses a trained LSTM model to generate quotes based on a selected category.

The model generates text one word at a time, using the previously generated sequence to predict the next word.

## Features

- Category-conditioned quote generation
- LSTM-based text generation
- Adjustable maximum quote length
- Adjustable creativity using temperature sampling
- Repetition penalty to reduce repeated words
- Interactive Streamlit interface

## Technologies

- Python
- TensorFlow
- Keras
- NumPy
- Streamlit

## Model

The project uses a trained LSTM model with an embedding layer and recurrent sequence modeling for next-word prediction.

During generation, temperature sampling controls the randomness of the predictions, while a repetition penalty helps reduce excessive repetition.

## Interactive Demo

The project includes an interactive Streamlit application where users can:

1. Select a quote category.
2. Set the maximum number of words.
3. Adjust creativity/temperature.
4. Adjust the repetition penalty.
5. Generate a quote.

**Live Demo:** https://ai-quote-generator-lstm.streamlit.app/

## Project Files

- `lstm_l1_v1.ipynb` — model development and training notebook
- `app.py` — Streamlit application
- `tokenizer_v3.pkl` — saved tokenizer
- `requirements.txt` — project dependencies

The trained LSTM model (`quote_lstm_model_v3.keras`) is maintained in the original project repository using Git LFS:

https://github.com/Abhinandan2023/AI-Quote-Generator

## Atlas Integration

This project is integrated into AI Project Atlas as:

**Project ID:** `dl-001`

**Project Type:** Deep Learning

**Capability:** Generate