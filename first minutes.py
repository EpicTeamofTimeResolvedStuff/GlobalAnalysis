# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 17:31:17 2019

@author: lucas
"""

import pandas as pd
import numpy as np

class SurfaceData:
    def __init__(self):
        self.excitation_wavelenght = None
        self.excitaton_power = None
        self.optical_path = None
        self.time_unit = None
        self.wavelenght_unit = None
        self.sample = None
        self.file_name = None
        self.solvent = None
        self.autocorrelation = None
        self.N_scans = None
        self.timestamp = None
        self.frames = None
        self.integration_time = None
        self.comments = None
    
        
    def load(self, filename):
        return None
        
    def loadLille(self, filename):
        self.data=pd.read_csv(filename, sep=',').dropna([1])
        self.time=pd.DataFrame([float(i.split(' ')[0]) for i in self.data.columns[1:]],columns=['time'])
        self.wavelength=self.data[self.data.columns[0]]
        
    def loadSX(self, filename):
        return None

    def loadRAL(self, filename):
        return None
    
name='C://Users/lucas/Desktop/Python/git_things/SurfaceAnalysis/test1/all 10189 DO 0.6 frames 800 cicles 1.asc'    
test1 = SurfaceData()
test1.loadLille(name)

      
        
        