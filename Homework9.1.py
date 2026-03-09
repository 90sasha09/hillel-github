def popular_words(text, words):
    text_words = text.lower().split()
    result = {}

    for word in words:
        result[word] = text_words.count(word)

    return result

