# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Contains:
    A method which takes a codon and returns an amino acid
"""

def codon_to_aa(codon = 'AUG'):
    '''Takes a codon and returns an amino acid.

    Args: 
        codon: A string containing three letter. These letters can be ACUG,
            in any order or number, and each triplet corresponds to an amino acid
        
    Returns: The amino acid associated with the entered codon. If the entered 
        value isn't a codon, a message is returned saying that "That isn't a 
        codon, please try again"
    '''
    
    
    