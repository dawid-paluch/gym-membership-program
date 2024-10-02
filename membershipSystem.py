#imported modules
import csv
from csv import writer
import tkinter as tk
import tkinter.font as font
import functools
import datetime
from datetime import date
from tkinter import ttk

#function that will return the employee login information
#will return the information stored on csv file in the form of two lists (member & PIN)
def employeeInfo (nameNecessary):
    csvFile = open('employeeInfo.csv')
    info = (csvFile)
    employeeName = []
    employeePin = []
    for row in info:
        employee = row.strip().split(",")
        employeeName.append(employee[0])
        employeePin.append(employee[1])
    if nameNecessary:
        return(employeeName,employeePin)
    else:
        return(employeePin)

#function that will return the member information
#will return the information stored on csv file in the form of multiple lists
def memberInfo (justDetails):
    csvFile = open('memberInfo.csv')
    info = (csvFile)
    memberFName = []
    memberLName = []
    memberEmail = []
    memberNumber = []
    memberEmer1 = []
    memberEmer2 = []
    memberAddress = []
    membershipLevel = []
    expireyDate = []
    for row in info:
        employee = row.strip().split(",")
        memberFName.append(employee[0])
        memberLName.append(employee[1])
        memberEmail.append(employee[2])
        memberNumber.append(employee[3])
        memberEmer1.append(employee[4])
        memberEmer2.append(employee[5])
        memberAddress.append(employee[6])
        membershipLevel.append(employee[7])
        expireyDate.append(employee[8])
    if justDetails:
        return(memberFName,memberLName,memberEmail,memberNumber,memberEmer1,memberEmer2,memberAddress)
    else:
        return(memberFName,memberLName,membershipLevel,expireyDate)

#function to confirm whether the entered member name is valid
#will be used for adding new members or editing existing members
def newMemberNameValid(enteredFName,enteredLName):
    newInvalidText = ""
    fNameList, lNameList, emailList, numbersList, emer1List, emer2List, addressList = memberInfo(True)
    validMember = True    
    if enteredFName == "":
        validMember = False
        print("First name field is empty.")
        newInvalidText = "!INVALID FIRST NAME!\n!FIRST NAME FIELD IS EMPTY!"
    elif len(enteredFName) > 20:
        validMember = False
        print("First name is over 20 characters.")
        newInvalidText = "!INVALID FIRST NAME!\n!NAME IS TOO LONG!\n!OVER 20 CHARACTERS LONG!"
    elif enteredLName == "":
        validMember = False
        print("Last name field is empty.")
        newInvalidText = "!INVALID LAST NAME!\n!LAST NAME FIELD IS EMPTY!"
    elif len(enteredLName) > 20:
        validMember = False
        print("Last name is over 20 characters.")
        newInvalidText = "!INVALID LAST NAME!\n!NAME IS TOO LONG!\n!OVER 20 CHARACTERS LONG!"
    else:
        for name in range(0,len(fNameList)-1):
            if enteredFName+enteredLName == fNameList[name]+lNameList[name]:
                validMember = False
                print("New name is already in use.")
                newInvalidText = "!INVALID NAME!\n!NAME ALREADY IN USE!"
    return(validMember, newInvalidText)

#function to confirm whether the entered member email is valid
#will be used for adding new members or editing existing members
def newMemberEmailValid(enteredEmail):
    newInvalidText = ""
    fNameList, lNameList, emailList, numbersList, emer1List, emer2List, addressList = memberInfo(True)
    firstLocatedAt = enteredEmail.find("@")
    firstLocatedDot = enteredEmail.find(".",firstLocatedAt)
    validMember = True    
    if enteredEmail == "":
        validMember = False
        print("Email field is empty.")
        newInvalidText = "!INVALID EMAIL!\n!EMAIL FIELD IS EMPTY!"
    elif len(enteredEmail) > 35:
        validMember = False
        print("Email is over 35 characters.")
        newInvalidText = "!INVALID EMAIL!\n!EMAIL IS TOO LONG!\n!OVER 35 CHARACTERS LONG!"
    elif firstLocatedAt == -1:
        validMember = False
        print("Email is not in standard email format. Missing @ symbol")
        newInvalidText = "!INVALID EMAIL!\n!EMAIL NOT IN STANDARD FORMAT!\n!MISSING @ SYMBOL!"
    elif enteredEmail.find("@", firstLocatedAt+1) != -1:
        validMember = False
        print("Email is not in standard email format. Has multiple @ symbol.")
        newInvalidText = "!INVALID EMAIL!\n!EMAIL NOT IN STANDARD FORMAT!\n!HAS MULTIPLE @ SYMBOLS!"
    elif firstLocatedDot == -1:
        validMember = False
        print("Email ending doesn't have a dot.")
        newInvalidText = "!INVALID EMAIL!\n!EMAIL NOT IN STANDARD FORMAT!\n!ENDING OF EMAIL DOESN'T HAVE A DOT!"
    elif firstLocatedDot-firstLocatedAt == 1:
        validMember = False
        print("Email ending doesn't have anything between @ and dot.")
        newInvalidText = "!INVALID EMAIL!\n!EMAIL NOT IN STANDARD FORMAT!\n!EMAIL NEEDS TEXT BETWEEN @ AND DOT!"
    elif len(enteredEmail)-1==firstLocatedDot:
        validMember = False
        print("Email ending doesn't have anything after dot.")
        newInvalidText = "!INVALID EMAIL!\n!EMAIL NOT IN STANDARD FORMAT!\n!EMAIL NEEDS TEXT AFTER DOT!"
    else:
        for email in emailList:
            if enteredEmail == email:
                validMember = False
                print("Email is already in use.")
                newInvalidText = "!INVALID EMAIL!\n!EMAIL ALREADY IN USE!"
    return(validMember, newInvalidText)

#function to confirm whether the entered member number is valid
#will be used for adding new members or editing existing members
def newMemberPhoneNumberValid(enteredNumber):
    newInvalidText = ""
    fNameList, lNameList, emailList, numbersList, emer1List, emer2List, addressList = memberInfo(True)
    validMember = True    
    if enteredNumber == "":
        validMember = False
        print("Phone number field is empty.")
        newInvalidText = "!INVALID PHONE NUMBER!\n!NUMBER FIELD IS EMPTY!"
    elif not(enteredNumber.isnumeric()):
        validMember = False
        print("Phone number isn't numeric.")
        newInvalidText = "!INVALID PHONE NUMBER!\n!NUMBER FIELD DOES NOT\nCONTAIN JUST NUMBERS!"
    elif len(enteredNumber) != 11:
        validMember = False
        print("Phone number isn't 11 characters.")
        newInvalidText = "!INVALID PHONE NUMBER!\n!NUMBER IS NOT 11 CHARACTERS!\n!NUMBER SHOULD BE 11 CHARACTERS!"
    else:
        for number in numbersList:
            if enteredNumber == number:
                validMember = False
                print("Phone number is already in use.")
                newInvalidText = "!INVALID PHONE NUMBER!\n!PHONE NUMBER ALREADY IN USE!"
    return(validMember, newInvalidText)

#function to confirm whether the entered member emergency number is valid
#will be used for adding new members or editing existing members
def newMemberEmergencyNumbersValid(emer1, emer2):
    newInvalidText = ""
    fNameList, lNameList, emailList, numbersList, emer1List, emer2List, addressList = memberInfo(True)
    validMember = True    
    if emer1 == "":
        validMember = False
        print("Emergency phone number 1 field is empty.")
        newInvalidText = "!INVALID EMERGENCY NUMBER 1!\n!NUMBER FIELD IS EMPTY!"
    elif not(emer1.isnumeric()):
        validMember = False
        print("Emergency phone number isn't numeric.")
        newInvalidText = "!INVALID EMERGENCY NUMBER 1!\n!NUMBER FIELD DOES NOT CONTAIN JUST NUMBERS!"
    elif len(emer1) != 11:
        validMember = False
        print("Emergency phone number 1 isn't 11 characters.")
        newInvalidText = "!INVALID EMERGENCY NUMBER 1!\n!NUMBER IS NOT 11 CHARACTERS!\n!NUMBER SHOULD BE 11 CHARACTERS!"
    elif not(emer2.isnumeric()) and len(emer2) > 0:
        validMember = False
        print("Emergency phone number 2 isn't numeric.")
        newInvalidText = "!INVALID EMERGENCY NUMBER 2!\n!NUMBER FIELD DOES NOT CONTAIN JUST NUMBERS!"
    elif len(emer2) != 0 and len(emer2) != 11:
        validMember = False
        print("Emergency phone number 2 has been entered without 11 characters.")
        newInvalidText = "!INVALID EMERGENCY NUMBER 2!\n!NUMBER IS INCORRECT LENGTH!\n!PLEASE ENTER REST OR NOTHING!"
    return(validMember, newInvalidText)

#function to confirm valid pin
#compares given details to all valids PIN or one specific one if necessary
def validatePin(specificPin,enteredPin):
    userAuthorisation="invalid"
    validPins = employeeInfo(False)
    if specificPin == "none":
        if enteredPin == validPins[0]:
            userAuthorisation = "owner"
        else:
            for pin in validPins:
                if enteredPin == pin:
                    userAuthorisation = "employee"
    else:
        if enteredPin == specificPin:
            userAuthorisation = "valid"
    return(userAuthorisation)
        
#function to confirm whether the entered employee name is valid
#will be used for adding new employees or editing existing employees
def newNameValid(enteredName):
    newInvalidText = ""
    nameList,pinList = employeeInfo(True)
    validEmployee = True    
    if enteredName == "":
        validEmployee = False
        print("Name field is empty.")
        newInvalidText = "!INVALID NAME!\n!NAME FIELD IS EMPTY!"
    elif len(enteredName) > 12:
        validEmployee = False
        print("Name is over 12 characters.")
        newInvalidText = "!INVALID NAME!\n!NAME IS TOO LONG!\n!OVER 12 CHARACTERS LONG!"
    else:
        for name in nameList:
            if enteredName == name:
                validEmployee = False
                print("New name is already in use.")
                newInvalidText = "!INVALID NAME!\n!NAME ALREADY IN USE!"
    return(validEmployee, newInvalidText)

#function to confirm whether the entered pin is valid
#will be used for adding new employees or editing existing employees
def newPinValid(enteredPin):
    newInvalidText = ""
    nameList,pinList = employeeInfo(True)
    validEmployee = True    
    if enteredPin == "":
        validEmployee = False
        print("Pin field is empty.")
        newInvalidText = "!INVALID PIN!\n!PIN FIELD IS EMPTY!"
    elif not(enteredPin.isnumeric()):
        validEmployee = False
        print("PIN does not contain only numbers.")
        newInvalidText = "!INVALID PIN!\n!PIN DOES NOT CONTAIN JUST NUMBERS!"
    elif len(enteredPin)!= 5:
        validEmployee = False
        print("PIN is not 5 digits long.")
        newInvalidText = "!INVALID PIN!\n!PIN IS NOT 5 DIGITS!"
    else:
        for pin in pinList:
            if enteredPin == pin:
                validEmployee = False
                print("New PIN is already in use.")
                newInvalidText = "!INVALID PIN!\n!PIN ALREADY IN USE!"
    return(validEmployee, newInvalidText)

#function will delete a specific employee from the csv file once it has been confirmed for this to happen
def confirmedDeleteEmployee(employeeIndex, enteredName, enteredPin):
    employeeNames, employeePins = employeeInfo(True)
    del employeeNames[employeeIndex]
    del employeePins[employeeIndex]
    with open("employeeInfo.csv", mode="w", newline='') as csvFile:
        writerObject = writer(csvFile)
        for employee in range(len(employeeNames)):
            row = [employeeNames[employee], employeePins[employee]]
            writerObject.writerow(row)
    confirmDeleteEmployee.destroy()
    listEmployees(enteredName, enteredPin)
    print("Emplyee Successfully deleted.")

#function used when having confirmed the deletion of a certain member
def confirmedDeleteMember(memberIndex,specifiedDetail,enteredDetail):
    memberFName,memberLName,memberEmail,memberPhoneNo,memberEmer1,memberEmer2,memberAddress = memberInfo(True)
    membeFName,memberLName,memberMembLvl,memberExpiryDate = memberInfo(False)
    del memberFName[memberIndex]
    del memberLName[memberIndex]
    del memberEmail[memberIndex]
    del memberPhoneNo[memberIndex]
    del memberEmer1[memberIndex]
    del memberEmer2[memberIndex]
    del memberAddress[memberIndex]
    del memberMembLvl[memberIndex]
    del memberExpiryDate[memberIndex]
    with open("memberInfo.csv", mode="w", newline='') as csvFile:
        writerObject = writer(csvFile)
        for member in range(len(memberFName)):
            row = [memberFName[member],memberLName[member],memberEmail[member],memberPhoneNo[member],
                   memberEmer1[member],memberEmer2[member],memberAddress[member],
                   memberMembLvl[member],memberExpiryDate[member]]
            writerObject.writerow(row)
    confirmDeleteMember.destroy()
    listMembers(specifiedDetail, enteredDetail)
    print("Member Successfully deleted.")

