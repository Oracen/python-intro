import numpy as np
import pandas as pd
import streamlit as st
from datasets import load_dataset
from npc_gzip.compressors.base import BaseCompressor
from npc_gzip.compressors.gzip_compressor import GZipCompressor
from npc_gzip.knn_classifier import KnnClassifier
from PIL import Image
from sklearn.metrics import classification_report

from python_intro import dpaths

# Set variables
image = Image.open(dpaths.STATIC / "gzip-performance.png")
not_so_rng = np.random.default_rng(42)
paper_url = "https://aclanthology.org/2023.findings-acl.426.pdf"


# Function definitions
@st.cache_data
def create_data(dataset="ag_news"):
    # Dataset arg is used to cache properly
    dataset = load_dataset(dataset)

    label_map = {
        idx: name
        for idx, name in enumerate(
            dataset["train"].features["label"].names  # type:ignore
        )
    }

    X_train = np.array(dataset["train"]["text"])  # type: ignore
    X_test = np.array(dataset["test"]["text"])  # type: ignore
    y_train = np.array(dataset["train"]["label"])  # type: ignore
    y_test = np.array(dataset["test"]["label"])  # type: ignore
    return X_train, X_test, y_train, y_test, label_map


@st.cache_resource
def create_model(x_train, y_train):
    compressor = GZipCompressor()
    model = KnnClassifier(
        compressor=compressor,
        training_inputs=x_train.tolist(),
        training_labels=y_train.tolist(),
        distance_metric="ncd",
    )
    return model


@st.cache_data
def generate_predictions(_model, list_of_test_items, sampling_percentage=0.2):
    (distances, labels, similar_samples) = model.predict(
        list_of_test_items, 1, sampling_percentage=sampling_percentage
    )
    labels = labels.reshape(-1)
    return (distances, labels, similar_samples)


st.title("Welcome to the Demo Club!")

st.markdown(
    "Congrats on making it this far! Here's a small reward for all your hard work "
    "getting this far - a bit of playtime before we get back to learning."
)

st.markdown(
    "This demo is a machine learning system live on your machine, being "
    "recalculated in response to your inputs. Have a play around with it, and "
    "later we'll explore how to build this site (on the branch `feature/simple-app`), "
    "as well as give you a more complicated demo to play with (on the branch "
    "`feature/complex-app`)."
)


# Instantiate components
X_train, X_test, y_train, y_test, label_map = create_data()

# Train model


st.subheader("Dataset Details")
st.markdown(
    "Here we are using the `ag_news` dataset, helpfully maintained by Huggingface. "
    "This dataset is a collection of headline items, alongside one of 4 category "
    "labels. The task, then, is to predict the category of the headline, given its "
    "text. You'll have a chance at the bottom of this page to test this out for "
    "yourself. Note that the model will only do 'well' if you give it sensible inputs "
    "(i.e. it will probably do badly with TikTok video titles!). But you can also have "
    "some fun with this, as the model struggles to classify some obscure input!"
)
st.markdown(
    f"Here are the dataset labels and the human-friendly categories: {label_map}"
)

model = create_model(X_train, y_train)

# Add text input
st.subheader("Try it yourself!")
st.markdown("Now you can have an idea of")
default_text = (
    "Socialites unite -  dolphin groups Dolphin groups, or 'pods', rely on socialites "
    "to keep them from collapsing, scientists claim."
)
test_sample = st.text_area("Input a headline here:", value=default_text)

(_, input_prediction_list, similar_samples) = generate_predictions(
    model, [test_sample], 0.25
)

user_prediction = input_prediction_list[0]

st.markdown("__The model predicts your label should be...__")
st.markdown(f"_{user_prediction} ({label_map[user_prediction]})_")

st.markdown("__And to see where it's getting that from, the similar datapoint is...__")
st.markdown(f'_"{similar_samples[0][0]}"_')
