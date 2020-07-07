from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox

ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

def resizeImage (image, new_width = 100):
	width, height = image.size
	ratio = height / width
	new_height = int(new_width * ratio / 2)
	return image.resize((new_width, new_height))

def pixel_to_ascii (image):
	grayscale = image.convert('L')
	pixels = grayscale.getdata()
	art = ''.join([ASCII_CHARS[p // 25] for p in pixels])
	return art

def main (path, wid = 200):
	while True:
		try:
			image = Image.open(path)
			break
		except:
			message()
			return False
	char_list = pixel_to_ascii(resizeImage(image, wid))
	art = '\n'.join(char_list[i:(i + wid)] for i in range(0, len(char_list), wid))
	asciiGui(art)
	# with open('Birthday ASCII.txt', 'w') as f:
	# f.write(art)
	return art

def asciiGui (text):
	root = tk.Tk()
	root.title('ASCII Art displayer')
	art = tk.Label(master = root, text = text)
	art.config(font = ('monospace', 1))
	art.place(relwidth = 1, relheight = 1)
	root.mainloop()

def message ():
	root = tk.Tk()
	root.attributes('-topmost', True)
	root.title('Path Error...')
	root.withdraw()
	tk.messagebox.showinfo('Path Error...', 'Please enter a valid path name!')

def menuGUI ():
	width = 180
	height = 60
	root = tk.Tk()
	root.title('ASCII art converter')
	canvas = tk.Canvas(master = root, bg = 'black', width = 300, height = 300)
	canvas.pack()

	logo = Image.open('logo.png')
	img = ImageTk.PhotoImage(logo.resize((width, height)))

	icon = tk.Label(master = canvas, image = img)
	icon.place(relx = 0.2, height = height, rely = 0.1, width = width)

	frame = tk.Frame(master = canvas, bg = 'cyan', bd = 5)
	frame.place(relx = 0.15, rely = 0.35, relheight = 0.15, relwidth = 0.7)
	entry = tk.Entry(master = frame)
	entry.pack(side = 'right', fill = 'y')
	label = tk.Label(master = frame, text = 'Path:', bg = 'cyan')
	label.pack(side = 'left', expand = True)
	frame2 = tk.Frame(master = canvas, bg = 'cyan', bd = 5)
	frame2.place(relx = 0.15, rely = 0.55, relheight = 0.15, relwidth = 0.7)
	entry2 = tk.Entry(master = frame2)
	entry2.pack(side = 'right', fill = 'y')
	label2 = tk.Label(master = frame2, text = 'Width:', bg = 'cyan')
	label2.pack(side = 'left', expand = True)

	button = tk.Button(master = canvas, text = 'Confirm', bg = 'green',
					   command = lambda: main(entry.get(), int(entry2.get())))
	button.place(relx = 0.175, rely = 0.8, relheight = 0.1, relwidth = 0.3)
	quit = tk.Button(master = canvas, text = 'Quit', bg = 'red', command = root.destroy)
	quit.place(relx = 0.525, rely = 0.8, relheight = 0.1, relwidth = 0.3)

	root.mainloop()

menuGUI()