#function linking login screen to pin validation
def compareLoginFromPin():
    global currentUserPin
    enteredPin = pinEntry.get()
    pinEntry.delete(0,tk.END)
    invalidPinLabel.forget()
    userAuthorisation = validatePin("none",enteredPin)
    if userAuthorisation == "employee":
        forgetAllWidgets()
        employeeMainMenu()
        currentUserPin = enteredPin
        print("Employee PIN entered")
    elif userAuthorisation == "owner":
        forgetAllWidgets()
        ownerMainMenu()
        currentUserPin = enteredPin
        print("Owner PIN entered")
    else:
        invalidPinLabel.pack(pady=80)
        print("Invalid PIN entered")
#this function will make sure that the entered PIN is valid
#it will run the corresponding function if the PIN is valid
def validPopupPin(specifiedFunction, enteredPin):
    loginPopupWindow.destroy()
    validPin = validatePin(currentUserPin,enteredPin)
    if validPin == "valid":
        if specifiedFunction == "addEmployee":
            addNewEmployee()
            print("User has correctly logged in to add employee.")
        elif specifiedFunction == "listEmployees":
            listEmployees("","")
            print("User has correctly logged in to list employees.")
        elif specifiedFunction == "changeOwnerPin":
            changeOwnerPin()
            print("User has correctly logged in to change the owner pin.")
        elif specifiedFunction == "addMember":
            addNewMember()
            print("User has correctly logged in to add member.")
        elif specifiedFunction == "listMembers":
            listMembers("none","none")
            print("User has correctly logged in to list members.")
        elif specifiedFunction == "listMemberships":
            listMemberships("none","none")
            print("User has correctly logged in to list memberships.")
    else:
        print("The user has entered the wrong PIN for logged in account.")
            
#function that results in closing of the application
def exitProgram():
    print("Exiting Program")
    root.destroy()

#function to forget all current widgets on the screen
def forgetAllWidgets():
    for widget in root.winfo_children():
        widget.forget()
        widget.place_forget()

#function for logging employee out of the system
def logOutOfSystem():
    forgetAllWidgets()
    initialLogin()
    print("Employee successfully logged out.")

#function to return to the owner main menu
def returnOwnerMenu():
    forgetAllWidgets()
    ownerMainMenu()

#function to return to the employee main menu
def returnEmployeeMenu():
    forgetAllWidgets()
    employeeMainMenu()

#function linked to the button that enters the details of a new member
#checks validity and saves/shows error depending on what the validity is
def addNewMemberEnter(enteredFName, enteredLName, enteredEmail, enteredNumber, enteredEmer1, enteredEmer2, enteredAddress):
    invalidNewMemberLabel.forget()
    enteredFName = enteredFName.replace(" ","")
    enteredLName = enteredLName.replace(" ","")
    enteredEmail = enteredEmail.replace(" ","")
    enteredNumber = enteredNumber.replace(" ","")
    enteredEmer1 = enteredEmer1.replace(" ","")
    enteredEmer2 = enteredEmer2.replace(" ","")
    enteredAddress = enteredAddress.replace(",","")
    newMemberValid, newInvalidText = newMemberNameValid(enteredFName,enteredLName)
    if newMemberValid:
        newMemberValid, newInvalidText = newMemberEmailValid(enteredEmail)
        if newMemberValid:
            newMemberValid, newInvalidText = newMemberPhoneNumberValid(enteredNumber)
            if newMemberValid:
                newMemberValid, newInvalidText = newMemberEmergencyNumbersValid(enteredEmer1, enteredEmer2)
    if newMemberValid:
        today = date.today().strftime("%d/%m/%y")
        with open('memberInfo.csv','a', newline='') as csvFile:
            writerObject = writer(csvFile)
            writerObject.writerow([enteredFName,enteredLName,enteredEmail,enteredNumber,enteredEmer1,enteredEmer2,enteredAddress,1,today])
        print("New member has been saved.")
        returnEmployeeMenu()
    else:
        invalidNewMemberLabel.config(text = newInvalidText)
        invalidNewMemberLabel.pack(pady=40)

#function linked to the button that enters the details of a new employee
#checks validity and saves/shows error depending on what the validity is
def addNewEmployeeEnter(enteredName, enteredPin):
    invalidNewEmployeeLabel.forget()
    enteredName = enteredName.replace(" ","")
    newEmployeeValid, newInvalidText = newNameValid(enteredName)
    if newEmployeeValid:
        newEmployeeValid, newInvalidText = newPinValid(enteredPin)
    if newEmployeeValid:
        with open('employeeInfo.csv','a', newline='') as csvFile:
            writerObject = writer(csvFile)
            writerObject.writerow([enteredName,enteredPin])
        print("New employee has been saved.")
        returnOwnerMenu()
    else:
        invalidNewEmployeeLabel.config(text = newInvalidText)
        invalidNewEmployeeLabel.pack(pady=80)

#function linked to enter button of modify employee button
def enterModifyEmployee(enteredName, enteredPin, employeeIndex, searchedName, searchedPin):
    invalidModifiedEmployeeLabel.forget()
    enteredName = enteredName.replace(" ","")
    employeeNames, employeePins = employeeInfo(True)
    employeeDetailsValid = True
    if enteredName != employeeNames[employeeIndex]:
        employeeDetailsValid, newInvalidText = newNameValid(enteredName)
    if employeeDetailsValid and enteredPin != employeePins[employeeIndex]:
        employeeDetailsValid, newInvalidText = newPinValid(enteredPin)
    if employeeDetailsValid:
        if not(enteredName == employeeNames[employeeIndex] and enteredPin == employeePins[employeeIndex]):
            employeeNames[employeeIndex] = enteredName
            employeePins[employeeIndex] = enteredPin
            with open("employeeInfo.csv", mode="w", newline='') as csvFile:
                writerObject = writer(csvFile)
                for employee in range(len(employeeNames)):
                    row = [employeeNames[employee], employeePins[employee]]
                    writerObject.writerow(row)
        modifyDetailsEmployee.destroy()
        listEmployees(searchedName, searchedPin)
        print("Modified employee details have been saved.")
    else:
        invalidModifiedEmployeeLabel.config(text = newInvalidText)
        invalidModifiedEmployeeLabel.config(bg="#e61e1e")
        invalidModifiedEmployeeLabel.grid(row=4, column=0, columnspan=2)

#function linked to the enter button for the change of the owner PIN
def changeOwnerPinEnter(enteredPin):
    global currentUserPin
    invalidChangedPinLabel.forget()
    newOwnerPinValid, newInvalidText = newPinValid(enteredPin)
    if newOwnerPinValid:
        employeeNames, employeePins = employeeInfo(True)
        employeePins[0] = enteredPin
        with open('employeeInfo.csv','w', newline='') as csvFile:
            writerObject = writer(csvFile)
            for employee in range(len(employeeNames)):
                row = [employeeNames[employee], employeePins[employee]]
                writerObject.writerow(row)
        changeOwnerPin()
        currentUserPin = enteredPin
        print("New owner PIN has been saved.")
    else:
        invalidChangedPinLabel.config(text = newInvalidText)
        invalidChangedPinLabel.pack(pady=80)

#function to change specfic detail for a member
def changeDetailEnter(changedDetail, newDetail, previousDetail, memberIndex):
    invalidModifiedMemberLabel.forget()
    memberFName,memberLName,memberEmail,memberNumber,memberEmer1,memberEmer2,memberAddress = memberInfo(True)
    memberFName,memberLName,membershipLevel,expiryDate = memberInfo(False)
    updated = [memberFName[memberIndex],memberLName[memberIndex],
               memberEmail[memberIndex],memberNumber[memberIndex],
               memberEmer1[memberIndex],memberEmer2[memberIndex],
               memberAddress[memberIndex]]
    if newDetail == previousDetail:
        modifyDetailsMember.destroy()
    elif changedDetail == "First Name":
        validMember, invalidMemberText = newMemberNameValid(newDetail,
                                                            memberLName[memberIndex])
        if validMember:
            memberFName[memberIndex] = newDetail
            updated[0] = newDetail
    elif changedDetail == "Last Name":
        validMember, invalidMemberText = newMemberNameValid(memberFName[memberIndex],
                                                            newDetail)
        if validMember:
            memberLName[memberIndex] = newDetail
            updated[1] = newDetail
    elif changedDetail == "Email":
        validMember, invalidMemberText = newMemberEmailValid(newDetail)
        if validMember:
            memberEmail[memberIndex] = newDetail
            updated[2] = newDetail
    elif changedDetail == "Phone No.":
        validMember, invalidMemberText = newMemberPhoneNumberValid(newDetail)
        if validMember:
            memberNumber[memberIndex] = newDetail
            updated[3] = newDetail
    elif changedDetail == "Emer No. 1":
        validMember, invalidMemberText = newMemberEmergencyNumbersValid(newDetail,
                                                                        memberEmer2[memberIndex])
        if validMember:
            memberEmer1[memberIndex] = newDetail
            updated[4] = newDetail
    elif changedDetail == "Emer No. 2":
        validMember, invalidMemberText = newMemberEmergencyNumbersValid(memberEmer1[memberIndex],
                                                                        newDetail)
        if validMember:
            memberEmer2[memberIndex] = newDetail
            updated[5] = newDetail
    else:
        validMember = True
        memberAddress[memberIndex] = newDetail
        updated[6] = newDetail
    if validMember:
        with open('memberInfo.csv','w', newline='') as csvFile:
            writerObject = writer(csvFile)
            for member in range (len(memberFName)):
                row = [memberFName[member],memberLName[member],memberEmail[member],
                       memberNumber[member],memberEmer1[member],memberEmer2[member],
                       memberAddress[member],membershipLevel[member],expiryDate[member]]
                writerObject.writerow(row)
        modifyDetailsMember.destroy()
        displayMemberDetails(updated[0],updated[1],updated[2],updated[3],
                             updated[4],updated[5],updated[6],searchedDetail,
                             enteredSearchedDetail,memberIndex)
    else:
        invalidModifiedMemberLabel.config(text = invalidMemberText)
        invalidModifiedMemberLabel.config(bg="#e61e1e")
        invalidModifiedEmployeeLabel.grid(row=4, column=0, columnspan=2)

#function for entering membership renewal info
def enterRenewMembership(memberIndex,newMembershipLevel,length,specifiedDetail, enteredDetail):
    if newMembershipLevel!="Choose Membership Level" and length!="Choose Membership Length":
        memberFName,memberLName,memberEmail,memberNumber,memberEmer1,memberEmer2,memberAddress = memberInfo(True)
        memberFName,memberLName,membershipLevel,expDate = memberInfo(False)
        today = date.today().strftime("%d/%m/%y")
        if length == "Day":
            date1 = datetime.datetime.strptime(today,"%d/%m/%y")
            date2 = date1 + datetime.timedelta(days=1)
            newExpDate = date2.strftime("%d/%m/%y")
        elif length == "Week":
            date1 = datetime.datetime.strptime(today,"%d/%m/%y")
            date2 = date1 + datetime.timedelta(days=7)
            newExpDate = date2.strftime("%d/%m/%y")
        elif length == "Month":
            date1 = datetime.datetime.strptime(today,"%d/%m/%y")
            date2 = date1 + datetime.timedelta(days=30)
            newExpDate = date2.strftime("%d/%m/%y")
        elif length == "Three Months":
            date1 = datetime.datetime.strptime(today,"%d/%m/%y")
            date2 = date1 + datetime.timedelta(days=90)
            newExpDate = date2.strftime("%d/%m/%y")
        membershipLevel[memberIndex] = newMembershipLevel
        expDate[memberIndex] = newExpDate
        with open('memberInfo.csv','w', newline='') as csvFile:
            writerObject = writer(csvFile)
            for member in range (len(memberFName)):
                row = [memberFName[member],memberLName[member],memberEmail[member],
                       memberNumber[member],memberEmer1[member],memberEmer2[member],
                       memberAddress[member],membershipLevel[member],expDate[member]]
                writerObject.writerow(row)
        renewMembership.destroy()
        listMemberships(specifiedDetail, enteredDetail)
        
        
        


#functions for tkinter gui design

