Day 06 - Smart Playlist Analyzer

Problem Statement:

Classify a playlist based on songs duration into Too short, TOO long, Repetitive, Balanced, Irregular, or Invalid Playlist.

Approach / Logic Used:
I created a python program that takes the number of songs and their duartions as input using a list. First, I validated the inputs by checking if any duration is less than or equal to zero and marked the playlist as invalid if found. This i calculated the total duration using sum() to check whether the playlist is Too short or Too long.I checked for repetition by comparing the length of the list with unique values.  Finally ,based on all conditions ,i categorized the playlist and displayed the result.


Test Cases:

Input: Enter number of songs: 4
Enter duration: 180
Enter duration: 200
Enter duration: 220
Enter duration: 210
Total Duration: 810 seconds
Songs: 4
Category: Balanced Playlist
Recommendation: Good listening session


