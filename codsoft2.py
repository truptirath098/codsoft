#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import string

def generate_password(length, complexity):
    if complexity == 'low':
        characters = string.ascii_lowercase + string.digits
    elif complexity == 'medium':
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == 'high':
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase
    else:
        return "Invalid complexity level. Please choose 'low', 'medium', or 'high'."

    return ''.join(random.choice(characters) for _ in range(length))

length = int(input("Enter the desired length of the password: "))
complexity = input("Enter the complexity level (low, medium, high): ").lower()

print("Generated Password:", generate_password(length, complexity))