#function for initial login screen
#creates the login screen, declaring all necessary widgets and placing them all correctly
def initialLogin():
    global initialLoginFrame
    global pinEntry
    global invalidPinLabel
    localEntryFont = font.Font(size=36, family="century gothic")
    localTitleFont = font.Font(size=50, family="century gothic",
                               underline=True, weight="bold")
    invalidLabelFont = font.Font(size=16, family="TkDefaultFont")
    initialLoginFrame = tk.Frame(root, bg=backgroundColour)
    initialLoginFrame.place(relx=0.5, rely=0.53, anchor="center")
    pinEntryFrame = tk.Frame(initialLoginFrame, bg=backgroundColour,
                             highlightbackground=foregroundColour,
                             highlightthickness=2)
    pinEntryFrame.grid(row=1, column=0)
    invalidPinLabel = tk.Label(
        root,
        text="!INVALID PIN!",
        height=3, width=20,
        fg="#000000", bg=redButtonColour)
    invalidPinLabel['font'] = invalidLabelFont
    pinTitleLabel = tk.Label(pinEntryFrame,text="Enter PIN:",
                             fg=foregroundColour, bg=backgroundColour)
    pinTitleLabel['font'] = localTitleFont
    pinTitleLabel.pack(padx=200, pady=(60,60))
    pinEntry = tk.Entry(pinEntryFrame,
                        fg=entryForegroundColour, bg=entryBackgroundColour, insertbackground="gray",
                        width=5,
                        show="*")
    pinEntry['font'] = localEntryFont
    pinEntry.pack()
    enterPinButton = tk.Button(
        pinEntryFrame,
        text="ENTER",
        bg=greenButtonColour,
        fg="#101010",
        width=10,
        height=2,
        command=compareLoginFromPin)
    enterPinButton['font'] = buttonFont
    enterPinButton.pack(pady=40)
    exitAppButton = tk.Button(
        initialLoginFrame,
        text="EXIT", bg=redButtonColour,
        fg="#101010", width=10,height=2,
        command=exitProgram)
    exitAppButton['font'] = buttonFont
    exitAppButton.grid(row=2, column=0, pady=40)

#function for owner main menu
#creates all necessary widgets and puts them into the window with buttons for each of the options that the owner should have
def ownerMainMenu():
    global ownerMenuFrame
    ownerMenuFrame = tk.Frame(root,
                              highlightbackground=foregroundColour,
                              highlightthickness=2,
                              bg=backgroundColour)
    ownerMenuFrame.place(relx=0.5, rely=0.5, anchor="center")
    ownerMainMenuLabel = tk.Label(
        ownerMenuFrame,
        text="Owner Main Menu",
        bg=backgroundColour,
        fg=foregroundColour)
    logOutButton = tk.Button(
        ownerMenuFrame,
        width=10, height=2,
        text="LOG OUT",
        bg=redButtonColour,
        fg="#101010",
        command=logOutOfSystem)
    addNewEmployeeButton = tk.Button(
        ownerMenuFrame,
        text="ADD NEW\nEMPLOYEE",
        width=17, height=3,
        bg="#994fe8",
        fg="#101010",
        command=lambda:userLoginPopup("addEmployee"))
    listEmployeesButton = tk.Button(
        ownerMenuFrame,
        text="LOOK AT A LIST\nOF EMPLOYEES",
        width=17, height=3,
        bg="#6d1dc2",
        fg="#101010",
        command=lambda:userLoginPopup("listEmployees"))
    changeOwnerPinButton = tk.Button(
        ownerMenuFrame,
        text="CHANGE\nOWNER PIN",
        width=17, height=3,
        bg="#544266",
        fg="#101010",
        command=lambda:userLoginPopup("changeOwnerPin"))
    logOutButton['font']=buttonFont
    ownerMainMenuLabel['font']=titleFont
    addNewEmployeeButton['font']=buttonFont
    listEmployeesButton ['font']=buttonFont
    changeOwnerPinButton ['font']=buttonFont
    ownerMainMenuLabel.grid(row=0, column=0, columnspan=3, pady=(80,50))
    addNewEmployeeButton.grid(row=1, column=0, padx=(80,30))
    listEmployeesButton.grid(row=1, column=1)
    changeOwnerPinButton.grid(row=1, column=2, padx=(30,80))
    logOutButton.grid(row=2, column=1, pady=(50,80), ipady=5, ipadx=5)

#function for adding a new employee to the system from the owner main menu
def addNewEmployee():
    global invalidNewEmployeeLabel
    forgetAllWidgets()
    addNewEmployeeFrame = tk.Frame(root, bg=backgroundColour,
                                   highlightbackground=foregroundColour,
                                   highlightthickness=2)
    addNewEmployeeFrame.place(relx=0.5, rely=0.5, anchor="center")
    innerNewEmployeeFrame = tk.Frame(addNewEmployeeFrame, bg=backgroundColour)
    
    invalidNewEmployeeLabel = tk.Label(
        root,
        text=" ",
        height=5, width=35,
        fg="#000000", bg="#e61e1e")
    newMemberTitleLabel = tk.Label(
        addNewEmployeeFrame, text="Add New Employee",
        bg=backgroundColour, fg=foregroundColour)
    newNameLabel = tk.Label(
        innerNewEmployeeFrame, text="Employee Name: ",
        bg=backgroundColour, fg=foregroundColour)
    newPinLabel = tk.Label(
        innerNewEmployeeFrame, text="New Employee PIN: ",
        bg=backgroundColour, fg=foregroundColour)
    newNameEntry = tk.Entry(
        innerNewEmployeeFrame, width=12,
        bg=entryBackgroundColour, fg=entryForegroundColour, insertbackground="gray")
    newPinEntry = tk.Entry(
        innerNewEmployeeFrame, width=12,
        bg=entryBackgroundColour, fg=entryForegroundColour, insertbackground="gray")
    enterNewEmployeeButton = tk.Button(
        addNewEmployeeFrame, text="ENTER", width=12,
        bg=greenButtonColour, fg="#101010",
        command=lambda: addNewEmployeeEnter((newNameEntry.get()).lower(),newPinEntry.get()))
    returnButton = tk.Button(
        addNewEmployeeFrame, text="RETURN", width=12,
        bg=redButtonColour, fg="#101010",
        command=returnOwnerMenu)
    newMemberTitleLabel['font'] = titleFont
    newNameLabel['font'] = labelFont
    newPinLabel['font'] = labelFont
    newNameEntry['font'] = entryFont
    newPinEntry['font'] = entryFont
    enterNewEmployeeButton['font'] = buttonFont
    returnButton['font'] = buttonFont
    newMemberTitleLabel.grid(row=0, column=0, padx=160,pady=(80,0))
    innerNewEmployeeFrame.grid(row=1, column=0, pady=20)
    newNameLabel.grid(row=0, column=0,pady=(40,0), padx=(30,0))
    newNameEntry.grid(row=0, column=1,pady=(40,0),padx=30)
    newPinLabel.grid(row=1, column=0, pady=(40,0), padx=(30,0))
    newPinEntry.grid(row=1, column=1, pady=(40,0),padx=30)
    enterNewEmployeeButton.grid(row=2, column=0, pady=(25,40))
    returnButton.grid(row=3, column=0, pady=(0,80))

#function to create the interface for the list of employees
#user should be able to modify user details and delete users
def listEmployees(enteredName, enteredPin):
    enteredPin.replace(" ","")
    enteredName.replace(" ","")
    forgetAllWidgets()
    localFont = font.Font(size=13, family="century gothic")
    listEmployeesFrame = tk.Frame(root, bg=backgroundColour,
                                  highlightbackground = foregroundColour,
                                  highlightthickness = 2)
    listEmployeesFrame.place(relx=0.5, rely=0.5, anchor="center")
    searchEmployeeFrame = tk.Frame(listEmployeesFrame, bg=backgroundColour)
    searchEmployeeNameLabel = tk.Label(searchEmployeeFrame,
                                       text="Search\nby Name",
                                       bg=backgroundColour,
                                       fg=foregroundColour)
    searchEmployeeNameEntry = tk.Entry(searchEmployeeFrame,
                                       width = 12,
                                       borderwidth=1, relief="solid",
                                       bg=entryBackgroundColour,
                                       fg=entryForegroundColour)
    searchEmployeeNameButton = tk.Button(searchEmployeeFrame,
                                         text="ENTER",
                                         bg=greenButtonColour,
                                         command=lambda:listEmployees((searchEmployeeNameEntry.get()).lower(), enteredPin))
    searchEmployeePinLabel = tk.Label(searchEmployeeFrame,
                                      text="Search\nby PIN",
                                      bg=backgroundColour,
                                      fg=foregroundColour)
    searchEmployeePinEntry = tk.Entry(searchEmployeeFrame,
                                      width = 12,
                                      borderwidth=1, relief="solid",
                                      bg=entryBackgroundColour,
                                      fg=entryForegroundColour)
    searchEmployeePinButton = tk.Button(searchEmployeeFrame,
                                         text="ENTER",
                                         bg=greenButtonColour,
                                         command=lambda:listEmployees(enteredName, searchEmployeePinEntry.get()))
    clearSearchButton = tk.Button(searchEmployeeFrame,
                                  text="CLEAR SEARCH",
                                  bg="#b83523",
                                  command=lambda:listEmployees("",""))
    employeeContainer = tk.Frame(listEmployeesFrame,borderwidth=1, relief="solid",
                                 bg=backgroundColour)
    employeeCanvas = tk.Canvas(employeeContainer, width=1000, height=400,
                               bg=backgroundColour)
    employeeScrollbar = tk.Scrollbar(employeeContainer,
                                     orient="vertical",
                                     command=employeeCanvas.yview,
                                     bg=backgroundColour)
    employeeScrollableFrame = tk.Frame(employeeCanvas, bg=backgroundColour)
    employeeScrollableFrame.bind(
        "<Configure>",
        lambda e: employeeCanvas.configure(
            scrollregion = employeeCanvas.bbox("all")))
    employeeCanvas.create_window((0,0), window=employeeScrollableFrame, anchor="nw")
    employeeCanvas.configure(yscrollcommand=employeeScrollbar.set)
    employeeNames,employeePins = employeeInfo(True)
    for employee in range(1,len(employeeNames)):
        if (enteredName == "" or enteredName in employeeNames[employee]) and (enteredPin == "" or enteredPin in employeePins[employee]):
            tempEmployeeFrame = tk.Frame(employeeScrollableFrame,
                                         bg=backgroundColour)
            tempEmployeeFrame.pack(pady=(0,20))
            tempNameLabel=tk.Label(tempEmployeeFrame,
                                   text=employeeNames[employee],
                                   width=12,
                                   bg=backgroundColour,
                                   fg=foregroundColour)
            tempPinLabel=tk.Label(tempEmployeeFrame,
                                  text=employeePins[employee],
                                  width=5,
                                  bg=backgroundColour,
                                  fg=foregroundColour)
            tempModifyButton=tk.Button(tempEmployeeFrame, text="MODIFY",
                                       bg="#34c3eb", fg="#101010",
                                       command=functools.partial(modifyEmployeePopup, employee, enteredName, enteredPin))
            tempDeleteButton=tk.Button(tempEmployeeFrame,
                                       text="DELETE",
                                       bg="#a23d29",
                                       fg="#101010",
                                       command=functools.partial(deleteEmployeePopup, employee, enteredName, enteredPin))
            tempNameLabel['font']=labelFont
            tempPinLabel['font']=labelFont
            tempModifyButton['font']=buttonFont
            tempDeleteButton['font']=buttonFont
            tempNameLabel.grid(row=0, column=0,padx=(0,150))
            tempPinLabel.grid(row=0, column=1)
            tempModifyButton.grid(row=0, column=2, padx=(145,40))
            tempDeleteButton.grid(row=0, column=3)
    tk.Label(employeeScrollableFrame, width=142, bg=backgroundColour).pack()
    listEmployeesTitleLabel = tk.Label(listEmployeesFrame,
                                       text="List Of Employees",
                                       bg=backgroundColour, fg=foregroundColour)
    listEmployeesTitleLabel['font'] = titleFont
    searchEmployeeNameLabel['font'] = localFont
    searchEmployeeNameEntry['font'] = localFont
    searchEmployeeNameButton['font'] = localFont
    searchEmployeePinLabel['font'] = localFont
    searchEmployeePinEntry['font'] = localFont
    searchEmployeePinButton['font'] = localFont
    clearSearchButton['font'] = localFont
    listEmployeesTitleLabel.pack(pady=(50,0))
    searchEmployeeFrame.pack(pady=(35,0))
    searchEmployeeNameLabel.grid(row=0, column=0, padx=(0,10))
    searchEmployeeNameEntry.grid(row=0, column=1, ipady=2, ipadx=1)
    searchEmployeeNameButton.grid(row=0, column=2, padx=(10,65))
    searchEmployeePinLabel.grid(row=0, column=3, padx=(0,10))
    searchEmployeePinEntry.grid(row=0, column=4, ipady=2, ipadx=2)
    searchEmployeePinButton.grid(row=0, column=5, padx=10)
    clearSearchButton.grid(row=0, column=6, padx=(218,0))
    employeeContainer.pack(padx=50, pady=(15,50))
    employeeCanvas.pack(side="left", fill="both", expand = True)
    employeeScrollbar.pack(side="right", fill="y")
    returnButton = tk.Button(listEmployeesFrame,
                             text="RETURN",
                             width=10, height=2,
                             bg=redButtonColour, fg="#101010",
                             command=returnOwnerMenu)
    returnButton['font']=buttonFont
    returnButton.pack(pady=(0,50))
    print("List of employees successfully shown.")

