# Apollos Eastman
# 10/4/2024
# Ceasar Cypher Starter

# encrypt
alphabet = 'abcdefghijklmnopqrstuvwxyz'
new_message = ''

user_message = input('Enter your unencrypted message:').lower()
key = int(input('Enter a key:'))
# print (user_message)

for character in user_message:
    if character in alphabet:
        position = alphabet.find(character)
        new_position = (position + key) % 26
        new_character = alphabet[new_position]
        new_message += new_character
    else:
        new_message += character
print ('Your new message is ' + new_message)

# decrypt

alphabet = 'abcdefghijklmnopqrstuvwxyz'
new_message = ''

user_message = input('Enter your encrypted message:').lower()
key = int(input('Enter a key:'))
# print (user_message)

for character in user_message:
    if character in alphabet:
        position = alphabet.find(character)
        new_position = (position - key) % 26
        new_character = alphabet[new_position]
        new_message += new_character
    else:
        new_message += character
print ('Your new message is ' + new_message)


