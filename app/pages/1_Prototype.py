import streamlit as st
from sklearn.metrics import classification_report

from python_intro import app_functions

model, label_map, test_cases, test_labels = app_functions.cycle_state()


st.title("Playing with the Prototype")

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
intro = f"Here are the dataset labels and the human-friendly categories:"
st.markdown(
    "\n".join([intro] + [f"- {key} = {value}" for key, value in label_map.items()])
)

# Prep some test cases
(distances, predictions, similar_samples) = app_functions.generate_predictions(
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
st.markdown(
    "Now you can have an idea of what is likely to work, try inputting a few made-up "
    "headlines below. See what words and phrases can confuse the model! (I've found "
    "random line-breaks and symbols can often produce strange results.)"
)
default_text = (
    "Socialites unite -  dolphin groups Dolphin groups, or 'pods', rely on socialites "
    "to keep them from collapsing, scientists claim."
)
test_sample = st.text_area("Input a headline here:", value=default_text)

(_, input_prediction_list, similar_samples) = app_functions.generate_predictions(
    model, [test_sample], 0.25
)

user_prediction = input_prediction_list[0]

st.markdown("__The model predicts your label should be...__")
st.markdown(f"_{user_prediction} ({label_map[user_prediction]})_")

st.markdown("__And to see where it's getting that from, the similar datapoint is...__")
st.markdown(f'_"{similar_samples[0][0]}"_')
