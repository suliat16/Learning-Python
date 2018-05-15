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
        codon: A string containing three letter. These letters can be ACUG, all caps,
            in any order or number, and each triplet corresponds to an amino acid
        
    Returns: The amino acid associated with the entered codon. If the entered 
        value isn't a codon, a message is returned saying that "That isn't a 
        codon, please try again"
    '''

# =============================================================================
#     if codon == 'AUG':
#         return 'Methionine'
#     elif codon == 'UUU' or 'UUC':
#         return 'Phenylalanine'
#     elif codon == 'UUA' or 'UUA' or 'CUU' or 'CUC' or 'CUA' or 'CUG':
#         return 'Leucine'
#     elif codon == 'AUU' or 'AUC' or 'AUA':
#         return 'Isoleucine'
#     elif codon == 'GUU' or 'GUC' or 'GUA' or 'GUG':
#         return 'Valine'
#     elif codon == 'UCU' or 'UCC' or 'UCA' or 'UCG':
#         return 'Serine'
#     elif codon ==  'CCU' or 'CCC' or 'CCA' or 'CCG':
#         return 'Proline'
#     elif codon == 'ACU' or 'ACC' or 'ACA' or 'ACG':
#         return 'Threonine'
#     elif codon == 'GCU' or 'GCC' or 'GCA' or 'GCG':
#         return 'Alanine'
#     elif codon == 'UAU' or 'UAC' :
#         return 'Tyrosine'
#     elif codon == 'CAU' or 'CAC':
#         return 'Histidine'
#     elif codon == 'CAA' or 'CAG':
#         return 'Glutamine'
#     elif codon == 'AAU' or 'AAC':
#         return 'Lysine'
#     elif codon == 'GAU' or 'GAC':
#         return 'Glutamate'
#     elif codon == 'UGU' or 'UGC':
#         return 'Cysteine'
#     elif codon == 'UGG':
#         return 'Tryptophan'
#     elif codon == 'CGU' or 'CGC' or ' CGA' or 'CGG' or 'AGA' or 'AGG':
#         return 'Arginine'
#     elif codon == 'AGU' or 'AGC':
#         return 'Serine'
#     elif codon == 'GGU' or 'GGC' or 'GGA' or 'GGG':
#         return 'Glycine'
#     else:
#         return 'Stop codon'
# =============================================================================
    
print (33)