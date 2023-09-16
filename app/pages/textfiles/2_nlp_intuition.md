We don't have time for a full rundown of how deep learning-based NLP works (it's a huge subject!), but let's concentrate on the essential details. Here's a simplified explanation of most NLP models:

1. First, we map our words to a maths-friendly representation (like `chocolate = [0.1, 0.333, -2]`) so we can do maths with them. We call this "vectorisation", because we're mapping from our input (text) space into a fixed "vector" space. Sometimes we'll do this at the sub-word level.
1. Next, we use the flexible sequence modelling of deep learning to combine the numbers together according to a flexible, parameterised model.
1. In the output layer of the model, our vectors now live in the "latent space" of our task, and as we train our model, this representation will be more and more useful for whatever task we're doing. We tend to think of this as the model knowing/learning the meanings of these words and how they relate to our output.
1. Finally, we apply some decision function to achieve our task, often some kind of classification. For the sake of similarity with our GZip example, assume we're doing a KNN lookup and just finding the closest points by some distance function. Here, because the model has done a lot of heavy lifting in shaping the meaning of the output space, we often just use the Euclidean (Pythagoras) distance you learned in high school.

Even though we've assumed we're doing KNN for the sake of discussion, it's worth noting that you can think of tasks like e.g. logistic regression as KNN. The neighbor in question though isn't another datapoint, but with respect to a hypothetical "average" datapoint which is encoded by the parameters of the model.

Regardless of which way we go, we understand NLP as learning the regularities that encode meaning in language, and understanding the relevance of these meanings as they relate to our task.
