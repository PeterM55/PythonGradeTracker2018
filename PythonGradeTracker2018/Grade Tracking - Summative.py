from tkinter import *

#made by Peter Mitchell 2018

numOfAssigns = 15
boxes = 3
mainSaveName = "classSaves"
global saveName
saveName = "savedMarks"
displayMode = 0
window = Tk()
window.title("Grade Tracker")
backgroudColour = "#4da6ff"
window.configure(background=backgroudColour)
tempvar = 0

informationText = list([[],[],[],[],[]] for i in range(1,numOfAssigns+2))
informationTopText = list([[],[],[],[],[]] for i in range(3))

def percentToLevel(float1):
    if float1 < 20:
        return "R-"
    elif float1 < 40:
        return "R"
    elif float1 < 50:
        return "R+"
    elif float1 < 52:
        return "1-"
    elif float1 < 56:
        return "1"
    elif float1 < 59:
        return "1+"
    elif float1 < 62:
        return "2-"
    elif float1 < 64:
        return "2"
    elif float1 < 69:
        return "2+"
    elif float1 < 72:
        return "3-"
    elif float1 < 76:
        return "3"
    elif float1 < 79:
        return "3+"
    elif float1 < 86:
        return "4-"
    elif float1 < 94:
        return "4"
    else:
        return "4+"   
    

def spaces(int1,int2):
    if int1 == 1:
        return(int2*"\n")
    else:
        return(int2*" ")

def deleteAll():
    for i in range(len(informationTopText)):
        for i2 in range(len(informationTopText[i])):
            if informationTopText[i][i2] != []:
                informationTopText[i][i2].delete(0.0,END)
    for i in range(len(informationText)):
        for i2 in range(len(informationText[i])):
            if informationText[i][i2] != []:
                informationText[i][i2].delete(0.0,END)

