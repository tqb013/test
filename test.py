import tkinter as tk
from tkinter import messagebox


# Functie om scores bij te werken
def update_score(player, score):
    global player1_score, player2_score, current_player, player1_sets, player2_sets, player1_legs, player2_legs, current_leg

    try:
        score = int(score)
        if score < 0 or score > 180:
            raise ValueError("De score moet tussen 0 en 180 liggen.")

        if current_player == "Player 1":
            if player1_score - score < 0:
                messagebox.showinfo("Overschrijding",
                                    "Ongeldige score. Overscore!")
                return
            player1_score -= score
            label_score_player1.config(text=f"{player1_name}\n{player1_score}")
            current_player = "Player 2"
        elif current_player == "Player 2":
            if player2_score - score < 0:
                messagebox.showinfo("Overschrijding",
                                    "Ongeldige score. Overscore!")
                return
            player2_score -= score
            label_score_player2.config(text=f"{player2_name}\n{player2_score}")
            current_player = "Player 1"

        # Check op winst in een leg
        if player1_score == 0:
            player1_legs += 1
            current_leg += 1
            label_legs_player1.config(
                text=f"{player1_name} Legs: {player1_legs}")
            messagebox.showinfo("Leg Winst", f"{player1_name} wint de leg!")
            reset_scores()
        elif player2_score == 0:
            player2_legs += 1
            current_leg += 1
            label_legs_player2.config(
                text=f"{player2_name} Legs: {player2_legs}")
            messagebox.showinfo("Leg Winst", f"{player2_name} wint de leg!")
            reset_scores()

        # Check op winst in een set
        if player1_legs == 3:
            player1_sets += 1
            label_sets_player1.config(
                text=f"{player1_name} Sets: {player1_sets}")
            player1_legs = 0
            player2_legs = 0
            messagebox.showinfo("Set Winst", f"{player1_name} wint de set!")
            if player1_sets == sets_to_win:
                messagebox.showinfo("Wedstrijd Winst",
                                    f"{player1_name} wint de wedstrijd!")
                reset_game()
        elif player2_legs == 3:
            player2_sets += 1
            label_sets_player2.config(
                text=f"{player2_name} Sets: {player2_sets}")
            player1_legs = 0
            player2_legs = 0
            messagebox.showinfo("Set Winst", f"{player2_name} wint de set!")
            if player2_sets == sets_to_win:
                messagebox.showinfo("Wedstrijd Winst",
                                    f"{player2_name} wint de wedstrijd!")
                reset_game()
        else:
            label_current_player.config(text=f"Aan de beurt: {current_player}")
    except ValueError:
        messagebox.showerror("Fout", "Voer een geldige score in.")


# Functie om de score in te voeren via een knop
def add_to_score(digit):
    current_score = entry_score.get() + str(digit)
    entry_score.delete(0, tk.END)
    entry_score.insert(0, current_score)


# Functie om de scores te resetten na een gewonnen leg
def reset_scores():
    global player1_score, player2_score
    player1_score = game_mode
    player2_score = game_mode
    label_score_player1.config(text=f"{player1_name}\n{player1_score}")
    label_score_player2.config(text=f"{player2_name}\n{player2_score}")
    entry_score.delete(0, tk.END)


# Functie om het spel te resetten
def reset_game():
    global player1_score, player2_score, current_player, player1_sets, player2_sets, player1_legs, player2_legs, current_leg

    player1_sets = 0
    player2_sets = 0
    player1_legs = 0
    player2_legs = 0
    current_leg = 1
    player1_score = game_mode
    player2_score = game_mode
    current_player = "Player 1"

    label_score_player1.config(text=f"{player1_name}\n{player1_score}")
    label_score_player2.config(text=f"{player2_name}\n{player2_score}")

    label_sets_player1.config(text=f"{player1_name} Sets: {player1_sets}")
    label_sets_player2.config(text=f"{player2_name} Sets: {player2_sets}")

    label_legs_player1.config(text=f"{player1_name} Legs: {player1_legs}")
    label_legs_player2.config(text=f"{player2_name} Legs: {player2_legs}")

    label_current_player.config(text=f"Aan de beurt: {current_player}")

    start_screen.pack_forget()
    game_screen.pack(fill="both", expand=True)


