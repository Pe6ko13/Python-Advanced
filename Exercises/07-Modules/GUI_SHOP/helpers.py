from GUI_SHOP.Canvas import tk

def clean_screen():
    for el in tk.grid_slaves():
        el.destroy()