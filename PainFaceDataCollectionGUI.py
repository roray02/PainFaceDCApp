#!/usr/bin/env/python

from tkinter import *
from tkinter import filedialog
import csv
import tkinter.ttk as ttk
from datetime import date
import os.path
from PIL import Image, ImageTk
from tkinter import messagebox
import numpy as np
#import picamera
import time

root = Tk() #name of our tkinter window
filedirectory = ""
font_bold = ('calibre',11,'bold')
font_normal = ('calibre',11,'normal')
label_font = ('calibre', 14, 'bold')
csv_label_font = ('Helvetica', 10, 'bold')
#camera = picamera.PiCamera()
# camera.rotation = 180
rec_duration = 0

#location and name of video label
label_location = Label(root, text = 'Location and Name of Video:', font = label_font)
label_location.place(x = 5, y = 15)

#painface logo
img = Image.open("painface.JPG")
img = img.resize((200,200))
logoimg = ImageTk.PhotoImage(img)
logo = Label(root, image=logoimg)
logo.place(x=90,y=570)


#filename command
filename_var = StringVar()
fileID_var = StringVar()
fileid_path = 'fileid.csv'

idlist = []
def confirm_filename():
    # if (filename.find(".mp4") < 0):
    #     filename += ".mp4"
    recordtype = "BASE"
    if(rec.get() == "Baseline"):
        recordtype = "BASE"
    elif (rec.get() == "Post-Operation"):
        recordtype = "PO"
    elif(rec.get() == "Test"):
        recordtype = "TEST"
    else:
        recordtype = "BASE"
    today = date.today()
    d1 = today.strftime("%y%m%d")
    # if(os.path.exists(fileid_path) == False):
    #     with open(fileid_path, 'w', newline='') as f:
    #         w = csv.writer(f, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #         w.writerow([fileID_var.get()])
    # else:
    #     opendropdownFileID()
    
    filename = d1 + '_' + recordtype + '_' + fileID_var.get()
    filename_var.set(filename)
    label_confirm_filename.configure(text = "Confirmed filename: " + filename)

# file name widget
label_filename = Label(root, text = "Enter file ID:", font = font_bold)
entry_filename = Entry(root, textvariable = fileID_var, font = font_normal)
button_confirm_filename = Button(root, text = "Confirm", font = font_normal, command = confirm_filename)
label_confirm_filename = Label(root, text = "", font = font_normal)
recordtype = "BASE"
# def opendropdownFileID():
#     if(chk_filelistvar.get()==1):
#         entry_filename.configure(state='disabled')
#         fileID = fileID_var.get()
#         idlist = []
#         with open(fileid_path, 'r') as g:
#             r = csv.reader(g, delimiter=',')
#             for lines in r:
#                 idlist = lines[0]
#         if(fileID not in idlist):
#             dropdown_fileID = OptionMenu(root, fileID_var, *idlist)
#             dropdown_fileID.place(x=270,y=20)
#     else:
#         dropdown_fileID = OptionMenu(root, fileID_var, 'null')
#         entry_filename.configure(state='normal')
#         dropdown_fileID.configure(state='disabled')

# chk_filelistvar = IntVar()
# check_filenamelist = Checkbutton(root, text = 'Select from previously used IDs', font = font_normal, variable=chk_filelistvar, onvalue=1, offvalue=0, command=opendropdownFileID)
# check_filenamelist.place(x=20, y=20)

today = date.today()
d1 = today.strftime("%y%m%d")
t1 = time.strftime("%H%M")
filename = d1 + '_' + recordtype + '_' + filename_var.get()
filename_var.set(filename)

filedir_var = StringVar()
#directory selector command
def command_directoryExplorer():
    filedir = filedialog.askdirectory(initialdir = "/",
    title = "Select a Directory")
    label_file_explorer.configure(text= "File Directory: " + filedir)
    filedir_var.set(filedir)

# directory selector widget
label_file_explorer = Label(root, text = "Select the Directory to save your file:", font = font_bold, width = 100, height = 4)
button_file_explorer = Button(root, text = "Select Directory", font = font_normal, command = command_directoryExplorer)

#experimental variables label
label_experimental = Label(root, text = 'Experimental Variables:', font = label_font)
label_experimental.place(x=5, y = 220)

