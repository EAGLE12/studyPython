def translate(inputWord):
    outputWord = ""
    for word in inputWord:
        if word.lower() in ("aiueo"):
            outputWord = outputWord + "g"
        else:
            outputWord = outputWord + word
    return outputWord

print(translate(input("input word: ")))