# Translator: Created by:
Amir Mohammad Tavallali Nia.
# github profile link:
```
https://github.com/Tavallali134/translator
```
---
A simple graphical translation application built with Python and wxPython
 
## Description
This is a straightforward graphical translation application that utilizes Google Translate to translate both your text and files. It fully supports all languages offered by Google Translate, providing translations for any type of content.
Note: Since it relies entirely on Google Translate, occasional inaccuracies may occur, as with any machine translation service.
 
###Features
• 
Text Translation – Enter text and translate it to any supported language
• 
File Translation – Upload .txt files and translate their content
• 
Swap Languages – Quickly swap between source and target languages
• 
Keyboard Shortcuts – Speed up your workflow with handy shortcuts:
◦ 
Ctrl+T – Translate
◦ 
Ctrl+F – Open file
◦ 
Ctrl+R – Clear all fields
◦ 
Ctrl+W – Swap languages
◦ 
Ctrl+L – Focus on language selector
• 
70+ Languages Supported – Full support for all languages available in Google Translate
• 
User-Friendly Interface – Clean and intuitive design
 
#### Requirements
• 
Python 3.x
• 
wxpython==4.2.5

• 
deep_translator==1.11.4
 
##### Installation
1: Clone the repository:
```
git clone https://github.com/Tavallali134/translator.git
```
2: Install dependencies:
```
pip install wxPython deep-translator
```
3: Run the application:
```
python translator.py
```
 
###### How to Use
1: Enter your text in the top text box
2: Select your target language from the dropdown menu
3: Click Translate or press Ctrl+T
4: View the translated text in the bottom box
Translate a File:
1: Click From File... or press Ctrl+F
2: Select a .txt file
3: The content will load automatically
4: Click Translate or press Ctrl+T
***Other Features:***
• 
Clear – Clear both text boxes (Ctrl+R)
• 
Swap – Swap source and target languages (Ctrl+W)
 
####### Note
• 
An active internet connection is required for translation
• 
Supported file format: .txt (with UTF-8 or Latin-1 encoding)