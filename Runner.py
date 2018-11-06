#Author: Ian Cornish

import UserInteraction as ui


def runChords():
    i = 0
    ui.showChart(ui.getChord())
    while i != 1:  
        cont = ui.keepGoing()
        if cont == 1:
            i = 0 
            ui.showChart(ui.getChord())
        elif cont == 2:
            i = 1 
        elif cont == 3:
            print ("Please enter y or n to proceed: ")    
        
    