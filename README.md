# HackPSU2023

# Nittany Guesser - Where AI Meets Imagination!

Hello there! 🚀 Welcome to the exciting world of `Nittany Guesser` - an intuitive application where the AI takes a wild yet educated guess about a location based on a sequence of yes/no questions.

## What's Inside?
`Nittany Guesser` is not just another guesser game; it's a fascinating fusion of `Tkinter` for GUI, the PIL library for image operations, and OpenAI's GPT-4 model. This application initiates a conversation, extracts insights from user inputs, and strategically crafts the next best question. All of this with a fun GUI interface sprinkled with captivating lion images.

## Why is it interesting?

### 1. **Binary Search Approach 🌲**
    - At its core, the AI operates on a principle reminiscent of binary search.
    - Just like binary search halves the possible search space with every step, our AI, with each question, tries to narrow down the location possibilities based on your answers.
    - By continually refining its scope, the AI can converge to a probable guess about the location in just a handful of questions!

### 2. **Integration with OpenAI 🧠**
    - We use the OpenAI API to dynamically generate questions.
    - With every answer you provide, the AI evaluates the conversation context and formulates the next optimal question.
    - This means no two games will be precisely the same. The AI adapts to the conversation flow, making the experience dynamic and engaging.

### 3. **A Picture is Worth a Thousand Words 🖼**
    - As the game progresses, there's a carousel of fun lion images to keep you entertained.
    - The real kicker? At the end, using the same OpenAI API, the application can even produce a tailored image based on the concluded guess of your location. That's right, an image that encapsulates the essence of the entire conversation!

## How does it work?

1. **Configuration First**:
   Begin by ensuring your `config.ini` contains the right API key. This key is the gateway for the application to harness the capabilities of OpenAI.

2. **Tkinter Magic**:
   Once initiated, `Tkinter` (augmented with `customtkinter` for those snazzy buttons) gets into action, setting up the game interface. Watch out for the cool loading screen with a Nittany Lion gif!

3. **Question-Answer Loop**:
   - The AI presents an initial question from a preset list. 
   - As you answer, the application consults OpenAI, evaluates past interactions, and crafts the next best question.
   - This continues until the AI feels confident enough to make a guess or reaches a predefined number of questions.

4. **Visual Finale**:
   Once the AI makes its final guess, it harnesses the OpenAI API's image generation capabilities. The result? A unique image that symbolically represents the concluded location. A visual treat to culminate a fun game!

## Dive in and Let the AI Guess!
Experience the thrill of AI-driven conversation. Challenge it, outthink it, or simply have fun with it. Who knows, you might just be surprised by how accurate or creative `Nittany Guesser` can be!

Happy Guessing! 🎉
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Setting Up and Running the Image Guessing Program

**Prerequisites**: Ensure you have Python installed on your machine.

## Step 1: Install Required Libraries

Open your terminal or command prompt and execute the following commands to install the necessary libraries:

```bash
pip install tkinter
pip install customtkinter
pip install Pillow
pip install openai
pip install requests
pip install configparser
```

## Step 2: Install Required Libraries
    - Create a new file named main.py. 
    - Copy and paste the provided code from the repository into this file.

## Step 3: Configure API Key
    - Create a new file in the same directory as main.py and name it config.ini.
    -Copy and paste the API key template provided in the repository into config.ini.
    -Replace the placeholder with your actual OpenAI API key.

## Step 4: Execute the Program
With everything in place, navigate to the directory containing main.py in your terminal or command prompt and run:
```bash
python main.py
```


