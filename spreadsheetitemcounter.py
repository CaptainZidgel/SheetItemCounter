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
def process(): # processes the file!
    opts = []
 #   labeled = ""
 #   labeled = input("Are your columns labeled at the top row? Answer 'yes' or 'no'")
 #   labeled = labeled.lower()
    with open(spreadsheet) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=",")
        print(labeled.get())
        c = int(cEntry.get()) - 1 # which column to count from || INDEXES AT 0!!
        for row in readCSV:
            if labeled.get() == 1 and readCSV.line_num == 1:
                continue
            opts.append(row[c])
        print("The counts are:")
        counts = Counter(opts)
        y = ""
        for k,v in counts.items():
            x = (k + ": \t" + str(v)+"\n")
            y = x + y    
        tcv.set(y)

        
#todo: add select only rows with certain other items
               
root = Tk()
root.geometry("400x700")
root.resizable(0,0)
textCounts = Label(root, text="")
text1 = Label(root, text="Select your file", font="50")
imButton = Button(root, text="Import", command=importFile, width=14, height=2)
subButton = Button(root, text="Submit", command=process, width=14, height=2)
text2 = Label(root, text="Are your columns labeled at the top row?", font=45)
text3 = Label(root, text="What column do you want to read?", font=45)
cEntry = Entry(root, width = 2)

tcv = StringVar()
textCounts = Label(root, textvariable=tcv, font=45) #tcv - textCounts Variable
textCounts.grid(row=9, column=2)

text1.grid(row=0, column=2, pady=10)
imButton.grid(row=1, padx=0, column = 2)
text2.grid(row=2, column=1, columnspan=3)
labeled = IntVar()
Radiobutton(root, text="Yes", variable=labeled, value=1).grid(row=3, column=1)
Radiobutton(root, text="No", variable=labeled, value=0).grid(row=3, column=3)
text3.grid(row=6, column=1, columnspan=2)
cEntry.grid(row=6, column=3)
cEntry.insert(END, 1)

root.grid_rowconfigure(2, minsize=50)
root.grid_rowconfigure(6, minsize=50)
root.grid_columnconfigure(0, minsize=50)