#pi number function
def pi_button():
    if pinumvar.get() == "Off":
        entry_pinum.configure(state='disabled')
        label_confirmed_pinum.configure(text = "")
    else:
        entry_pinum.configure(state="normal")
        entry_pinum.insert(0, '')


#pi number widget
pinumvar = StringVar()
raspinum = IntVar()
entry_pinum = Entry(root, width = 15, font = font_normal, textvariable = raspinum, state='disabled')
checkbox_pinum = Checkbutton(root, text = "Pi Number", width = 15, font = font_bold, variable = pinumvar, onvalue="On", offvalue="Off", command=pi_button)
checkbox_pinum.deselect()
entry_pinum.place(x=55,y=360)
checkbox_pinum.place(x=0,y=330)

label_confirmed_pinum = Label(root, text = "")
label_confirmed_pinum.place(x=50, y=375)
def confirm_pinum():
    if(pinumvar.get() == "On"):
        label_confirmed_pinum.configure(text = "Confirmed Pi Number: " + str(raspinum.get()), font = font_normal)

button_confirm_pinum = Button(root, text = "Confirm", font = font_normal, command = confirm_pinum)
button_confirm_pinum.place(x=200, y =350)


#recording duraction command
duration_var =  DoubleVar()
def confirm_duration():
    duration = duration_var.get()
    rec_duration = duration * 60
    label_confirm_duration.configure(text = "Confirmed duration: " + str(rec_duration) + " seconds")

# recording duration widget
label_duration = Label(root, text = "Recording duration (in minutes):", font = font_bold)
entry_duration = Entry(root, width = 10, textvariable= duration_var, font = font_normal)
button_confirm_duration = Button(root, text = "Confirm", font = font_normal, command = confirm_duration)
label_confirm_duration = Label(root, text = "", font = font_normal)

#Experiment Type Function
'''Experiment Type'''
rectype_list = []
dynamic_widgets = []
        
def rec_chk():
    if rec_var.get() == "Off":
        dropdown_recType.configure(state = 'disabled')
        for i in dynamic_widgets:
            i.destroy()  
    else:
        dropdown_recType.configure(state = 'normal')

types = StringVar()
def rectype(self):
    choice = rec.get()
    # print(choice)
    if choice == "Post-Operation":
        for i in dynamic_widgets:
            i.destroy()
        # polabel = Label(root, text="PO Type:")
        # dynamic_widgets.append(polabel)
        # polabel.place(x=100, y=180)
        types.set("Select PO Type")
        postop = OptionMenu(root, types, "Sham","Laparotomy")
        dynamic_widgets.append(postop)
        postop.place(x=160, y=430)
        POtype = types.get()
        if POtype == "Sham":
            recordingtype = 'SHAM'
        elif POtype == "Laparotomy":
            recordingtype = 'LAPA'
        animalid = Label(root, text="Animal ID:")
        dynamic_widgets.append(animalid)
        animalid.place(x=20, y=485)
        animalid_entry = Entry(root, width=10)
        dynamic_widgets.append(animalid_entry)
        animalid_entry.place(x=85, y=485)
        strain = Label(root, text="Strain:")
        dynamic_widgets.append(strain)
        strain.place(x=20, y=515)
        strain_entry = Entry(root, width=10)
        dynamic_widgets.append(strain_entry)
        strain_entry.place(x=85, y=515)
        surgeon = Label(root, text="Surgeon:")
        dynamic_widgets.append(surgeon)
        surgeon.place(x=20, y=455)
        surgeon_entry = Entry(root, width = 10)
        dynamic_widgets.append(surgeon_entry)
        surgeon_entry.place(x=85, y=455)
        surgery_start = Label(root, text="Start Time (HH:MM):")
        dynamic_widgets.append(surgery_start)
        surgery_start.place(x=190, y=455)
        start_entry = Entry(root, width=10)
        dynamic_widgets.append(start_entry)
        start_entry.place(x=320, y=455)
        surgery_end = Label(root, text = "End Time (HH:MM):")
        dynamic_widgets.append(surgery_end)
        surgery_end.place(x=190, y=485)
        end_entry = Entry(root, width=10)
        dynamic_widgets.append(end_entry)
        end_entry.place(x=320, y=485)
        animal_weight = Label(root, text="Weight (g):")
        dynamic_widgets.append(animal_weight)
        animal_weight.place(x=190, y=515)
        weight_entry = Entry(root, width=5)
        dynamic_widgets.append(weight_entry)
        weight_entry.place(x=320, y=515)
        lorr = Label(root, text="LORR (s):")
        dynamic_widgets.append(lorr)
        lorr.place(x=20, y=545)
        lorr_entry = Entry(root, width=5)
        dynamic_widgets.append(lorr_entry)
        lorr_entry.place(x=85, y=545)

    elif choice == "Baseline":
        for i in dynamic_widgets:
            i.destroy()
        recordingtype = 'BASE'
        animalid = Label(root, text="Animal ID:")
        dynamic_widgets.append(animalid)
        animalid.place(x=20, y=455)
        animalid_entry = Entry(root, width=20)
        dynamic_widgets.append(animalid_entry)
        animalid_entry.place(x=120, y=455)
        strain = Label(root, text="Strain:")
        dynamic_widgets.append(strain)
        strain.place(x=20, y=480)
        strain_entry = Entry(root, width=20)
        dynamic_widgets.append(strain_entry)
        strain_entry.place(x=120, y=480)
    
    elif choice == "Test":
        for i in dynamic_widgets:
            i.destroy()
        replicate = Label(root, text="Rep #:")
        dynamic_widgets.append(replicate)
        replicate.place(x=20, y=455)
        replicate_entry = Entry(root, width = 20)
        dynamic_widgets.append(replicate_entry)
        replicate_entry.place(x=90, y=455)
        recordingtype = 'TEST'
    else:
        for i in dynamic_widgets:
            i.destroy()

