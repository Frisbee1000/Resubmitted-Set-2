#!/usr/bin/env python
# coding: utf-8

# In[1]:


def shift_letter(letter, shift):
    if letter == " ":
        return " "
        
    original_position = ord(letter) - ord('A')
    new_position = (original_position + shift) % 26
    new_letter = chr(new_position + ord('A'))
    
    return new_letter

shift_letter(" ", 2)


# In[3]:


def caesar_cipher(message, shift):
    encrypted_text = ""
    
    for letter in message:
        if letter.isalpha():
            
            uppercase = letter.isupper()
            Value = ord(letter)
            New_Value = (Value - ord('A') + shift) % 26 + ord('A')
            New_Letter = chr(New_Value)
            
        else:
            New_Letter = letter
            
        encrypted_text += New_Letter
    
    return encrypted_text

caesar_cipher('I am Migs', 2)


# In[5]:


def shift_by_letter(letter, letter_shift):

    if letter == " ":
        return " "
    
    letter = letter.upper()
    letter_shift = letter_shift.upper()
    
    letter_position = ord(letter) - ord('A')
    shift_position = ord(letter_shift) - ord('A')
    
    new_position = (letter_position + shift_position) % 26
    
    shifted_letter = chr(new_position + ord('A'))
    
    return shifted_letter

shift_by_letter(" ","Z")


# In[7]:


def vigenere_cipher(message, key):
    key = key * (len(message) // len(key)) + key[:len(message) % len(key)]
    encrypted_message = []
    
    for a in range(len(message)):
        char = message[a]
        if char == ' ':
            encrypted_message.append(' ')
        else:
            shift = ord(key[a]) - ord('A') 
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_message.append(encrypted_char)
    
    return ''.join(encrypted_message)

vigenere_cipher("A C", "KEY")


# In[9]:


def scytale_cipher(message, shift):
   
    message_length = len(message)
    if message_length % shift != 0:
        message += '_' * (shift - (message_length % shift))

    encoded_message = []
    for a in range(len(message)):
        new_index = (a // shift) + (len(message) // shift) * (a % shift)
        encoded_message.append(message[new_index])

    return ''.join(encoded_message)

scytale_cipher("INFORMATION_AGE", 3)


# In[11]:


def scytale_decipher(message, shift):
    
    number_columns = len(message) // shift
    deciphered_message = [''] * len(message)
    index = 0
    
    for i in range(number_columns):
        for j in range(shift):
            
            original_index = i + j * number_columns
            deciphered_message[original_index] = message[index]
            index += 1
    
    return ''.join(deciphered_message)

scytale_decipher("IRIANMOGFANEOT__", 4)


# In[ ]:




