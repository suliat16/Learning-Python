#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 10:06:57 2018

@author: suliat16

Reads a FASTA file, returns a single string.
"""

class FastaRead:
    
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
        
        
    def change_mode(self, mode='r'):
        """
        """
        self.object = open(self.file, mode)
        
        
    def get_sequence(self):
        """
        """
        strr=self.object.read()
        
        



