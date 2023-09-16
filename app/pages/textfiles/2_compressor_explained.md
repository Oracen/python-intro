As this presentation has been alluding to, GZip is at the core of the compressor model, though it's reasonable to assume that other algorithms could work too. Compression algorithms are used to "shrink" files down. The details of how compression algorithms do this aren't important. We just need to note a single thing - that compression algorithms use repeated patterns in their input to find a more space-efficient 'coding' of the input. That is, compression can be used to make data (including text) shorter, and the more repeating patterns are in the text, the better this works.

So how does the model use Gzip to make predictions? It's actually quite simple. Alarmingly simple. The model takes in a list of strings - or bits of text - as input. It then compresses the strings and measures the length of the compressed examples. This is just some number $n >= 0$. These values are stored as a set of `(example, length_examples, label)` pairs. With that, the training step is done. No, seriously.

At inference time, it's a little more complicated, but only a little. Given a new string `input`, the model does the following:

1. The `input` is compressed and its length (`length_input`) recorded
1. The model randomly samples from the `examples`.
1. The model concatenates (joins) the `input` string to each of the sampled `examples`, compresses the resulting long string, and measures the length `length_joined`.

   - Think about it for a moment and convince yourself that `length_joined` will be at least as long as one of the other two lengths, and should be no longer than both of their lengths added. Let's call these the `lower` and `upper` bounds respectively

1. We then measure how "far" the `input` is from any other datapoint by considering how "far" from the `lower` bound `length_joined` is. We call this the distance
1. Finally, we check the `labels` where the distance is lowest, corresponding to the most compressible points. We then take the max or use a simple voting algorithm to pick a label.

So, in essence, what we do is check how much of a compression saving we get between any two strings, and consider this as a measure of similarity. Compared to a transformer or an RNN, this is trivial to reason about. It's technically not even machine learning, because there aren't really parameters here.

**This is wild.**
