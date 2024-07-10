from tkinter import Tk, Canvas, Entry, Button, PhotoImage
from cache import FormData, Directory


def submit_form(entries, event = None):
    form_data = FormData()
    for key, entry in entries.items():
        form_data.update_data(key, entry.get())
        print(f"{key}: {entry.get()}")


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
    fill = "#00D3C1",
    outline = ""
)
canvas.create_rectangle(
    0.0,
    0.0,
    70.0,
    550.0,
    fill = "#002EEA",
    outline = ""
)

entries = {}

canvas.create_text(
    117.0,
    92.5,
    anchor = "nw",
    text = "Standard",
    fill = "#000000",
    font = ("UbuntuMono Regular", 20 * -1)
)
entry_image_1 = PhotoImage(file = Directory.relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(497.0, 102.5, image = entry_image_1)
entries["standard"] = Entry(
    font = ("UbuntuMono Regular", 20 * -1),
    bd = 0,
    bg = "#FFFFFF",
    fg = "#000716",
    highlightthickness = 0
)
entries["standard"].place(x = 382.0, y = 85.0, width = 230.0, height = 33.0)


canvas.create_text(
    122.0,
    154.5,
    anchor = "nw",
    text = "Chapters",
    fill = "#000000",
    font = ("UbuntuMono Regular", 20 * -1)
)

entry_image_2 = PhotoImage(file = Directory.relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(349.5, 164.5, image = entry_image_2)
entries["chapters_1"] = Entry(
    font = ("UbuntuMono Regular", 20 * -1),
    bd = 0,
    bg = "#FFFFFF",
    fg = "#000716",
    highlightthickness = 0
)
entries["chapters_1"].place(x = 297.0, y = 147.0, width = 105.0, height = 33.0)

entry_image_3 = PhotoImage(file = Directory.relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(559.5, 164.5, image = entry_image_3)
entries["chapters_2"] = Entry(
    font = ("UbuntuMono Regular", 20 * -1),
    bd = 0,
    bg = "#FFFFFF",
    fg = "#000716",
    highlightthickness = 0
)
entries["chapters_2"].place(x = 507.0, y = 147.0, width = 105.0, height = 33.0)

entry_image_4 = PhotoImage(file = Directory.relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(354.5, 216.5, image = entry_image_4)
entries["chapter_details"] = Entry(
    font = ("UbuntuMono Regular", 20 * -1),
    bd = 0,
    bg = "#FFFFFF",
    fg = "#000716",
    highlightthickness = 0
)
entries["chapter_details"].place(x = 97.0, y = 199.0, width = 515.0, height = 33.0)

canvas.create_text(
    118.0,
    264.5,
    anchor = "nw",
    text = "Years",
    fill = "#000000",
    font = ("UbuntuMono Regular", 20 * -1)
)

entry_image_5 = PhotoImage(file = Directory.relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(354.5, 274.5, image = entry_image_5)
entries["years_1"] = Entry(
    font = ("UbuntuMono Regular", 20 * -1),
    bd = 0,
    bg = "#FFFFFF",
    fg = "#000716",
    highlightthickness = 0
)
entries["years_1"].place(x = 302.0, y = 257.0, width = 105.0, height = 33.0)

entry_image_6 = PhotoImage(file = Directory.relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(559.5, 274.5, image = entry_image_6)
entries["years_2"] = Entry(
    font = ("UbuntuMono Regular", 20 * -1),
    bd = 0,
    bg = "#FFFFFF",
    fg = "#000716",
    highlightthickness = 0
)
entries["years_2"].place(x = 507.0, y = 257.0, width = 105.0, height = 33.0)

entry_image_7 = PhotoImage(file = Directory.relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(354.5, 324.5, image = entry_image_7)
entries["year_details"] = Entry(
    font = ("UbuntuMono Regular", 20 * -1),
    bd = 0,
    bg = "#FFFFFF",
    fg = "#000716",
    highlightthickness = 0
)
entries["year_details"].place(x = 97.0, y = 307.0, width = 515.0, height = 33.0)

canvas.create_text(
    112.0,
    371.5,
    anchor = "nw",
    text = "Output Path",
    fill = "#000000",
    font = ("UbuntuMono Regular", 20 * -1)
)

entry_image_8 = PhotoImage(file = Directory.relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(472.0, 381.5, image = entry_image_8)
entries["output_path"] = Entry(
    font = ("UbuntuMono Regular", 20 * -1),
    bd = 0,
    bg = "#FFFFFF",
    fg = "#000716",
    highlightthickness = 0
)
entries["output_path"].place(x = 332.0, y = 364.0, width = 280.0, height = 33.0)

canvas.create_text(
    112.0,
    430.5,
    anchor = "nw",
    text = "Prefix File Name",
    fill = "#000000",
    font = ("UbuntuMono Regular", 20 * -1)
)

entry_image_9 = PhotoImage(file = Directory.relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(497.0, 440.5, image = entry_image_9)
entries["prefix_file_name"] = Entry(
    font = ("UbuntuMono Regular", 20 * -1),
    bd = 0,
    bg = "#FFFFFF",
    fg = "#000716",
    highlightthickness = 0
)
entries["prefix_file_name"].place(x = 382.0, y = 423.0, width = 230.0, height = 33.0)

button_image_1 = PhotoImage(file = Directory.relative_to_assets("button_1.png"))
button_1 = Button(
    image = button_image_1,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: print("button_1 clicked"),
    relief = "flat"
)
button_1.place(x = 10.0, y = 9.0, width = 50.0, height = 50.0)

button_image_2 = PhotoImage(file = Directory.relative_to_assets("button_2.png"))
button_2 = Button(
    image = button_image_2,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: print("button_2 clicked"),
    relief = "flat"
)
button_2.place(x = 525.0, y = 19.0, width = 25.0, height = 25.0)

button_image_3 = PhotoImage(file = Directory.relative_to_assets("button_3.png"))
button_3 = Button(
    image = button_image_3,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: print("button_3 clicked"),
    relief = "flat"
)
button_3.place(x = 570.0, y = 19.0, width = 25.0, height = 25.0)

button_image_4 = PhotoImage(file = Directory.relative_to_assets("button_4.png"))
button_4 = Button(
    image = button_image_4,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: print("button_4 clicked"),
    relief = "flat"
)
button_4.place(x = 615.0, y = 19.0, width = 25.0, height = 25.0)

button_image_5 = PhotoImage(file = Directory.relative_to_assets("button_5.png"))
button_5 = Button(
    image = button_image_5,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: submit_form(entries),
    relief = "flat"
)
button_5.place(x = 305.0, y = 486.0, width = 100.0, height = 40.0)

window.bind('<Return>', lambda event: submit_form(entries, event))
window.resizable(False, False)
window.mainloop()
