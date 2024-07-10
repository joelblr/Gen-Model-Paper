from tkinter import Tk, Canvas, Entry, Button, PhotoImage
from cache import FormData, Directory

def create_canvas(window, bg_color, height, width):
    canvas = Canvas(
        window,
        bg=bg_color,
        height=height,
        width=width,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)
    return canvas


def create_entry(canvas, entry_image, img_x, img_y, x, y, width, height) :
    entry_image = PhotoImage(file=Directory.relative_to_assets(entry_image))
    # canvas.create_image(x + width/2, y + height/2, image=entry_image)
    canvas.create_image(img_x, img_y, image = entry_image)
    entry = Entry(
        font=("UbuntuMono Regular", 20 * -1),
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry.place(x=x, y=y, width=width, height=height)
    return entry


def create_text(canvas, x, y, text, fill, font) :
    canvas.create_text(
        x,
        y,
        anchor="nw",
        text=text,
        fill=fill,
        font=font
    )


def create_button(image, x, y, width, height, command):
    button_image = PhotoImage(file=Directory.relative_to_assets(image))
    button = Button(
        image=button_image,
        borderwidth=0,
        highlightthickness=0,
        command=command,
        relief="flat"
    )
    button.place(x=x, y=y, width=width, height=height)
    return button


def submit_form(entries, event=None):
    form_data = FormData()
    for key, entry in entries.items():
        form_data.update_data(key, entry.get())
        print(f"{key}: {entry.get()}")

window = Tk()
window.geometry("660x550")
window.configure(bg="#FFFFFF")

canvas = create_canvas(window, "#FFFFFF", 550, 660)
canvas.create_rectangle(70.0, 0.0, 660.0, 68.0, fill="#00D3C1", outline="")
canvas.create_rectangle(0.0, 0.0, 70.0, 550.0, fill="#002EEA", outline="")

entries = {}

create_text(canvas, 117.0, 92.5, "Standard", "#000000", ("UbuntuMono Regular", 20 * -1))
entries["standard"] = create_entry(canvas, "entry_1.png", *(497.0, 102.5), 382.0, 85.0, 230.0, 33.0)

create_text(canvas, 122.0, 154.5, "Chapters", "#000000", ("UbuntuMono Regular", 20 * -1))
entries["chapters_1"] = create_entry(canvas, "entry_2.png", *(349.5, 164.5), 297.0, 147.0, 105.0, 33.0)
entries["chapters_2"] = create_entry(canvas, "entry_3.png", *(559.5, 164.5), 507.0, 147.0, 105.0, 33.0)

entries["chapter_details"] = create_entry(canvas, "entry_4.png", *(354.5, 216.5), 97.0, 199.0, 515.0, 33.0)

create_text(canvas, 118.0, 264.5, "Years", "#000000", ("UbuntuMono Regular", 20 * -1))
entries["years_1"] = create_entry(canvas, "entry_5.png", *(354.5, 274.5), 302.0, 257.0, 105.0, 33.0)
entries["years_2"] = create_entry(canvas, "entry_6.png", *(559.5, 274.5), 507.0, 257.0, 105.0, 33.0)

entries["year_details"] = create_entry(canvas, "entry_7.png", *(354.5, 324.5), 97.0, 307.0, 515.0, 33.0)

create_text(canvas, 112.0, 371.5, "Output Path", "#000000", ("UbuntuMono Regular", 20 * -1))
entries["output_path"] = create_entry(canvas, "entry_8.png", *(472.0, 381.5), 332.0, 364.0, 280.0, 33.0)

create_text(canvas, 112.0, 430.5, "Prefix File Name", "#000000", ("UbuntuMono Regular", 20 * -1))
entries["prefix_file_name"] = create_entry(canvas, "entry_9.png", *(497.0, 440.5), 382.0, 423.0, 230.0, 33.0)

create_button("button_1.png", 10.0, 9.0, 50.0, 50.0, lambda: print("button_1 clicked"))
create_button("button_2.png", 525.0, 19.0, 25.0, 25.0, lambda: print("button_2 clicked"))
create_button("button_3.png", 570.0, 19.0, 25.0, 25.0, lambda: print("button_3 clicked"))
create_button("button_4.png", 615.0, 19.0, 25.0, 25.0, lambda: print("button_4 clicked"))
create_button("button_5.png", 305.0, 486.0, 100.0, 40.0, lambda: submit_form(entries))

window.bind('<Return>', lambda event: submit_form(entries, event))
window.resizable(False, False)
window.mainloop()
