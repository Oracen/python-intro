import pathlib

import streamlit as st
from PIL import Image

from python_intro import dpaths

TEXTFILES = pathlib.Path(__file__).parent / "textfiles"

image_gzip_explained = Image.open(dpaths.STATIC / "gzip-explained.png")
image_nlp_intuition = Image.open(dpaths.STATIC / "nlp-intuition.png")


def load_text(filename):
    with open(TEXTFILES / filename, "r") as handle:
        return handle.read()


st.title("A Peek Inside The Black Box")
st.markdown(load_text("2_intro.md"))

st.subheader("What Compressor Models Do")
st.image(image_gzip_explained)
st.markdown(load_text("2_compressor_explained.md"))

st.subheader("How We Think Of NLP's Mechanics")
st.image(image_nlp_intuition)
st.markdown(load_text("2_nlp_intuition.md"))

st.subheader("So What's Going On Here?")
st.subheader("What Can We Learn?")
