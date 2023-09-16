import numpy as np
import streamlit as st
from datasets import load_dataset
from npc_gzip.compressors.gzip_compressor import GZipCompressor
from npc_gzip.knn_classifier import KnnClassifier

not_so_rng = np.random.default_rng(42)


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


@st.cache_data
def generate_predictions(_model, list_of_test_items, sampling_percentage=0.2):
    (distances, labels, similar_samples) = _model.predict(
        list_of_test_items, 1, sampling_percentage=sampling_percentage
    )
    labels = labels.reshape(-1)
    return (distances, labels, similar_samples)


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


@st.cache_resource
def cycle_state():
    checks = ["model", "label_map", "test_cases", "test_labels"]
    if all(item in st.session_state for item in checks):
        print("Session cache hits!")
        model, label_map = st.session_state.model, st.session_state.label_map
        test_cases = st.session_state.test_cases
        test_labels = st.session_state.test_labels
        return model, label_map, test_cases, test_labels

    X_train, X_test, y_train, y_test, label_map = create_data()
    model = create_model(X_train, y_train)

    random_indicies = not_so_rng.choice(X_test.shape[0], 100, replace=False)
    test_cases = X_test[random_indicies].tolist()
    test_labels = y_test[random_indicies].tolist()

    st.session_state.model = model
    st.session_state.test_cases = test_cases
    st.session_state.test_labels = test_labels
    st.session_state.label_map = label_map

    return model, label_map, test_cases, test_labels
