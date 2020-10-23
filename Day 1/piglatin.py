def pig_it(text):
    new_sentence = []
    sentence = text.split(" ")
    for word in sentence:
        if word == "!" or word == "?":
            new_sentence.append(word)
        else:
            new_word = f"{word[1:]}{word[0]}ay"
            new_sentence.append(new_word)
    return " ".join(new_sentence)