def submitButton():
    save()
    deleteAll()
    #print((informationText[0][0]).get("1.0",END))
    enteredText = textEntry.get('1.0', END).replace("\n","")
    if enteredText.lower() in "students":

        informationTopText[2][0].insert(END, 'Student Name')
        informationTopText[2][1].insert(END, 'Overall mark')
        informationTopText[2][2].insert(END, 'Level')
        informationTopText[2][3].insert(END, 'Average\nPercentage')

        informationTopText[0][0].insert(END, 'Students')
        informationTopText[0][1].insert(END, 'Overall Mark')
        informationTopText[0][2].insert(END, 'Overall Level')
        informationTopText[0][3].insert(END, 'Average Mark')
        
        displayMode = 0
        for i in range(numOfAssigns):
            #printing names
            informationText[i][0].insert(END, pastInformation[0][i])

            averageMark = [[0,0,0] for i2 in range(numOfAssigns)]
            for i2 in range(numOfAssigns):
                try:
                    averageMark[i][0] += pastInformation[2][i2][i][1]
                    averageMark[i][1] += 1
                except:
                    pass
        temparr3 = []
        temparr4 = []
        for i in range(len(pastInformation[2][0])): #going down the list, changin student.
            tempvar = 0
            temparr = []
            temparr2 = []
            for i2 in range(len(pastInformation[2])):#going through the assignments
                #calculating average.
                
                try:
                    temparr.append(int(pastInformation[2][i2][i][1]))
                    
                    temparr2.append(int(pastInformation[2][i2][i][1])*(int(pastInformation[1][i2][1])/100))
                    tempvar += float(pastInformation[1][i2][1])/100
                except:
                    pass
                    #print("test1")
            try:
                informationText[i][3].insert(END, str(round(sum(temparr)/len(temparr),2)))
                temparr3.append(round(sum(temparr)/len(temparr),2))
                informationText[i][1].insert(END, str(round(sum(temparr2)/tempvar,2)))
                temparr4.append(round(sum(temparr2)/tempvar,2))
                informationText[i][2].insert(END, percentToLevel(sum(temparr2)/tempvar))
                #informationText[i][2].insert(END, percentToLevel(tempvar/len(temparr)))
            except:
                #print("test")
                pass
        try:
            informationTopText[1][3].insert(END, str(round(sum(temparr3)/len(temparr3), 2)))
            informationTopText[1][2].insert(END, percentToLevel(round(sum(temparr3)/len(temparr3), 2)))
            informationTopText[1][1].insert(END, str(round(sum(temparr4)/len(temparr4), 2)))
        except:
            pass

    elif enteredText.lower() in "assignments":
        displayMode = 1
        informationTopText[2][0].insert(END, 'Assignment Name')
        informationTopText[2][1].insert(END, 'Average\nPercentage')
        informationTopText[2][2].insert(END, 'Mark Worth')

        informationTopText[0][0].insert(END, 'Assignments')
        informationTopText[0][1].insert(END, 'Overall Mark')
        informationTopText[0][2].insert(END, 'Overall Level')
        informationTopText[0][3].insert(END, 'Average Mark')

        for i in range(numOfAssigns):
            #printing names
            informationText[i][0].insert(END, pastInformation[1][i][0])
            informationText[i][2].insert(END, pastInformation[1][i][1])

        temparr2 = []
        for i in range(len(pastInformation[2][0])): #going down the list, changin student.
            tempvar = 0
            tempvar2 = 0
            temparr = []
            for i2 in range(len(pastInformation[2])):#going through the assignments
                #calculating average.
                
                try:
                    tempvar += float(pastInformation[2][i][i2][1])
                    temparr.append(float(pastInformation[2][i][i2][1]))
                    tempvar2 += float(pastInformation[2][i][i2][1])
                except:
                    pass

            try:
                informationText[i][1].insert(END, str(round(tempvar/len(temparr), 2)))
                temparr2.append(tempvar/len(temparr))
                #informationText[i][2].insert(END, percentToLevel(tempvar/len(temparr)))
            except:
                informationText[i][1].insert(END, "")
        try:
            informationTopText[1][3].insert(END, str(round(sum(temparr2)/len(temparr2), 2)))
        except:
            pass

        tempvar = 0
        tempvar2 = 0
        for i in range(numOfAssigns):
            try:
                tempvar2 += temparr2[i]*(float(pastInformation[1][i][1])/100)
                tempvar += float(pastInformation[1][i][1])/100
            except:
                pass
        try:
            informationTopText[1][1].insert(END, str(round(tempvar2/tempvar, 2)))
            informationTopText[1][2].insert(END, percentToLevel(round(tempvar2/tempvar, 2)))
        except:
            pass
    else: #searches for an assignment or student with the name inputted
        for searchint in range(numOfAssigns):
            if enteredText.lower() in pastInformation[0][searchint].lower():
                #student found
                informationTopText[2][0].insert(END, 'Assignment Name')
                informationTopText[2][1].insert(END, 'Mark Out of\na Number')
                informationTopText[2][2].insert(END, 'Mark\nPercentage')
                informationTopText[2][3].insert(END, 'Mark Worth')

                informationTopText[0][1].insert(END, 'Overall Mark')
                informationTopText[0][2].insert(END, 'Overall Level')
                informationTopText[0][3].insert(END, 'Average Mark')

                informationTopText[0][0].insert(END, pastInformation[0][searchint])

                for i in range(numOfAssigns):
                    informationText[i][0].insert(END, pastInformation[1][i][0])
                    informationText[i][3].insert(END, pastInformation[1][i][1])
                    informationText[i][1].insert(END, pastInformation[2][i][searchint][0])
                    if pastInformation[2][i][searchint][1] == "" and pastInformation[2][i][searchint][0] != "":
##                        try:
                        tempvar = pastInformation[2][i][searchint][0].split("/")
                        tempvar = round(float(tempvar[0])/float(tempvar[1])*100)
                        informationText[i][2].insert(END, str(tempvar))
                        pastInformation[2][i][searchint][1] = tempvar