#recording type widget
rec_var = StringVar()
checkbox_recType = Checkbutton(root, text='Experiment Type', width = 15, font = font_bold, variable = rec_var, onvalue="On", offvalue="Off", command=rec_chk)
checkbox_recType.deselect()
checkbox_recType.place(x=20, y=400)

rec = StringVar()
rec.set("Select Experiment Type")
dropdown_recType = OptionMenu(root, rec, "Baseline", "Post-Operation", "Test", command=rectype)
dropdown_recType.configure(state = 'disabled')
dropdown_recType.place(x=30, y=430)

#notes widget
# notes_label = Label(root, text="Notes (optional):", font=font_bold)
# notes_label.place(x=30, y=600)   
# notes_text = Text(root, width=25, height=5, font=font_normal)
# notes_text.place(x=35,y=630)

#camera settings labels
label_camera = Label(root, text = 'Camera Settings:', font = label_font)
label_camera.place(x=450, y=15)

# resolution function
res_var = StringVar()
confirmed_res = "(640, 480)"
def confirm_resolution():
    label_confirmed_res = Label(root, text = "Confirmed Resolution: " + res_var.get()).place(x=650, y=70)
    confirmed_res = res_var.get()
    strRes = res_var.get()
    print(res_var.get())
    res1 = int(strRes[1:strRes.find(',')])
    res2 = int(strRes[strRes.find(',')+2:len(strRes)-1])
    update_framerate_options()
    #camera.resolution = (res1,res2)

#resolution widget
label_resolution = Label(root, text = 'Select Camera Resolution: ', font = font_bold)
label_resolution.pack()
res_options = ["(640, 480)", "(1296, 972)", "(1296, 730)", "(1920, 1080)", "(2592, 1944)"]
res_var.set(res_options[0])
dropdown_resolution = OptionMenu(root, res_var, *res_options)
dropdown_resolution.pack()

button_confirm_resolution = Button(root, text = "Confirm", font = font_normal, command = confirm_resolution)
label_confirm_resolution = Label(root, text = "", font = font_normal)

# frame rate function and widget
frame_var = StringVar(root)
def confirm_framerate():
    label_confirmed_framerate = Label(root, text = "Confirmed Frame Rate: " + frame_var.get() + " fps").place(x=650, y=135)
    #camera.framerate = int(frame_var.get())

