from tkinter import *
from tkinter import messagebox

main_window = Tk()
main_window.title("Basketball Gamescore Calculator")

main_window.config(background='orange')

STAT_LINES = [
    ("Points Scored", 'point'), ("Field Goals Made", 'field goal'), 
    ("Field Goal Attempts", 'field goal attempt'), ("Freethrows Made", 'freethrow'), 
    ("Freethrow Attempts", 'freethrow attempt'), ("Offensive Rebounds", 'offensive rebound'), 
    ("Defensive Rebounds", 'defensive rebound'), ("Steals", 'steal'), 
    ("Assists", 'assist'), ("Blocks", 'block'), 
    ("Personal Fouls", 'foul'), ("Turnovers", 'turnover')
]

entries = {}

def calculate_game_score():
    try:
        player_data = {stat_name: float(widget.get()) for stat_name, widget in entries.items()}

        game_score = (
            player_data['point']
            + 0.4 * player_data['field goal']
            - 0.7 * player_data['field goal attempt']
            - 0.4 * (player_data['freethrow attempt'] - player_data['freethrow'])
            + 0.7 * player_data['offensive rebound']
            + 0.3 * player_data['defensive rebound']
            + player_data['steal']
            + 0.7 * player_data['assist']
            + 0.7 * player_data['block']
            - 0.4 * player_data['foul']
            - player_data['turnover']
        )

        messagebox.showinfo("Result", f"The Player's Game Score is: {game_score:.2f}")

    except ValueError:
        messagebox.showerror("Input Error!", "Please enter valid numbers in all fields.")

header = Label(main_window, 
              text="Basketball Gamescore Calculator", 
              font=('Comic Sans MS', 40, 'bold'),
              foreground='black',
              background='white',
              relief=RAISED,
              border=10,
              padx=5)
header.pack(pady=10)

body_frame = Frame(main_window, bg='orange')
body_frame.pack(fill=BOTH, expand=True, padx=20)

left_column = Frame(body_frame, bg='orange')
left_column.pack(side=LEFT, fill=Y, padx=10)

for label_text, key in STAT_LINES:
    row = Frame(left_column, bg='orange')
    row.pack(fill=X, pady=2)
    
    label = Label(row, text=label_text, width=20, anchor='w', background='orange', font=('Arial', 12, 'bold'))
    label.pack(side=LEFT)
    
    entry = Entry(row)
    entry.pack(side=LEFT, padx=5)
    entries[key] = entry

right_column = Frame(body_frame, background='white', relief=SUNKEN, border=2)
right_column.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)

info_text = (
    "ABOUT GAME SCORE\n\n"
    "Game Score was created by John Hollinger to give a rough measure "
    "of a player's productivity for a single game.\n\n"
    "A score of 10 is considered average, while a score of 40+ is "
    "considered an all-time great performance.\n\n"
    "Instructions:\n"
    "Enter the box score stats on the left and click 'Calculate' to "
    "see the final efficiency rating."
)

info_label = Label(right_column, text=info_text, font=('Arial', 11), 
                   wraplength=300, justify=LEFT, bg='white', padx=15, pady=15)
info_label.pack()

calculate_button = Button(main_window, text="Calculate Gamescore", command=calculate_game_score)
calculate_button.config(font=('Arial', 20, 'bold'), activebackground='blue')
calculate_button.pack(pady=20)

icon_image = PhotoImage(file='ball_icon.png')
main_window.iconphoto(True, icon_image)

main_window.mainloop()