##                        except:
##                            informationText[i][2].insert(END, "error")
                    else:
                        informationText[i][2].insert(END, pastInformation[2][i][searchint][1])

                tempvar = 0
                tempvar2 = 0
                temparr = []
                for i in range(numOfAssigns):
                    try:
                        tempvar += float(pastInformation[2][i][searchint][1])*(float(pastInformation[1][i][1])/100)
                        tempvar2 += float(pastInformation[1][i][1])/100
                        temparr.append(float(pastInformation[2][i][searchint][1]))
                    except:
                        pass
                
                try:
                    informationTopText[1][1].insert(END, str(round(tempvar/tempvar2,2)))
                    informationTopText[1][2].insert(END, percentToLevel(round(tempvar/tempvar2,2)))
                    informationTopText[1][3].insert(END, str(round(sum(temparr)/len(temparr),2)))
                except:
                    pass
                
                break
        
            if enteredText.lower() in pastInformation[1][searchint][0].lower():
                #assignment found
                informationTopText[2][0].insert(END, 'Student Name')
                informationTopText[2][1].insert(END, 'Mark Out of\na Number')
                informationTopText[2][2].insert(END, 'Mark\nPercentage')
                informationTopText[2][3].insert(END, 'Level')
                informationTopText[0][0].insert(END, pastInformation[1][searchint][0])
                informationTopText[0][2].insert(END, 'Average Mark')
                informationTopText[0][3].insert(END, 'Average Level')
                
                for i in range(numOfAssigns):
                    informationText[i][1].insert(END, pastInformation[2][searchint][i][0])
                    if pastInformation[2][searchint][i][1] == "" and pastInformation[2][searchint][i][0] != "":
                        try:
                            tempvar = pastInformation[2][searchint][i][0].split("/")
                            tempvar = round(float(tempvar[0])/float(tempvar[1])*100)
                            informationText[i][2].insert(END, str(tempvar))
                        except:
                            informationText[i][1].delete(0.0,END)
                            informationText[i][1].insert(END, "error")
                    else:
                        informationText[i][2].insert(END, pastInformation[2][searchint][i][1])

                    informationText[i][0].insert(END, pastInformation[0][i])
                save()
                for i in range(numOfAssigns):
                    try:
                        informationText[i][3].insert(END, percentToLevel(float(pastInformation[2][searchint][i][1]))) 
                    except:
                        pass
                #calculating average.
                tempvar = 0
                tempvar2 = 0
                for i in range(numOfAssigns):
                    try:
                        if int(pastInformation[2][searchint][i][1]) != 0:
                            tempvar += int(pastInformation[2][searchint][i][1])
                            tempvar2 += 1
                    except:
                        pass
                try:
                    informationTopText[1][2].insert(END, str(tempvar/tempvar2))
                    informationTopText[1][3].insert(END, percentToLevel(tempvar/tempvar2))
                except:
                    pass
                break

                
    
def exit_Button():
    save()
    window.destroy()

def save_Button():
    save()

def save():
    #print(saveName)
    for i in range(numOfAssigns):
