# -*- coding: utf-8 -*-
import sys
import re
import json
from os import path
sys.path.append(path.abspath('./Class'))
from File import *

class OutFile(File):
    '''Constructor'''
    def __init__(self,path,isConfig=False,outName=''):
        
        File.__init__(self)
        self.repeats=[] # list of int,  - no repeat, x - number of senetnce 
        if(isConfig):
            self.GenerateOutFileFromJSONConfig(path,outName)
        else:
            self.GenerateOutFile(path)
    
    def HowManyRepeats(self):
        howMany=0
        for number in repeats:
            if(number):howMany+=1
        return howMany
    
    def GenerateOutFileFromJSONConfig(self,config,outName):    
        self.hashedText=config['Hashes']
        self.fileName=outName
        self.repeats=config['Repeats']
        self.clearText=config['Sentences']
        return True
    
    def GenerateOutFile(self,path):
        ''' This method end when OutFile is properly created
            
            TODO: KAMIL
        '''
        self.fileName=path.split('/')[len(path.split('/'))-1]
        if (self.IsLink(path)):  # Contain www or http ? 
            downText=self.DownloadText(path)  
            text=self.ParseHTML(downText)
        else:
            text=self.LoadTextFromFile(path)
        #text=text.encode('utf-8','ignore')
        self.MakeClearAndHashedText(text)

        return True
    
    
    def AddOutFileToConfigJSON(self,configName):
        f = open(configName+'.json', 'r')
        config=f.read()
        f.close()
        config= json.loads(config)
        
        outFile={
        "Sentences": self.clearText,
        "Hashes" : self.hashedText,
        "Repeats": self.repeats
        }
        config['outFiles'][self.fileName]=outFile
        config= json.dumps(config,indent=2)
        f = open(configName+'.json', 'w')
        f.write(config)
        f.close()
        
        return True
    
