from tkinter import *
from tkinter import messagebox

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

    except ValueError:
        messagebox.showerror("Input Error!", "Please enter valid numbers in all fields.")

CALCULATOR_WINDOW = Tk()
CALCULATOR_WINDOW.title("Basketball Gamescore Calculator")

CALCULATOR_WINDOW.config(background='orange')

ICON = PhotoImage(file='C:\\Users\\azale\\Desktop\\python_projects\\ball_icon.png')
CALCULATOR_WINDOW.iconphoto(True, ICON)

header = Label(CALCULATOR_WINDOW, 
              text="Basketball Gamescore Calculator", 
              font=('Comic Sans MS', 40, 'bold'),
              foreground='black',
              background='white',
              relief=RAISED,
              border=10,
              padx=5)
header.pack()

stat_lines = [
    ("Points Scored", 'point'), ("Field Goals Made", 'field goal'), 
    ("Field Goal Attempts", 'field goal attempt'), ("Freethrows Made", 'freethrow'), 
    ("Freethrow Attempts", 'freethrow attempt'), ("Offensive Rebounds", 'offensive rebound'), 
    ("Defensive Rebounds", 'defensive rebound'), ("Steals", 'steal'), 
    ("Assists", 'assist'), ("Blocks", 'block'), 
    ("Personal Fouls", 'foul'), ("Turnovers", 'turnover')
]

entries = {}

calculate_button = Button(CALCULATOR_WINDOW, text="Calculate Gamescore")
calculate_button.config(font=('Arial', 25, 'bold'))
calculate_button.config(activebackground='blue')
calculate_button.pack()

CALCULATOR_WINDOW.mainloop()