def update_framerate_options():
    import tkinter as tk
    frame_var.set('')
    confirmed_res = res_var.get()
    frOptions1 = ("42", "45", "50", "55", "60", "65", "70", "75", "80", "85", "90")
    frOptions2 = ("10", "20", "30", "40", "42")
    frOptions3 = ("10", "20", "30", "40", "42", "49")
    frOptions4 = ("10", "15", "20", "25", "30")
    frOptions5 = ("1", "5", "10", "15")

    if(confirmed_res == "(640, 480)"):
        framerate_options = frOptions1
    elif(confirmed_res == "(1296, 972)"):
        framerate_options = frOptions2
    elif(confirmed_res == "(1296, 730)"):
        framerate_options = frOptions3
    elif(confirmed_res == "(1920, 1080)"):
        framerate_options = frOptions4
    elif(confirmed_res == "(2592, 1944)"):
        framerate_options = frOptions5
    else:
        framerate_options = frOptions4
    
    dropdown_framerate['menu'].delete(0, 'end')
    print(framerate_options)
    for option in framerate_options:
        dropdown_framerate['menu'].add_command(label = option, command = tk._setit(frame_var, option))

label_framerate = Label(root, text = 'Select Camera Frame Rate: ', font = font_bold)
label_framerate.pack()

framerate_options = ("10", "20", "30", "40", "60")
dropdown_framerate = OptionMenu(root, frame_var, *framerate_options)

button_confirm_framerate = Button(root, text = "Confirm", font = font_normal, command = confirm_framerate)
button_confirm_framerate.pack()
label_confirm_framerate = Label(root, text = "", font = font_normal)
label_confirm_framerate.pack()


# sharpness slider widget and function
slider_sharpness = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=10, length=300)
slider_sharpness.set(50)
slider_sharpness.place(x= 460, y=180)

label_sharpness_number = Label(root, text = "Sharpness: ", font = font_bold)
label_sharpness_number.place(x= 460, y = 155)

def confirm_sharpness():
    label_confirm_sharpness = Label(root, text="Confirmed sharpness: " + str(slider_sharpness.get()))
    sharpness = slider_sharpness.get()
    label_confirm_sharpness.place(x=460, y= 240)
    #camera.sharpness = sharpness

button_confirm_sharpness = Button(root, text='Confirm', command=confirm_sharpness).place(x=770, y=200)


#brightness slider widget and function
slider_brightness = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=10, length=300)
slider_brightness.set(50)
slider_brightness.place(x= 460, y=290)

label_brightness_number = Label(root, text = "Brightness: ", font = font_bold)
label_brightness_number.place(x= 460, y = 265)

def confirm_brightness():
    label_confirm_brightness = Label(root, text="Confirmed brightness: " + str(slider_brightness.get()))
    brightness = slider_brightness.get()
    label_confirm_brightness.place(x=460, y= 350)
    #camera.brightness = brightness

button_confirm_brightness = Button(root, text='Confirm', command=confirm_brightness).place(x=770, y=310)

#video preview label
label_video_preview = Label(root, text = 'Video Preview:', font = label_font)
label_video_preview.place(x =450, y =400)

#recording start end time
t= time.localtime()
starttimeVar = StringVar()
endtimeVar = StringVar()

# picamera initialization
def CameraON():
    camera.preview_fullscreen = False
    camera.preview_window = (90, 100, 320, 240)
    camera.resolution = (640, 480)
    camera.start_preview()

def CameraOFF():
    camera.stop_preview()


def CameraRECORD():
    rec_duration = duration_var.get() * 60
    if(filename_var.get() == ""):
        label_recording_status.configure(text = "Enter filename before starting recording!")
    elif(rec_duration == 0):
        label_recording_status.configure(text = "Enter recording duration before starting recording!")
    else:
        label_recording_status.configure(text = "Recording has begun!")
        label_recording_status.place(x = 720, y= 390)
        button_start_recording.configure(bg = "red")
        print(rec_duration)
        print(filename_var.get())
        directory = filedir_var.get()
        filename = filename_var.get()
        directory += filename
        t = time.localtime()
        recording_start_time = (time.strftime("%H:%M:%S", t)) 
        starttimeVar.set(recording_start_time)
        #camera.start_recording(f'{directory}.h264')
        bar()
        #camera.wait_recording(rec_duration)
        #camera.stop_recording()
        label_recording_status.configure(text = "Recording is complete!")
        button_start_recording.configure(bg = "skyblue1")
        #camera.close()
        t = time.localtime()
        recording_end_time = (time.strftime("%H:%M:%S", t))
        endtimeVar.set(recording_end_time)
        if(CSVflagVar.get() == "On"):
            create_csv()
        openNextRecordingWindow()

