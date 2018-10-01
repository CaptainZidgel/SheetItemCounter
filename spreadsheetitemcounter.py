import csv
from tkinter import *
from tkinter.filedialog import *
from collections import Counter

spreadsheet = ""
def importFile():
    global spreadsheet
    spreadsheet = askopenfilename(parent=root, filetypes =[("CSV files", ".csv")])
    print(spreadsheet)
    subButton.grid(row=4, column=2, sticky="S")
def process(): # processes the file!
    opts = []
 #   labeled = ""
 #   labeled = input("Are your columns labeled at the top row? Answer 'yes' or 'no'")
 #   labeled = labeled.lower()
    with open(spreadsheet) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=",")
        print(labeled.get())
        for row in readCSV:
            if labeled.get() == 1 and readCSV.line_num == 1:
                continue
            opts.append(row[1])
        print("The counts are:")
        counts = Counter(opts)
        #print(counts)
        y = ""
        for k,v in counts.items():
            x = (k + ": \t" + str(v)+"\n")
            y = x + y   
        textCounts = Label(root, text=y, font=45)
        textCounts.grid(row=5, column=2)
#todo: add select column, add select only rows with certain other items
        
root = Tk()
root.geometry("400x500")
root.resizable(0,0)
text1 = Label(root, text="Select your file", font="50")
imButton = Button(root, text="Import", command=importFile, width=14, height=2)
subButton = Button(root, text="Submit", command=process, width=14, height=2)
text2 = Label(root, text="Are your columns labeled at the top row?", font=45)

imButton.grid(row=1, padx=0, column = 2)
text1.grid(row=0, column=2, pady=10)
text2.grid(row=2, column=1, columnspan=3)
labeled = IntVar()
Radiobutton(root, text="Yes", variable=labeled, value=1).grid(row=3, column=1)
Radiobutton(root, text="No", variable=labeled, value=0).grid(row=3, column=3)

root.grid_rowconfigure(2, minsize=50)
root.grid_columnconfigure(0, minsize=50)
