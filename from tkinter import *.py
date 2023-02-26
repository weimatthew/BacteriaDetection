from tkinter import *

window = Tk()
window.title('Add Image')
window = Canvas(window,width=450, height=450)
window.pack()
image=PhotoImage(file = '/Users/matthewwei/Downloads/FoT_QlhaUAEg9S5.jpeg') #photo file
window.create_image(0,0, anchor = NW, image = image)

window.mainloop()