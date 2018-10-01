import csv
from tkinter import *
from tkinter.filedialog import *
from collections import Counter

spreadsheet = ""
def importFile():
    global spreadsheet
    global tcv
    spreadsheet = askopenfilename(parent=root, filetypes =[("CSV files", ".csv")])
    print(spreadsheet)
    subButton.grid(row=8, column=2, sticky="S")
def openAdv():
    global cir
    global ctc
    advButton.grid_remove()
    Label(root, text="Only count in rows that contain:").grid(row=11,column=1)
    Label(root, text="in column:").grid(row=12,column=1)
    cir = Entry(root)
    cir.grid(row=11,column=2)
    ctc = Entry(root, width=3)
    ctc.grid(row=12,column=2)
    cir.insert(END,"")
    ctc.insert(END,"")
    Label(root, text="LEAVE BLANK if you want to count in every single row").grid(row=13,column=1,columnspan=2)
def process(): # processes the file!
    opts = []
    with open(spreadsheet) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=",")
        c = int(cEntry.get()) - 1 # which column to count from || INDEXES AT 0!!
            
        for row in readCSV:
            if labeled.get() == 1 and readCSV.line_num == 1:
                continue #sends you to top instead of continuing down
            if ctc.get() == "" or cir.get() == "":
                opts.append(row[c])
            else:
                if row[int(ctc.get())-1] == cir.get():
                    opts.append(row[c])
                
        print("The counts are:")
        counts = Counter(opts)
        y = ""
        for k,v in counts.items():
            x = (k + ": \t" + str(v)+"\n")
            y = x + y    
        tcv.set(y)
               
root = Tk()
root.geometry("700x700")
root.resizable(0,0)
textCounts = Label(root, text="")
text1 = Label(root, text="Select your file", font="50")
imButton = Button(root, text="Import", command=importFile, width=14, height=2)
subButton = Button(root, text="Submit", command=process, width=14, height=2)
text2 = Label(root, text="Are your columns labeled at the top row?", font=45)
text3 = Label(root, text="What column do you want to count in?", font=45)
cEntry = Entry(root, width = 2)
advButton = Button(root, text="Advanced", width=7, command=openAdv)
tcv = StringVar()
textCounts = Label(root, textvariable=tcv, font=45) #tcv - textCounts Variable
textCounts.grid(row=9, column=2)
cir = Entry()
ctc = Entry()

text1.grid(row=0, column=2, pady=10)
imButton.grid(row=1, padx=0, column = 2)
text2.grid(row=2, column=1, columnspan=3)
labeled = IntVar()
Radiobutton(root, text="Yes", variable=labeled, value=1).grid(row=3, column=1)
Radiobutton(root, text="No", variable=labeled, value=0).grid(row=3, column=3)
text3.grid(row=6, column=1, columnspan=2)
cEntry.grid(row=6, column=3)
cEntry.insert(END, 1)
advButton.grid(row=11,column=1)

root.grid_rowconfigure(2, minsize=50)
root.grid_rowconfigure(6, minsize=50)
root.grid_columnconfigure(0, minsize=50)
