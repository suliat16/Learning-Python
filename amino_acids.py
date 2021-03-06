# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Contains:
    A method which takes a codon and returns an amino acid
"""

def codon_dict():
    """
    A dictionary relating codons to amino acids
    
    A dictionary where the keys are the codons and the values are the corresponding
    amino acids
    
    Args:
        
    Returns: A dictionary mapping an amino acid to each codon
    """
    
    ct = dict()
    ct['AUG']= 'Methionine'
    ct['UUU']= 'Phenylalanine'
    ct['UUC']= 'Phenylalanine'
    ct['UUA']= 'Leucine'
    ct['UUG']= 'Leucine'
    ct['CUU']= 'Leucine'
    ct['CUC']= 'Leucine'
    ct['CUA']= 'Leucine'
    ct['CUG']= 'Leucine'
    ct['AUU']= 'Isoleucine'
    ct['AUC']= 'Isoleucine'
    ct['AUA']= 'Isoleucine'
    ct['GUU']= 'Valine'
    ct['GUC']= 'Valine'
    ct['GUA']= 'Valine'
    ct['GUG']= 'Valine'
    ct['UCU']= 'Serine'
    ct['UCC']= 'Serine'
    ct['UCA']= 'Serine'
    ct['UCG']= 'Serine'
    ct['CCU']= 'Proline'
    ct['CCC']= 'Proline'
    ct['CCA']= 'Proline'
    ct['CCG']= 'Proline'
    ct['ACU']= 'Threonine'
    ct['ACC']= 'Threonine'
    ct['ACA']= 'Threonine'
    ct['ACG']= 'Threonine'
    ct['GCU']= 'Alanine'
    ct['GCC']= 'Alanine'
    ct['GCA']= 'Alanine'
    ct['GCG']= 'Alanine'
    ct['UAU']= 'Tyrosine'
    ct['UAC']= 'Tyrosine'
    ct['CAU']= 'Histidine'
    ct['CAC']= 'Histidine'
    ct['CAA']= 'Glutamine'
    ct['CAG']= 'Glutamine'
    ct['AAU']= 'Asparagine'
    ct['AAC']= 'Asparagine'
    ct['AAA']= 'Lysine'
    ct['AAG']= 'Lysine'
    ct['GAA']= 'Glutamate'
    ct['GAG']= 'Glutamate'
    ct['GAU']= 'Aspartate'
    ct['GAC']= 'Aspartate'
    ct['UGU']= 'Cysteine'
    ct['UGC']= 'Cysteine'
    ct['UGG']= 'Tryptophan'
    ct['CGU']= 'Arginine'
    ct['CGC']= 'Arginine'
    ct['CGA']= 'Arginine'
    ct['CGG']= 'Arginine'
    ct['AGA']= 'Arginine'
    ct['AGG']= 'Arginine'
    ct['AGU']= 'Serine'
    ct['AGC']= 'Serine'
    ct['GGU']= 'Glycine'
    ct['GGC']= 'Glycine'
    ct['GGA']= 'Glycine'
    ct['GGG']= 'Glycine'
    ct['UAA']= 'Stop codon'
    ct['UAG']= 'Stop codon'
    ct['UGA']= 'Stop codon'
    
    return ct

def amino_dict():
    ''' A dictionary relating amino acids to potential codons
    Args:
    
    Returns: A dictionary mapping each amino acid to the codons that encode for it
    '''
    at = dict()
    at[('alanine', 'a', 'ala')]= ['GCC', 'GCA', 'GCU', 'GCG']
    at[('arginine', 'arg', 'r')]= ['CGC', 'CGU', 'CGA', 'CGG', 'AGA', 'AGG']
    at[('asparagine', 'asn', 'n')]= ['AAU', 'AAC']
    at[('aspartate', 'aspartic acid', 'asp', 'd')]=['GAU', 'GAC']
    at[('cysteine', 'cys', 'c')]=['UGU', 'UGC']
    at[('glutamine', 'gln', 'e')]=['CAA', 'CAG']
    at[('glutamate', 'glutamic acid', 'glu', 'q')]= ['GAA', 'GAG']
    at[('glycine', 'gly', 'g')]= ['GGU', 'GGC', 'GGA', 'GGG']
    at[('histidine', 'his', 'h')]=['CAU', 'CAC']
    at[('isoleucine', 'ile', 'i')]= ['AUU', 'AUC', 'AUA']
    at[('leucine', 'leu', 'l')]=['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG']
    at[('lysine', 'lys', 'k')]= ['AAC', 'AAG'] 
    at[('methionine', 'met', 'm')]=['AUG']
    at[('phenylalanine', 'phe', 'f')]= ['UUU', 'UUC']
    at[('proline', 'pro', 'p')]= ['CCU', 'CCC', 'CCA', 'CCG'] 
    at[('serine', 'ser', 's')]= ['AGU', 'AGC']
    at[('threonine', 'thr', 't')]= ['ACU', 'ACC', 'ACA', 'ACG']
    at[('tryptophan', 'trp', 'w')]=['UGG']
    at[('tyrosine', 'tyr', 'y')]= ['UAU', 'UAC'] 
    at[('valine', 'val', 'v')]= ['GUU', 'GUC', 'GUA', 'GUG']
   
    return at
    
    
def codon_to_aa(codon = 'AUG'):
    """
    Take a codon and return an amino acid.

    Args: 
        codon (str): A string containing three letter. These letters can be ACUG,
            in any order, and each triplet corresponds to an amino acid
        
    Returns: The amino acid associated with the entered codon. 
    
    Raise: 
        If the entered value isn't a codon, a message is returned saying that "That isn't a 
        codon, please try again"
    """
    cdict = codon_dict()
    codon = codon.upper()
    #assert(codon in cdict.keys()), "That isn't a codon, please try again."
    try:
        return cdict[codon]
    except KeyError:
        print("That isn't a codon, please try again.")

def aa_to_codon(aa= 'W'):
    """
    Take an amino acid and return the codons encoding for it
    
    Args:
        aa (str) : A string either containing the amino acid name, its 3 letter code, or 
            its 1 letter code
    Returns:
        A list of the codons that could have coded for the amino acid
    """
    
    adict = amino_dict()
    aa = aa.lower()
    akeys = adict.keys()
    
    try:
        for x in akeys:
            if aa in x:
                return adict[x]
        raise KeyError
    except KeyError:
        print("That isn't an amino acid, please try again")
  