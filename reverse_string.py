def reverse_string(s):
#base case: if the string is empty or contains only one character, return the string as it is
    if len(s) <= 1:
        return s
#recursive case: segarate the first character from the remaining characters
    first_char = s[0]
    remaining_chars = s[1:]
#recursively call reverse_string function with the remaining characters
    reversed_remaining =  reverse_string(remaining_chars)
#append the first character to the end of the reversed string of the remaining characters
    return reversed_remaining + first_char

#test cases
print(reverse_string("hello")) #output: olleh
print(reverse_string("python")) #output: nohtyp
print(reverse_string("")) #output: ""

    