import regex
import os
import json


class BadWordsPlus:
    bad_words = [
    ]
    hard_mode = True

    def __init__(self, load_bad_words: bool = False, hard_mode: bool = True) -> None:
        if load_bad_words:
            for bad in json.loads(open(os.path.join(os.getcwd(), os.path.join(
                    "words", "default.json")), "r").read()):
                self.add_bad_word(bad)
        self.hard_mode = hard_mode
        pass

    def add_bad_word(self, bad_word: str):
        self.bad_words.append(regex.sub('[^A-Za-z0-9]+', '', bad_word))
        return self.bad_words

    def is_profane(self, text):
        """
        Returns True if text contains any profane words.
        """
        result = regex.search(r"\b(?:{})\b".format(
            (".*|.*" if self.hard_mode else "|").join(self.bad_words)), text)
        if result is not None:
            return len(result.group()) > 0
        else:
            return False

    def check_from_list(self, text_list: list, censor: bool = False):
        safe_list = list(
            filter(None, [self.check_from_string(t) for t in text_list]))
        return safe_list

    def check_from_string(self, text_string: str, censor: bool = False):
        safe_string = text_string if not self.is_profane(text_string) else None
        return safe_string
