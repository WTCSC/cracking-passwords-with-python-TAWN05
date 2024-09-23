def count_chars(text):
    # Returns the lenth of text
    return len(text)


def count_words(text):
    # Returns length of text split into words.
    return len(text.split())
    
def count_sentences(text):
    # Counts periods and sets the number equal to i.
    i = text.count('.')
    # Counts bang's and sets the number equal to b.
    b = text.count('!')
    # Counts question marks and sets the number equal to a.
    a = text.count('?')
    # Defines num_sentances = to the sum of i, b, and a.
    num_sentences = (i + b + a)
    # Returns the varable num_sentences
    return num_sentences

def count_lines(filename):
    # Defines filename = "sample.txt".
    # Opens filename(sample.txt) as file.
    with open(filename) as file:
        # Defines lines = to read the lines of file.
        lines = file.readlines()
    # Return the length of lines.
    return len(lines)