#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 10:06:57 2018

@author: suliat16

Reads a FASTA file, returns a single string.
"""

import re
from itertools import chain

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
          
    
    def get_head(self):
        """
        """
        fstr= self.indv_block(st=self.read)
        fstr = [f.splitlines() for f in fstr]
        fstr = list(chain.from_iterable(fstr))
        astr = []
        for f in fstr:
            if f.startswith(">"): 
                astr.append(f)
        astr = [re.split('[|\s]',f) for f in astr]
        print(astr)
        rstr = []
        for f in astr:
            r = f[0].replace(">", "")
            rstr.append(r)
        return rstr
    
    def get_sequence(self, index=0):
        """
        Given a fasta file, return the sequence at the given index
        
        Args:
            index(int): For a fasta file with muyltiple proteins, is the zero
                indexed position of the desired protein within the file
        
        Returns: 
            The sequence of the specified protein, as a single string, with newline
            characters removed.
        """
        fstr= self.indv_block(st=self.read)
        fstr=fstr[index]
        fstr= fstr.splitlines()
        for f in fstr:
            if f.startswith('>'):
                fstr.remove(f)
        fstr= "".join(fstr)
        return fstr
        
    def indv_block(self, st=""):
        """
        Return the header line and the sequence of individual constructs in a file
        
        Args:
            st(str): The text contained in a fasta file, as a string. Consists of a 
                header, which is inititated by > and ends with a newline. Subsequent 
                lines are sequence data, until another > is found.
            
        Returns: 
            A list of strings, where each string is the construct header and sequence,
            as a single string. For example, a file containing 4 proteins would
            a list of 4 strings. Each string begins with >, and contains both the
            headers and the newline characters. 
        """
        fstr=re.split('>',st)
        fstr = list(filter(None, fstr))
        fstr = ['>' + f for f in fstr]
        return fstr
    