#function that creates the confirm delete employee pop up
#this will create the extra pop up window and link buttons to their corresponding functions
def deleteEmployeePopup(employeeIndex, enteredName, enteredPin):
    global confirmDeleteEmployee
    localLabelFont = font.Font(size=15, family="century gothic")
    localButtonFont = font.Font(size=12, family="century gothic", weight="bold")
    confirmDeleteEmployee = tk.Toplevel(bg=backgroundColour)
    confirmDeleteEmployee.wait_visibility()
    confirmDeleteEmployee.grab_set_global()
    employeeNames,employeePins = employeeInfo(True)
    labelBorderFrame = tk.Frame(
        confirmDeleteEmployee,
        bg=backgroundColour,
        highlightbackground=foregroundColour,
        highlightthickness=2)
    confirmDeleteEmployeeLabel = tk.Label(
        labelBorderFrame,
        text="Would you like to confirm that\nyou would like to delete "
        + employeeNames[employeeIndex].upper()+"?",
        width=31, bg=backgroundColour,
        fg=foregroundColour)
    cancelButton = tk.Button(confirmDeleteEmployee,
                             text="CANCEL",
                             width=12, height=2,
                             bg="#9fa0a1", fg="#101010",
                             command=confirmDeleteEmployee.destroy)
    confirmButton = tk.Button(confirmDeleteEmployee,
                              text="CONFIRM",
                              width=12, height=2,
                              bg="#a23d29", fg="#101010",
                              command=lambda: confirmedDeleteEmployee(employeeIndex, enteredName, enteredPin))
    confirmDeleteEmployeeLabel['font'] = localLabelFont
    cancelButton['font'] = localButtonFont
    confirmButton['font'] = localButtonFont
    labelBorderFrame.grid(row=0, column=0,
                                    columnspan=2,
                                    pady=(30,0), padx=30, ipadx=15, ipady=15)
    confirmDeleteEmployeeLabel.pack()
    cancelButton.grid(row=1, column=0, padx=(0,10))
    confirmButton.grid(row=1, column=1, pady=(20,30))

#function that creates the modify employee details pop up
#this will create the extra pop up window and link buttons to their corresponding functions
def modifyEmployeePopup(employeeIndex, enteredName, enteredPin):
    global modifyDetailsEmployee
    global invalidModifiedEmployeeLabel
    localLabelFont = font.Font(size=15, family="century gothic")
    localButtonFont = font.Font(size=12, family="century gothic", weight="bold")
    localEntryFont = font.Font(size=20, family="century gothic")
    localInvalidFont = font.Font(size=15, family="TkDefaultFont")
    modifyDetailsEmployee = tk.Toplevel(bg=backgroundColour)
    modifyDetailsEmployee.wait_visibility()
    modifyDetailsEmployee.grab_set_global()
    invalidModifiedEmployeeLabel = tk.Label(
        modifyDetailsEmployee,
        text=" ", width=34, height=3,
        bg=backgroundColour)
    employeeNames,employeePins = employeeInfo(True)
    labelBorderFrame = tk.Frame(
        modifyDetailsEmployee,
        bg=backgroundColour,
        highlightbackground=foregroundColour,
        highlightthickness=2)
    modifyDetailsEmployeeLabel = tk.Label(labelBorderFrame,
        text="Modify Details for\n" + employeeNames[employeeIndex].upper(),
        width=31, bg=backgroundColour, fg=foregroundColour)
    modifiedEmployeeNameLabel = tk.Label(
        modifyDetailsEmployee,text="New Employee Name:",
        bg=backgroundColour, fg=foregroundColour)
    modifiedEmployeePinLabel = tk.Label(
        modifyDetailsEmployee,text="New Employee PIN:",
        bg=backgroundColour, fg=foregroundColour)
    modifiedEmployeeNameEntry = tk.Entry(
        modifyDetailsEmployee,
        width=12, bg=entryBackgroundColour, fg=entryForegroundColour, insertbackground=("gray"))
    modifiedEmployeePinEntry = tk.Entry(
        modifyDetailsEmployee,
        width=12, bg=entryBackgroundColour, fg=entryForegroundColour, insertbackground=("gray"))
    cancelButton = tk.Button(modifyDetailsEmployee, text="CANCEL", width=12, height=2,
                             bg=redButtonColour, fg="#101010",
                             command=modifyDetailsEmployee.destroy)
    enterButton = tk.Button(modifyDetailsEmployee, text="ENTER", width=12, height=2,
                              bg=greenButtonColour, fg="#101010",
                              command=lambda: enterModifyEmployee(
                                  (modifiedEmployeeNameEntry.get()).lower(),
                                  modifiedEmployeePinEntry.get(), employeeIndex, enteredName, enteredPin))
    modifiedEmployeeNameLabel['font'] = localLabelFont
    modifiedEmployeePinLabel['font'] = localLabelFont
    modifiedEmployeeNameEntry['font'] = localEntryFont
    modifiedEmployeePinEntry['font'] = localEntryFont
    modifyDetailsEmployeeLabel['font'] = localLabelFont
    cancelButton['font'] = localButtonFont
    enterButton['font'] = localButtonFont
    invalidModifiedEmployeeLabel['font'] = localInvalidFont
    labelBorderFrame.grid(row=0, column=0,columnspan=2,
                                    pady=(30,0), ipadx=15, ipady=15)
    modifyDetailsEmployeeLabel.pack()
    modifiedEmployeeNameLabel.grid(row=1, column=0, padx=(50,20))
    modifiedEmployeePinLabel.grid(row=2, column=0, padx=20)
    modifiedEmployeeNameEntry.grid(row=1, column=1, pady=15, padx=(0,50), ipady=4, ipadx=4)
    modifiedEmployeePinEntry.grid(row=2, column=1, pady=(0,15), padx=(0,50),
                                  ipady=4, ipadx=4)
    cancelButton.grid(row=3, column=0, padx=(0,10))
    enterButton.grid(row=3, column=1, pady=(20,30))
    invalidModifiedEmployeeLabel.grid(row=4, column=0, columnspan=2)

#function to create the interface for changing the owners pin
#will declare each of the widgets and make sure that all of them work as well
def changeOwnerPin():
    global invalidChangedPinLabel
    localTitleFont = font.Font(size=35, family="century gothic",
                               underline=True, weight="bold")
    employeePins = employeeInfo(False)
    forgetAllWidgets()
    changeOwnerPinFrame = tk.Frame(root, bg=backgroundColour,
                                   highlightbackground=foregroundColour,
                                   highlightthickness=2)
    changeOwnerPinFrame.place(relx=0.5, rely=0.5, anchor="center")
    innerFrame = tk.Frame(changeOwnerPinFrame, bg=backgroundColour)
    invalidChangedPinLabel = tk.Label(
        root, text=" ",
        height=5, width=35,
        fg="#000000", bg="#e61e1e")
    changeOwnerPinTitleLabel = tk.Label(
        changeOwnerPinFrame, text="Change Owner PIN",
        bg=backgroundColour, fg=foregroundColour)
    currentPinLabel = tk.Label(
        changeOwnerPinFrame, text="The current PIN is: "+employeePins[0],
        bg=backgroundColour, fg=foregroundColour)
    newPinLabel = tk.Label(
        innerFrame, text="New PIN: ",
        bg=backgroundColour, fg=foregroundColour)
    newPinEntry = tk.Entry(
        innerFrame, width=5,
        bg=entryBackgroundColour, fg=entryForegroundColour, insertbackground="gray")
    returnButton = tk.Button(changeOwnerPinFrame,
                             text="RETURN", width=8,
                             bg=redButtonColour, fg="#101010",
                             command=returnOwnerMenu)
    enterButton = tk.Button(changeOwnerPinFrame,
                            text="ENTER", width=8,
                            bg=greenButtonColour, fg="#101010",
                            command=lambda: changeOwnerPinEnter(newPinEntry.get()))
    changeOwnerPinTitleLabel['font']=titleFont
    currentPinLabel['font']=labelFont
    newPinLabel['font']=labelFont
    newPinEntry['font']=entryFont
    returnButton['font']=buttonFont
    enterButton['font']=buttonFont
    changeOwnerPinTitleLabel.grid(row=0, column=0, columnspan=2, pady=(50,0))
    currentPinLabel.grid(row=1, column=0, columnspan=2, pady=30)
    innerFrame.grid(row=2, column=0, columnspan=2)
    newPinLabel.grid(row=0, column=0, padx=5, ipadx=5, ipady=2)
    newPinEntry.grid(row=0, column=1, padx=3, ipadx=5, ipady=2)
    returnButton.grid(row=3, column=0, padx=100, ipadx=5, ipady=5)
    enterButton.grid(row=3, column=1, padx=100, pady=(40,50), ipadx=5, ipady=5)

#function that creates the login pop up
#this will be used to confirm that the user attempting to do something has the 
def userLoginPopup(specifiedFunction):
    global loginPopupWindow
    localLabelFont = font.Font(size=15, family="century gothic")
    localButtonFont = font.Font(size=12, family="century gothic", weight="bold")
    loginPopupWindow = tk.Toplevel(bg=backgroundColour)
    loginPopupWindow.wait_visibility()
    loginPopupWindow.grab_set_global()
    employeeNames,employeePins = employeeInfo(True)
    labelBorderFrame = tk.Frame(
        loginPopupWindow,
        bg=backgroundColour,
        highlightbackground=foregroundColour,
        highlightthickness=2)
    tellUserToLoginLabel = tk.Label(
        labelBorderFrame,
        text="Please enter\nyour PIN:",
        width=31,
        bg=backgroundColour, fg=foregroundColour)
    enterYourPinLabel = tk.Label(loginPopupWindow,
                                 text="PIN: ",
                                 bg=backgroundColour, fg=foregroundColour,
                                 width=6)
    enterYourPinEntry = tk.Entry(loginPopupWindow,
                                 width=5,
                                 bg=entryBackgroundColour,
                                 fg=entryForegroundColour, insertbackground="gray",
                                 show="*")
    cancelButton = tk.Button(loginPopupWindow,
                             text="CANCEL",
                             width=12, height=2,
                             bg=redButtonColour, fg="#101010",
                             command=loginPopupWindow.destroy)
    confirmButton = tk.Button(loginPopupWindow,
                              text="CONFIRM",
                              width=12, height=2,
                              bg=greenButtonColour, fg="#101010",
                              command=lambda:validPopupPin(specifiedFunction, enterYourPinEntry.get()))
    tellUserToLoginLabel['font'] = localLabelFont
    enterYourPinLabel['font'] = labelFont
    enterYourPinEntry['font'] = entryFont
    cancelButton['font'] = localButtonFont
    confirmButton['font'] = localButtonFont
    labelBorderFrame.grid(row=0, column=0,
                                    columnspan=2,
                                    pady=(30,0), padx=30, ipadx=15, ipady=15)
    tellUserToLoginLabel.pack()
    enterYourPinLabel.grid(row=1, column=0, pady=20)
    enterYourPinEntry.grid(row=1, column=1, pady=20)
    cancelButton.grid(row=2, column=0, padx=(0,10), pady=(0,30))
    confirmButton.grid(row=2, column=1, pady=(0,30))

#function for normal employee main menu
#creates all necessary widgets and puts them into the window with buttons for each of the options that the employee should have
def employeeMainMenu():
    employeeMenuFrame = tk.Frame(root, bg=backgroundColour,
                                 highlightbackground=foregroundColour,
                                 highlightthickness=2)
    employeeMenuFrame.place(relx=0.5,rely=0.5,anchor="center")
    employeeMainMenuLabel = tk.Label(
        employeeMenuFrame,
        text="Employee Main Menu",
        bg=backgroundColour, fg=foregroundColour)
    addNewMemberButton = tk.Button(
        employeeMenuFrame,
        text="ADD NEW\nMEMBER",
        width=17, height = 3,
        bg="#40bfe6",fg="#101010",
        command=lambda: userLoginPopup("addMember"))
    listMembersButton = tk.Button(
        employeeMenuFrame,
        text="LIST OF\nMEMBERS",
        width=17, height = 3,
        bg="#375cb3",fg="#101010",
        command=lambda:userLoginPopup("listMembers"))
    membershipButton = tk.Button(
        employeeMenuFrame,
        text="LIST OF\nMEMBERSHIPS",
        width=17, height = 3,
        bg="#69f5cd",fg="#101010",
        command=lambda:userLoginPopup("listMemberships"))
    logOutButton = tk.Button(
        employeeMenuFrame,
        text="LOG OUT",
        width=10, height=2,
        bg=redButtonColour,fg="#101010",
        command=logOutOfSystem)
    employeeMainMenuLabel['font']=titleFont
    addNewMemberButton['font']=buttonFont
    listMembersButton['font']=buttonFont
    membershipButton['font']=buttonFont
    logOutButton['font']=buttonFont
    employeeMainMenuLabel.grid(row=0,column=0,columnspan=3,pady=(80,50))
    addNewMemberButton.grid(row=1,column=0,padx=(80,0),pady=(0,40))
    listMembersButton.grid(row=1,column=1,padx=50,pady=(0,40))
    membershipButton.grid(row=1,column=2,padx=(0,80),pady=(0,40))
    logOutButton.grid(row=2,column=1,pady=(0,80))

