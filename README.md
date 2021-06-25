# Story Reader
A small script to have branched stories read with multiple choices. you can easily edit it. 
The script comes with an example story, so you can play with it and see how it works.

## HOW TO USE

### 1) Add your story pages into the "Story.py" file following this template :

      {
          "page_number": {
              "text": 
                  "Enter text here\n",
              "outcomes": [""],
              "settings": [LINE_DELAY, DELAY],
      },
      
Explanation of each field : 
 * text : you can enter you text here, it will be displayed in the console. If you want to insert multiple lines you still can use breakline character "\n"
 * outcomes : your story can have 1 or more choices to make. Say your text says "Say A to go right, B to go left". If user type A, first outcome is read and we're going to the page indicated by the first item of "Outcome".
If there is only one possible outcome, this outcome is automatically selected.
 * settings : This script prints letters one by one at varying speed, you can leave default settings or pick a faster / slower rate to display your text.
    * LINE_DELAY : Time in ms before the line starts to write
    * DELAY : delay between each letter.
 
### 2) Launch "Story_reader.py"
Your story unfolds ! You only have to say what path you take. 
