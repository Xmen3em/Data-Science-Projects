import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
import pickle

max_len = 14
vocab_size = 4801

# Load the vocabulary using pickle
with open('vocab.pkl', 'rb') as f:
    vocab = pickle.load(f)

# Load the vectorizer using pickle
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Define the model structure (using your saved model)
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(max_len - 1,), name='Input'),
    tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=100, input_length=max_len - 1),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(150, return_sequences=True)),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(100)),
    tf.keras.layers.Dense(100, activation='relu'),
    tf.keras.layers.Dense(vocab_size, activation='softmax')
], name='model')

# Load pre-trained model weights
model.load_weights('Model.weights.h5')

# Function to generate text
def generate_text(model, seed_text, next_words, max_sequence_len, vocab):
    for _ in range(next_words):
        # Ensure the seed_text is wrapped in a list
        token_list = vectorizer(seed_text).numpy()  
        pad_sequence = np.array(tf.keras.preprocessing.sequence.pad_sequences([token_list], maxlen=max_sequence_len - 1, padding='pre'))
        
        # Predict next word
        predicted = np.argmax(model.predict(pad_sequence), axis=-1)
        if predicted == 0:
            continue
        
        output_word = vocab[predicted[0]]
        seed_text += " " + output_word
    return seed_text


# Streamlit app interface
st.title("Next Word Prediction")

# Input seed text
seed_text = st.text_input("Enter the seed text:", "the Rituals of my Watch, bid them make")

# Input number of words to predict
next_words = st.number_input("Number of words to predict:", min_value=1, max_value=50, value=10)

# Prediction button
if st.button("Predict"):
    # Generate text based on user input
    predicted_text = generate_text(model, seed_text, next_words, max_len, vocab)
    st.write(f"{predicted_text}")