#function for the add new employee interface
#creates all necessary widget and loads them in so user can add a new member or return to main menu
def addNewMember():
    global invalidNewMemberLabel
    customTitleFont = font.Font(size=30, family="century gothic", underline=True, weight="bold")
    customLabelFont = font.Font(size=15, family="century gothic")
    customEntryFont = font.Font(size=18, family="century gothic")
    forgetAllWidgets()
    addNewMemberFrame = tk.Frame(root, bg=backgroundColour,
                                 highlightbackground=foregroundColour,
                                 highlightthickness=2)
    addNewMemberFrame.place(relx=0.5, rely=0.5, anchor="center")
    innerNewMemberFrame = tk.Frame(addNewMemberFrame, bg=backgroundColour)
    invalidNewMemberLabel = tk.Label(
        root,
        text=" ",
        height=5, width=45,
        fg="#000000", bg="#e61e1e")
    newMemberTitleLabel = tk.Label(
        addNewMemberFrame, text="Add New Member",
        bg=backgroundColour, fg=foregroundColour)
    newFirstNameLabel = tk.Label(
        innerNewMemberFrame, text="First Name: ",
        bg=backgroundColour, fg=foregroundColour)
    newLastNameLabel = tk.Label(
        innerNewMemberFrame, text="Last Name: ",
        bg=backgroundColour, fg=foregroundColour)
    newEmailLabel = tk.Label(
        innerNewMemberFrame, text="Email: ",
        bg=backgroundColour, fg=foregroundColour)
    newPhoneNoLabel = tk.Label(
        innerNewMemberFrame, text="Phone Number: ",
        bg=backgroundColour, fg=foregroundColour)
    newEmergencyNo1Label = tk.Label(
        innerNewMemberFrame, text="Emergency No. 1: ",
        bg=backgroundColour, fg=foregroundColour)
    newEmergencyNo2Label = tk.Label(
        innerNewMemberFrame, text="Emergency No. 2: ",
        bg=backgroundColour, fg=foregroundColour)
    newAddressLabel = tk.Label(
        innerNewMemberFrame, text="Address: ",
        bg=backgroundColour, fg=foregroundColour)
    newFirstNameEntry = tk.Entry(
        innerNewMemberFrame, width=15,
        bg=entryBackgroundColour, fg=entryForegroundColour, insertbackground="gray")
    newLastNameEntry = tk.Entry(
        innerNewMemberFrame, width=15,
        bg=entryBackgroundColour, fg=entryForegroundColour, insertbackground="gray")
    newEmailEntry = tk.Entry(
        innerNewMemberFrame, width=24,
        bg=entryBackgroundColour, fg=entryForegroundColour, insertbackground="gray")
    newPhoneNoEntry = tk.Entry(
        innerNewMemberFrame, width=24,
        bg=entryBackgroundColour, fg=entryForegroundColour, insertbackground="gray")
    newEmergencyNo1Entry = tk.Entry(
        innerNewMemberFrame, width=20,
        bg=entryBackgroundColour, fg=entryForegroundColour, insertbackground="gray")
    newEmergencyNo2Entry = tk.Entry(
        innerNewMemberFrame, width=20,
        bg=entryBackgroundColour, fg=entryForegroundColour, insertbackground="gray")
    newAddressText = tk.Text(
        innerNewMemberFrame, width=30, height=4, wrap="word",
        bg=entryBackgroundColour, fg=entryForegroundColour, insertbackground="gray")
    enterNewMemberButton = tk.Button(
        innerNewMemberFrame, text="ENTER", width=12,
        bg=greenButtonColour, fg="#101010",
        command=lambda: addNewMemberEnter((newFirstNameEntry.get()).lower(),
                                          (newLastNameEntry.get()).lower(),
                                          (newEmailEntry.get()).lower(),
                                          (newPhoneNoEntry.get()).lower(),
                                          (newEmergencyNo1Entry.get()).lower(),
                                          (newEmergencyNo2Entry.get()).lower(),
                                          (newAddressText.get("1.0","end-1c")).lower()))
    returnButton = tk.Button(
        innerNewMemberFrame, text="RETURN", width=12,
        bg=redButtonColour, fg="#101010",
        command=returnEmployeeMenu)
    newMemberTitleLabel['font'] = customTitleFont
    newFirstNameLabel['font'] = customLabelFont
    newLastNameLabel['font'] = customLabelFont
    newEmailLabel['font'] = customLabelFont
    newPhoneNoLabel['font'] = customLabelFont
    newEmergencyNo1Label['font'] = customLabelFont
    newEmergencyNo2Label['font'] = customLabelFont
    newAddressLabel['font'] = customLabelFont
    newFirstNameEntry['font'] = customEntryFont
    newLastNameEntry['font'] = customEntryFont
    newEmailEntry['font'] = customEntryFont
    newPhoneNoEntry['font'] = customEntryFont
    newEmergencyNo1Entry['font'] = customEntryFont
    newEmergencyNo2Entry['font'] = customEntryFont
    newAddressText['font'] = customEntryFont
    enterNewMemberButton['font'] = buttonFont
    returnButton['font'] = buttonFont
    newMemberTitleLabel.grid(row=0, column=0,pady=(60,0))
    innerNewMemberFrame.grid(row=1, column=0, pady=5)
    newFirstNameLabel.grid(row=0, column=0,pady=25, padx=(20,0))
    newLastNameLabel.grid(row=1, column=0,pady=25, padx=(20,0))
    newEmailLabel.grid(row=0, column=2,pady=25, padx=(10,0))
    newPhoneNoLabel.grid(row=1, column=2,pady=25, padx=(10,0))
    newEmergencyNo1Label.grid(row=0, column=4,pady=25, padx=(5,0))
    newEmergencyNo2Label.grid(row=1, column=4,pady=25, padx=(5,0))
    newAddressLabel.grid(row=2, column=0, pady=30)
    newFirstNameEntry.grid(row=0, column=1,pady=25,padx=5)
    newLastNameEntry.grid(row=1, column=1,pady=25,padx=5)
    newEmailEntry.grid(row=0, column=3,pady=25,padx=5)
    newPhoneNoEntry.grid(row=1, column=3,pady=25,padx=5)
    newEmergencyNo1Entry.grid(row=0, column=5,pady=25,padx=(5,20))
    newEmergencyNo2Entry.grid(row=1, column=5,pady=25,padx=(5,20))
    newAddressText.grid(row=2, column=1, columnspan=2, pady=(30,60),padx=5)
    enterNewMemberButton.grid(row=2, column=3, columnspan=2, pady=(30,60))
    returnButton.grid(row=2, column=4, columnspan=2, pady=(30,60))


#function to create the interface for the list of members
def listMembers(specifiedDetail, enteredDetail):
    forgetAllWidgets()
    localFont = font.Font(size=11, family="century gothic")
    listMembersFrame = tk.Frame(root, bg=backgroundColour,
                                highlightbackground=foregroundColour,
                                highlightthickness=2)
    listMembersFrame.place(relx=0.5, rely=0.5, anchor="center")
    searchMembersFrame = tk.Frame(listMembersFrame, bg=backgroundColour)
    searchMembersFNameLabel = tk.Label(searchMembersFrame,
                                       text="Search by\nFirst Name",
                                       bg=backgroundColour, fg=foregroundColour)
    searchMembersFNameEntry = tk.Entry(searchMembersFrame,
                                       width = 12,
                                       borderwidth=1, relief="solid",
                                       bg=entryBackgroundColour,
                                       fg=entryForegroundColour)
    searchMembersFNameButton = tk.Button(searchMembersFrame,
                                         text="ENTER",
                                         bg="#42d458",
                                         command=lambda:listMembers("fname",
                                                                    searchMembersFNameEntry.get().lower()))
    searchMembersLNameLabel = tk.Label(searchMembersFrame,
                                      text="Search by\nLast Name",
                                      bg=backgroundColour, fg=foregroundColour)
    searchMembersLNameEntry = tk.Entry(searchMembersFrame,
                                      width = 12,
                                      borderwidth=1, relief="solid",
                                       bg=entryBackgroundColour,
                                       fg=entryForegroundColour)
    searchMembersLNameButton = tk.Button(searchMembersFrame,
                                         text="ENTER",
                                         bg="#42d458",
                                         command=lambda:listMembers("lname",
                                                                    searchMembersLNameEntry.get().lower()))
    searchMembersEmailLabel = tk.Label(searchMembersFrame,
                                       text="Search\nby Email",
                                       bg=backgroundColour, fg=foregroundColour)
    searchMembersEmailEntry = tk.Entry(searchMembersFrame,
                                       width = 12,
                                       borderwidth=1, relief="solid",
                                       bg=entryBackgroundColour,
                                       fg=entryForegroundColour)
    searchMembersEmailButton = tk.Button(searchMembersFrame,
                                         text="ENTER",
                                         bg="#42d458",
                                         command=lambda:listMembers("email",
                                                                    searchMembersEmailEntry.get().lower()))
    searchMembersPhoneNoLabel = tk.Label(searchMembersFrame,
                                       text="Search by\nPhone No.",
                                       bg=backgroundColour, fg=foregroundColour)
    searchMembersPhoneNoEntry = tk.Entry(searchMembersFrame,
                                       width = 12,
                                       borderwidth=1, relief="solid",
                                       bg=entryBackgroundColour,
                                       fg=entryForegroundColour)
    searchMembersPhoneNoButton = tk.Button(searchMembersFrame,
                                         text="ENTER",
                                         bg="#42d458",
                                         command=lambda:listMembers("phoneNo",
                                                                    searchMembersPhoneNoEntry.get().lower()))
    searchMembersEmerNoLabel = tk.Label(searchMembersFrame,
                                       text="Search by\nEmergency No.",
                                       bg=backgroundColour, fg=foregroundColour)
    searchMembersEmerNoEntry = tk.Entry(searchMembersFrame,
                                       width = 12,
                                       borderwidth=1, relief="solid",
                                       bg=entryBackgroundColour,
                                       fg=entryForegroundColour)
    searchMembersEmerNoButton = tk.Button(searchMembersFrame,
                                         text="ENTER",
                                         bg="#42d458",
                                         command=lambda:listMembers("emerNo",
                                                                    searchMembersEmerNoEntry.get().lower()))
    searchMembersAddressLabel = tk.Label(searchMembersFrame,
                                       text="Search by\nAddress",
                                       bg=backgroundColour, fg=foregroundColour)
    searchMembersAddressEntry = tk.Entry(searchMembersFrame,
                                       width = 12,
                                       borderwidth=1, relief="solid",
                                       bg=entryBackgroundColour,
                                       fg=entryForegroundColour)
    searchMembersAddressButton = tk.Button(searchMembersFrame,
                                         text="ENTER",
                                         bg="#42d458",
                                         command=lambda:listMembers("address",
                                                                    searchMembersAddressEntry.get().lower()))
    clearSearchButton = tk.Button(searchMembersFrame,
                                  text="CLEAR SEARCH",
                                  bg="#b83523",
                                  command=lambda:listMembers("none",""))
    membersContainer = tk.Frame(listMembersFrame,borderwidth=1, relief="solid",
                                bg=backgroundColour)
    membersCanvas = tk.Canvas(membersContainer, width=955, height=400,
                              bg=backgroundColour)
    membersScrollbar = tk.Scrollbar(membersContainer,
                                    orient="vertical",
                                    command=membersCanvas.yview,
                                    bg=backgroundColour)
    membersScrollableFrame = tk.Frame(membersCanvas,bg=backgroundColour)
    membersScrollableFrame.bind(
        "<Configure>",
        lambda e: membersCanvas.configure(
            scrollregion = membersCanvas.bbox("all")))
    membersCanvas.create_window((0,0), window=membersScrollableFrame, anchor="nw")
    membersCanvas.configure(yscrollcommand=membersScrollbar.set)
    memberFName,memberLName,memberEmail,memberNumber,memberEmer1,memberEmer2,memberAddress = memberInfo(True)
    for member in range(0,len(memberFName)):
        memberIsValid = False
        if specifiedDetail == "none":
            memberIsValid = True
        elif specifiedDetail == "fname" and enteredDetail in memberFName[member]:
            memberIsValid = True
        elif specifiedDetail == "lname" and enteredDetail in memberLName[member]:
            memberIsValid = True
        elif specifiedDetail == "email" and enteredDetail in memberEmail[member]:
            memberIsValid = True
        elif specifiedDetail == "phoneNo" and enteredDetail in memberNumber[member]:
            memberIsValid = True
        elif specifiedDetail == "emerNo" and (enteredDetail in memberEmer1[member]
                                               or enteredDetail in memberEmer2[member]):
            memberIsValid = True
        elif specifiedDetail == "address" and enteredDetail in memberAddress[member]:
            memberIsValid = True
        if memberIsValid:
            tempMembersFrame = tk.Frame(membersScrollableFrame, bg=backgroundColour)
            tempMembersFrame.pack(pady=(0,10))
            tempFNameLabel=tk.Label(tempMembersFrame,
                                   text=memberFName[member],
                                   width=20,
                                    bg=backgroundColour, fg=foregroundColour)
            tempLNameLabel=tk.Label(tempMembersFrame,
                                  text=memberLName[member],
                                  width=20,
                                    bg=backgroundColour, fg=foregroundColour)
            tempDeleteButton=tk.Button(tempMembersFrame, text="DELETE",
                                       bg="#a60907", fg="#101010",
                                       command=functools.partial(deleteMemberPopup,
                                                                 member,
                                                                 specifiedDetail,
                                                                 enteredDetail))
            tempDetailsButton=tk.Button(tempMembersFrame, text="CHECK DETAILS",
                                       bg="#4e49d1", fg="#101010",
                                       command=functools.partial(displayMemberDetails,
                                                                 memberFName[member],
                                                                 memberLName[member],
                                                                 memberEmail[member],
                                                                 memberNumber[member],
                                                                 memberEmer1[member],
                                                                 memberEmer2[member],
                                                                 memberAddress[member],
                                                                 specifiedDetail,
                                                                 enteredDetail,
                                                                 member))
            tempFNameLabel['font']=smallLabelFont
            tempLNameLabel['font']=smallLabelFont
            tempDeleteButton['font']=buttonFont
            tempDetailsButton['font']=buttonFont
            tempFNameLabel.grid(row=0, column=0, padx=5)
            tempLNameLabel.grid(row=0, column=1, padx=(0,5))
            tempDeleteButton.grid(row=0, column=2, padx=(0,8))
            tempDetailsButton.grid(row=0, column=3, padx=(0,8))
    tk.Label(membersScrollableFrame, width=10, bg=backgroundColour).pack()
    listMembersTitleLabel = tk.Label(listMembersFrame, text="List Of Members",
                                     bg=backgroundColour, fg=foregroundColour)
    listMembersTitleLabel['font'] = titleFont
    searchMembersFNameLabel['font'] = localFont
    searchMembersFNameEntry['font'] = localFont
    searchMembersFNameButton['font'] = localFont
    searchMembersLNameLabel['font'] = localFont
    searchMembersLNameEntry['font'] = localFont
    searchMembersLNameButton['font'] = localFont
    searchMembersEmailLabel['font'] = localFont
    searchMembersEmailEntry['font'] = localFont
    searchMembersEmailButton['font'] = localFont
    searchMembersPhoneNoLabel['font'] = localFont
    searchMembersPhoneNoEntry['font'] = localFont
    searchMembersPhoneNoButton['font'] = localFont
    searchMembersEmerNoLabel['font'] = localFont
    searchMembersEmerNoEntry['font'] = localFont
    searchMembersEmerNoButton['font'] = localFont
    searchMembersAddressLabel['font'] = localFont
    searchMembersAddressEntry['font'] = localFont
    searchMembersAddressButton['font'] = localFont
    clearSearchButton['font'] = localFont
    listMembersTitleLabel.grid(row=0, column=0, columnspan=3, pady=(50,0))
    searchMembersFrame.grid(row=1, column=0, padx=35)
    searchMembersFNameLabel.grid(row=0, column=0, pady=(0,15))
    searchMembersFNameEntry.grid(row=0, column=1, ipady=2, ipadx=1, padx=(5,10), pady=(0,15))
    searchMembersFNameButton.grid(row=0, column=2, pady=(0,15))
    searchMembersLNameLabel.grid(row=1, column=0, pady=(0,15))
    searchMembersLNameEntry.grid(row=1, column=1, ipady=2, ipadx=2, padx=(5,10), pady=(0,15))
    searchMembersLNameButton.grid(row=1, column=2, pady=(0,15))
    searchMembersEmailLabel.grid(row=2, column=0, pady=(0,15))
    searchMembersEmailEntry.grid(row=2, column=1, ipady=2, ipadx=1, padx=(5,10), pady=(0,15))
    searchMembersEmailButton.grid(row=2, column=2, pady=(0,15))
    searchMembersPhoneNoLabel.grid(row=3, column=0, pady=(0,15))
    searchMembersPhoneNoEntry.grid(row=3, column=1, ipady=2, ipadx=1, padx=(5,10), pady=(0,15))
    searchMembersPhoneNoButton.grid(row=3, column=2, pady=(0,15))
    searchMembersEmerNoLabel.grid(row=4, column=0, pady=(0,15))
    searchMembersEmerNoEntry.grid(row=4, column=1, ipady=2, ipadx=1, padx=(5,10), pady=(0,15))
    searchMembersEmerNoButton.grid(row=4, column=2, pady=(0,15))
    searchMembersAddressLabel.grid(row=5, column=0, pady=(0,25))
    searchMembersAddressEntry.grid(row=5, column=1, ipady=2, ipadx=1, padx=(5,10), pady=(0,15))
    searchMembersAddressButton.grid(row=5, column=2, pady=(0,15))
    clearSearchButton.grid(row=6, column=0, columnspan=3)
    membersContainer.grid(row=1, column=1, columnspan=2, padx=(0,50), pady=(15,50))
    membersCanvas.pack(side="left", fill="both", expand = True)
    membersScrollbar.pack(side="right", fill="y")
    returnButton = tk.Button(listMembersFrame,
                             text="RETURN",
                             bg=redButtonColour, fg="#101010",
                             command=returnEmployeeMenu)
    returnButton['font']=buttonFont
    returnButton.grid(row=2, column=0, columnspan=3, pady=(0,50))
    print("List of members successfully shown.")

