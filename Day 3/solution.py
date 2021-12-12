def spin_words(sentence):
    new_sentence = ""
    for word in sentence.split(" "):
        if len(word) >= 5:
            new_sentence += word[::-1]
        else:
            new_sentence += word
    return new_sentence