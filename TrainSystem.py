from tkinter import*
from tkinter import StringVar, ttk, Tk
import matplotlib.pyplot as plt
import random
import time
import datetime

root = Tk ()
root.geometry ("1350x750+0+0")
root.title ("Train Ticket")
root.configure (background = 'black')

Tops = Frame (root, width = 1350, height = 100, bd = 14, relief = 'raise')
Tops.pack (side =TOP)

f1 = Frame (root, width = 700, height = 650, bd=7, relief = 'raise')
f1.pack (side = LEFT)
f2 = Frame (root, width = 500, height = 650, bd=8, relief = 'raise')
f2.pack (side = RIGHT)

frametopRight = Frame (f2, width = 445, height = 650, bd=15, relief = 'raise')
frametopRight.pack (side = TOP)
frameBottompRight = Frame (f2, width = 550, height = 65, bd=5,)
frameBottompRight.pack (side = BOTTOM)

f1a = Frame (f1, width = 900, height = 330, bd=8, relief = 'raise')
f1a.pack (side = TOP)
f2a = Frame (f1, width = 300, height = 320, bd=6, relief = 'raise')
f2a.pack (side = BOTTOM)

topLeft1 = Frame (f1a, width = 200, height = 200, bd=10, relief = 'raise')
topLeft1.pack (side = LEFT)
topLeft2= ft2 = Frame (f1a, width = 300, height = 200, bd=16, relief = 'raise')
topLeft2.pack (side = RIGHT)
topLeft3 = Frame (f1a, width = 300, height = 200, bd=16, relief = 'raise')
topLeft3.pack (side = RIGHT)

#--------------------------------------------------------------------------------

bottomLeft1 = Frame (f2a, width = 440, height = 450, bd = 14, relief = "raise")
bottomLeft1.pack (side = LEFT)

bottomLeft2 = Frame (f2a, width = 440, height = 450, bd = 14, relief = "raise")
bottomLeft2.pack (side = RIGHT)
#--------------------------------------------------------------------------------


Tops.configure (background = 'black')
f1.configure(background = 'black')
f2.configure(background ='black')
lblTitle = Label(Tops, font = ('aerial', 40, 'bold'), text = "Train Ticketing Systems", bd =5, width = 30, justify = 'center')
lblTitle.grid (row = 0, column = 0)


Date1 = StringVar ()
time1 = StringVar ()
TicketClass = StringVar ()
TicketPrice = StringVar ()
Child_Ticket = StringVar ()
Adult_Ticket = StringVar ()
From_Destination = StringVar ()
To_Destination = StringVar ()
Fee_Price = StringVar ()
Route = StringVar ()
Receipt_Ref = StringVar ()


TicketClass.set("")
TicketPrice.set("")
Child_Ticket.set("")
Adult_Ticket.set("")
To_Destination.set("")
Fee_Price.set("")
Route.set ("")
Receipt_Ref.set("")

#------------------------------------------------------------------------------------
lblReceipt = Label(frametopRight, font = ('aerial', 15, 'bold'), text = "Travelling Ticketing Systems",
                   bd =5, width = 25, relief = 'sunken', justify = 'center')
lblReceipt.grid (row = 0, column = 0)


lblClass1 = Label(frameBottompRight, font = ('aerial', 13, 'bold'), text = "Class",
                     bd = 10, width = 4, relief = 'sunken' ,justify = 'center')
lblClass1.grid (row = 0, column = 0)

lblClass2 = Label(frameBottompRight, font = ('aerial', 13, 'bold'),
                     width = 4, relief = 'sunken' ,justify = 'center')
lblClass2.grid (row = 1, column = 0)


lblTicket1 = Label(frameBottompRight, font = ('aerial', 13, 'bold'), text = "Ticket",
                    bd = 10, width = 5, relief = 'sunken', justify = 'center')
lblTicket1.grid (row = 0, column = 1)