#function used for deleting members from the system
def deleteMemberPopup(memberIndex, specifiedDetail, enteredDetail):
    global confirmDeleteMember
    localLabelFont = font.Font(size=15, family="century gothic")
    localButtonFont = font.Font(size=12, family="century gothic", weight="bold")
    confirmDeleteMember = tk.Toplevel(bg=backgroundColour)
    confirmDeleteMember.wait_visibility()
    confirmDeleteMember.grab_set_global()
    memberFName,memberLName,memberEmail,memberPhoneNo,memberEmer1,memberEmer2,memberAddress = memberInfo(True)
    labelBorderFrame = tk.Frame(
        confirmDeleteMember,
        bg=backgroundColour,
        highlightbackground=foregroundColour,
        highlightthickness=2)
    confirmDeleteMemberLabel = tk.Label(
        labelBorderFrame,
        text="Would you like to confirm that\nyou would like to delete "
        +memberFName[memberIndex].upper()+memberLName[memberIndex].upper()+"?",
        width=31, bg=backgroundColour,
        fg=foregroundColour)
    cancelButton = tk.Button(confirmDeleteMember,
                             text="CANCEL",
                             width=12, height=2,
                             bg="#9fa0a1", fg="#101010",
                             command=confirmDeleteMember.destroy)
    confirmButton = tk.Button(confirmDeleteMember,
                              text="CONFIRM",
                              width=12, height=2,
                              bg="#a23d29", fg="#101010",
                              command=lambda: confirmedDeleteMember(memberIndex,specifiedDetail,enteredDetail))
    confirmDeleteMemberLabel['font'] = localLabelFont
    cancelButton['font'] = localButtonFont
    confirmButton['font'] = localButtonFont
    labelBorderFrame.grid(row=0, column=0,
                                    columnspan=2,
                                    pady=(30,0), padx=30, ipadx=15, ipady=15)
    confirmDeleteMemberLabel.pack()
    cancelButton.grid(row=1, column=0, padx=(0,10))
    confirmButton.grid(row=1, column=1, pady=(20,30))

#function that will be used for the display of a specific members details
def displayMemberDetails(fName, lName, email, phoneNo,
                         emer1, emer2, address, specifiedDetail,
                         enteredDetail, memberIndex):
    forgetAllWidgets()
    global searchedDetail
    global enteredSearchedDetail
    searchedDetail = specifiedDetail
    enteredSearchedDetail = enteredDetail
    memberDetailsFrame = tk.Frame(root, bg=backgroundColour,
                            highlightbackground=foregroundColour,
                            highlightthickness=2)
    memberDetailsFrame.place(relx=0.5, rely=0.5, anchor="center")
    innerMemberDetailsFrame = tk.Frame(memberDetailsFrame,
                                       bg=backgroundColour)
    memberDetailsTitleLabel = tk.Label(
        memberDetailsFrame,
        text=fName[0].upper()+fName[1:len(fName)]+" "+"Details",
        bg=backgroundColour, fg=foregroundColour)
    fNameTitleLabel = tk.Label(
        innerMemberDetailsFrame, text="First Name",
        bg=backgroundColour, fg=foregroundColour,
        width=20)
    fNameLabelBorder = tk.Frame(
        innerMemberDetailsFrame,
        bg=backgroundColour,
        highlightbackground=foregroundColour,
        highlightthickness=2)
    newFirstNameLabel = tk.Label(
        fNameLabelBorder, text=fName,
        bg=backgroundColour, fg=foregroundColour,
        width=20, borderwidth=1, relief="solid")
    changeFNameButton = tk.Button(
        innerMemberDetailsFrame, text="CHANGE",
        bg="#34c3eb", fg="black",
        command= lambda: modifyMemberPopup(
            memberIndex, "First Name", fName))
    lNameTitleLabel = tk.Label(
        innerMemberDetailsFrame, text="Last Name",
        bg=backgroundColour, fg=foregroundColour,
        width=20)
    lNameLabelBorder = tk.Frame(
        innerMemberDetailsFrame,
        bg=backgroundColour,
        highlightbackground=foregroundColour,
        highlightthickness=2)
    newLastNameLabel = tk.Label(
        lNameLabelBorder, text=lName,
        bg=backgroundColour, fg=foregroundColour,
        width=20, borderwidth=1, relief="solid")
    changeLNameButton = tk.Button(
        innerMemberDetailsFrame, text="CHANGE",
        bg="#34c3eb", fg="black",
        command= lambda: modifyMemberPopup(memberIndex,
                                    "Last Name", lName))
    emailTitleLabel = tk.Label(
        innerMemberDetailsFrame, text="Email",
        bg=backgroundColour,fg=foregroundColour,
        width=20)
    emailLabelBorder = tk.Frame(
        innerMemberDetailsFrame,
        bg=backgroundColour,
        highlightbackground=foregroundColour,
        highlightthickness=2)
    newEmailLabel = tk.Label(
        emailLabelBorder, text=email,
        bg=backgroundColour, fg=foregroundColour,
        width=20, borderwidth=1, relief="solid")
    changeEmailButton = tk.Button(
        innerMemberDetailsFrame, text="CHANGE",
        bg="#34c3eb", fg="black",
        command= lambda: modifyMemberPopup(
            memberIndex,"Email", email))
    phoneNoTitleLabel = tk.Label(
        innerMemberDetailsFrame, text="Phone Number",
        bg=backgroundColour, fg=foregroundColour,
        width=20)
    phoneNoLabelBorder = tk.Frame(
        innerMemberDetailsFrame,
        bg=backgroundColour,
        highlightbackground=foregroundColour,
        highlightthickness=2)
    newPhoneNoLabel = tk.Label(
        phoneNoLabelBorder, text=phoneNo,
        bg=backgroundColour, fg=foregroundColour,
        width=20, borderwidth=1, relief="solid")
    changePhoneNoButton = tk.Button(
        innerMemberDetailsFrame, text="CHANGE",
        bg="#34c3eb", fg="black",
        command= lambda: modifyMemberPopup(
            memberIndex, "Phone No.", phoneNo))
    emer1TitleLabel = tk.Label(
        innerMemberDetailsFrame, text="Emergency Number 1",
        bg=backgroundColour, fg=foregroundColour,
        width=20)
    emer1LabelBorder = tk.Frame(
        innerMemberDetailsFrame,
        bg=backgroundColour,
        highlightbackground=foregroundColour,
        highlightthickness=2)
    newEmergencyNo1Label = tk.Label(
        emer1LabelBorder, text=emer1,
        bg=backgroundColour, fg=foregroundColour,
        width=20, borderwidth=1, relief="solid")
    changeEmer1Button = tk.Button(
        innerMemberDetailsFrame, text="CHANGE",
        bg="#34c3eb", fg="black",
        command= lambda: modifyMemberPopup(
            memberIndex, "Emer No. 1", emer1))
    emer2TitleLabel = tk.Label(
        innerMemberDetailsFrame, text="Emergency Number 2",
        bg=backgroundColour, fg=foregroundColour,
        width=20)
    emer2LabelBorder = tk.Frame(
        innerMemberDetailsFrame,
        bg=backgroundColour,
        highlightbackground=foregroundColour,
        highlightthickness=2)
    newEmergencyNo2Label = tk.Label(
        emer2LabelBorder, text=emer2,
        bg=backgroundColour, fg=foregroundColour,
        width=20, borderwidth=1, relief="solid")
    changeEmer2Button = tk.Button(
        innerMemberDetailsFrame, text="CHANGE",
        bg="#34c3eb", fg="black",
        command= lambda: modifyMemberPopup(
            memberIndex, "Emer No. 2", emer2))
    addressTitleLabel = tk.Label(
        innerMemberDetailsFrame, text="Address",
        bg=backgroundColour, fg=foregroundColour,
        width=20)
    addressLabelBorder = tk.Frame(
        innerMemberDetailsFrame,
        bg=backgroundColour,
        highlightbackground=foregroundColour,
        highlightthickness=2)
    newAddressLabel = tk.Text(
        addressLabelBorder,
        bg=backgroundColour, fg=foregroundColour,
        height=4, wrap="word",
        width=22, borderwidth=1, relief="solid")
    changeAddressButton = tk.Button(
        innerMemberDetailsFrame, text="CHANGE",
        bg="#34c3eb", fg="black",
        command= lambda: modifyMemberPopup(
            memberIndex, "Address", address))
    returnButton = tk.Button(
        innerMemberDetailsFrame, text="RETURN",
        width=12,
        bg=redButtonColour, fg="#101010",
        command=lambda:listMembers(
            specifiedDetail, enteredDetail))
    memberDetailsTitleLabel['font'] = titleFont
    fNameTitleLabel['font'] = smallLabelFont
    newFirstNameLabel['font'] = smallLabelFont
    lNameTitleLabel['font'] = smallLabelFont
    newLastNameLabel['font'] = smallLabelFont
    emailTitleLabel['font'] = smallLabelFont
    newEmailLabel['font'] = smallLabelFont
    phoneNoTitleLabel['font'] = smallLabelFont
    newPhoneNoLabel['font'] = smallLabelFont
    emer1TitleLabel['font'] = smallLabelFont
    newEmergencyNo1Label['font'] = smallLabelFont
    emer2TitleLabel['font'] = smallLabelFont
    newEmergencyNo2Label['font'] = smallLabelFont
    addressTitleLabel['font'] = smallLabelFont
    newAddressLabel['font'] = smallLabelFont
    changeFNameButton['font'] = buttonFont
    changeLNameButton['font'] = buttonFont
    changeEmailButton['font'] = buttonFont
    changePhoneNoButton['font'] = buttonFont
    changeEmer1Button['font'] = buttonFont
    changeEmer2Button['font'] = buttonFont
    changeAddressButton['font'] = buttonFont
    returnButton['font'] = buttonFont
    memberDetailsTitleLabel.grid(row=0,
                        column=0,pady=(60,0))
    innerMemberDetailsFrame.grid(row=1,
                        column=0, pady=(2,5))
    fNameTitleLabel.grid(row=0,
                         column=0, padx=15, pady=(10,0))
    fNameLabelBorder.grid(row=1,
                          column=0, padx=15, pady=(2,5))
    newFirstNameLabel.pack()
    changeFNameButton.grid(row=0,
                           column=1, rowspan=2)
    lNameTitleLabel.grid(row=2,
                         column=0, padx=15, pady=(10,0))
    lNameLabelBorder.grid(row=3,
                          column=0, padx=15, pady=(2,5))
    newLastNameLabel.pack()
    changeLNameButton.grid(row=2,
                           column=1, rowspan=2)
    emailTitleLabel.grid(row=0,
                         column=3, padx=15, pady=(10,0))
    emailLabelBorder.grid(row=1,
                          column=3, padx=15, pady=(2,5))
    newEmailLabel.pack()
    changeEmailButton.grid(row=0,
                           column=4, rowspan=2)
    phoneNoTitleLabel.grid(row=2,
                           column=3, padx=15, pady=(10,0))
    phoneNoLabelBorder.grid(row=3,
                            column=3, padx=15, pady=(2,5))
    newPhoneNoLabel.pack()
    changePhoneNoButton.grid(row=2,
                             column=4, rowspan=2)
    emer1TitleLabel.grid(row=0,
                         column=6, padx=15, pady=(10,0))
    emer1LabelBorder.grid(row=1,
                          column=6, padx=15, pady=(2,5))
    newEmergencyNo1Label.pack()
    changeEmer1Button.grid(row=0,
                           column=7, rowspan=2)
    emer2TitleLabel.grid(row=2,
                         column=6, padx=15, pady=(10,0))
    emer2LabelBorder.grid(row=3,
                          column=6, padx=15, pady=(2,5))
    newEmergencyNo2Label.pack()
    changeEmer2Button.grid(row=2,
                           column=7, rowspan=2)
    addressTitleLabel.grid(row=4,
                           column=0, padx=15, pady=(10,0))
    addressLabelBorder.grid(row=5,
                            column=0, padx=15, pady=(2,5))
    newAddressLabel.pack()
    changeAddressButton.grid(row=4, column=1, rowspan=2)
    newAddressLabel.insert("end",address)
    newAddressLabel.configure(state="disabled")
    returnButton.grid(row=5, column=6, columnspan=2)

