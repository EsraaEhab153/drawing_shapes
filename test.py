import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
from PIL import ImageTk,Image
from tkinter import colorchooser
import matplotlib.pyplot as plt
def on_circle_click():
    def draw_circle(radius):
        x = 0
        y = radius
        d = 1 - radius
        points = []
        while x <= y:
            points.extend([(x, y), (y, x), (y, -x), (x, -y),(-x, -y), (-y, -x), (-y, x), (-x, y) ])
            if d <= 0:
                d += 2 * x + 3
                x += 1
            else:
                d += 2 * (x - y) + 3
                y -= 1
                x += 1
        return points
        
    def plot_circle(radius):
        points = draw_circle(radius)
        x, y = zip(*points)

        # Plotting the circle and filling it with red color
        plt.fill(x, y, color=colorchooser.askcolor()[1])
        plt.gca().set_aspect('equal', adjustable='box')
        plt.grid(True)
        plt.show()

    def get_radius_entry():
        radius = int(entry.get())
        plot_circle(radius)

    # Create Tkinter window
    cir1 = tk.Tk()
    cir1.geometry("500x500")
    cir1['background']="#4BF5F5"
    cir1.title("Circle Drawe")

    # Label and Entry for entering radius
    label = Label(cir1, text="Enter Radius:",bg="#4BF5F5")
    label.pack()

    entry = Entry(cir1,bg="#EcFF58")
    entry.pack()

    # Button to plot the circle
    button = Button(cir1, text="Draw Circle", command=get_radius_entry,bg="#ff0340",fg='white')
    button.pack()

    # Run Tkinter event loop
    cir1.mainloop()
    
#line function    
def on_line_click():
    def midpoint(x1,y1,x2,y2):
        dx=x2-x1
        dy=y2-y1

    #intialize the decision parameter
        d=dy-(dx/2)
        x=x1
        y=y1

        print(f"x={x},y={y}")
    #intialize the plotting points
        xcoordinates = [x]
        ycoordinates = [y]

        while(x<x2):
            x=x+1
    #East
        if(d<0):
            d=d+dy
    #North East
        else:
            d=d+(dy-dx)
            y=y+1

        xcoordinates.append(x)
        ycoordinates.append(y)
        print(f"x={x},y={y}")
        plt.plot(xcoordinates,ycoordinates,color=colorchooser.askcolor()[1])
        plt.show()
    def draw_line_button():
        x1 = int(entry_x1.get())
        y1 = int(entry_y1.get())
        x2 = int(entry_x2.get())
        y2 = int(entry_y2.get())

        midpoint(x1,y1,x2,y2)
        
        
    lin1=Tk()
    lin1.geometry("500x500")    
    lin1['background']='#4BF5F5'
    lin1.title("Line Drawe")
    # Create entry widgets for coordinates
    tk.Label(lin1, text="X1:",bg='#4BF5F5').pack()
    entry_x1 = tk.Entry(lin1,bg="#ECFF58")
    entry_x1.pack()

    tk.Label(lin1, text="Y1:",bg='#4BF5F5').pack()
    entry_y1 = tk.Entry(lin1,bg="#ECFF58")
    entry_y1.pack()

    tk.Label(lin1, text="X2:",bg='#4BF5F5').pack()
    entry_x2 = tk.Entry(lin1,bg="#ECFF58")
    entry_x2.pack()

    tk.Label(lin1, text="Y2:",bg='#4BF5F5').pack()
    entry_y2 = tk.Entry(lin1,bg="#ECFF58")
    entry_y2.pack()
    button =Button(lin1, text="Draw Line",command=draw_line_button,bg="#FF0340",fg="white").pack()
    lin1.mainloop()

    
def on_rectangle_click():
    
    def draw_rectangle():
        try:
            # Get user input for height and width
            height = int(height_entry.get())
            width = int(width_entry.get())

            # Create a canvas
            canvas.delete("all")
            canvas.create_rectangle(150-width, 150-height, 150 + width, 150 + height, outline="black", width=2,fill=colorchooser.askcolor()[1])

        except ValueError:
            result_label.config(text="Please enter valid integers for height and width.")

    # Create the rectangle window
    rec1 = tk.Tk()
    rec1.geometry("500x500")
    rec1['background']="#4BF5F5"
    rec1.title("Rectangle Drawer")

    # Create input labels and entry widgets
    height_label = tk.Label(rec1, text="Height:",bg="#4BF5F5")
    height_label.grid(row=0, column=0, padx=5, pady=5)

    height_entry = tk.Entry(rec1)
    height_entry.grid(row=0, column=1, padx=5, pady=5)
    width_label = tk.Label(rec1, text="Width:",bg="#4BF5F5")
    width_label.grid(row=1, column=0, padx=5, pady=5)

    width_entry = tk.Entry(rec1)
    width_entry.grid(row=1, column=1, padx=5, pady=5)

    # Create a button to draw the rectangle
    draw_button = tk.Button(rec1, text="Draw Rectangle", command=draw_rectangle,bg="#FF0340",fg="white")
    draw_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Create a canvas to draw the rectangle
    canvas = tk.Canvas(rec1, width=300, height=300,bg="#ECFF58")
    canvas.grid(row=3, column=0, columnspan=2,padx=50)


    # Create a label to display error messages
    result_label = tk.Label(rec1, text="")
    result_label.grid(row=4, column=0, columnspan=2)

    # Start the main loop
    rec1.mainloop() 

# Create the main window
root = tk.Tk()
root.title("CG project")
root.geometry("700x700")
# Load the background image
background_image =ImageTk.PhotoImage(Image.open("CGBG.jpg"))  # Replace with the path to your image file
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Create a circle button on top of the background
circle_button=ImageTk.PhotoImage(Image.open("circle_button.jpeg"),width=20,height=40)
img_label1=Label(image=circle_button)
my_button1=Button(root,image=circle_button,command=on_circle_click,borderwidth=0,bg="#F6F6F6")
my_button1.pack(pady=20)
my_label1=Label(root,text="")
my_label1.pack(pady=20)
my_button1.place(relx=0.5, rely=0.44, anchor="center")

# Create a line button on center of the background
line_button=ImageTk.PhotoImage(Image.open("line_button.jpeg"),width=20,height=40)
img_label2=Label(image=circle_button)
my_button2=Button(root,image=line_button,command=on_line_click,borderwidth=0,bg="#F6F6F6")
my_button2.pack(pady=20)
my_label2=Label(root,text="")
my_label2.pack(pady=20)
my_button2.place(relx=0.5, rely=0.57, anchor="center")


# Create a rectangle button on center of the background
rec_button=ImageTk.PhotoImage(Image.open("rectangle_button.jpeg"),width=20,height=40)
img_label3=Label(image=circle_button)
my_button3=Button(root,image=rec_button,command=on_rectangle_click,borderwidth=0,bg="#F6F6F6")
my_button3.pack(pady=20)
my_label3=Label(root,text="")
my_label3.pack(pady=20)
my_button3.place(relx=0.5, rely=0.70, anchor="center")

#label of operations
label_op=Label(root,text="choose the operation you want to do",font="36",width="30",height="1",bg="#F6F6F6")
label_op.place(relx=0.5, rely=0.52, anchor="center")
label_op.pack(pady=51)


# Run the Tkinter event loop
root.mainloop()