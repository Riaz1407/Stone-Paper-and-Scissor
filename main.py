import tkinter as tk
import random

choices = ["stone", "paper", "scissor"]

def play(my_choice):
    computer = random.choice(choices)
    
    if my_choice == computer:
        result = "Its a tie"
    elif (computer == "stone" and my_choice == "scissor") or \
         (computer == "paper" and my_choice == "stone") or \
         (computer == "scissor" and my_choice == "paper"):
        result = "computer wins"
    else:
        result = "you win"
    
    result_label.config(
        text=f"you : {my_choice} | opponent : {computer}\nResult : {result}"
    )

root = tk.Tk()
root.title("Stone, Paper and Scissor")
root.geometry("350x250")

title = tk.Label(root, text="Stone Paper Scissor Game")
title.pack(pady=10)

# buttons
stone_btn = tk.Button(root, text="stone", command=lambda: play("stone"))
stone_btn.pack(pady=5)

paper_btn = tk.Button(root, text="paper", command=lambda: play("paper"))
paper_btn.pack(pady=5)

scissor_btn = tk.Button(root, text="scissor", command=lambda: play("scissor"))
scissor_btn.pack(pady=5)

# result
result_label = tk.Label(root, text="")
result_label.pack(pady=20)

root.mainloop()