##        print(informationTopText[0][0].get('1.0', END).replace("\n",""))
##        print(informationTopText[2][0].get('1.0', END).replace("\n",""))
##        print(informationTopText[2][0].get('1.0', END).replace("\n","") == 'Assignment Name', informationTopText[0][0].get('1.0', END).replace("\n","") == 'Assignments')
        if informationTopText[2][0].get('1.0', END).replace("\n","") == 'Assignment Name' and informationTopText[0][0].get('1.0', END).replace("\n","") == 'Assignments':
            pastInformation[1][i][0] = informationText[i][0].get('1.0', END).replace("\n","")
            pastInformation[1][i][1] = informationText[i][2].get('1.0', END).replace("\n","")
        elif informationTopText[2][0].get('1.0', END).replace("\n","") == 'Student Name' and informationTopText[0][0].get('1.0', END).replace("\n","") == 'Students':
            pastInformation[0][i] = informationText[i][0].get('1.0', END).replace("\n","")
        elif informationTopText[2][0].get('1.0', END).replace("\n","") == 'Student Name':
            for i2 in range(numOfAssigns):
                if informationTopText[0][0].get('1.0', END).replace("\n","") == pastInformation[1][i2][0]:
                    tempvar = i2
                    break
            try:
                pastInformation[2][tempvar][i][0] = informationText[i][1].get('1.0', END).replace("\n","")
                pastInformation[2][tempvar][i][1] = informationText[i][2].get('1.0', END).replace("\n","")
                pastInformation[0][i] = informationText[i][0].get('1.0', END).replace("\n","")
            except:
                pass
        elif informationTopText[2][0].get('1.0', END).replace("\n","") == 'Assignment Name':
            for i2 in range(numOfAssigns):
                if informationTopText[0][0].get('1.0', END).replace("\n","") == pastInformation[0][i2]:
                    tempvar = i2
                    break
            try:
                pastInformation[2][i][tempvar][0] = informationText[i][1].get('1.0', END).replace("\n","")
                pastInformation[2][i][tempvar][1] = informationText[i][2].get('1.0', END).replace("\n","")
            except:
                pass
    save = open(saveName+".txt", "w+")
    save.write(str(pastInformation))

def openSave(str1):
    try:
        if str1 in classesDirectory:
            pass
        else:
            for i in range(len(classesDirectory)):
                if str1 in classesDirectory[i]:
                    str1 = classesDirectory[i]
        with open(str1+".txt") as save:
            for i in save:
                global pastInformation
                global saveName
                pastInformation = eval(i)
                saveName = str1
                return pastInformation
    except FileNotFoundError:
        classesDirectory.remove(str1)
        pastInformation = newClassSave(str1)
        return pastInformation

def newClassSave(str1):
    if str1 == "":
        str1 = saveName
    pastInformation = [["" for i in range(numOfAssigns)],[["",""] for i in range(numOfAssigns)], [[["",""] for i in range(numOfAssigns)] for i2 in range(numOfAssigns)]]
    #print(pastInformation)
    save = open(str1+".txt", "w+")
    save.write(str(pastInformation))
    save.close()
    
    save = open(mainSaveName+".txt", "w+")
    classesDirectory.append(str1)
    save.write(str(classesDirectory))
    save.close()
    return pastInformation

def newClassDir():
    classesDirectory = [saveName]
    #print(pastInformation)
    save = open(mainSaveName+".txt", "w+")
    save.write(str(classesDirectory))
    return classesDirectory

def openClassDir():
    try:
        with open(mainSaveName+".txt") as save:
            for i in save:
                classesDirectory = eval(i)
                return classesDirectory
    except FileNotFoundError:
        classesDirectory = newClassDir()
        return classesDirectory

def commandSubmitButton():
    save()
    '''
    1. new class
    2. open class'''
    commandString = commandtext.get("1.0",END)
    if "new" in commandString.lower():
        newClassName = (commandString.split(" "))[1:]
        newClassName = " ".join(newClassName)
        newClassName = newClassName.replace("\n", "")
        #call create class function
        newClassSave(newClassName)
        #open the new save
        pastInformation = openSave(newClassName)
        #update home screen
        textEntry.delete(0.0, END)
        textEntry.insert(END, 'students')
        deleteAll()
        submitButton()
    elif "open" in commandString.lower():
        newClassName = (commandString.split(" "))[1:]
        newClassName = " ".join(newClassName)
        newClassName = newClassName.replace("\n", "")
        #find the class in the class directory
        pastInformation = openSave(newClassName)
        #update home screen
        textEntry.delete(0.0, END)
        textEntry.insert(END, 'students')
        deleteAll()
        submitButton()

    else:
        pass #change text in box to read could not recignize command
        commandtext.delete(0.0, END)
        commandtext.insert(END, "could not recignize command")

    