# Functie om het spel te starten
def start_game():
    global player1_name, player2_name, game_mode, player1_score, player2_score, current_player, sets_to_win, player1_sets, player2_sets, player1_legs, player2_legs, current_leg

    player1_name = entry_name_player1.get()
    player2_name = entry_name_player2.get()
    game_mode = int(game_choice.get())
    sets_to_win = int(entry_sets.get())
    player1_score = game_mode
    player2_score = game_mode
    player1_sets = 0
    player2_sets = 0
    player1_legs = 0
    player2_legs = 0
    current_player = "Player 1"
    current_leg = 1

    if not player1_name or not player2_name or not entry_sets.get().isdigit(
    ) or sets_to_win < 1:
        messagebox.showerror(
            "Fout",
            "Voer beide spelersnamen in en kies een geldig aantal sets.")
        return

    start_screen.pack_forget()
    game_screen.pack(fill="both", expand=True)

    label_score_player1.config(text=f"{player1_name}\n{player1_score}")
    label_score_player2.config(text=f"{player2_name}\n{player2_score}")
    label_sets_player1.config(text=f"{player1_name} Sets: {player1_sets}")
    label_sets_player2.config(text=f"{player2_name} Sets: {player2_sets}")
    label_legs_player1.config(text=f"{player1_name} Legs: {player1_legs}")
    label_legs_player2.config(text=f"{player2_name} Legs: {player2_legs}")
    label_current_player.config(text=f"Aan de beurt: {current_player}")


# GUI maken
root = tk.Tk()
root.title("Darts Scoreboard")
root.geometry("800x700")
root.configure(bg="#F1F1F1")

# Startscherm
start_screen = tk.Frame(root, bg="#F1F1F1")
start_screen.pack(fill="both", expand=True)

label_start = tk.Label(start_screen,
                       text="Welkom bij Darts Scoreboard",
                       font=("Helvetica", 24, 'bold'),
                       bg="#F1F1F1",
                       fg="#4CAF50")
label_start.pack(pady=30)

label_name_player1 = tk.Label(start_screen,
                              text="Naam Speler 1:",
                              font=("Helvetica", 14),
                              bg="#F1F1F1",
                              fg="#333333")
label_name_player1.pack(pady=10)

entry_name_player1 = tk.Entry(start_screen,
                              font=("Helvetica", 16),
                              width=20,
                              borderwidth=2,
                              relief="solid")
entry_name_player1.pack(pady=10)

label_name_player2 = tk.Label(start_screen,
                              text="Naam Speler 2:",
                              font=("Helvetica", 14),
                              bg="#F1F1F1",
                              fg="#333333")
label_name_player2.pack(pady=10)

entry_name_player2 = tk.Entry(start_screen,
                              font=("Helvetica", 16),
                              width=20,
                              borderwidth=2,
                              relief="solid")
entry_name_player2.pack(pady=10)

label_game_choice = tk.Label(start_screen,
                             text="Kies spelmodus:",
                             font=("Helvetica", 14),
                             bg="#F1F1F1",
                             fg="#333333")
label_game_choice.pack(pady=10)

game_choice = tk.StringVar(value="501")
button_501 = tk.Radiobutton(start_screen,
                            text="501",
                            variable=game_choice,
                            value="501",
                            font=("Helvetica", 12),
                            bg="#F1F1F1",
                            fg="#333333")
button_501.pack()

button_301 = tk.Radiobutton(start_screen,
                            text="301",
                            variable=game_choice,
                            value="301",
                            font=("Helvetica", 12),
                            bg="#F1F1F1",
                            fg="#333333")
button_301.pack()

label_sets = tk.Label(start_screen,
                      text="Aantal sets:",
                      font=("Helvetica", 14),
                      bg="#F1F1F1",
                      fg="#333333")
label_sets.pack(pady=10)

entry_sets = tk.Entry(start_screen,
                      font=("Helvetica", 16),
                      width=5,
                      borderwidth=2,
                      relief="solid")
entry_sets.pack(pady=10)

button_start_game = tk.Button(start_screen,
                              text="Start Spel",
                              command=start_game,
                              font=("Helvetica", 16),
                              bg="#4CAF50",
                              fg="white",
                              relief="flat")
button_start_game.pack(pady=20)

# Speelscherm
game_screen = tk.Frame(root, bg="#F1F1F1")

# Bovenste deel: scores van beide spelers
frame_scores = tk.Frame(game_screen, bg="#F1F1F1")
frame_scores.pack(fill="x", pady=10)

label_score_player1 = tk.Label(frame_scores,
                               text="Speler 1\n501",
                               font=("Helvetica", 20),
                               bg="#9E9E9E",
                               fg="white",
                               width=15,
                               height=5)
label_score_player1.pack(side="left", padx=20)

label_score_player2 = tk.Label(frame_scores,
                               text="Speler 2\n501",
                               font=("Helvetica", 20),
                               bg="#9E9E9E",
                               fg="white",
                               width=15,
                               height=5)
label_score_player2.pack(side="right", padx=20)

# Het aantal sets en legs
frame_sets_legs = tk.Frame(game_screen, bg="#F1F1F1")
frame_sets_legs.pack(fill="x", pady=10)

