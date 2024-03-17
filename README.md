**PART 1**
# text-completion-model-autocomplete
A Text Completion Generative Language Model using Python

**How this works?**
The model simplifies its task by analyzing only the last word in a given sentence.  For each input word, the model maintains a 'chart' (like a dictionary) mapping it to a list of possible subsequent words, along with their probabilities. This resembles a raffle where words have varying chances of being drawn. As the model progresses, it uses the newly predicted word to consult the chart again, predicting the next word in a sequence. Imagine the model has a box of word tokens.  When you give it a word, it looks inside the box for matching tokens and finds a bunch of other words frequently seen after it.  It then picks one of those "next" words, somewhat randomly, and uses this new word to repeat the process! Our model only considers the last word in the input.

**PART 2**
# sentiment-analysis-model
A Negative/Positive Comments Sentiment Analysis model using Python

**PART 3**
# word-embeddings-model
A model that calculates cosine similarity between words of similar length




