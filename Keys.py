#Author: Ian Cornish

import Chords as ch
import random as rnd

def majorKeys(): 
    aMajor = [ch.a(), ch.bm(), ch.cSharpm(), ch.d(), ch.e(), ch.fSharpm(), ch.gSharpDim()]
    bMajor = [ch.b(), ch.cSharpm(), ch.dSharpm(), ch.e(), ch.fSharp(), ch.gSharpm(), ch.aSharpDim()]
    cMajor = [ch.c(), ch.dm(), ch.em(),ch.f(), ch.g(), ch.am(), ch.bDim()]
    dMajor = [ch.d(), ch.em(), ch.fSharpm(), ch.g(), ch.a(), ch.bm(), ch.cSharpDim()]
    eMajor = [ch.e(), ch.fSharpm(), ch.gSharpm(), ch.a(), ch.b(), ch.cSharpm(), ch.dSharpDim()]
    fMajor = [ch.f(), ch.gm(), ch.am(), ch.aSharp(), ch.c(), ch.dm(), ch.eDim()]
    gMajor = [ch.g(), ch.am(), ch.bm(), ch.c(), ch.d(), ch.em(), ch.fSharpDim()]
    
    majorKeys = [aMajor, bMajor, cMajor, dMajor, eMajor, fMajor, gMajor]
    #if randomNum == 1:
    #    return aMajor
    #elif randomNum == 2:       
    #    return bMajor
    #elif randomNum == 3:
    #    return cMajor
    #elif randomNum == 4:       
    #    return dMajor
    #elif randomNum == 5:
    #    return eMajor
    #elif randomNum == 6:       
    #    return fMajor
    #elif randomNum == 7:
    #    return gMajor
    
def minorKeys():
    
    aMinor = [ch.am(), ch.bDim(), ch.c(), ch.dm(), ch.em(), ch.f(), ch.g()]
    bMinor = [ch.bm(), ch.cSharpDim(), ch.d(), ch.em(), ch.fSharpm(), ch.g(), ch.a()]
    cMinor = [ch.cm(), ch.dDim, ch.dSharp(), ch.fm(), ch.gm(), ch.gSharp(), ch.aSharp()]
    dMinor = [ch.dm(), ch.eDim(), ch.f(), ch.gm(), ch.am(), ch.aSharp(), ch.c()]
    eMinor = [ch.em(), ch.fSharpDim(), ch.g(), ch.am(), ch.bm(), ch.c(),ch.d()]
    fMinor = [ch.fm(), ch.gDim(), ch.gSharp(), ch.aSharpm(), ch.cm(), ch.cSharp(), ch.dSharp()]
    gMinor = [ch.gm(), ch.aDim(), ch.aSharp(), ch.cm(), ch.dm(), ch.dSharp(), ch.fSharp()]
    
    minorKeys = [aMinor, bMinor, cMinor, dMinor, eMinor, fMinor, gMinor]
    
    #if randomNum == 1:
    #   return aMinor
    #elif randomNum == 2:       
    #   return bMinor
    #elif randomNum == 3:
     #   return cMinor
    #elif randomNum == 4:       
     #   return dMinor
    #elif randomNum == 5:
     #   return eMinor
    #elif randomNum == 6:       
    #   return fMinor
    #elif randomNum == 7:
    #    return gMinor
        
    return minorKeys

def randomKey():
    
    number = rnd.randint(1,7)
    return number
    