import csv
from tkinter import *
from tkinter.filedialog import *
from collections import Counter

spreadsheet = ""
errorRaised = ""
def importFile():
    global spreadsheet
    global tcv
    spreadsheet = askopenfilename(parent=root, filetypes =[("CSV files", ".csv")])
    print(spreadsheet)
    subButton.grid(row=10, column=2, sticky="S")
def openAdv():
    global conInRow   #contains in row
    global colToCheck #columns to check for conInRow
    advButton.grid_remove()
    Label(root, text="Only count in rows that contain:").grid(row=6,column=1,columnspan=2)
    Label(root, text="in column:").grid(row=7,column=2)
    colToCheck = Entry(root, width=3,bg=None)
    colToCheck.grid(row=7,column=3)
    conInRow = Entry(root, width=5)
    conInRow.grid(row=6,column=3)
    colToCheck.insert(END,"")
    conInRow.insert(END,"")
    Label(root, text="LEAVE BLANK if you want to count in every single row").grid(row=8,column=1,columnspan=3)
def process(): # processes the file!
    opts = []
    global errorRaised
    colToCheck.configure(bg="White")
    cEntry.configure(bg="White")
    errorRaised.set("")
    with open(spreadsheet) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=",")
        try:
            c = int(cEntry.get()) - 1
        except ValueError:
            cEntry.configure(bg="Red")
            errorRaised.set("You may only use numbers to pick columns")    
        for row in readCSV:
            if labeled.get() == 1 and readCSV.line_num == 1:
                continue #sends you to top instead of continuing down
            if colToCheck.get() == "" or conInRow.get() == "":
                try:
                    opts.append(row[c])
                except IndexError:
                    cEntry.configure(bg="Red")
                    errorRaised.set("That isn't a valid column")
            else:
                try:
                    if row[int(colToCheck.get())-1] == conInRow.get():
                        try:
                            opts.append(row[c])
                        except ValueError:
                            cEntry.configure(bg="Red")
                            errorRaised.set("You may only use numbers to pick columns")
                        except IndexError:
                            cEntry.configure(bg="Red")
                            errorRaised.set("That isn't a valid column")
                except ValueError:
                    colToCheck.configure(bg="Red")
                    errorRaised.set("You may only use numbers to pick columns")
                    break
                except IndexError:
                    colToCheck.configure(bg="Red")
                    errorRaised.set("That isn't a valid column")
                    break
                
        print("The counts are:")
        counts = Counter(opts)
        y = ""
        for k,v in counts.items():
            x = (k + ": \t" + str(v)+"\n")
            y = x + y    
        tcv.set(y)
               
root = Tk()
root.geometry("330x700")
root.resizable(0,0)
textCounts = Label(root, text="")
text1 = Label(root, text="Select your file", font="50")
imButton = Button(root, text="Import", command=importFile, width=14, height=2)
subButton = Button(root, text="Submit", command=process, width=14, height=2)
text2 = Label(root, text="Are your columns labeled at the top row?", font=45)
text3 = Label(root, text="What column do you want to count in?", font=45, background=None)
cEntry = Entry(root, width = 2)
advButton = Button(root, text="Advanced", width=7, command=openAdv)
tcv = StringVar()
textCounts = Label(root, textvariable=tcv, font=45) #tcv - textCounts Variable
textCounts.grid(row=11, column=1, columnspan=3)
conInRow = Entry()
colToCheck = Entry()
errorRaised = StringVar()
errorWarning = Label(root, textvariable=errorRaised)

text1.grid(row=0, column=2, pady=10)
imButton.grid(row=1, column=2)
text2.grid(row=2, column=0, columnspan=4)
labeled = IntVar()
Radiobutton(root, text="Yes", variable=labeled, value=1).grid(row=3, column=1)
Radiobutton(root, text="No", variable=labeled, value=0).grid(row=3, column=3)
text3.grid(row=4, column=0, columnspan=3)
cEntry.grid(row=4, column=3)
cEntry.insert(END, 1)
advButton.grid(row=6,column=2)
errorWarning.grid(row=12, column = 2)

for i in range(10):
    root.grid_rowconfigure(i, minsize=30)
