from pathlib import Path
from tkinter import *
from PIL import *
import youtube_dl
from tkinter import messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


root = Tk()
root.title('Youtube To Mp3 / Euwer')
root.geometry("800x600")
root.configure(bg = "#000000")
root.iconbitmap(bitmap=relative_to_assets('pytomp3.ico'))

canvas = Canvas(
    root,
    bg = "#000000",
    height = 600,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    339.9999999999999,
    114.0,
    459.9999999999999,
    157.0,
    fill="#000000",
    outline="")

canvas.create_text(
    348.9999999999999,
    124.0,
    anchor="nw",
    text="Video Url",
    fill="#FFFFFF",
    font=("Roboto Bold", 24 * -1)
)

canvas.create_rectangle(
    369.9999999999999,
    162.0,
    429.9999999999999,
    167.0,
    fill="#FCFCFC",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    399.4999999999999,
    209.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F1F5FF",
    highlightthickness=0
)   
entry_1.place(
    x=238.9999999999999,
    y=179.0,
    width=321.0,
    height=59.0
)

def downloadmp3():
    videourl = entry_1.get()

    videoinfo = youtube_dl.YoutubeDL().extract_info(
        url = videourl,download=False)

    nameofvideo = f"{videoinfo['title']}.mp3"
    
    settings={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':nameofvideo,
        }
    with youtube_dl.YoutubeDL(settings) as ydl:
        ydl.download([videoinfo['webpage_url']])

    complete =str("successfully")
    messagebox.showinfo("Download Info", "Successfully completed")

        

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=downloadmp3,
    relief="flat"
)
button_1.place(
    x=309.9999999999999,
    y=245.0,
    width=180.0,
    height=55.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    178.0000000000001,
    536.0,
    image=image_image_1
)

canvas.create_text(
    320.0,
    500.0,
    anchor="nw",
    text="to MP3",
    fill="#FFFFFF",
    font=("AlegreyaSans Bold", 64 * -1)
)

canvas.create_text(
    234.9999999999999,
    335.0,
    anchor="nw",
    text="will be downloaded directly to folder code is running on",
    fill="#FFFFFF",
    font=("Aleo Bold", 13 * -1)
)
root.resizable(False, False)
root.mainloop()