label_sets_player1 = tk.Label(frame_sets_legs,
                              text="Speler 1 Sets: 0",
                              font=("Helvetica", 14),
                              bg="#F1F1F1",
                              fg="#333333",
                              width=20)
label_sets_player1.pack(side="left", padx=20)

label_sets_player2 = tk.Label(frame_sets_legs,
                              text="Speler 2 Sets: 0",
                              font=("Helvetica", 14),
                              bg="#F1F1F1",
                              fg="#333333",
                              width=20)
label_sets_player2.pack(side="right", padx=20)

frame_legs = tk.Frame(game_screen, bg="#F1F1F1")
frame_legs.pack(fill="x", pady=10)

label_legs_player1 = tk.Label(frame_legs,
                              text="Speler 1 Legs: 0",
                              font=("Helvetica", 14),
                              bg="#F1F1F1",
                              fg="#333333",
                              width=20)
label_legs_player1.pack(side="left", padx=20)

label_legs_player2 = tk.Label(frame_legs,
                              text="Speler 2 Legs: 0",
                              font=("Helvetica", 14),
                              bg="#F1F1F1",
                              fg="#333333",
                              width=20)
label_legs_player2.pack(side="right", padx=20)

label_current_player = tk.Label(game_screen,
                                text="Aan de beurt: Speler 1",
                                font=("Helvetica", 16),
                                bg="#F1F1F1",
                                fg="#333333")
label_current_player.pack(pady=20)

# Score invoeren
frame_score_input = tk.Frame(game_screen, bg="#F1F1F1")
frame_score_input.pack(pady=20)

entry_score = tk.Entry(frame_score_input,
                       font=("Helvetica", 16),
                       width=10,
                       borderwidth=2,
                       relief="solid")
entry_score.pack(side="left", padx=20)

# Knoppen voor score in telefoonachtige lay-out
frame_number_pad = tk.Frame(game_screen, bg="#F1F1F1")
frame_number_pad.pack(pady=10)

button_1 = tk.Button(frame_number_pad,
                     text="1",
                     command=lambda: add_to_score(1),
                     font=("Helvetica", 14),
                     width=5,
                     height=2)
button_1.grid(row=0, column=0, padx=5, pady=5)

button_2 = tk.Button(frame_number_pad,
                     text="2",
                     command=lambda: add_to_score(2),
                     font=("Helvetica", 14),
                     width=5,
                     height=2)
button_2.grid(row=0, column=1, padx=5, pady=5)

button_3 = tk.Button(frame_number_pad,
                     text="3",
                     command=lambda: add_to_score(3),
                     font=("Helvetica", 14),
                     width=5,
                     height=2)
button_3.grid(row=0, column=2, padx=5, pady=5)

button_4 = tk.Button(frame_number_pad,
                     text="4",
                     command=lambda: add_to_score(4),
                     font=("Helvetica", 14),
                     width=5,
                     height=2)
button_4.grid(row=1, column=0, padx=5, pady=5)

button_5 = tk.Button(frame_number_pad,
                     text="5",
                     command=lambda: add_to_score(5),
                     font=("Helvetica", 14),
                     width=5,
                     height=2)
button_5.grid(row=1, column=1, padx=5, pady=5)

button_6 = tk.Button(frame_number_pad,
                     text="6",
                     command=lambda: add_to_score(6),
                     font=("Helvetica", 14),
                     width=5,
                     height=2)
button_6.grid(row=1, column=2, padx=5, pady=5)

button_7 = tk.Button(frame_number_pad,
                     text="7",
                     command=lambda: add_to_score(7),
                     font=("Helvetica", 14),
                     width=5,
                     height=2)
button_7.grid(row=2, column=0, padx=5, pady=5)

button_8 = tk.Button(frame_number_pad,
                     text="8",
                     command=lambda: add_to_score(8),
                     font=("Helvetica", 14),
                     width=5,
                     height=2)
button_8.grid(row=2, column=1, padx=5, pady=5)

button_9 = tk.Button(frame_number_pad,
                     text="9",
                     command=lambda: add_to_score(9),
                     font=("Helvetica", 14),
                     width=5,
                     height=2)
button_9.grid(row=2, column=2, padx=5, pady=5)

button_0 = tk.Button(frame_number_pad,
                     text="0",
                     command=lambda: add_to_score(0),
                     font=("Helvetica", 14),
                     width=5,
                     height=2)
button_0.grid(row=3, column=1, padx=5, pady=5)

button_add_score = tk.Button(
    game_screen,
    text="Voeg score toe",
    command=lambda: update_score(current_player, entry_score.get()),
    font=("Helvetica", 16),
    bg="#4CAF50",
    fg="white")
button_add_score.pack(pady=20)

root.mainloop()
