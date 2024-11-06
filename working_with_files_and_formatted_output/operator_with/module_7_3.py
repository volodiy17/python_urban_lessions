from words_finder import WordsFinder

finder = WordsFinder('test_file.txt', 'captain.txt')
print(finder.get_all_words())
print(finder.find('TEXT'))
print(finder.count('teXT'))
print(finder.find('captain'))
print(finder.count('captain'))
print(finder.count('foR'))