import streamlit as st
from PIL import Image

from python_intro import app_functions, dpaths

# Set variables

image = Image.open(dpaths.STATIC / "gzip-performance.png")
paper_url = "https://aclanthology.org/2023.findings-acl.426.pdf"

st.title("Basic ML Model Prototype")

st.markdown(
    "This demo is a machine learning system live on your machine, being "
    "recalculated in response to your inputs."
)

# Instantiate components
app_functions.cycle_state()

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
