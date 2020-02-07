import tkinter as tk
from tkinter import*
import random
import time;
import datetime
from tkinter import Tk, StringVar, ttk
from tkinter.messagebox import showinfo

root=Tk()
root.geometry('1150x650+0+0')
root.title('WOW! SILOG MENU')

Tops = Frame (root, width = 1150, height = 150)
Tops.pack(side = TOP)
lblTitle = Label(Tops, font = ('elephant', 25,'bold'), text = 'SILOG TO GO')
lblTitle.grid(row = 0, column = 0)
BottomMainFrame = Frame (root, width = 1150, height = 650, bd = 12, relief = 'raise')
BottomMainFrame.pack(side = BOTTOM)

f1 = Frame (BottomMainFrame, width = 383, height = 650, bd = 12, relief = 'raise')
f1.pack(side = LEFT)

f2 = Frame (BottomMainFrame, width = 383, height = 650, bd = 12, relief = 'raise')
f2.pack(side = LEFT)

f3 = Frame (BottomMainFrame, width = 383, height = 650, bd = 12, relief = 'raise')
f3.pack(side = LEFT)
f3TOP = Frame (f3, width = 383, height = 2505, bd = 4, relief = 'raise')
f3TOP.pack(side = TOP)
f3BOTTOM = Frame (f3, width = 383, height = 400, bd = 4, relief = 'raise')
f3BOTTOM.pack(side = BOTTOM)
"""
IntVar() = [var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16,var17,var18,
              var19,var20,var21,var22,var23,var24,var15,var26,var27,var28,var29]
"""
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()
var28 = IntVar()
var29 = StringVar()

var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)
var17.set(0)
var18.set(0)
var19.set(0)
var20.set(0)
var21.set(0)
var22.set(0)
var23.set(0)
var24.set(0)
var25.set(0)
var26.set(0)
var27.set(0)
var28.set(0)
var29.set('')

#frame1
varChixsilog = StringVar()
varPorksilog = StringVar()
varTorgisilog = StringVar()
varSpamsilog = StringVar()
varBangsilog = StringVar()
varMixsilog = StringVar()
varTapsilog = StringVar()
varSisiglog = StringVar()
varTosilog = StringVar()
varHamsilog = StringVar()
varHotsilog = StringVar()
varMasilog = StringVar()

#frame2
varLongsilog = StringVar()
varShanghaisilog = StringVar()
varPlainRice = StringVar()
varFriedRice = StringVar()
varLomi = StringVar()
varCoke = StringVar()
varRoyal = StringVar()
varRootBeer = StringVar()
varCoffee = StringVar()
varBottleWater = StringVar()
varTea = StringVar()

#frame3
varIceCream = StringVar()
varMangoFloat = StringVar()
varLecheFlan = StringVar()
varMaruya = StringVar()
varCassavaCake = StringVar()


varTax = StringVar()
varChange = StringVar()
varSubTotal = StringVar()
varTotal = StringVar()
varPayment = IntVar()

#frame1
varChixsilog.set('0')
varPorksilog.set('0')
varTorgisilog.set('0')
varSpamsilog.set('0')
varBangsilog.set('0')
varMixsilog.set('0')
varTapsilog.set('0')
varSisiglog.set('0')
varTosilog.set('0')
varHamsilog.set('0')
varHotsilog.set('0')
varMasilog.set('0')
varTea.set('0')

#frame2
varLongsilog.set('0')
varShanghaisilog.set('0')
varPlainRice.set('0')
varFriedRice.set('0')
varLomi.set('0')
varCoke.set('0')
varRoyal.set('0')
varRootBeer.set('0')
varCoffee.set('0')
varBottleWater.set('0')

#frame3
varIceCream.set('0')
varMangoFloat.set('0')
varLecheFlan.set('0')
varMaruya.set('0')
varCassavaCake.set('0')

varTax.set('0')
varChange.set('0')
varSubTotal.set('0')
varTotal.set('0')
varPayment.set('')


