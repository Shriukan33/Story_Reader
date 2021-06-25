
#Default settings
LINE_DELAY = 0.35
DELAY = 0.025

pages = {
    # outcomes key = List of page numbers depending on you choice. Option A -> 1st item of outcomes and so on 
    "page_number": {
        "text": 
            "Enter text here\n",
        "outcomes": [""],
        "settings": [LINE_DELAY, DELAY],
    },

    "intro": {
        "text":
            "Hey this is the intro of my story !\n",
        "outcomes": ["1"],
        "settings": [LINE_DELAY, DELAY],
    }, 

    "1": {
        "text": 
            "This is page 1 of my story, easy to edit ! Choose path A (slow text) or B (fast text)\n", 
        "outcomes": ["3", '4'],
        "settings": [LINE_DELAY, DELAY],
    },

    "3": 
        {"text": 
            "You chose path A on the page 1 ! going to the end now.\n", 
        "outcomes": ["end"],
        "settings": [LINE_DELAY, 0.05],
    },
    
    "4": 
        {"text": 
            "You chose path B on the page 1 ! going to the end now.\n", 
        "outcomes":["end"],
        "settings": [LINE_DELAY, 0.01],
    },

    "end": {
        "text": 
            "This is the end of the demo\n",
        "outcomes": ["exit"],
        "settings": [LINE_DELAY, DELAY],
    },
}