def openNextRecordingWindow():
    def recordAgain():
        nrWindow.destroy()
        progress["value"] = 0
        label_progressbar_status.configure(text = "0% Complete")
        label_recording_status.configure(text = "")
    def closeGUI():
        nrWindow.destroy()
        root.destroy()

    nrWindow = Toplevel(root)
    nrWindow.title("Recording Complete")
    nrWindow.geometry("400x160")
    Label(nrWindow, text="Recording is complete!\n Would you like to record another video?", font = font_normal).pack()
    Button(nrWindow, text="Yes", font=font_normal,command=recordAgain).place(x=130,y=60)
    Button(nrWindow,text="No",font=font_normal,command=closeGUI).place(x=230,y=60)

    

#open preview button
button_open_preview = Button(root, text = "Open Preview", font = font_bold, bg = "green2", command = CameraON)
button_open_preview.place(x=482,y=435)

#close preview button
button_close_preview = Button(root, text = "Close Preview", font = font_bold, bg = "tomato", command = CameraOFF)
button_close_preview.place(x=480, y = 470)

#start recording button
button_start_recording = Button(root, text = "Start Recording", height = 2, font = font_bold, bg = "skyblue1", command = CameraRECORD)
button_start_recording.place(x = 720, y = 450)
label_recording_status = Label(root, text = '', font = font_normal)
label_recording_status.place(x = 660, y = 420)

#progress bar
label_progress = Label(root, text = "Recording Progress:", font = font_bold).place(x = 605, y = 530)
progress = ttk.Progressbar(root, orient = HORIZONTAL, length = 400, mode= 'determinate')
progress.place(x= 480, y = 550)

label_progressbar_status = Label(root, text = "0% Complete", font = font_normal)
label_progressbar_status.place(x=625, y = 575)

def bar():
    rec_duration = duration_var.get() * 60
    for second in range(int(rec_duration + 1)):
        progresspct = second/rec_duration * 100
        progress['value'] = progresspct
        ppct = int(progresspct)
        label_progressbar_status.configure(text = str(ppct) + "% Complete")
        root.update_idletasks()
        time.sleep(1)