def iExit():
    qExit = tk.messagebox.askyesno("Silog list", "Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return

def Reset():
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
    var28.set(0)
    var29.set(0)
    
    varChixsilog.set('0')
    varPorksilog.set('0')
    varTorgisilog.set('0')
    varSpamsilog.set('0')
    varBangsilog.set('0')
    varMixsilog.set('0')
    varTapsilog.set('0')
    varSisiglog.set('0')
    varTosilog.set('0')
    varHamsilog.set('0')
    varHotsilog.set('0')
    varMasilog.set('0')
    varTea.set('0')

    varLongsilog.set('0')
    varShanghaisilog.set('0')
    varPlainRice.set('0')
    varFriedRice.set('0')
    varLomi.set('0')
    varCoke.set('0')
    varRoyal.set('0')
    varRootBeer.set('0')
    varCoffee.set('0')
    varBottleWater.set('0')

    varIceCream.set('0')
    varMangoFloat.set('0')
    varLecheFlan.set('0')
    varMaruya.set('0')
    varCassavaCake.set('0')

    varTax.set('0')
    varChange.set(' ')
    varSubTotal.set('0')
    varTotal.set('0')
    varPayment.set(' ')

    txtChixsilog.configure(state = DISABLED)
    txtPorksilog.configure(state = DISABLED)
    txtTorgisilog.configure(state = DISABLED)
    txtSpamsilog.configure(state = DISABLED)
    txtBangsilog.configure(state = DISABLED)
    txtMixsilog.configure(state = DISABLED)
    txtTapsilog.configure(state = DISABLED)
    txtSisiglog.configure(state = DISABLED)
    txtTosilog.configure(state = DISABLED)
    txtHamsilog.configure(state = DISABLED)
    txtHotsilog.configure(state = DISABLED)
    txtMasilog.configure(state = DISABLED)
    txtLongsilog.configure(state = DISABLED)
    txtShanghaisilog.configure(state = DISABLED)
    txtFriedRice.configure(state = DISABLED)
    txtPlainRice.configure(state = DISABLED)

    txtCoke.configure(state = DISABLED)
    txtRoyal.configure(state = DISABLED)
    txtRootBeer.configure(state = DISABLED)
    txtCoffee.configure(state = DISABLED)
    txtTea.configure(state = DISABLED)
    txtBottleWater.configure(state = DISABLED)
     
    txtIceCream.configure(state = DISABLED)
    txtMangoFloat.configure(state = DISABLED)
    txtLecheFlan.configure(state = DISABLED)
    txtMaruya.configure(state = DISABLED)
    txtCassavaCake.configure(state = DISABLED)
    #txtPayment.configure(state = DISABLED)
    txtChange.configure(state = DISABLED)
    txtTax.configure(state = DISABLED)
    txtSubTotal.configure(state = DISABLED)
    txtTotal.configure(state = DISABLED)
"""
def check():
    if (var1.get () == 1):
        txtChixsilog.configure(state = NORMAL)
        varChixsilog.set('')
    if (var2.get () == 1):
        txtPorksilog.configure(state = NORMAL)
        varPorksilog.set('')
    
    elif (var1.get () == 0):
        txtChixsilog.configure(state = DISABLED)
        varChixsilog.set('0')
    elif (var2.get () == 0):
        txtPorksilog.configure(state = DISABLED)
        varPorksilog.set('0')
"""
def checkChixsilog():
    if(var1.get () == 1):
        txtChixsilog.configure(state = NORMAL)
        varChixsilog.set('')
    elif (var1.get () == 0):
        txtChixsilog.configure(state = DISABLED)
        varChixsilog.set('0')

def checkPorksilog():
    if(var2.get () == 1):
        txtPorksilog.configure(state = NORMAL)
        varPorksilog.set('')
    elif (var2.get () == 0):
        txtPorksilog.configure(state = DISABLED)
        varPorksilog.set('0')

def checkTorgisilog():
    if(var3.get () == 1):
        txtTorgisilog.configure(state = NORMAL)
        varTorgisilog.set('')
    elif (var3.get () == 0):
        txtTorgisilog.configure(state = DISABLED)
        varTorsilog.set('0')

def checkSpamsilog():
    if(var4.get () == 1):
        txtSpamsilog.configure(state = NORMAL)
        varSpamsilog.set('')
    elif (var4.get () == 0):
        txtSpamsilog.configure(state = DISABLED)
        varSpamsilog.set('0')

def checkBangsilog():
    if(var5.get () == 1):
        txtBangsilog.configure(state = NORMAL)
        varBangsilog.set('')
    elif (var5.get () == 0):
        txtBangsilog.configure(state = DISABLED)
        varBangsilog.set('0')

def checkMixsilog():
    if(var6.get () == 1):
        txtMixsilog.configure(state = NORMAL)
        varMixsilog.set('')
    elif (var6.get () == 0):
        txtMixsilog.configure(state = DISABLED)
        varMixsilog.set('0')

def checkTapsilog():
    if(var7.get () == 1):
        txtTapsilog.configure(state = NORMAL)
        varTapsilog.set('')
    elif (var7.get () == 0):
        txtTapsilog.configure(state = DISABLED)
        varTapsilog.set('0')

def checkSisiglog():
    if(var8.get () == 1):
        txtSisiglog.configure(state = NORMAL)
        varSisiglog.set('')
    elif (var8.get () == 0):
        txtSisiglog.configure(state = DISABLED)
        varSisiglog.set('0')

def checkTosilog():
    if(var9.get () == 1):
        txtTosilog.configure(state = NORMAL)
        varTosilog.set('')
    elif (var9.get () == 0):
        txtTosilog.configure(state = DISABLED)
        varTosilog.set('0')

def checkHamsilog():
    if(var10.get () == 1):
        txtHamsilog.configure(state = NORMAL)
        varHamsilog.set('')
    elif (var10.get () == 0):
        txtHamsilog.configure(state = DISABLED)
        varHamsilog.set('0')

def checkHotsilog():
    if(var11.get () == 1):
        txtHotsilog.configure(state = NORMAL)
        varHotsilog.set('')
    elif (var11.get () == 0):
        txtHotsilog.configure(state = DISABLED)
        varHamsilog.set('0')

def checkMasilog():
    if(var12.get () == 1):
        txtMasilog.configure(state = NORMAL)
        varMasilog.set('')
    elif (var12.get () == 0):
        txtMasilog.configure(state = DISABLED)
        varMasilog.set('0')

def checkLongsilog():
    if(var13.get () == 1):
        txtLongsilog.configure(state = NORMAL)
        varLongsilog.set('')
    elif (var13.get () == 0):
        txtLongsilog.configure(state = DISABLED)
        varLongsilog.set('0')

def checkShanghaisilog():
    if(var14.get () == 1):
        txtShanghaisilog.configure(state = NORMAL)
        varShanghaisilog.set('')
    elif (var14.get () == 0):
        txtShanghaisilog.configure(state = DISABLED)
        varShanghaisilog.set('0')

def checkPlainRice():
    if(var15.get () == 1):
        txtPlainRice.configure(state = NORMAL)
        varPlainRice.set('')
    elif (var15.get () == 0):
        txtPlainRice.configure(state = DISABLED)
        varPlainRice.set('0')

def checkFriedRice():
    if(var16.get () == 1):
        txtFriedRice.configure(state = NORMAL)
        varFriedRice.set('')
    elif (var16.get () == 0):
        txtFriedRice.configure(state = DISABLED)
        varFriedRice.set('0')

def checkLomi():
    if(var17.get () == 1):
        txtLomi.configure(state = NORMAL)
        varLomi.set('')
    elif (var17.get () == 0):
        txtLomi.configure(state = DISABLED)
        varLomi.set('0')

def checkCoke():
    if(var18.get () == 1):
        txtCoke.configure(state = NORMAL)
        varCoke.set('')
    elif (var18.get () == 0):
        txtCoke.configure(state = DISABLED)
        varCoke.set('0')

def checkRoyal():
    if(var19.get () == 1):
        txtRoyal.configure(state = NORMAL)
        varRoyal.set('')
    elif (var19.get () == 0):
        txtRoyal.configure(state = DISABLED)
        varRoyal.set('0')

def checkRootBeer():
    if(var20.get () == 1):
        txtRootBeer.configure(state = NORMAL)
        varRootBeer.set('')
    elif (var20.get () == 0):
        txtRootBeer.configure(state = DISABLED)
        varRootBeer.set('0')

def checkCoffee():
    if(var21.get () == 1):
        txtCoffee.configure(state = NORMAL)
        varCoffee.set('')
    elif (var21.get () == 0):
        txtCoffee.configure(state = DISABLED)
        varCoffee.set('0')

def checkTea():
    if(var22.get () == 1):
        txtTea.configure(state = NORMAL)
        varTea.set('')
    elif (var22.get () == 0):
        txtTea.configure(state = DISABLED)
        varTea.set('0')

def checkBottleWater():
    if(var23.get () == 1):
        txtBottleWater.configure(state = NORMAL)
        varBottleWater.set('')
    elif (var23.get () == 0):
        txtBottleWater.configure(state = DISABLED)
        varBottleWater.set('0')

def checkIceCream():
    if(var24.get () == 1):
        txtIceCream.configure(state = NORMAL)
        varIceCream.set('')
    elif (var24.get () == 0):
        txtIceCream.configure(state = DISABLED)
        varIceCream.set('0')

def checkMangoFloat():
    if(var25.get () == 1):
        txtMangoFloat.configure(state = NORMAL)
        varMangoFloat.set('')
    elif (var25.get () == 0):
        txtMangoFloat.configure(state = DISABLED)
        varMangoFloat.set('0')

def checkLecheFlan():
    if(var26.get () == 1):
        txtLecheFlan.configure(state = NORMAL)
        varLecheFlan.set('')
    elif (var26.get () == 0):
        txtLecheFlan.configure(state = DISABLED)
        varLecheFlan.set('0')

def checkMaruya():
    if(var27.get () == 1):
        txtMaruya.configure(state = NORMAL)
        varMaruya.set('')
    elif (var27.get () == 0):
        txtMaruya.configure(state = DISABLED)
        varMaruya.set('0')

def checkCassavaCake():
    if(var28.get () == 1):
        txtCassavaCake.configure(state = NORMAL)
        varCassavaCake.set('')
    elif (var28.get () == 0):
        txtCassavaCake.configure(state = DISABLED)
        varCassavaCake.set('0')


def costofmeal():
    meal1 = float(varChixsilog.get())
    meal2 = float(varPorksilog.get())
    meal3 = float(varTorgisilog.get())
    meal4 = float(varSpamsilog.get())
    meal5 = float(varBangsilog.get())
    meal6 = float(varMixsilog.get())
    meal7 = float(varTapsilog.get())
    meal8 = float(varSisiglog.get())
    meal9 = float(varTosilog.get())
    meal10 = float(varHamsilog.get())
    meal11 = float(varHotsilog.get())
    meal12 = float(varMasilog.get())
    meal13 = float(varLongsilog.get())
    meal14 = float(varShanghaisilog.get())
    meal15 = float(varPlainRice.get())
    meal16 = float(varFriedRice.get())
    meal17 = float(varLomi.get())
    meal18 = float(varCoke.get())
    meal19 = float(varRoyal.get())
    meal20 = float(varRootBeer.get())
    meal21 = float(varCoffee.get())
    meal22 = float(varTea.get())
    meal23 = float(varBottleWater.get())
    meal24 = float(varIceCream.get())
    meal25 = float(varMangoFloat.get())
    meal26 = float(varLecheFlan.get())
    meal27 = float(varMaruya.get())
    meal28 = float(varCassavaCake.get())
    

    iTotal1= (meal1 * 85.00) + (meal2 * 85.00) + (meal3 * 85.00) + (meal4 * 85.00) + (meal5 * 75.00) + (meal6 * 75.00)
    iTotal2 = (meal7 * 75.00) + (meal8 * 75.00) + (meal9 * 65.00) + (meal10 * 65.00) + (meal11 * 65.00) + (meal12 * 65.00)
    iTotal3 = (meal13 * 75.00) + (meal14 * 55.00) + (meal15 * 15.00) + (meal16 * 20.00) + (meal17 * 45.00) + (meal18 * 18.00)
    iTotal4 = (meal19 * 18.00) + (meal20 * 23.00) + (meal21 * 30.00) + (meal22 * 30.00) + (meal23 * 15.00) + (meal24 * 25.00)
    iTotal5 = (meal25 * 35.00) + (meal26 * 49.00) + (meal27 * 39.00) + (meal28 * 99.00) 

    if (var29.get() == 'Cash'):
        iChange = float(varPayment.get())
        iCost = (iTotal1 + iTotal2 + iTotal3 + iTotal4 + iTotal5)
        iTax =  (iCost * 3.4) / 100
        iTaxq = '₱' , str('%.2f'% (iTax))
        varTax.set(iTaxq)
        iCostq = '₱', str('%.2f' % (iCost))
        varSubTotal.set(iCostq)
        iTotalq = '₱', str('%.2f' % ((iCost + iTax)))
        varTotal.set(iTotalq)
        cChange = (iChange - (iCost + iTax))
        cChangeq = '₱', str('%.2f' % (cChange))
        varChange.set(cChangeq)

    elif (var29.get() == 'Master Card' or 'Visa Card' or 'Debit Card'):
          varPayment.set('')
          iCost = (iTotal1 + iTotal2 + iTotal3 + iTotal4 + iTotal5)
          iTax =  (iCost * 3.4) / 100
          iTaxq = '₱' , str('%.2f'% (iTax))
          varTax.set(iTaxq)
          iCostq = '₱', str('%.2f' % (iCost))
          varSubTotal.set(iCostq)
          iTotalq = '₱', str('%.2f' % ((iCost + iTax)))
          varTotal.set(iTotalq)
          varChange.set('')


#---------------------------------------------------Frame1------------------------------------------------
lblMeal = Label(f1, font = ('arial', 18,'bold'), text = '\t     Meals\t         ')
lblMeal.grid(row = 0, column = 0)
 
#chixsilog alignment
Chixsilog = Checkbutton (f1, text = 'Chixsilog\t\t85.00', variable = var1, onvalue = 1, offvalue = 0,
                         font = ('times new roman', 16, 'bold'), command = checkChixsilog ).grid(row = 1, column = 0, sticky = W)
txtChixsilog = Entry (f1, font = ('times new roman', 16, 'bold'), textvariable = varChixsilog, width = 6, justify = 'left',  state = DISABLED)
txtChixsilog.grid(row = 1, column = 1)

#porksilog alignment
Porksilog = Checkbutton (f1, text = 'Porksilog\t\t85.00', variable = var2, onvalue = 1, offvalue = 0,
                         font = ('times new roman', 16, 'bold'), command = checkPorksilog).grid(row = 2, column = 0, sticky = W)
txtPorksilog = Entry (f1, font = ('times new roman', 16, 'bold'), textvariable = varPorksilog, width = 6, justify = 'left', state = DISABLED)
txtPorksilog.grid(row = 2, column = 1)

#torgisilog
Torgisilog = Checkbutton (f1, text = 'Torgisilog\t85.00', variable = var3, onvalue = 1, offvalue = 0,
                         font = ('times new roman', 16, 'bold'), command = checkTorgisilog).grid(row = 3, column = 0, sticky = W)
txtTorgisilog = Entry (f1, font = ('times new roman', 16, 'bold'), textvariable = varTorgisilog, width = 6, justify = 'left',  state = DISABLED)
txtTorgisilog.grid(row = 3, column = 1)

#spamsilog
Spamsilog = Checkbutton (f1, text = 'Spamsilog\t85.00', variable = var4, onvalue = 1, offvalue = 0,
                         font = ('times new roman', 16, 'bold'), command = checkSpamsilog).grid(row = 4, column = 0, sticky = W)
txtSpamsilog = Entry (f1, font = ('times new roman', 16, 'bold'), textvariable = varSpamsilog, width = 6, justify = 'left',  state = DISABLED)
txtSpamsilog.grid(row = 4, column = 1)

#bangsilog
Bangsilog = Checkbutton (f1, text = 'Bangsilog\t75.00', variable = var5, onvalue = 1, offvalue = 0,
                         font = ('times new roman', 16, 'bold'), command = checkBangsilog).grid(row = 5, column = 0, sticky = W)
txtBangsilog = Entry (f1, font = ('times new roman', 16, 'bold'), textvariable = varBangsilog, width = 6, justify = 'left',  state = DISABLED)
txtBangsilog.grid(row = 5, column = 1)

#mixsilog
Mixsilog = Checkbutton (f1, text = 'Mixsilog\t\t75.00', variable = var6, onvalue = 1, offvalue = 0,
                         font = ('times new roman', 16, 'bold'), command = checkMixsilog).grid(row = 6, column = 0, sticky = W)
txtMixsilog = Entry (f1, font = ('times new roman', 16, 'bold'), textvariable = varMixsilog, width = 6, justify = 'left',  state = DISABLED)
txtMixsilog.grid(row = 6, column = 1)

#tapsilog
Tapsilog = Checkbutton (f1, text = 'Tapsilog\t\t75.00', variable = var7, onvalue = 1, offvalue = 0,
                         font = ('times new roman', 16, 'bold'), command = checkTapsilog).grid(row = 7, column = 0, sticky = W)
txtTapsilog = Entry (f1, font = ('times new roman', 16, 'bold'), textvariable = varTapsilog, width = 6, justify = 'left',  state = DISABLED)
txtTapsilog.grid(row = 7, column = 1)

#sisiglog
Sisiglog = Checkbutton (f1, text = 'Sisilog\t\t75.00', variable = var8, onvalue = 1, offvalue = 0,
                         font = ('times new roman', 16, 'bold'), command = checkSisiglog).grid(row = 8, column = 0, sticky = W)
txtSisiglog = Entry (f1, font = ('times new roman', 16, 'bold'), textvariable = varSisiglog, width = 6, justify = 'left',  state = DISABLED)
txtSisiglog.grid(row = 8, column = 1)

#tosilog
Tosilog = Checkbutton (f1, text = 'Tosilog\t\t65.00', variable = var9, onvalue = 1, offvalue = 0,
                         font = ('times new roman', 16, 'bold'), command = checkTosilog).grid(row = 9, column = 0, sticky = W)
txtTosilog = Entry (f1, font = ('times new roman', 16, 'bold'), textvariable = varTosilog, width = 6, justify = 'left',  state = DISABLED)
txtTosilog.grid(row = 9, column = 1)

#hamsilog
Hamsilog = Checkbutton (f1, text = 'Hamsilog\t\t65.00', variable = var10, onvalue = 1, offvalue = 0,
                         font = ('times new roman', 16, 'bold'), command = checkHamsilog).grid(row = 10, column = 0, sticky = W)
txtHamsilog = Entry (f1, font = ('times new roman', 16, 'bold'), textvariable = varHamsilog, width = 6, justify = 'left',  state = DISABLED)
txtHamsilog.grid(row = 10, column = 1)

#hotsilog
Hotsilog = Checkbutton (f1, text = 'Hotsilog\t\t65.00', variable = var11, onvalue = 1, offvalue = 0,
                         font = ('times new roman', 16, 'bold'), command = checkHotsilog).grid(row = 11, column = 0, sticky = W)
txtHotsilog = Entry (f1, font = ('times new roman', 16, 'bold'), textvariable = varHotsilog, width = 6, justify = 'left',  state = DISABLED)
txtHotsilog.grid(row = 11, column = 1)

#masilog
Masilog = Checkbutton (f1, text = 'Masilog\t\t65.00', variable = var12, onvalue = 1, offvalue = 0,
                         font = ('times new roman', 16, 'bold'), command = checkMasilog).grid(row = 12, column = 0, sticky = W)
txtMasilog = Entry (f1, font = ('times new roman', 16, 'bold'), textvariable = varMasilog, width = 6, justify = 'left',  state = DISABLED)
txtMasilog.grid(row = 12, column = 1)

lblspace = Label(f1, text = '\n\n\n\n\n\n\n\n\n\n\n\n\n')
lblspace.grid(row = 13, column = 0)

#---------------------------------------------------Frame2------------------------------------------------

#longsilog
Longsilog = Checkbutton (f2, text = 'Longsilog\t\t75.00', variable = var13, onvalue = 1, offvalue = 0,
                         font = ('times new roman', 16, 'bold'), command = checkLongsilog).grid(row = 3, column = 0, sticky = W)
txtLongsilog = Entry (f2, font = ('times new roman', 16, 'bold'), textvariable = varLongsilog, width = 6, justify = 'left',  state = DISABLED)
txtLongsilog.grid(row = 3, column = 1)

#shanghaisilog
Shanghaisilog = Checkbutton (f2, text = 'Shanghaisilog\t55.00', variable = var14, onvalue = 1, offvalue = 0,
                         font = ('times new roman', 16, 'bold'), command = checkShanghaisilog).grid(row = 4, column = 0, sticky = W)
txtShanghaisilog = Entry (f2, font = ('times new roman', 16, 'bold'), textvariable = varShanghaisilog, width = 6, justify = 'left',  state = DISABLED)
txtShanghaisilog.grid(row = 4, column = 1)

#plainrice
PlainRice = Checkbutton (f2, text = 'Plain Rice\t15.00', variable = var15, onvalue = 1, offvalue = 0,
                         font = ('times new roman', 16, 'bold'), command = checkPlainRice).grid(row = 5, column = 0, sticky = W)
txtPlainRice = Entry (f2, font = ('times new roman', 16, 'bold'), textvariable = varPlainRice, width = 6, justify = 'left',  state = DISABLED)
txtPlainRice.grid(row = 5, column = 1)

#friedrice
FriedRice = Checkbutton (f2, text = 'Fried Rice\t20.00', variable = var16, onvalue = 1, offvalue = 0,
                         font = ('times new roman', 16, 'bold'), command = checkFriedRice).grid(row = 6, column = 0, sticky = W)
txtFriedRice = Entry (f2, font = ('times new roman', 16, 'bold'), textvariable = varFriedRice, width = 6, justify = 'left',  state = DISABLED)
txtFriedRice.grid(row = 6, column = 1)

#lomi
Lomi = Checkbutton (f2, text = 'Lomi\t\t45.00', variable = var17, onvalue = 1, offvalue = 0,
                         font = ('times new roman', 16, 'bold'), command = checkLomi).grid(row = 7, column = 0, sticky = W)
txtLomi = Entry (f2, font = ('times new roman', 16, 'bold'), textvariable = varLomi, width = 6, justify = 'left',  state = DISABLED)
txtLomi.grid(row = 7, column = 1)


lblDrinks = Label(f2, font = ('arial', 16,'bold'), text = '\n\t     Drinks       \t\n')
lblDrinks.grid(row = 8, column = 0)

#coke
Coke = Checkbutton (f2, text = 'Coke\t\t18.00', variable = var18, onvalue = 1, offvalue = 0,
                         font = ('times new roman', 16, 'bold'), command = checkCoke).grid(row = 9, column = 0, sticky = W)
txtCoke = Entry (f2, font = ('times new roman', 16, 'bold'), textvariable = varCoke, width = 6, justify = 'left',  state = DISABLED)
txtCoke.grid(row = 9, column = 1)

#royal
Royal = Checkbutton (f2, text = 'Royal\t\t18.00', variable = var19, onvalue = 1, offvalue = 0,
                         font = ('times new roman', 16, 'bold'), command = checkRoyal).grid(row = 10, column = 0, sticky = W)
txtRoyal = Entry (f2, font = ('times new roman', 16, 'bold'), textvariable = varRoyal, width = 6, justify = 'left',  state = DISABLED)
txtRoyal.grid(row = 10, column = 1)

#rootbeer
RootBeer = Checkbutton (f2, text = 'Root Beer\t23.00', variable = var20, onvalue = 1, offvalue = 0,
                         font = ('times new roman', 16, 'bold'), command = checkRootBeer).grid(row = 11, column = 0, sticky = W)
txtRootBeer = Entry (f2, font = ('times new roman', 16, 'bold'), textvariable = varRootBeer, width = 6, justify = 'left',  state = DISABLED)
txtRootBeer.grid(row = 11, column = 1)

#coffee
Coffee = Checkbutton (f2, text = 'Coffee\t\t30.00', variable = var21, onvalue = 1, offvalue = 0,
                         font = ('times new roman', 16, 'bold'), command = checkCoffee).grid(row = 12, column = 0, sticky = W)
txtCoffee = Entry (f2, font = ('times new roman', 16, 'bold'), textvariable = varCoffee, width = 6, justify = 'left',  state = DISABLED)
txtCoffee.grid(row = 12, column = 1)
#tea
Tea = Checkbutton (f2, text = 'Tea\t\t30.00', variable = var22, onvalue = 1, offvalue = 0,
                         font = ('times new roman', 16, 'bold'), command = checkTea).grid(row = 13, column = 0, sticky = W)
txtTea = Entry (f2, font = ('times new roman', 16, 'bold'), textvariable = varTea, width = 6, justify = 'left',  state = DISABLED)
txtTea.grid(row = 13, column = 1)

#bottlewater
BottleWater = Checkbutton (f2, text = 'Bottle Water\t15.00', variable = var23, onvalue = 1, offvalue = 0,
                         font = ('times new roman', 16, 'bold'), command = checkBottleWater).grid(row = 14, column = 0, sticky = W)
txtBottleWater = Entry (f2, font = ('times new roman', 16, 'bold'), textvariable = varBottleWater, width = 6, justify = 'left',  state = DISABLED)
txtBottleWater.grid(row = 14, column = 1)

lblspace = Label(f2, text = '\n\n\n\n\n\n\n\n\n\n\n\n\n')
lblspace.grid(row = 15, column = 0)

#---------------------------------------------------Frame3top------------------------------------------------

lblDesserts = Label(f3TOP, font = ('arial', 18,'bold'), text = '\tDesserts\t      ')
lblDesserts.grid(row = 0, column = 0)

#icecream 
IceCream = Checkbutton (f3TOP, text = 'Ice Cream\t25.00', variable = var24, onvalue = 1, offvalue = 0,
                         font = ('times new roman', 16, 'bold'), command = checkIceCream).grid(row = 1, column = 0, sticky = W)
txtIceCream = Entry (f3TOP, font = ('times new roman', 16, 'bold'), textvariable = varIceCream, width = 6, justify = 'left',  state = DISABLED)
txtIceCream.grid(row = 1, column = 1)

#mangofloat
MangoFloat = Checkbutton (f3TOP, text = 'Mango Float\t35.00', variable = var25, onvalue = 1, offvalue = 0,
                         font = ('times new roman', 16, 'bold'), command = checkMangoFloat).grid(row = 2, column = 0, sticky = W)
txtMangoFloat = Entry (f3TOP, font = ('times new roman', 16, 'bold'), textvariable = varMangoFloat, width = 6, justify = 'left',  state = DISABLED)
txtMangoFloat.grid(row = 2, column = 1)

#lecheflan
LecheFlan = Checkbutton (f3TOP, text = 'Leche Flan\t49.00', variable = var26, onvalue = 1, offvalue = 0,
                         font = ('times new roman', 16, 'bold'), command = checkLecheFlan).grid(row = 3, column = 0, sticky = W)
txtLecheFlan = Entry (f3TOP, font = ('times new roman', 16, 'bold'), textvariable = varLecheFlan, width = 6, justify = 'left',  state = DISABLED)
txtLecheFlan.grid(row = 3, column = 1)

#maruya
Maruya = Checkbutton (f3TOP, text = 'Maruya\t\t39.00', variable = var27, onvalue = 1, offvalue = 0,
                         font = ('times new roman', 16, 'bold'), command = checkMaruya).grid(row = 4, column = 0, sticky = W)
txtMaruya = Entry (f3TOP, font = ('times new roman', 16, 'bold'), textvariable = varMaruya, width = 6, justify = 'left',  state = DISABLED)
txtMaruya.grid(row = 4, column = 1)

#cassava cake
CassavaCake = Checkbutton (f3TOP, text = 'Cassava Cake\t99.00', variable = var28, onvalue = 1, offvalue = 0,
                         font = ('times new roman', 16, 'bold'), command = checkCassavaCake).grid(row = 5, column = 0, sticky = W)
txtCassavaCake = Entry (f3TOP, font = ('times new roman', 16, 'bold'), textvariable = varCassavaCake, width = 6, justify = 'left',  state = DISABLED)
txtCassavaCake.grid(row = 5, column = 1)

lblspace = Label(f3TOP, text = '\n')
lblspace.grid(row = 6, column = 0)
#-------------------------------------------------Frame3bottom------------------------------------------------

lblPaymentMethod = Label(f3BOTTOM, font = ('arial', 12, 'bold'), text = 'Payment Method', width = 14, justify = 'left', anchor = 'w')
lblPaymentMethod.grid(row = 0, column = 0)

lblChange = Label(f3BOTTOM, font = ('arial', 12, 'bold'), text = 'Change', bd = 10 , anchor = 'w')
lblChange.grid(row = 0, column = 1)
txtChange = Entry (f3BOTTOM, font = ('arial', 12, 'bold'), textvariable = varChange, width = 8, state = DISABLED)
txtChange.grid(row = 0, column = 2)

cmbPaymentMethod = ttk.Combobox(f3BOTTOM, textvariable = var29, state = 'readonly', font = ('arial', 12, 'bold'), width = 14)
cmbPaymentMethod['value'] = ('Cash', 'Master Card', 'Visa Card', 'Debit Card')
cmbPaymentMethod.current(0)
cmbPaymentMethod.grid(row = 1, column = 0)

lblTax =  Label(f3BOTTOM, font = ('arial', 12, 'bold'), text = 'Tax     ', bd = 10,  anchor = 'w')
lblTax.grid(row = 1, column = 1)
txtTax = Entry (f3BOTTOM, font = ('arial', 12, 'bold'), textvariable = varTax, width = 8, justify = 'left',  state = DISABLED)
txtTax.grid(row = 1, column = 2)

txtPayment = Entry (f3BOTTOM, font = ('arial', 12, 'bold'), textvariable = varPayment, width = 8, justify = 'left')
txtPayment.grid(row = 2, column = 0)

lblSubTotal =  Label(f3BOTTOM, font = ('arial', 12, 'bold'), text = 'Sub Total', bd = 10, width = 8, anchor = 'w')
lblSubTotal.grid(row = 2, column = 1)
txtSubTotal = Entry (f3BOTTOM, font = ('arial', 12, 'bold'), textvariable = varSubTotal, width = 8, justify = 'left',  state = DISABLED)
txtSubTotal.grid(row = 2, column = 2)

lblTotal =  Label(f3BOTTOM, font = ('arial', 12, 'bold'), text = 'Total', bd = 10, width = 6, anchor = 'w')
lblTotal.grid(row = 3, column = 1)
txtTotal = Entry (f3BOTTOM, font = ('arial', 12, 'bold'), textvariable = varTotal, width = 8, justify = 'left',  state = DISABLED)
txtTotal.grid(row = 3, column = 2)

#-------------------------------------------------Frame3bottom------------------------------------------------
btnTotal = Button (f3BOTTOM, padx = 14, pady = 1, fg = 'blue', font = ('arial', 12, 'bold'), width = 5,
                   text = 'Total ', command = costofmeal ).grid(row = 4, column = 0)

btnReset = Button (f3BOTTOM, padx = 14, pady = 1, fg = 'blue', font = ('arial', 12, 'bold'), width = 5,
                   text = 'Reset ', command = Reset ).grid(row = 4, column = 1)

btnExit = Button (f3BOTTOM, padx = 14, pady = 1, fg = 'blue', font = ('arial', 12, 'bold'), width = 5,
                   text = 'Exit ', command = lambda: iExit()).grid(row = 4, column = 2)

lblspace = Label(f3BOTTOM, text = '\n\n\n\n\n\n\n\n\n\n\n\n\n')
lblspace.grid(row = 5, column = 0)


root.mainloop()
"""
Jennifer Monsayac
BSCS 1st Year
WOW SILOG!
"""
