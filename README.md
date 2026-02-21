Day 05 - Smart Transport Load Balancing System`

1.Count the characters in "sandhya reddy" excluding space → L = 12.
2.Calculate PLI = L % 3 = 12 % 3 = 0.
3.Since PLI = 0, apply Rule 1 → Move all overload items to invalid entries and clear the overload list.

Problem Statement:

Design a Python program to classify the weights of packages into load categories and determine a Personal Load Index (PLI) based on the length of a given name (excluding spaces). According to the PLI value, apply certain rules to adjust the categories and print the final results along with the number of items affected.

Approach / Logic Used:

The program begins by calculating the number of characters in the given name (excluding spaces) to determine the Personal Load Index (PLI) through the modulus operation.
The program then proceeds to classify the weights according to their categories, which include Very Light, Normal Load, Heavy Load, Overload, and Invalid through the use of conditional statements. Lastly, the program alters the categories according to the PLI value and displays the final results.



