
import random
from string import punctuation
from collections import defaultdict


class MarkovChain:
    def __init__(self):
        # gives model a default dictionary that produces lists as its graph to hold raffle possibilities for each token
        self.graph = defaultdict(list)

    #get rid of punctuation
    def _tokenize(self, text):
        return (
            text.translate(str.maketrans("", "", punctuation + "1234567890"))
            .replace("\n", " ")
            .split(" ")
        )

    #
    def train(self, text):
        tokens = self._tokenize(text)
        #loop through tokens
        for i,token in enumerate(tokens):
            if (len(tokens)-1)==i:
                break
            self.graph[token].append(tokens[i+1])


    def generate(self, prompt, length=10):
        # get the lask token from the prompt
        current = self._tokenize(prompt)[-1]
        # initialize the output
        output = prompt
        for i in range(length):
            # look up the options in the graph dictionary
            options = self.graph.get(current, [])
            if not options:
                continue
            # use random.choice method to pick a current option

            # add the random choice to the output string

        return output
