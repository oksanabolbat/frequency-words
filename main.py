import tkinter as tk
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

try:
    words_df = pd.read_csv("data/sk_words_to_learn.csv")
except FileNotFoundError:
    words_df = pd.read_csv("data/sk_words.csv")

to_learn = words_df.to_dict(orient="records")
current_card = {}
timer_ref = ""
timer_next_card_ref = ""
lang = "Slovak"
to_lang = "Ukrainian"


def flip_card():
    global timer_next_card_ref
    bg_canvas.itemconfig(text_word, text=current_card[to_lang], fill="#fff")
    bg_canvas.itemconfig(text_lang, text=to_lang, fill="#fff")
    bg_canvas.itemconfig(canvas_img, image=canvas_img_back)
    timer_next_card_ref = window.after(3000, generate_next_card)


def generate_next_card():
    global current_card, timer_ref
    current_card = random.choice(to_learn)
    bg_canvas.itemconfig(canvas_img, image=canvas_img_front)
    bg_canvas.itemconfig(text_word, text=current_card[lang], fill="#000")
    bg_canvas.itemconfig(text_lang, text=lang, fill="#000")
    timer_ref = window.after(3000, flip_card)


def clear_timers():
    if timer_ref != "" and timer_next_card_ref != "":
        window.after_cancel(timer_ref)
        window.after_cancel(timer_next_card_ref)
    generate_next_card()

def right_btn_handler():
    to_learn.remove(current_card)
    df = pd.DataFrame(to_learn)
    df.to_csv('data/sk_words_to_learn.csv', index=False)
    clear_timers()


def wrong_btn_handler():
    clear_timers()


bg_canvas = tk.Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
canvas_img_back = tk.PhotoImage(file="images/card_back.png")
canvas_img_front = tk.PhotoImage(file="images/card_front.png")
canvas_img = bg_canvas.create_image(400, 263, image=canvas_img_front)
text_lang = bg_canvas.create_text(400, 150, text="Slovak", font=TITLE_FONT)
text_word = bg_canvas.create_text(400, 263, text="", font=WORD_FONT)

bg_canvas.grid(row=0, column=0, columnspan=2)

btn_img_r = tk.PhotoImage(file='images/right.png')
btn_img_l = tk.PhotoImage(file='images/wrong.png')
btn_right = tk.Button(image=btn_img_r, command=right_btn_handler, highlightthickness=0)
btn_wrong = tk.Button(image=btn_img_l, command=wrong_btn_handler, highlightthickness=0)
btn_right.grid(row=1, column=0)
btn_wrong.grid(row=1, column=1)

generate_next_card()

window.mainloop()
