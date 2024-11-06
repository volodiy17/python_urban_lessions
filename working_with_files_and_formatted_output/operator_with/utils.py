def string_to_wordlist(string: str) -> list:
    symbols_to_remove = [',', '.', '=', '!', '?', ';', ':', '-', u'\t']
    return [word for word in string.translate(str.maketrans('', '', ''.join(symbols_to_remove))).replace(u"\n", " ").split(" ") if word != ""]