lblTicket2= Label(frameBottompRight, font = ('aerial', 13, 'bold'),
                    width = 5, relief = 'sunken', justify = 'center')
lblTicket2.grid (row = 1, column = 1)


lblAdult1 = Label(frameBottompRight, font = ('aerial', 13, 'bold'), text = "Adult",
                  bd=10, width = 5, relief = 'sunken',  justify = 'center')
lblAdult1.grid (row = 0, column = 2)

lblAdult2 = Label(frameBottompRight, font = ('aerial', 13, 'bold'),
                    bd = 10, width = 5, relief = 'sunken',  justify = 'center')
lblAdult2.grid (row = 1, column = 2)


lblChild1 = Label(frameBottompRight, font = ('aerial', 13, 'bold'), text = "Child",
                 bd = 5, width = 8, relief = 'sunken', justify = 'center')
lblChild1.grid (row = 0, column = 3, columnspan = 10)

lblChild2 = Label(frameBottompRight, font = ('aerial', 13, 'bold'),
                 bd = 5, width = 8, relief = 'sunken', justify = 'center')
lblChild2.grid (row = 1, column = 3, columnspan = 10)


#-------------------------------------- CODE FOR SPACE -------------------------

lblSp = Label(frameBottompRight, font = ('aerial', 14, 'bold'),
                 width = 30, relief = 'sunken', justify = 'center')
lblSp.grid (row = 2, column = 0 , columnspan = 4)
#------------------------------------------------------------------------------



lblFrom1 = Label(frameBottompRight, font = ('aerial', 14, 'bold'), text = "From",
                 bd=5, width = 8, relief = 'sunken', justify = 'center')
lblFrom1.grid (row = 2, column = 1)

lblFrom2 = Label(frameBottompRight, font = ('aerial', 14, 'bold'),
                 bd=5, width = 8, relief = 'sunken', justify = 'center')
lblFrom2.grid (row = 2, column = 2)


lblTo1 = Label(frameBottompRight, font = ('aerial', 14, 'bold'), text = "To",
               bd=5, width = 8, relief = 'sunken', justify = 'center')
lblTo1.grid (row = 3, column = 1)

lblTo2 = Label(frameBottompRight, font = ('aerial', 14, 'bold'),
               bd=5, width = 8, relief = 'sunken', justify = 'center')
lblTo2.grid (row = 3, column = 2)


lblPrice1 = Label(frameBottompRight, font = ('aerial', 14, 'bold'), text = "Price",
                  bd=5, width = 8, relief = 'sunken', justify = 'center')
lblPrice1.grid (row = 4, column = 1)

lblPrice12 = Label(frameBottompRight, font = ('aerial', 14, 'bold'),
                   bd=5, width = 8, relief = 'sunken', justify = 'center')
lblPrice12.grid (row = 4, column = 2)

#-----------------------space --------------------------------

lblSp = Label(frameBottompRight, font = ('aerial', 14, 'bold'),
                 width = 30, relief = 'sunken', justify = 'center')
lblSp.grid (row = 6, column = 0 , columnspan = 4)
#-----------------------------------------------------------------

lblRefNo1 = Label(frameBottompRight, font = ('aerial', 14, 'bold'), text = "Ref No",
                  bd=5, width = 8, relief = 'sunken', justify = 'center')
lblRefNo1.grid (row = 5, column = 0)

lblRefNo2 = Label(frameBottompRight, font = ('aerial', 14, 'bold'),
                  bd=5, width = 8, relief = 'sunken', justify = 'center')
lblRefNo2.grid (row = 6, column = 0)



lblTime1 = Label(frameBottompRight, font = ('aerial', 14, 'bold'), text = "Time",
                 bd=5, width = 8, relief = 'sunken', justify = 'center')
lblTime1.grid (row = 5, column = 1)

lblTime2 = Label(frameBottompRight, font = ('aerial', 14, 'bold'),
                 bd=5, width = 8, relief = 'sunken', textvariable = time1, justify = 'center' )
lblTime2.grid (row = 6, column = 1)


