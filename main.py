#pip install tkinter
#pip install customtkinter
#pip install Pillow
#pip install openai
#pip install requests
#pip install configparser

import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import openai
import random
import requests
import os
import configparser

# Parse the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Set the OpenAI API key
openai.api_key = config.get('OPENAI', 'API_KEY')

initial_questions = [
    "Is the place where you are hot?",
    "Is the place where you are real?",
    "Is there water around you?",
    "Do you hear any noise?",
    "Is it crowded where you are?"
]


def generate_next_question(initial_question, answer):
    prompt = (f"Given the initial question: '{initial_question}' and the user's answer: '{answer}', what should be the "
              f"next question to narrow down the location?")
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=150)
    return response.choices[0].text.strip()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Nittany Guesser")
        self.geometry("800x600")
        self.resizable(False, False)
        self.background = "black"
        self.font = "white"
        self.questions_asked = 0
        self.conversation_history = []
        self.lion_images = [f for f in os.listdir("lions") if
                            os.path.isfile(os.path.join("lions", f)) and f.endswith(".png")]

        self.loading_screen()

    def loading_screen(self):
        self.playing_gif = True
        # Load and resize each frame of the GIF
        gif_frames = []
        gif = Image.open("nittany_lion.gif")
        for frame in range(0, gif.n_frames):
            gif.seek(frame)
            resized_frame = gif.copy().resize((800, 600))  # Adjusted image dimensions
            gif_frames.append(ImageTk.PhotoImage(resized_frame))

        self.mascot_gif = gif_frames
        self.current_gif_frame = 0

        self.mascot_label = tk.Label(self, image=self.mascot_gif[self.current_gif_frame], bg="#2288b7")
        self.mascot_label.pack(fill=tk.BOTH, expand=tk.YES)

        self.update_gif_frame()
        self.after(3000, self.main_screen)

    def update_gif_frame(self):
        if not self.playing_gif:
            return
        if hasattr(self, 'mascot_gif') and self.mascot_label.winfo_exists():
            self.current_gif_frame += 1
            if self.current_gif_frame == len(self.mascot_gif):
                self.current_gif_frame = 0

        self.mascot_label.configure(image=self.mascot_gif[self.current_gif_frame])
        self.after(850, self.update_gif_frame)  # frame delay of 850ms

    def main_screen(self):
        self.mascot_label.destroy()
        self.playing_gif = False
        self.main_frame = tk.Frame(self, bg=self.background)
        self.main_frame.pack(fill="both", expand=True)

        welcome_label = tk.Label(self.main_frame, text="Welcome to:", bg=self.background, fg=self.font,
                                 font=("Arial", 15))
        welcome_label.place(relx=0.5, rely=0.1, anchor="center")
        name_label = tk.Label(self.main_frame, text="Nittany Guesser!", bg=self.background, fg="cyan",
                              font=("Arial", 36))
        name_label.place(relx=0.5, rely=0.2, anchor="center")

        self.welcome_image = Image.open("lions/feli.png")
        self.welcome_image = self.welcome_image.resize((250, 350))
        self.welcome_image = ImageTk.PhotoImage(self.welcome_image)

        canvas = tk.Canvas(self, width=250, height=350)
        canvas.place(relx=0.30, rely=0.6, anchor="center")

        canvas.create_image(125, 177, image=self.welcome_image, anchor=tk.CENTER)
        canvas.create_text(175, 35, text="⌄Hello!!!", font=("Arial", 16), fill="white")

        btn_width = 0.3
        btn_height = 0.1

        run_button = ctk.CTkButton(self.main_frame, text="Run", font=("Arial", 20), command=self.question_gui)
        run_button.place(relx=0.7, rely=0.4, relwidth=btn_width, relheight=btn_height, anchor="center")

        settings_button = ctk.CTkButton(self.main_frame, text="Change theme", font=("Arial", 20), command=self.theme)
        settings_button.place(relx=0.7, rely=0.55, relwidth=btn_width, relheight=btn_height, anchor="center")

        exit_button = ctk.CTkButton(self.main_frame, text="Exit", font=("Arial", 20), command=self.destroy)
        exit_button.place(relx=0.7, rely=0.7, relwidth=btn_width, relheight=btn_height, anchor="center")

    def theme(self):  # Para cambiar el tema
        if self.background == "black":
            self.background = "white"
            self.font = "black"
        else:
            self.background = "black"
            self.font = "white"
        self.main_frame.destroy()
        self.main_screen()

    def show_hhmm_image(self):
        self.welcome_image = Image.open("lions/feli.png")
        self.welcome_image = self.welcome_image.resize((250, 350))
        self.welcome_image = ImageTk.PhotoImage(self.welcome_image)

    def question_gui(self):
        self.main_frame.destroy()
        self.configure(bg=self.background)

        back_button = ctk.CTkButton(self, text="←", font=("Arial", 24), command=self.back_to_main)
        back_button.place(relx=0.55, rely=0.04, anchor="center", relwidth=0.05)

        self.character_frame = tk.Frame(self,
                                        bg=self.background)  # aqui va un ciclo de imagenes random de leones de montaña
        self.character_frame.place(relx=0.25, rely=0.5, anchor="center", relwidth=0.5, relheight=1)
        self.display_random_lion_image()

        self.question_var = tk.StringVar()  # bloque de preguntas de arriba
        self.question_label = tk.Label(self, textvariable=self.question_var, font=("Arial", 16), wraplength=300,
                                       justify='left', bg=self.background, fg=self.font, relief=tk.FLAT, bd=5,
                                       highlightbackground=self.font,
                                       highlightcolor="red",
                                       highlightthickness=5)
        random_question = random.choice(initial_questions)
        self.question_var.set(random_question)
        self.question_label.place(relx=0.75, rely=0.23, anchor="center", relwidth=0.45,
                                  relheight=0.3)  # Adjusted the positioning

        btn_width = 0.45
        btn_height = 0.08
        y_positions = [0.43, 0.53, 0.63, 0.73, 0.83, 0.93]

        buttons_text = ["Yes", "No", "Don't know", "Probably yes", "Probably no", "That's not a question"]
        commands = [lambda response=response: self.get_response_from_openai(response) for response in buttons_text]

        for i, (text, cmd) in enumerate(zip(buttons_text, commands)):
            btn = ctk.CTkButton(self, text=text, command=cmd)
            btn.place(relx=0.75, rely=y_positions[i], anchor="center", relwidth=btn_width, relheight=btn_height)

    def display_random_lion_image(self):
        selected_image_path = random.choice(self.lion_images)
        self.current_lion_image = tk.PhotoImage(file="lions/" + selected_image_path)
        self.lion_label = tk.Label(self.character_frame, image=self.current_lion_image, bg=self.background)
        self.lion_label.pack(fill=tk.BOTH, expand=True)
        self.lion_label.configure(image=self.current_lion_image)

    def back_to_main(self):
        self.character_frame.destroy()
        try:
            self.question_label.destroy()
        except:
            pass
        self.conversation_history = []  # Resetting the conversation history
        self.questions_asked = 0  # Resetting the number of questions asked
        self.main_screen()
        self.remove_generated_image()

    def get_image_url(self, prompt):
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024",
            response_format="url"
        )
        return response.data[0].url

    def download_and_save_image(self, url):
        response = requests.get(url)
        file_name = "generated_image.jpg"
        with open(file_name, "wb") as file:
            file.write(response.content)
        return file_name

    def show_generated_image(self, image_path):
        self.character_frame.destroy()
        self.question_label.destroy()

        original_image = Image.open(image_path)
        resized_image = original_image.resize((800, 600))
        self.generated_image = ImageTk.PhotoImage(resized_image)

        self.image_label = tk.Label(self, image=self.generated_image)
        self.image_label.pack(fill=tk.BOTH, expand=tk.YES)

    def remove_generated_image(self):
        # Check if the image_label exists, then destroy it
        if hasattr(self, 'image_label'):
            self.image_label.destroy()
        # Optionally, set the generated_image to None
        self.generated_image = None

    def get_response_from_openai(self, button_text):
        # change the lion image
        self.lion_label.destroy()
        self.display_random_lion_image()

        self.questions_asked += 1
        # Update the conversation history
        current_question = self.question_var.get()
        self.conversation_history.append({"question": current_question, "answer": button_text})

        # Utilize the conversation history in the prompt for better context
        conversation_text = " ".join(
            [f"{item['question']} Answer: {item['answer']}." for item in self.conversation_history])

        prompt_text = (
            f"Given the conversation context: {conversation_text}, and considering your aim is to guess the user's location, "
            "suggest a coherent and relevant yes/no question to further narrow down the location, or provide a final guess. "
            "The question must be framed such that the answer can ONLY be YES or NO. "
            "Ensure you don't ask a question that's already been asked.")

        # Truncate the prompt if its length exceeds 950 (to allow some space for API-specific characters)
        if len(prompt_text) > 950:
            prompt_text = prompt_text[:950] + "..."

        openai_response_text = \
            openai.Completion.create(engine="text-davinci-002", prompt=prompt_text, max_tokens=150).choices[
                0].text.strip()

        # Ensure at least 5 questions are asked before taking a guess
        if self.questions_asked < 5:
            if openai_response_text.endswith("?"):
                self.question_var.set(openai_response_text)
            else:
                # If the response isn't a question, ask the API for another one
                self.question_gui()  # Or any other mechanism to request another question from the API
        elif openai_response_text.endswith("?") and self.questions_asked < 15:
            self.question_var.set(openai_response_text)
        else:
            # Generate the image based on the conversation
            image_prompt = (
                f"Take into consideration {conversation_text}. Make sense from it and create a prompt based on where this user might be thinking that it is")
            if len(image_prompt) > 950:
                image_prompt = image_prompt[:950] + "..."
            image_url = self.get_image_url(image_prompt)
            image_path = self.download_and_save_image(image_url)
            self.show_generated_image(image_path)
            # Add the back button here
            back_button = ctk.CTkButton(self, text="←", font=("Arial", 24), command=self.back_to_main)
            back_button.place(relx=0, rely=0, anchor="nw", relwidth=0.05)


if __name__ == "__main__":
    app = App()
    app.mainloop()
