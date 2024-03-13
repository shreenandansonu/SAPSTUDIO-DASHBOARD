import serial
import serial.tools.list_ports
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


# Get a list of all available ports
available_ports = serial.tools.list_ports.comports()
active_port = "NOT CONNECTED"
footer_text=active_port

# Print information about each port
for port in available_ports:
    active_port = port.device
    footer_text = "Your device is connected to " + active_port + " port."


# functions for the main software
def read_serial_data():
    try:
        serial_data = serial.readline().decode('utf-8').rstrip()
        data_list = serial_data.split('/')
        if len(data_list) == 6:
            soil_temp, soil_moisture, leaf_temp, leaf_moisture, ambient_voc, electrical_conductivity = map(int, data_list)
            return soil_temp, soil_moisture, leaf_temp, leaf_moisture, ambient_voc, electrical_conductivity
        else:
            return None
    except Exception as e:
        print(f"Error reading serial data: {e}")
        return None





# main screen
root = Tk()

# screen properties
root.title('SAP-STUDIO') 
root.iconbitmap('tkinter/logo1.ico')
root.configure(background='#1D3557')
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.minsize(width, height)
root.maxsize(width, height)
root.geometry(f"+0+0")
root.state('zoomed')

# Main UI
# img = Image.open('tkinter/logo1.png')  # opening the image
# img_resized = img.resize((200, 200))  # resizing the image
# img = ImageTk.PhotoImage(img_resized)
# img_label = Label(root, image=img)  # creating image label
# img_label.grid(row=0, column=0, columnspan=6, pady=(50, 10))

footer_label = Label(root, text=footer_text, font=("Courier New", 12), bg="black", fg="white", padx=10, pady=5)
footer_label.grid(row=0, column=0, columnspan=6, sticky='we')

logo=Label(root, text="SAPSTUDIO", font=("Helvetica", 30), bg="#1D3557", fg="#A8DADC", padx=10, pady=5)
logo.grid(row=0, column=0, columnspan=6, sticky='we')
# Placeholders for the data
labels = [
    Label(root, text="soil_temp"),
    Label(root, text="soil_moisture"),
    Label(root, text="leaf_temp"),
    Label(root, text="leaf_moisture"),
    Label(root, text="ambient_voc"),
]

for i, label in enumerate(labels):
    label.grid(row=2, column=i, padx=0, pady=10, columnspan=1 )
    # root.grid_columnconfigure(0, minsize=300)
    
root.mainloop()
