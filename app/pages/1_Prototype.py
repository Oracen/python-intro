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


# Instantiate components
X_train, X_test, y_train, y_test, label_map = create_data()

# Train model
model = create_model(X_train, y_train)


st.title("Basic ML Model Prototype")

st.subheader("Gzip Is All You Need")
st.markdown(
    f"Recently a paper was [published]({paper_url}) which caused quite a stir. With a "
    'the rather pedestrian title, \'"Low-Resource" Text Classification: A Parameter-'
    "Free Classification Method with Compressors', it showed a novel method of "
    "attaining competitive text classification scores on many benchmarks. It often "
    "outperformed transformer-based approaches, which are a class of significantly "
    "more complicated text models."
)
st.markdown(
    "The approach used was novel, but also kind of crazy. It was the sort of thing "
    "that probably shouldn't work. But, the theory behind it was sound, and gives "
    "us insights as to how LLMs achieve the things they do. It's also a handy reminder "
    "that you don't always need the most complicated approach, when something simple "
    "will do."
)
st.markdown("Tonight, we're going to play with this crazy little idea!")

st.image(
    image, caption="Red is where (bigger, more complex) models lose to a silly approach"
)

st.markdown(
    "As you read this, the model has already been trained, and we're "
    "generating some test data now. (This model is fast to train but the current) "
    "implementation is slow at test time.) Take a look and have a play, and we'll "
    "explain what's going on, and how this works, in the next page. For now, it's "
    "conceptually enough to know that the model is mapping the test input to the most "
    "'similar' training input, and assuming the label must be the same."
)

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

# Prep some test cases
random_indicies = not_so_rng.choice(X_test.shape[0], 100, replace=False)
test_cases = X_test[random_indicies].tolist()
test_labels = y_test[random_indicies].tolist()
(distances, predictions, similar_samples) = generate_predictions(
    model, test_cases, 0.025
)
report = classification_report(test_labels, predictions)

st.subheader("Predictive Accuracy")
st.markdown(
    "Below we have the classification report of our model. Note that the performance, "
    "while not amazing, is still pretty good for such a simple system with no tuning. "
    "This sort of performance was pretty much unheard of a few years ago, at least "
    "if you weren't using large RNN models."
)
st.text(report)

# Add text input
st.subheader("Try it yourself!")
st.markdown("Now you can have an idea of")
default_text = (
    "Socialites unite -  dolphin groups Dolphin groups, or 'pods', rely on socialites "
    "to keep them from collapsing, scientists claim."
)
test_sample = st.text_area("Input a headline here:", value=default_text)

(_, input_prediction_list, similar_samples) = generate_predictions(
    model, [test_sample], 0.1
)

user_prediction = input_prediction_list[0]

st.markdown("__The model predicts your label should be...__")
st.markdown(f"_{user_prediction} ({label_map[user_prediction]})_")

st.markdown("__And to see where it's getting that from, the similar datapoint is...__")
st.markdown(f'_"{similar_samples[0][0]}"_')
