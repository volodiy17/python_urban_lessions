from utils import string_to_wordlist

class WordsFinder:
    file_names = list

    def __init__(self, *files):
        self.file_names = files

    def get_all_words(self):
        all_words = dict()
        for file_name in self.file_names:
            with open(file_name, 'r') as f:
                all_words.update({file_name: [word.lower() for word in string_to_wordlist(f.read())]})
        return all_words

    def find(self, word: str):
        result = dict()
        all_files = self.get_all_words()
        for file_name in self.file_names:
            words = all_files.get(file_name)
            for i in range(0, len(words)):
                if words[i] == word.lower():
                    result.update({file_name: i + 1})
                    break
        return result

    def count(self, word: str):
        result = dict()
        all_files = self.get_all_words()
        for file_name in self.file_names:
            words = all_files.get(file_name)
            for i in range(0, len(words)):
                if words[i] == word.lower():
                    result.update({file_name: result.pop(file_name) + 1}) if result.get(file_name) else result.update({file_name: 1})
        return result
