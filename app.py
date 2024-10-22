from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")
DATASET_PATH = OUTPUT_PATH / Path(r"data-set")
TEMPLATE_PATH = OUTPUT_PATH / Path(r"templates")


def get_absolute_path(root_path: str, path: str) -> Path:
    return root_path / Path(path)


window = Tk()

window.geometry("660x550")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 550,
    width = 660,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    70.0,
    0.0,
    660.0,
    68.0,
    fill="#00D3C1",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    70.0,
    550.0,
    fill="#002EEA",
    outline="")

canvas.create_text(
    117.0,
    92.5,
    anchor="nw",
    text="Standard",
    fill="#000000",
    font=("UbuntuMono Regular", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=get_absolute_path(ASSETS_PATH, "entry_1.png"))
entry_bg_1 = canvas.create_image(
    497.0,
    101.3,
    image=entry_image_1
)
entry_1 = Entry(
    font=("UbuntuMono Regular", 15 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=2
)
entry_1.place(
    x=382.0,
    y=85.0,
    width=230.0,
    height=33.0
)

canvas.create_text(
    122.0,
    154.5,
    anchor="nw",
    text="Chapters",
    fill="#000000",
    font=("UbuntuMono Regular", 20 * -1)
)

entry_image_2 = PhotoImage(
    file=get_absolute_path(ASSETS_PATH, "entry_2.png"))
entry_bg_2 = canvas.create_image(
    349.5,
    164.5,
    image=entry_image_2
)
entry_2 = Entry(
    font=("UbuntuMono Regular", 20 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=297.0,
    y=147.0,
    width=105.0,
    height=33.0
)

entry_image_3 = PhotoImage(
    file=get_absolute_path(ASSETS_PATH, "entry_3.png"))
entry_bg_3 = canvas.create_image(
    559.5,
    164.5,
    image=entry_image_3
)
entry_3 = Entry(
    font=("UbuntuMono Regular", 20 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=507.0,
    y=147.0,
    width=105.0,
    height=33.0
)

entry_image_4 = PhotoImage(
    file=get_absolute_path(ASSETS_PATH, "entry_4.png"))
entry_bg_4 = canvas.create_image(
    354.5,
    216.5,
    image=entry_image_4
)
entry_4 = Entry(
    font=("UbuntuMono Regular", 20 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=97.0,
    y=199.0,
    width=515.0,
    height=33.0
)

canvas.create_text(
    118.0,
    264.5,
    anchor="nw",
    text="Years",
    fill="#000000",
    font=("UbuntuMono Regular", 20 * -1)
)

entry_image_5 = PhotoImage(
    file=get_absolute_path(ASSETS_PATH, "entry_5.png"))
entry_bg_5 = canvas.create_image(
    354.5,
    274.5,
    image=entry_image_5
)
entry_5 = Entry(
    font=("UbuntuMono Regular", 20 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=302.0,
    y=257.0,
    width=105.0,
    height=33.0
)

entry_image_6 = PhotoImage(
    file=get_absolute_path(ASSETS_PATH, "entry_6.png"))
entry_bg_6 = canvas.create_image(
    559.5,
    274.5,
    image=entry_image_6
)
entry_6 = Entry(
    font=("UbuntuMono Regular", 20 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=507.0,
    y=257.0,
    width=105.0,
    height=33.0
)

entry_image_7 = PhotoImage(
    file=get_absolute_path(ASSETS_PATH, "entry_7.png"))
entry_bg_7 = canvas.create_image(
    354.5,
    324.5,
    image=entry_image_7
)
entry_7 = Entry(
    font=("UbuntuMono Regular", 20 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=97.0,
    y=307.0,
    width=515.0,
    height=33.0
)

canvas.create_text(
    112.0,
    371.5,
    anchor="nw",
    text="Output Path",
    fill="#000000",
    font=("UbuntuMono Regular", 20 * -1)
)

entry_image_8 = PhotoImage(
    file=get_absolute_path(ASSETS_PATH, "entry_8.png"))
entry_bg_8 = canvas.create_image(
    472.0,
    381.5,
    image=entry_image_8
)
entry_8 = Entry(
    font=("UbuntuMono Regular", 20 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=332.0,
    y=364.0,
    width=280.0,
    height=33.0
)

canvas.create_text(
    112.0,
    430.5,
    anchor="nw",
    text="Prefix File Name",
    fill="#000000",
    font=("UbuntuMono Regular", 20 * -1)
)

entry_image_9 = PhotoImage(
    file=get_absolute_path(ASSETS_PATH, "entry_9.png"))
entry_bg_9 = canvas.create_image(
    497.0,
    440.5,
    image=entry_image_9
)
entry_9 = Entry(
    font=("UbuntuMono Regular", 20 * -1),
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=382.0,
    y=423.0,
    width=230.0,
    height=33.0
)

button_image_1 = PhotoImage(
    file=get_absolute_path(ASSETS_PATH, "button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=10.0,
    y=9.0,
    width=50.0,
    height=50.0
)

button_image_2 = PhotoImage(
    file=get_absolute_path(ASSETS_PATH, "button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=525.0,
    y=19.0,
    width=25.0,
    height=25.0
)

button_image_3 = PhotoImage(
    file=get_absolute_path(ASSETS_PATH, "button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=570.0,
    y=19.0,
    width=25.0,
    height=25.0
)

button_image_4 = PhotoImage(
    file=get_absolute_path(ASSETS_PATH, "button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=615.0,
    y=19.0,
    width=25.0,
    height=25.0
)

button_image_5 = PhotoImage(
    file=get_absolute_path(ASSETS_PATH, "button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=305.0,
    y=486.0,
    width=100.0,
    height=40.0
)
window.resizable(False, False)
window.mainloop()