#command entry text 
commandtext = Text(window, width = 30, height = 1, bg = "white",
      fg = "black", font = "none 12 bold")
commandtext.grid(row=1,column=1,columnspan=3,sticky=W)
#search bar submit button
Button(window, text="Submit", width=10,
       command = commandSubmitButton).grid(row=2,column=1, sticky=W)

#pic1 = PhotoImage(file="test.png")
#Label(window, image=pic1, bg = "grey").grid(row = 0, column = 0, sticky=W)

#top label
Label(window, text="Please enter a value", bg = backgroudColour,
      fg = "white", font = "none 12 bold").grid(row=0,column=0,sticky=W)

#text entry
textEntry = Text(window, width=25, height = 1, bg="white", font="none 12 bold")
textEntry.grid(row=1,column=0,stick=W)

#submit button
Button(window, text="search/update", width=15,
       command = submitButton).grid(row=2,column=0, sticky=W)

#information quote
Label (window, text="\nInformation:", bg=backgroudColour, fg="white",
       font="none 12 bold").grid(row=3,column=0, sticky=W)

#information on creating/opening classes
Label (window, text="New/open <name> to create/open classes", bg=backgroudColour, fg="white",
       font="none 12 bold").grid(row=0,column=1, sticky=W, columnspan = 3)

#information top text (the top two rows)
for i in range(1,3):
    informationTopText[i][0] = Text(window, width = 30, height = 1*(i), bg = "white",
          fg = "black", font = "none 12 bold")
    informationTopText[i][0].grid(row=5+2*(i-1),column=0,sticky=W)
    for i2 in range(1,(boxes+1)):
        informationTopText[i][i2] = Text(window, width = 12, height = 1*(i),
            bg = "white", fg = "black", font = "none 12 bold")
        informationTopText[i][i2].grid(row = 5+2*(i-1), column = i2, sticky = W)

informationTopText[0][0] = Text(window, width = 30, height = 1, bg = "white",
      fg = "black", font = "none 12 bold")
informationTopText[0][0].grid(row=4,column=0,sticky=W)
for i2 in range(1,(boxes+1)):
    informationTopText[0][i2] = Text(window, width = 12, height = 1,
        bg = "white", fg = "black", font = "none 12 bold")
    informationTopText[0][i2].grid(row = 4, column = i2, sticky = W)

#information text
for i in range((numOfAssigns)):
    informationText[i][0] = Text(window, width = 30, height = 1, bg = "white",
          fg = "black", font = "none 12 bold")
    informationText[i][0].grid(row=8+i,column=0,sticky=W)
    for i2 in range(1,(boxes+1)):
        informationText[i][i2] = Text(window, width = 12, height = 1,
            bg = "white", fg = "black", font = "none 12 bold")
        informationText[i][i2].grid(row = 8+i, column = i2, sticky = W)

#save button
Button (window, text="Save", width=8,
        command=save_Button).grid(row=1,column=boxes+2,sticky=NW)

#exit button
Button (window, text="Save\nand exit", width=8,
        command=exit_Button).grid(row=0,column=boxes+2,sticky=NW)

#space around the edges and between stuff
Label(window, text=spaces(1,2), bg = backgroudColour,
      fg = "white", font = "none 12 bold").grid(row=100,column=0,sticky=W)

Label(window, text=spaces(1,0), bg = backgroudColour,
      fg = "white", font = "none 12 bold").grid(row=6,column=0,sticky=W)
##Label(window, text=spaces(2,20), bg = "grey",
##      fg = "white", font = "none 12 bold").grid(row=0,column=1,sticky=W)

classesDirectory = openClassDir()
global pastInformation
pastInformation = openSave(classesDirectory[0])

#pastInformation = new()


#opens the main menu thing
textEntry.delete(0.0, END)
textEntry.insert(END, 'students')
submitButton()

#run the program
window.mainloop()



































