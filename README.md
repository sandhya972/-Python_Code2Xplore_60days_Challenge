Day 05 - Smart Transport Load Balancing
Full Name:Sandhya Yerragudi
L value (letters excluding spaces): 12
PLI value: 0
Applied Rule: Rule A - Move all Overload items to invalid Entries

Problem Statement
Classify package weights into Very Light, Normal, Heavy, Overload, or Invalid entries. Apply personalized logic (PLI) based on the number of letters in the name.

Approach / Logic Used
Take input weights and classify based on ranges.
Apply PLI rules based on L % 3.
Display final categorized weights and counts.
Test Cases
Input: [30, -5, 0, 80, 26, 15]
Output: L value: 12
PLI value: 0
Total Valid Weights: 5
Affected items due to PLI: 1
Very Light: [0]
Normal Load: [15]
Heavy Load: [30, 26]
Overload: []
Invalid Entries: [-5, 80]