lblDate1 = Label(frameBottompRight, font = ('aerial', 14, 'bold'), text = "Date",
                 bd=5, width = 8, relief = 'sunken', justify = 'center')
lblDate1.grid (row = 5, column = 2)

lblDate2 = Label(frameBottompRight, font = ('aerial', 14, 'bold'),
                 bd=5, width = 8, relief = 'sunken', textvariable = Date1, justify = 'center')
lblDate2.grid (row = 6, column = 2)


lblRoute1 = Label(frameBottompRight, font = ('aerial', 14, 'bold'), text = "Route",
                  bd=5, width = 8, relief = 'sunken', justify = 'center')
lblRoute1.grid (row = 5, column = 3, columnspan = 10)

lblRoute2 = Label(frameBottompRight, font = ('aerial', 14, 'bold'),
                    width = 8, relief = 'sunken', justify = 'center')
lblRoute2.grid (row = 6, column = 3)



#----------------Function for Calculator------------------------------
def btnClick (numbers):
    global operator
    operator = operator + str (numbers)
    text_Input.set(operator)

def btnClearDisplay ():
    global operator
    operator = " "
    text_Input.set("")

def btnEqualsInput ():
    global operator
    sumup = str (eval(operator))
    text_Input.set(sumup)
    operator = ""

def iExit ():
    qExit = messagebox.askyesno (" Quit Sysyem", "Do you want to quit")
    if qExit > 0:
        root.directory ()
        return


