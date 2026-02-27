# ASCII-Clock
A Python-based terminal utility that converts digital timestamps into stylized ASCII art displays. This project was developed as part of a programming assignment to demonstrate data structure manipulation, string formatting, and time conversion logic.

Features
Custom ASCII Font: Uses a dictionary-based mapping to render digits (0-9), separators (:), and meridiem indicators (AM/PM) in a 5-row high block format.

12/24 Hour Toggle: Includes logic to automatically convert 24-hour input (e.g., 14:30) into 12-hour format with AM/PM suffixes (e.g., 2:30PM).

Character Skinning: Allows users to "skin" the clock by replacing the standard digits with a preferred character (e.g., @, *, or &).

Input Validation: Features a robust whitelist filter to ensure only permitted special characters and lowercase letters are used for rendering.

🛠️ Technical Implementation
The script utilizes a modular approach to handle the display logic:

Data Structures: Each character is stored as a list of five strings, representing its vertical rows.

display_ascii Function: A core rendering engine that iterates through each row of the time string, replaces characters based on user preference, and joins them into a cohesive terminal output.

String Formatting: Uses f-strings and list splitting to manage time transitions and formatting.

🚀 Usage
Run the script: python ascii_clock.py

Provide the following inputs when prompted:

Time: (e.g., 13:45)

Clock Type: (12 or 24)

Preferred Character: (e.g., *)

