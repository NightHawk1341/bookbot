def turn_to_words(text):
    words = text.split()
    number_of_words = len(words)
    return number_of_words
def count_characters(text):
    chars_frequency = {}
    for char in text:
        char = char.lower()
        if char not in chars_frequency:
            chars_frequency[char] = 1
        else:
            chars_frequency[char] += 1
    return chars_frequency

def sorted_characters(chars_frequency):
    sorted = []
    def sort_on(dict):
        return dict["num"]
    for char, frequency in chars_frequency.items():
        sorted.append({"char": char, "num": frequency})
    sorted.sort(reverse=True, key=sort_on)
    return sorted