def Travel_Cost():
    if (var9.get() == "Killburn" and var1.get () == 1 and var4.get() == 1):
        Tcost = float (30.8)
        Single = float (var12.get())
        Adult_Tax = "$", str ('%.2f'% ((Tcost * Single)* 0.03))
        Adult_Fees = "$", str ('%.2f'% (Tcost * Single))
        TotalCost = "$", str ('%.2f'% ((Tcost * Single) + ((Tcost * Single)*0.03)))
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        TicketClass.set ("Standard")
        TicketPrice.set (Adult_Fees)
        Child_Ticket.set ("No")
        Adult_Ticket.set ("Yes")
        From_Destination.set ("Killburn")
        To_Destination.set("London")
        Fee_Price.set (TotalCost)
        Total.set(TotalCost)
        Total.set (TotalCost)
        Route.set ("Direct")


        X = random.randint (109, 5876)
        randomRef = str(X)
        Receipt_Ref.set ("TFL"+ randomRef)

    elif (var9.get() == "Killburn" and var1.get() == 1 and var5.get() == 1 ):
        Tcost = float(23.8)
        single = float(var12.get())
        child_Tax = "$", str ('%.2f'% (Tcost * 0))
        TotalCost = "$", str('%.2f'% ((Tcost * Single) + (Tcost * 0)))
        Tax.set(child_Tax)
        SubTotal.set(child_Fees)
        TicketClass.set (child_Fees)
        Child_Ticket.set ("Yes")
        Adult_Ticket.set ("No")
        From_Destination.set ("London")
        To_Destination.set("Killburn")
        Fee_Price.set (TotalCost)
        Total.set("TotalCost")
        Route.set("Direct")

    X = random.randint (109, 5876)
    randomRef = str (X)
    Receipt_Ref.set ("TFL" + randomRef)

    if (var9.get() == "Preston" and var1.get() == 1 and var4.get() == 1):
        Tcost = float(42.8)
        Single = float(var12.get())
        Adult_Tax = "$", str('%.2f' % ((Tcost * Single) * 0.03))
        Adult_Fees = "$", str('%.2f' % (Tcost * Single))
        TotalCost = "$", str('%.2f' % ((Tcost * Single) + ((Tcost * Single) * 0.03)))
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        TicketClass.set("Standard")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set("Killburn")
        To_Destination.set("London")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")

        X = random.randint(109, 5876)
        randomRef = str(X)
        Receipt_Ref.set("TFL" + randomRef)

    elif (var9.get() == "Preston" and var1.get() == 1 and var5.get() == 1):
        Tcost = float(28.23)
        single = float(var12.get())
        child_Tax = "$", str('%.2f' % (Tcost * 0))
        TotalCost = "$", str('%.2f' % ((Tcost * Single) + (Tcost * 0)))
        Tax.set(child_Tax)
        SubTotal.set(child_Fees)
        TicketClass.set(child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("London")
        To_Destination.set("Killburn")
        Fee_Price.set(TotalCost)
        Total.set("TotalCost")
        Route.set("Direct")

    X = random.randint(109, 5876)
    randomRef = str(X)
    Receipt_Ref.set("TFL" + randomRef)


    if (var9.get() == "Oxford" and var1.get() == 1 and var4.get() == 1):
        Tcost = float(42.8)
        Single = float(var12.get())
        Adult_Tax = "$", str('%.2f' % ((Tcost * Single) * 0.03))
        Adult_Fees = "$", str('%.2f' % (Tcost * Single))
        TotalCost = "$", str('%.2f' % ((Tcost * Single) + ((Tcost * Single) * 0.03)))
        Tax.set(Adult_Tax)
        SubTotal.set(Adult_Fees)
        TicketClass.set("Standard")
        TicketPrice.set(Adult_Fees)
        Child_Ticket.set("No")
        Adult_Ticket.set("Yes")
        From_Destination.set("Killburn")
        To_Destination.set("London")
        Fee_Price.set(TotalCost)
        Total.set(TotalCost)
        Total.set(TotalCost)
        Route.set("Direct")

        X = random.randint(109, 5876)
        randomRef = str(X)
        Receipt_Ref.set("TFL" + randomRef)

    elif (var9.get() == "Oxford" and var1.get() == 1 and var5.get() == 1):
        Tcost = float(28.23)
        single = float(var12.get())
        child_Tax = "$", str('%.2f' % (Tcost * 0))
        TotalCost = "$", str('%.2f' % ((Tcost * Single) + (Tcost * 0)))
        Tax.set(child_Tax)
        SubTotal.set(child_Fees)
        TicketClass.set(child_Fees)
        Child_Ticket.set("Yes")
        Adult_Ticket.set("No")
        From_Destination.set("London")
        To_Destination.set("Killburn")
        Fee_Price.set(TotalCost)
        Total.set("TotalCost")
        Route.set("Direct")

def Chkbutton_value ():
    if (var10.get() == 1):
        var12.set("")
        entSingle.configure(state = NORMAL)
    elif var10.get() == 0:
        entSingle.configure(state = DISABLED)
        var12.set("0")
    if (var11.get() == 1):
        var6.set("")
        entReturn.configure(state= NORMAL )
    elif var11.get() == 0:
        entReturn.configure(state = DISABLED)
        var6.set("0")



def Reset ():
    Tax.set("0")
    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var8.set("0")
    var9.set("0")
    var10.set("0")
    var11.set("0")
    var12.set("0")
    SubTotal.set("0")
    Total.set("0")
    TicketClass.set ("0")
    TicketPrice.set("0")
    Child_Ticket.set ("")
    Adult_Ticket.set("")
    From_Destination.set ("")
    To_Destination.set("")
    Fee_Price.set ("")






#-------------------------------Variables---------------------------------------

var1  = StringVar ()
var2  = StringVar ()
var3  = StringVar ()
var4  = StringVar ()
var5  = StringVar ()
var6  = StringVar ()
var7  = StringVar ()
var8 = StringVar ()
var9 = StringVar ()
var10 = StringVar ()
var11 = StringVar ()
var12 = StringVar ()
Tax = StringVar ()

var1.set("0")
var2.set("0")
var3.set("0")
var4.set("0")
var5.set("0")
var6.set("0") #6, 10,11 12
var7.set("0")
var8.set("0")
var9.set("0")
var10.set ("10")
var11.set("0")
var12.set("0")

DateOfOrder = StringVar ()
SubTotal = StringVar ()
timer = StringVar()
Total = StringVar ()
text_Input = StringVar ()
operator = ""



#----------------------------------------Date and Time --------------------------------------
Date1.set(time.strftime("%d/%m/%Y")) #date
time1.set (time.strftime('%H:%M:%S')) #time
#--------------------------------------------------------------------------------------------



#------------------------------Create Widget topLeft1-------------------------------------
lblClass = Label (topLeft1, font = ('arial', 17, 'bold'), text = 'Class', bd = 8)
lblClass.grid ( row = 0, column = 0, sticky = W)
chkStandard= Checkbutton (topLeft1, font = ('arial', 10, 'bold'), text = 'Standard', variable = var1, onvalue = 1, offvalue = 0)
chkStandard.grid ( row = 1, column = 0, sticky = W)

chkEconomy= Checkbutton (topLeft1, font = ('arial', 10, 'bold'), text = 'Economy', variable = var2, onvalue = 1, offvalue = 0)
chkEconomy.grid ( row = 2, column = 0, sticky = W)
chkFirstClass= Checkbutton (topLeft1, font = ('arial', 10, 'bold'), text = 'First Class', variable = var3, onvalue = 1, offvalue = 0)
chkFirstClass.grid ( row = 3, column = 0, sticky = W)

#------------------------------Create Widget topLeft2-------------------------------------

lblSelect = Label (topLeft3, font = ('arial', 13, 'bold'), text = 'Destination Selector', bd = 8)
lblSelect.grid ( row = 0, column = 0, sticky = W , columnspan = 2)
lblDestination = Label (topLeft3, font = ('airial', 20, 'bold'), text = 'Destination', bd = 4)

CboDestination = ttk.Combobox (topLeft3, textvariable = var9, state = 'readonly', font = ('arial', 22, 'bold'), width = 8)
CboDestination ['value'] = ('', 'killburn', 'Preston', 'Oxford', 'Leeds', 'Brixton')
CboDestination.current (0)
CboDestination.grid ( row = 1, column = 1)

chkAdult= Checkbutton (topLeft3, font = ('arial', 10, 'bold'), text = 'Adult', variable = var4, onvalue = 1, offvalue = 0)
chkAdult.grid ( row = 1, column = 0, sticky = W)

chkChild= Checkbutton (topLeft3, font = ('arial', 10, 'bold'), text = 'Child', variable = var5, onvalue = 1, offvalue = 0)
chkChild.grid ( row = 3, column = 0, sticky = W)

#--------------------------Ticket -----------------------------------------------

lblClass = Label (topLeft2, font = ('arial', 17, 'bold'), text = 'Ticket Type', bd = 8)
lblClass.grid ( row = 0, column = 0, sticky = W)


chkSingle= Checkbutton (topLeft2, font = ('arial', 10, 'bold'), text = 'Single', variable = var10, onvalue = 1, offvalue = 0)
chkSingle.grid ( row = 2, column = 0, sticky = W)
entSingle = Entry (topLeft2, font = ('arial', 10, 'bold'), textvariable = var7, bd =2 , width = 7)
entSingle.grid (row = 2, column = 1, sticky=W)

chkReturn= Checkbutton (topLeft2, font = ('arial', 10, 'bold'), text = 'Return', variable = var11, onvalue = 1, offvalue = 0)
chkReturn.grid ( row = 3, column = 0, sticky = W)
entReturn = Entry (topLeft2, font = ('arial', 10, 'bold'), textvariable = var5, bd =2 , width = 7)
entReturn.grid (row = 3, column = 1, sticky=W)

lblComment = Label (topLeft2, font = ('arial', 17, 'bold'), text = 'Comment', bd = 8)
lblComment.grid ( row = 4, column = 0, sticky = W)
entComment = Entry (topLeft2, font = ('arial', 8, 'bold'), textvariable = var7, bd =2 , width = 7)
entComment.grid (row = 4, column = 1, sticky=W)


#--------------------------Calculator---------------------------------------
text_Input = StringVar ()
txtDisplay = Entry (bottomLeft2, font = ('arial', 8 , 'bold'), textvariable = text_Input, bd = 7,
                    bg = "Powder blue", justify = 'right')
txtDisplay.grid (columnspan = 3)

# ----------------------calculator buttons ----------------------------------

btn7 = Button (bottomLeft2, padx = 8, fg = "black", font = ('arial', 10, 'bold'),
               text = "7", bg = "powder blue", command = lambda : btnClick (7)).grid (row = 2, column =0)

btn8 = Button (bottomLeft2, padx = 8, fg = "black", font = ('arial', 10, 'bold'),
               text = "8", bg = "powder blue", command = lambda : btnClick (8)).grid (row = 2, column =1)

btn9 = Button (bottomLeft2, padx = 8, fg = "black", font = ('arial', 10, 'bold'),
               text = "9", bg = "powder blue", command = lambda : btnClick (9)).grid (row = 2, column =2)

Addition = Button (bottomLeft2,padx = 8,bd = 8 , fg = "black", font = ('arial', 10, 'bold'),
                   text = "+", bg = "powder blue", command = lambda : btnClick ("+")).grid (row =2, column = 3)

#--------------------------------------------------------------------------------


btn4 = Button (bottomLeft2, padx = 8, fg = "black", font = ('arial', 10, 'bold'),
               text = "4", bg = "powder blue", command = lambda : btnClick (4)).grid (row = 3, column =0)

btn5 = Button (bottomLeft2, padx = 8, fg = "black", font = ('arial', 10, 'bold'),
               text = "5", bg = "powder blue", command = lambda : btnClick (5)).grid (row = 3, column =1)

btn6 = Button (bottomLeft2, padx = 8, fg = "black", font = ('arial', 10, 'bold'),
               text = "6", bg = "powder blue", command = lambda : btnClick (6)).grid (row = 3, column =2)

Subtraction = Button (bottomLeft2,padx = 8,bd = 8 , fg = "black", font = ('arial', 10, 'bold'),
                   text = "-", bg = "powder blue", command = lambda : btnClick ("-")).grid (row =3, column = 3)


#-----------------------------------------------------------------------------------

btn1 = Button (bottomLeft2, padx = 8, fg = "black", font = ('arial', 10, 'bold'),
               text = "1", bg = "powder blue", command = lambda : btnClick (1)).grid (row = 4, column =0)

btn2 = Button (bottomLeft2, padx = 8, fg = "black", font = ('arial', 10, 'bold'),
               text = "2", bg = "powder blue", command = lambda : btnClick (2)).grid (row = 4, column =1)

btn3 = Button (bottomLeft2, padx = 8, fg = "black", font = ('arial', 10, 'bold'),
               text = "3", bg = "powder blue", command = lambda : btnClick (3), width = 4).grid (row = 4, column =2)

Multiply = Button (bottomLeft2,padx = 8,bd = 8 , fg = "black", font = ('arial', 10, 'bold'),
                   text = "*", bg = "powder blue", command = lambda : btnClick ("*"), width = 4).grid (row =4, column = 3)


#------------------------------------------------------------------------------------

btn0 = Button (bottomLeft2, padx = 8, fg = "black", font = ('arial', 10, 'bold'),
               text = "0", bg = "powder blue", command = lambda : btnClick (0), width = 4).grid (row = 5, column =0)

btnClear = Button (bottomLeft2, padx = 8, fg = "black", font = ('arial', 10, 'bold'),
               text = "C", bg = "powder blue", width = 4, command = btnClearDisplay).grid (row = 5, column =1)

btnEquals = Button (bottomLeft2, padx = 8, fg = "black", font = ('arial', 10, 'bold'),
               text = "=", bg = "powder blue", width = 4, command = btnEqualsInput).grid (row = 5, column =2)

Division = Button (bottomLeft2,padx = 8,bd = 8 , fg = "black", font = ('arial', 10, 'bold'),
                   text = "/", bg = "powder blue", command = lambda : btnClick ("/"), width = 4).grid (row =5, column = 3)

#--------------------------------Tax, subTotal, Total---------------------------------

lblStateTax = Label (bottomLeft1, font = ('arial', 16, 'bold'), text = "State Tax", bd = 13, anchor = 'w')
lblStateTax.grid (row = 3, column = 2)
txtStateTax = Entry (bottomLeft1, font = ('arial', 14, 'bold'),textvariable = Tax , bd = 10, insertwidth = 4,
                     bg ="#ffffff", justify = 'right')
txtStateTax.grid (row = 3, column = 3)


lblSubTotal = Label (bottomLeft1, font = ('arial', 16, 'bold'), text = "Sub Total", bd = 13, anchor = 'w')
lblSubTotal.grid (row = 4, column = 2)
txtSubTotal = Entry (bottomLeft1, font = ('arial', 14, 'bold'),textvariable = Tax , bd = 10, insertwidth = 4,
                     bg = "#ffffff", justify = 'right')
txtSubTotal.grid (row = 4, column = 3)



lblTotalCost = Label (bottomLeft1, font = ('arial', 16, 'bold'), text = "Total Cost", bd = 13, anchor = 'w')
lblTotalCost.grid (row = 5, column = 2)
txtTotalCost = Entry (bottomLeft1, font = ('arial', 14, 'bold'),textvariable = Tax , bd = 10, insertwidth = 4,
                     bg = "#ffffff", justify = 'right')
txtTotalCost.grid (row = 5 , column = 3)

#-------------------------------Empty spaace or widget--------------------------
lblSpace = Label (bottomLeft1, font = ('arial', 20, 'bold'), text = "   \n     ", bd = 16, anchor = 'w')
lblSpace.grid (row = 6, column = 0, columnspan = 4)

lblSpace = Label (bottomLeft1, font = ('arial', 20, 'bold'), text = "   \n     ", bd = 16, anchor = 'w')
lblSpace.grid (row = 6, column = 2)
#---------------------------------------------------------
lblSpace = Label (bottomLeft2, font = ('arial', 20, 'bold'), text = "   \n     ", bd = 16, anchor = 'w')
lblSpace.grid (row = 6, columnspan = 3)
#---------------------------------------------------------


#---------------------------------------------------------
lblSp = Label (frameBottompRight, font = ('arial', 14, 'bold'), width = 34, height = 1, relief = 'sunken',
               justify = 'center')
lblSp.grid (row = 9, column = 0, columnspan = 4)

#---------------------------------------------------------

btnTotal = Button (frameBottompRight , text = 'Convert', padx = 2, pady = 2, bd = 2, fg = "black",
                   font = ('arial', 12, 'bold'), width = 6, height = 1)
btnTotal.grid (row = 7, column = 0)

btnReset = Button (frameBottompRight, text= 'Reset', width = 6, padx = 2, pady = 2, bd = 2, fg = "black",
                    font = ('arial', 12, 'bold'), height = 1 ,command = Reset ).grid (row = 7, column = 1)

btnClear = Button (frameBottompRight, text= 'Clear', width = 6, padx = 2, pady = 2, bd = 2, fg = "black",
                    font = ('arial', 12, 'bold'), height = 1 ,command = Reset).grid (row = 7, column = 2)

btnExit = Button (frameBottompRight, text= 'Exit', width = 6, padx = 2, pady = 2, bd = 2, fg = "black",
                    font = ('arial', 12, 'bold'), height = 1, command = iExit ).grid (row = 7, column = 3)


#----------------------------Spacing-----------------------
lblSp = Label (frameBottompRight, font = ('arial', 14, 'bold'), width = 34, height = 1, relief = 'sunken',
               justify = 'center')
lblSp.grid (row =11, column = 0, columnspan = 4)
#-------------------------------------------------------------

root.mainloop ()

