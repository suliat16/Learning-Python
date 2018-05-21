#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 10:06:57 2018

@author: suliat16

Reads a FASTA file, returns a single string.
"""

import re

class FastaRead():
    
    """
    Open FASTA file and return a stream
    
    Todo: Class information
    """
    
    def __init__(self, fasta=None):
        """
        Initiates FastaRead with given fasta file
        
        """
        self.file=fasta
        self.object=open(self.file, 'r')
        self.read = self.object.read()
        
        
        
    def change_mode(self, mode='r'):
        """
        """
        self.object = open(self.file, mode)
        
        
    def indv_block(self, st= ""):
        """
        """
        fstr=re.split('(>)', st)
        fstr = list(filter(None, fstr))
        return fstr
    
    def get_head(self, index=0):
        """
        """
        fstr= indv_block(self.read)
        fstr=fstr[index]
        fstr=re.split('>|\s', fstr)
        return fstr[0]
    
    def get_sequence(self, index=0):
        """
        """
        fstr=indv_block(self.read)
        fstr=fstr[index]
        fstr= fstr.splitlines()
        for f in fstr:
            if f.startswith(">"):
                fstr.remove(f)
        fstr= "".join(fstr)
        