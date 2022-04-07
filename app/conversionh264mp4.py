from picamera import PiCamera
from time import sleep
from subprocess import call
from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk

root2 = Tk()

font_bold = ('calibre',11,'bold')
font_normal = ('calibre',11,'normal')
label_font = ('calibre', 14, 'bold')

filedir_var = StringVar()
#directory selector command
def command_directoryExplorer():
    filedir = filedialog.askopenfilename(initialdir = "/media",
    title = "Select a File", filetypes=[(".h264 files", "*.h264")])
    label_file_explorer.configure(text= "Selected H264 File: " + filedir)
    filedir_var.set(filedir)
    
# directory selector widget
label_file_explorer = Label(root2, text = "Select H264 File:", font = font_bold)
button_file_explorer = Button(root2, text = "Select File", font = font_normal, command = command_directoryExplorer)
label_file_explorer.place(x=10,y=100)
button_file_explorer.place(x=150,y=200)

def convert():
    file_h264 = filedir_var.get()
    file_mp4 = file_h264[:-5] + '.mp4'
    command = "MP4Box -add " + file_h264 + " " + file_mp4
    call([command], shell = True)
    label_conversion_status.configure(text = "Conversion complete!")
    print("\r\nRasp_Pi => Video Converted! \r\n")
    
button_convert = Button(root2, text = "Convert .h264 to .mp4", font = font_normal, command = convert)
button_convert.place(x=100, y= 250)
label_conversion_status = Label(root2, text= "", font = font_bold)
label_conversion_status.place(x=100, y= 150)
                    

# filename = '/media/pi/3386-026D/220407_BASE_conversiontry1.h264'
# print(filename)
# mp4filename = filename[:-5] + '.mp4'
# print(mp4filename)
#     
# convert(filename, mp4filename)


root2.title("Convert H264 TO MP4")
root2.geometry("400x300")
root2.resizable(width = False, height = False)
root2.mainloop()