#fucntion for changing a members details
def modifyMemberPopup(memberIndex, desiredChange, currentDetail):
    global modifyDetailsMember
    global invalidModifiedMemberLabel
    localLabelFont = font.Font(size=15, family="century gothic")
    localButtonFont = font.Font(size=12, family="century gothic", weight="bold")
    localEntryFont = font.Font(size=20, family="century gothic")
    localInvalidFont = font.Font(size=15, family="TkDefaultFont")
    modifyDetailsMember = tk.Toplevel(bg=backgroundColour)
    modifyDetailsMember.wait_visibility()
    modifyDetailsMember.grab_set_global()
    invalidModifiedMemberLabel = tk.Label(
        modifyDetailsMember,
        text=" ", width=34, height=3,
        bg=backgroundColour)
    memberFName,memberLName,memberEmail,memberNumber,memberEmer1,memberEmer2,memberAddress = memberInfo(True)
    labelBorderFrame = tk.Frame(
        modifyDetailsMember,
        bg=backgroundColour,
        highlightbackground=foregroundColour,
        highlightthickness=2)
    modifyDetailsLabel = tk.Label(labelBorderFrame,
        text="Modify "+ desiredChange +" for\n" + memberFName[memberIndex].upper(),
        width=31, bg=backgroundColour, fg=foregroundColour)
    currentDescriptionLabel = tk.Label(
        modifyDetailsMember,text="Current "+ desiredChange +":",
        bg=backgroundColour, fg=foregroundColour,
        width=20)
    newDescriptionLabel = tk.Label(
        modifyDetailsMember,text="New "+ desiredChange +":",
        bg=backgroundColour, fg=foregroundColour,
        width=20)
    currentDetailLabel = tk.Label(
        modifyDetailsMember, width=20,
        bg=backgroundColour, fg=foregroundColour,
        text=currentDetail)
    addressDetailText = tk.Text(
        modifyDetailsMember, width=20, height=4,
        relief="flat", wrap="word",
        bg=backgroundColour, fg=foregroundColour)
    newDetailEntry = tk.Entry(
        modifyDetailsMember,
        width=20, bg=entryBackgroundColour, fg=entryForegroundColour,
        insertbackground=("gray"))
    cancelButton = tk.Button(modifyDetailsMember, text="CANCEL", width=12, height=2,
                             bg=redButtonColour, fg="#101010",
                             command = modifyDetailsMember.destroy)
    enterButton = tk.Button(modifyDetailsMember, text="ENTER", width=12, height=2,
                              bg=greenButtonColour, fg="#101010",
                              command = lambda: changeDetailEnter(desiredChange,
                                                                  newDetailEntry.get().lower(),
                                                                  currentDetail, memberIndex))
    currentDescriptionLabel['font'] = localLabelFont
    newDescriptionLabel['font'] = localLabelFont
    currentDetailLabel['font'] = localEntryFont
    addressDetailText['font'] = localEntryFont
    newDetailEntry['font'] = localEntryFont
    modifyDetailsLabel['font'] = localLabelFont
    cancelButton['font'] = localButtonFont
    enterButton['font'] = localButtonFont
    invalidModifiedMemberLabel['font'] = localInvalidFont
    labelBorderFrame.grid(row=0, column=0,columnspan=2,
                                    pady=(30,0), ipadx=15, ipady=15)
    modifyDetailsLabel.pack()
    currentDescriptionLabel.grid(row=1, column=0, padx=(50,20))
    newDescriptionLabel.grid(row=2, column=0, padx=20)
    if desiredChange == "Address":
        addressDetailText.grid(row=1, column=1, pady=15, padx=(0,50), ipady=4, ipadx=4)
        addressDetailText.insert("end",currentDetail)
        addressDetailText.configure(state="disabled")
    else:
        currentDetailLabel.grid(row=1, column=1, pady=15, padx=(0,50), ipady=4, ipadx=4)
    newDetailEntry.grid(row=2, column=1, pady=(0,15), padx=(0,50),
                                  ipady=4, ipadx=4)
    cancelButton.grid(row=3, column=0, padx=(0,10))
    enterButton.grid(row=3, column=1, pady=(20,30))
    invalidModifiedMemberLabel.grid(row=4, column=0, columnspan=2)

