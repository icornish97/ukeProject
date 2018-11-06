#Author: Ian Cornish

import Chords as ch

def getChord():
   
    i = 0 
    while i != 1: 
        userChoice = input("What chord would you like to see?: ") 
#Base Chords   
        if userChoice == "a":
            i = 1
            return userChoice
        elif userChoice == "b":
            i= 1
            return userChoice
        elif userChoice == "c":
            i= 1
            return userChoice
        elif userChoice == "d":
            i= 1   
            return userChoice         
        elif userChoice == "e":
            i= 1
            return userChoice
        elif userChoice == "f":
            i= 1
            return userChoice
        elif userChoice == "g":
            i= 1
            return userChoice
#Minor Chords     
        elif userChoice == "am":
            i = 1
            return userChoice
        elif userChoice == "bm":
            i= 1
            return userChoice
        elif userChoice == "cm":
            i= 1
            return userChoice
        elif userChoice == "dm":
            i= 1   
            return userChoice         
        elif userChoice == "em":
            i= 1
            return userChoice
        elif userChoice == "fm":
            i= 1
            return userChoice
        elif userChoice == "gm":
            i= 1
            return userChoice 
#Sixth Chords
        elif userChoice == "a6":
            i = 1
            return userChoice
        elif userChoice == "b6":
            i= 1
            return userChoice
        elif userChoice == "c6":
            i= 1
            return userChoice
        elif userChoice == "d6":
            i= 1   
            return userChoice         
        elif userChoice == "e6":
            i= 1
            return userChoice
        elif userChoice == "f6":
            i= 1
            return userChoice
        elif userChoice == "g6":
            i= 1
            return userChoice 
#Seventh Chords         
        elif userChoice == "a7":
            i = 1
            return userChoice
        elif userChoice == "b7":
            i= 1
            return userChoice
        elif userChoice == "c7":
            i= 1
            return userChoice
        elif userChoice == "d7":
            i= 1   
            return userChoice         
        elif userChoice == "e7":
            i= 1
            return userChoice
        elif userChoice == "f7":
            i= 1
            return userChoice
        elif userChoice == "g7":
            i= 1
            return userChoice
#Sharp Chords
        elif userChoice == "a#":
            i = 1
            return userChoice
        elif userChoice == "c#":
            i = 1
            return userChoice
        elif userChoice == "d#":
            i = 1
            return userChoice
        elif userChoice == "f#":
            i = 1
            return userChoice
        elif userChoice == "g#":
            i = 1
            return userChoice
#Sharp Diminished Chords
        elif userChoice == "a#dim":
            i = 1
            return userChoice
        elif userChoice == "c#dim":
            i = 1
            return userChoice
        elif userChoice == "d#dim":
            i = 1
            return userChoice
        elif userChoice == "f#dim":
            i = 1
            return userChoice
        elif userChoice == "g#dim":
            i = 1
            return userChoice
#Diminished Chords
        elif userChoice == "aDim":
            i = 1 
            return userChoice
        elif userChoice == "bDim":
            i = 1
            return userChoice
        elif userChoice == "cDim":
            i = 1 
            return userChoice
        elif userChoice == "dDim":
            i = 1 
            return userChoice
        elif userChoice == "eDim":
            i = 1
            return userChoice
        elif userChoice == "fDim":
            i = 1 
            return userChoice
        elif userChoice == "gDim":
            i = 1 
            return userChoice
#Sharp Minor Chords
        elif userChoice == "a#m":
            i = 1 
            return userChoice
        elif userChoice == "c#m":
            i = 1 
            return userChoice
        elif userChoice == "d#m":
            i = 1 
            return userChoice
        elif userChoice == "f#m":
            i = 1 
            return userChoice
        elif userChoice == "g#m":
            i = 1 
            return userChoice
        elif userChoice == "help":
            i = 1
            return userChoice
        else:
            invalid = "invalid"
            return invalid
         
def showChart(userChoice):
    
    if userChoice == "a":
        ch.a()
    elif userChoice == "b":
        ch.b()
    elif userChoice == "c":
        ch.c()
    elif userChoice == "d":
        ch.d()         
    elif userChoice == "e":
        ch.e()
    elif userChoice == "f":
        ch.f()
    elif userChoice == "g":
        ch.g()
    elif userChoice == "am":
        ch.am()
    elif userChoice == "bm":
        ch.bm()
    elif userChoice == "cm":
        ch.cm()
    elif userChoice == "dm":
        ch.dm()         
    elif userChoice == "em":
        ch.em()
    elif userChoice == "fm":
        ch.fm()
    elif userChoice == "gm":
        ch.gm()        
    elif userChoice == "a6":
        ch.a6()
    elif userChoice == "b6":
        ch.b6()
    elif userChoice == "c6":
        ch.c6()
    elif userChoice == "d6":
        ch.d6()         
    elif userChoice == "e6":
        ch.e6()
    elif userChoice == "f6":
        ch.f6()
    elif userChoice == "g6":
        ch.g6()  
    elif userChoice == "a7":
        ch.a7()
    elif userChoice == "b7":
        ch.b7()
    elif userChoice == "c7":
        ch.c7()
    elif userChoice == "d7":
        ch.d7()         
    elif userChoice == "e7":
        ch.e7()
    elif userChoice == "f7":
        ch.f7()
    elif userChoice == "g7":
        ch.g7()
    elif userChoice == "a#":
        ch.aSharp()
    elif userChoice == "c#":
        ch.cSharp()
    elif userChoice == "d#":
        ch.dSharp()
    elif userChoice == "f#":
        ch.fSharp()         
    elif userChoice == "g#":
        ch.gSharp() 
    elif userChoice == "a#dim":
        ch.aSharpDim()
    elif userChoice == "c#dim":
        ch.cSharpDim()
    elif userChoice == "d#dim":
        ch.dSharpDim()
    elif userChoice == "f#dim":
        ch.fSharpDim()         
    elif userChoice == "g#dim":
        ch.gSharpDim()
    elif userChoice == "aDim":
        ch.aDim()  
    elif userChoice == "bDim":
        ch.bDim()
    elif userChoice == "cDim":
        ch.cDim() 
    elif userChoice == "dDim":
        ch.dDim()  
    elif userChoice == "eDim":
        ch.eDim()
    elif userChoice == "fDim":
        ch.fDim() 
    elif userChoice == "gDim":
        ch.gDim() 
    elif userChoice =="a#m":
        ch.aSharpm()
    elif userChoice == "c#m":
        ch.cSharpm()
    elif userChoice == "d#m":
        ch.dSharpm()
    elif userChoice == "f#m":
        ch.fSharpm()
    elif userChoice == "g#m":
        ch.gSharpm()
    elif userChoice == "help":
        ch.chordList()
    elif userChoice == "invalid":
        ch.invalid()
        
def keepGoing(): 

    userChoice = input("Would you like to keep going? (y/n): ")   
    if userChoice == "y":
        return 1 
    elif userChoice == "n":
        return 2
    else:
        return 3                     