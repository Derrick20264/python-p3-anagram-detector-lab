# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, candidate_list):
        results = []
        for candidate in candidate_list:
            # skip identical word
            if candidate.lower() != self.word and sorted(candidate.lower()) == sorted(self.word):
                results.append(candidate)
        return results