#function to create the interface for the list of memberships
def listMemberships(specifiedDetail, enteredDetail):
    forgetAllWidgets()
    localFont = font.Font(size=11, family="century gothic")
    localLabelFont = font.Font(size=9, family="century gothic")
    listMembershipsFrame = tk.Frame(root, bg=backgroundColour,
                                    highlightbackground=foregroundColour,
                                    highlightthickness=2)
    listMembershipsFrame.place(relx=0.5, rely=0.5, anchor="center")
    searchMembershipsFrame = tk.Frame(listMembershipsFrame, bg=backgroundColour)
    searchMembersFNameLabel = tk.Label(searchMembershipsFrame,
                                       text="Search by\nFirst Name",
                                       bg=backgroundColour, fg=foregroundColour)
    searchMembersFNameEntry = tk.Entry(searchMembershipsFrame,
                                       width = 12,
                                       borderwidth=1, relief="solid",
                                       bg=entryBackgroundColour,
                                       fg=entryForegroundColour)
    searchMembersFNameButton = tk.Button(searchMembershipsFrame,
                                         text="ENTER",
                                         bg="#42d458",
                                         command=lambda:listMemberships("fname",
                                                                    searchMembersFNameEntry.get().lower()))
    searchMembersLNameLabel = tk.Label(searchMembershipsFrame,
                                      text="Search by\nLast Name",
                                       bg=backgroundColour, fg=foregroundColour)
    searchMembersLNameEntry = tk.Entry(searchMembershipsFrame,
                                      width = 12,
                                      borderwidth=1, relief="solid",
                                       bg=entryBackgroundColour,
                                       fg=entryForegroundColour)
    searchMembersLNameButton = tk.Button(searchMembershipsFrame,
                                         text="ENTER",
                                         bg="#42d458",
                                         command=lambda:listMemberships("lname",
                                                                    searchMembersLNameEntry.get().lower()))
    searchMembershipLevelLabel = tk.Label(searchMembershipsFrame,
                                       text="Search by\nMembership Level",
                                       bg=backgroundColour, fg=foregroundColour)
    searchMembershipLevelEntry = tk.Entry(searchMembershipsFrame,
                                       width = 12,
                                       borderwidth=1, relief="solid",
                                       bg=entryBackgroundColour,
                                       fg=entryForegroundColour)
    searchMembershipLevelButton = tk.Button(searchMembershipsFrame,
                                         text="ENTER",
                                         bg="#42d458",
                                         command=lambda:listMemberships("membership level",
                                                                    searchMembershipLevelEntry.get().lower()))
    searchExpDateLabel = tk.Label(searchMembershipsFrame,
                                       text="Search by\nExpiry Date",
                                       bg=backgroundColour, fg=foregroundColour)
    searchExpDateEntry = tk.Entry(searchMembershipsFrame,
                                       width = 12,
                                       borderwidth=1, relief="solid",
                                       bg=entryBackgroundColour,
                                       fg=entryForegroundColour)
    searchExpDateButton = tk.Button(searchMembershipsFrame,
                                         text="ENTER",
                                         bg="#42d458",
                                         command=lambda:listMemberships("exp date",
                                                                    searchExpDateEntry.get().lower()))
    clearSearchButton = tk.Button(searchMembershipsFrame,
                                  text="CLEAR SEARCH",
                                  bg="#b83523",
                                  command=lambda:listMemberships("none",""))
    membershipsContainer = tk.Frame(listMembershipsFrame,borderwidth=1, relief="solid",
                                    bg=backgroundColour)
    membershipsCanvas = tk.Canvas(membershipsContainer, width=1160, height=400,
                                  bg=backgroundColour)
    membershipsScrollbar = tk.Scrollbar(membershipsContainer,
                                        orient="vertical",
                                        command=membershipsCanvas.yview,
                                        bg=backgroundColour)
    membershipsScrollableFrame = tk.Frame(membershipsCanvas, bg=backgroundColour)
    membershipsScrollableFrame.bind(
        "<Configure>",
        lambda e: membershipsCanvas.configure(
            scrollregion = membershipsCanvas.bbox("all")))
    membershipsCanvas.create_window((0,0), window=membershipsScrollableFrame, anchor="nw")
    membershipsCanvas.configure(yscrollcommand=membershipsScrollbar.set)
    memberFName,memberLName,membershipLevel,expiryDate = memberInfo(False)
    for member in range(0,len(memberFName)):
        memberIsValid = False
        if specifiedDetail == "none":
            memberIsValid = True
        elif specifiedDetail == "fname" and enteredDetail in memberFName[member]:
            memberIsValid = True
        elif specifiedDetail == "lname" and enteredDetail in memberLName[member]:
            memberIsValid = True
        elif specifiedDetail == "membership level" and enteredDetail in membershipLevel[member]:
            memberIsValid = True
        elif specifiedDetail == "exp date" and enteredDetail in expiryDate[member]:
            memberIsValid = True
        if memberIsValid:
            tempMembershipsFrame = tk.Frame(membershipsScrollableFrame, bg=backgroundColour)
            tempMembershipsFrame.pack(pady=(0,10))
            tempFNameLabel=tk.Label(tempMembershipsFrame,
                                    text=memberFName[member],
                                    width=20,
                                    bg=backgroundColour, fg=foregroundColour)
            tempLNameLabel=tk.Label(tempMembershipsFrame,
                                    text=memberLName[member],
                                    width=20,
                                    bg=backgroundColour, fg=foregroundColour)
            tempMembershipLevelLabel=tk.Label(tempMembershipsFrame,
                                              text=membershipLevel[member],
                                              width=4,
                                              bg=backgroundColour, fg=foregroundColour)
            tempExpiryDateLabel=tk.Label(tempMembershipsFrame,
                                         text=expiryDate[member],
                                         width=12,
                                         bg=backgroundColour, fg=foregroundColour)
            tempMembershipButton=tk.Button(tempMembershipsFrame, text="RENEW MEMBERSHIP",
                                       bg="#f7e23e", fg="#101010",
                                       command=functools.partial(renewMembershipPopup,
                                                                 member,
                                                                 specifiedDetail,
                                                                 enteredDetail))
            tempFNameLabel['font']=smallLabelFont
            tempLNameLabel['font']=smallLabelFont
            tempMembershipLevelLabel['font']=smallLabelFont
            tempExpiryDateLabel['font']=smallLabelFont
            tempMembershipButton['font']=buttonFont
            tempFNameLabel.grid(row=0, column=0, padx=5)
            tempLNameLabel.grid(row=0, column=1, padx=(0,5))
            tempMembershipLevelLabel.grid(row=0, column=2, padx=(0,5))
            tempExpiryDateLabel.grid(row=0, column=3, padx=(0,5))
            tempMembershipButton.grid(row=0, column=4, padx=(0,8))
    tk.Label(membershipsScrollableFrame, width=10, bg=backgroundColour).pack()
    listMembershipsTitleLabel = tk.Label(listMembershipsFrame, text="List Of Memberships",
                                         bg=backgroundColour, fg=foregroundColour)
    listMembershipsTitleLabel['font'] = titleFont
    searchMembersFNameLabel['font'] = localLabelFont
    searchMembersFNameEntry['font'] = localFont
    searchMembersFNameButton['font'] = localFont
    searchMembersLNameLabel['font'] = localLabelFont
    searchMembersLNameEntry['font'] = localFont
    searchMembersLNameButton['font'] = localFont
    searchMembershipLevelLabel['font'] = localLabelFont
    searchMembershipLevelEntry['font'] = localFont
    searchMembershipLevelButton['font'] = localFont
    searchExpDateLabel['font'] = localLabelFont
    searchExpDateEntry['font'] = localFont
    searchExpDateButton['font'] = localFont
    clearSearchButton['font'] = localFont
    listMembershipsTitleLabel.grid(row=0, column=0, pady=(50,0))
    searchMembershipsFrame.grid(row=1, column=0, padx=35)
    searchMembersFNameLabel.grid(row=0, column=0, pady=5)
    searchMembersFNameEntry.grid(row=1, column=0, ipady=2, ipadx=1, padx=(5,10), pady=(0,5))
    searchMembersFNameButton.grid(row=0, column=1, rowspan=2, padx=(8,18))
    searchMembersLNameLabel.grid(row=0, column=2, pady=5)
    searchMembersLNameEntry.grid(row=1, column=2, ipady=2, ipadx=2, padx=(5,10), pady=(0,5))
    searchMembersLNameButton.grid(row=0, column=3, rowspan=2, padx=(8,18))
    searchMembershipLevelLabel.grid(row=0, column=4, pady=5)
    searchMembershipLevelEntry.grid(row=1, column=4, ipady=2, ipadx=2, padx=(5,10), pady=(0,5))
    searchMembershipLevelButton.grid(row=0, column=5, rowspan=2, padx=(8,18))
    searchExpDateLabel.grid(row=0, column=6, pady=5)
    searchExpDateEntry.grid(row=1, column=6, ipady=2, ipadx=2, padx=(5,10), pady=(0,5))
    searchExpDateButton.grid(row=0, column=7, rowspan=2, padx=(8,18))
    clearSearchButton.grid(row=0, column=8,rowspan=2, padx=(20,0))
    membershipsContainer.grid(row=2, column=0, padx=50, pady=(15,20))
    membershipsCanvas.pack(side="left", fill="both", expand = True)
    membershipsScrollbar.pack(side="right", fill="y")
    returnButton = tk.Button(listMembershipsFrame,
                             text="RETURN",
                             bg=redButtonColour, fg="#101010",
                             command=returnEmployeeMenu)
    returnButton['font']=buttonFont
    returnButton.grid(row=3, column=0, pady=(0,20))
    print("List of memberships successfully shown.")

#function that creates the modify employee details pop up
#this will create the extra pop up window and link buttons to their corresponding functions
def renewMembershipPopup(memberIndex, specifiedDetail, enteredDetail):
    global renewMembership
    global finalExpiryDateLabel
    localLabelFont = font.Font(size=15,
                family="century gothic")
    localMiniLabelFont = font.Font(size=10,
                family="century gothic")
    localButtonFont = font.Font(size=12,
                family="century gothic",
                weight="bold")
    localComboFont = font.Font(size=11,
                family="century gothic")
    renewMembership = tk.Toplevel(
        bg=backgroundColour)
    renewMembership.wait_visibility()
    renewMembership.grab_set_global()
    memberFName, memberLName, membershipLevel, expDate = memberInfo(False)
    labelBorderFrame = tk.Frame(
        renewMembership,
        bg=backgroundColour,
        highlightbackground=foregroundColour,
        highlightthickness=2)
    renewMembershipLabel = tk.Label(
        labelBorderFrame,
        text="Renew Membership for\n" + (
            memberFName[memberIndex]+" "+
            memberLName[memberIndex]).upper(),
        width=31, bg=backgroundColour,
        fg=foregroundColour)
    newMembershipLevelLabel = tk.Label(
        renewMembership,text="New Membership Level:",
        bg=backgroundColour,fg=foregroundColour)
    levelList = ["1","2","3","4","5"]
    membershipLevelCombo = ttk.Combobox(
        renewMembership,state="readonly",
        width=25, values=levelList)
    membershipLevelCombo.set(
        "Choose Membership Level")
    currentMembershipLevelLabel = tk.Label(
        renewMembership,
        text="Current Membership Level:",
        bg=backgroundColour, fg=foregroundColour)
    actualMembershipLevelLabel = tk.Label(
        renewMembership,text=membershipLevel[memberIndex],
        bg=backgroundColour, fg=foregroundColour)
    newLengthLabel = tk.Label(
        renewMembership,text="New Expiry Date:",
        bg=backgroundColour, fg=foregroundColour)
    lengthList= ["Day","Week","Month","Three Months"]
    expiryDateCombo = ttk.Combobox(
        renewMembership,state="readonly",
        width=25, values=lengthList)
    expiryDateCombo.set("Choose Membership Length")
    currentDateLabel = tk.Label(
        renewMembership,text="Current Date:",
        bg=backgroundColour, fg=foregroundColour)
    today = date.today().strftime("%d/%m/%y")
    actualDateLabel = tk.Label(
        renewMembership,text=today,
        bg=backgroundColour, fg=foregroundColour)
    newExpiryDateLabel = tk.Label(
        renewMembership, text="New Expiry Date:",
        bg=backgroundColour, fg=foregroundColour)
    finalExpiryDateLabel = tk.Label(
        renewMembership, text=today,
        bg=backgroundColour,fg=foregroundColour)
    cancelButton = tk.Button(renewMembership,
                text="CANCEL", width=12, height=2,
                bg=redButtonColour, fg="#101010",
                command=renewMembership.destroy)
    enterButton = tk.Button(renewMembership,
                text="ENTER", width=12, height=2,
                bg=greenButtonColour, fg="#101010",
                command= lambda:enterRenewMembership(
                memberIndex,membershipLevelCombo.get(),
                expiryDateCombo.get(),specifiedDetail,
                enteredDetail))
    newMembershipLevelLabel['font'] = localLabelFont
    currentMembershipLevelLabel['font'] = localMiniLabelFont
    actualMembershipLevelLabel['font'] = localMiniLabelFont
    membershipLevelCombo['font'] = localComboFont
    newLengthLabel['font'] = localLabelFont
    expiryDateCombo['font'] = localComboFont
    currentDateLabel['font'] = localMiniLabelFont
    actualDateLabel['font'] = localMiniLabelFont
    newExpiryDateLabel['font'] = localMiniLabelFont
    finalExpiryDateLabel['font'] = localMiniLabelFont
    renewMembershipLabel['font'] = localLabelFont
    cancelButton['font'] = localButtonFont
    enterButton['font'] = localButtonFont
    labelBorderFrame.grid(row=0, column=0,columnspan=2,
                                    pady=(30,0), ipadx=15, ipady=15)
    renewMembershipLabel.pack()
    newMembershipLevelLabel.grid(row=1, column=0, padx=(50,20))
    membershipLevelCombo.grid(row=1, column=1, pady=(15,0), padx=(0,50), ipady=4, ipadx=4)
    currentMembershipLevelLabel.grid(row=2, column=0, pady=(3,12))
    actualMembershipLevelLabel.grid(row=2, column=1, pady=(3,12))
    newLengthLabel.grid(row=3, column=0, padx=20, pady=(0,15))
    expiryDateCombo.grid(row=3, column=1, pady=(0,15), padx=(0,50),
                                  ipady=4, ipadx=4)
    currentDateLabel.grid(row=4, column=0)
    actualDateLabel.grid(row=4, column=1)
    newExpiryDateLabel.grid(row=5,column=0)
    finalExpiryDateLabel.grid(row=5, column=1)
    cancelButton.grid(row=6, column=0, padx=(0,10))
    enterButton.grid(row=6, column=1, pady=(20,30))
    expiryDateCombo.bind("<<ComboboxSelected>>",lambda e: updateExpiryDatePopup(expiryDateCombo.get(),today))

def updateExpiryDatePopup (length, currentDate):
    validLength = False
    if length == "Day":
        date1 = datetime.datetime.strptime(currentDate,"%d/%m/%y")
        date2 = date1 + datetime.timedelta(days=1)
        tempExpDate = date2.strftime("%d/%m/%y")
        validLength = True
    elif length == "Week":
        date1 = datetime.datetime.strptime(currentDate,"%d/%m/%y")
        date2 = date1 + datetime.timedelta(days=7)
        tempExpDate = date2.strftime("%d/%m/%y")
        validLength = True
    elif length == "Month":
        date1 = datetime.datetime.strptime(currentDate,"%d/%m/%y")
        date2 = date1 + datetime.timedelta(days=30)
        tempExpDate = date2.strftime("%d/%m/%y")
        validLength = True
    elif length == "Three Months":
        date1 = datetime.datetime.strptime(currentDate,"%d/%m/%y")
        date2 = date1 + datetime.timedelta(days=90)
        tempExpDate = date2.strftime("%d/%m/%y")
        validLength = True
    if validLength:
        finalExpiryDateLabel.config(text=tempExpDate)
    
#main window
#setting up basic properties for the main window
root = tk.Tk()
root.attributes('-fullscreen',True)
root.configure(background="#2a2a2a")
root.title("Membership Tracking")

#declaring most used fonts
global buttonFont
global labelFont
global entryFont
global entryTitleFont
buttonFont = font.Font(size=18, family="arial")
smallButtonFont = font.Font(size=11, family="arial")
labelFont = font.Font(size=25, family="century gothic")
smallLabelFont = font.Font(size=18, family="century gothic")
entryFont = font.Font(size=30, family="century gothic")
smallEntryFont = font.Font(size=23, family="century gothic")
titleFont = font.Font(size=45, family="century gothic", underline=True, weight="bold")

global backgroundColour
global foregroundColour
global entryBackgroundColour
global entryForgroundColour
global redButtonColour
global greenButtonColour
backgroundColour = "#2a2a2a"
foregroundColour = "#efefef"
entryBackgroundColour = "#c0c0c0"
entryForegroundColour = "#191919"
redButtonColour = "#e65949"
greenButtonColour = "#63e15f"

initialLogin()
root.mainloop()