#csv file
#check if filename_var is confirmed
def create_csv():
    directory = filedir_var.get() + '/'
    todaydate = date.today()
    d2 = todaydate.strftime("%y%m%d")
    csvName = d2 + '_' + 'DATA' 
    directory += csvName
    if(os.path.isfile(directory + '.csv') == False):
        with open(directory + '.csv', 'w', newline='') as f:
            w = csv.writer(f, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            #TODO: check to make sure these are confirmed
            resolution = res_var.get()
            res1 = str(resolution[1:resolution.find(',')])
            res2 = str(resolution[resolution.find(',')+2:len(resolution)-1])
            newres = res1 + 'x' + res2
            rowHeaders = ['Recording Name', 'Brightness', 'Sharpness', 'Resolution', 'Framerate', 'Start Time', 'End Time', 'Pi Number', 'Experiment Type', 'Post-Operation Type', 'Post-Op Info']
            trialData = [filename_var.get(), slider_brightness.get(), slider_sharpness.get(), newres, frame_var.get(), starttimeVar.get(), endtimeVar.get()]
            # as an example, i created a boolean flag variable that is true when the pi button is confirmed. 
            # not sure if there is a better way to do this 
            if pinumvar.get() == "On":
                trialData.append(raspinum.get())

            #recording type variables: i used label['text'] to retrieve text from labels and .get() to retrieve text from entry boxes
            postOpVars = []
            postOpData = []
            baselineVars = []
            baselineData = []
            if rec_var.get() == "On":
                trialData.append(rec.get())
                if rec.get() == "Post-Operation":
                    trialData.append(types.get())
                    for i in range(1, len(dynamic_widgets)):
                        if i % 2 != 0:
                            postOpVars.append(dynamic_widgets[i]['text'])
                            postOpData.append(dynamic_widgets[i+1].get())
                    for var in postOpVars:
                        rowHeaders.append(var)
                    for data in postOpData:
                        trialData.append(data)
                elif rec.get() == 'Baseline' or rec.get() == 'Test':
                    for i in range(len(dynamic_widgets)):
                        if i%2 == 0:
                            baselineVars.append(dynamic_widgets[i]['text'])
                            baselineData.append(dynamic_widgets[i+1].get())
                            for var in baselineVars:
                                rowHeaders.append(var)
                            for data in baselineData:
                                trialData.append(data)
            w.writerow(rowHeaders)
            w.writerow(trialData)
    else:
        with open(directory + '.csv', 'a', newline='') as f:
            w = csv.writer(f, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            #TODO: check to make sure these are confirmed
            print(res_var.get())
            resolution = res_var.get()
            res1 = str(resolution[1:resolution.find(',')])
            res2 = str(resolution[resolution.find(',')+2:len(resolution)-1])
            newres = res1 + 'x' + res2
            rowHeaders = ['FileName', 'Brightness', 'Sharpness', 'Resolution', 'Framerate', 'Start Time', 'End Time', 'Pi Number', 'Experiment Type', 'Post-Operation Type', 'Post-Op Info']
            trialData = [filename_var.get(), slider_brightness.get(), slider_sharpness.get(), newres, frame_var.get(), starttimeVar.get(), endtimeVar.get()]
            # as an example, i created a boolean flag variable that is true when the pi button is confirmed. 
            # not sure if there is a better way to do this 
            if pinumvar.get() == "On":
                trialData.append(raspinum.get())

            #recording type variables: i used label['text'] to retrieve text from labels and .get() to retrieve text from entry boxes
            postOpVars = []
            postOpData = []
            baselineVars = []
            baselineData = []
            if rec_var.get() == "On":
                trialData.append(rec.get())
                if rec.get() == "Post-Operation":
                    trialData.append(types.get())
                    for i in range(1, len(dynamic_widgets)):
                        if i % 2 != 0:
                            postOpVars.append(dynamic_widgets[i]['text'])
                            postOpData.append(dynamic_widgets[i+1].get())
                    for var in postOpVars:
                        rowHeaders.append(var)
                    for data in postOpData:
                        trialData.append(data)
                elif rec.get() == 'Baseline' or rec.get() == 'Test':
                    for i in range(len(dynamic_widgets)):
                        if i%2 == 0:
                            baselineVars.append(dynamic_widgets[i]['text'])
                            baselineData.append(dynamic_widgets[i+1].get())
                            for var in baselineVars:
                                rowHeaders.append(var)
                            for data in baselineData:
                                trialData.append(data)
            w.writerow(trialData)


        
# csv_button = Button(root,height=2, width=30, text="Create CSV", font=font_bold, padx=-5, pady=-5, bg = "pink", command=set_csv_Flag)
# csv_button.place(x=550, y=640)
# csv_label = Label(root, text="Make sure all necessary fields are entered before creating csv.", font=csv_label_font)
# csv_label.place(x=500, y=700)

CSVflagVar = StringVar()
includeincsv_checkbox = Checkbutton(root, text='Include in CSV',font = font_bold, variable = CSVflagVar, onvalue="On", offvalue="Off")
includeincsv_checkbox.deselect()
includeincsv_checkbox.place(x=550,y=640)

 
# Place Widgets

#filename place
label_filename.place(x=20, y=50)
entry_filename.place(x=150, y=50)
button_confirm_filename.place(x=50, y=75)
label_confirm_filename.place(x=150,y=75)

#directory place
label_file_explorer.place(x=-280, y = 100)
button_file_explorer.place(x = 50, y= 150)

#duration place
label_duration.place(x=20, y=265)
entry_duration.place(x=260, y=265)
button_confirm_duration.place(x=40, y=290)
label_confirm_duration.place(x=130,y=295) 

#resolution place
label_resolution.place(x= 460, y= 40)
dropdown_resolution.place(x=660, y= 40)
button_confirm_resolution.place(x=760, y=40)

#framerate place
label_framerate.place(x= 460, y= 100)
dropdown_framerate.place(x=660, y= 100)
button_confirm_framerate.place(x=750, y=100)


root.title("PainFace Data Collection App")
root.geometry("1000x800")
root.resizable(width = False, height = False)

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        #camera.close()
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
