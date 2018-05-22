def longestWord(word):
    longest_word_count = 0
    longest_word = ''
    curr_count = 0
    curr_word = ''

    for i,alpha in enumerate(word):
        if word[i].isalpha():
            curr_word += word[i]
            curr_count += 1
        else :
            if curr_count > longest_word_count:
                longest_word = curr_word
                curr_word = ''
                longest_word_count = curr_count
                curr_count = 0
    if curr_count > longest_word_count:
                return curr_word

   # if curr_count == len(word) :
    #     return word
    return longest_word.strip()

print(longestWord("A!! AA[]z, 123,AAzz"))