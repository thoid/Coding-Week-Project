import tkinter as tk


def end_battle_of_life(game_end, number_red, number_blue, t):
    """Announces the end of the game, the winner and the circomstances of their victory

    Args:
        game_end (int): number of the winner
        number_red (int): number of red soldiers still alive at the end of the game
        number_blue (int): number of blue soldiers still alive at the end of the game
        t (int): number of iterations that have already been run
    """
    root = tk.Tk()
    img_1 = tk.PhotoImage(master=root, file="src/images/end_image.gif")
    img_2 = tk.PhotoImage(master=root, file="src/images/tie_image.gif")
    if game_end > 0:
        panel = tk.Label(root, image=img_1)
        panel.pack(side="top", fill="both", expand="yes")
        label_field = tk.Label(
            root, text="Congratulations player %s , you win!" % game_end, font=("Courier", 17))
    else:
        panel = tk.Label(root, image=img_2)
        panel.pack(side="top", fill="both", expand="yes")
        label_field = tk.Label(
            root, text="No win, no loss... Let's play again!", font=("Courier", 17))
    f1 = tk.Frame(root, bd=1, relief='solid')
    tk.Label(f1, text="Number of blue soldiers still alive :%s" %
             number_blue, font=("Courier", 17)).grid(row=0, column=0)
    tk.Label(f1, text="Number of red soldiers still alive :%s" %
             number_red, font=("Courier", 17)).grid(row=1, column=0)
    tk.Label(f1, text="Remaining time :%s" %
             (101-t), font=("Courier", 17)).grid(row=2, column=0)
    f1.pack(side="bottom", fill="both", expand="yes")
    label_field.pack(side="top", fill="both", expand="yes")
    root.mainloop()
