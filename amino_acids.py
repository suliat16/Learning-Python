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
    ct['AAU']= 'Lysine'
    ct['AAC']= 'Lysine'
    ct['GAU']= 'Glutamate'
    ct['GAC']= 'Glutamate'
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
    ct['UGA'] = 'Stop codon'
    
    return ct[codon]
    
# =============================================================================
# #     if codon == 'AUG':
# #         return 'Methionine'
# #  #   elif codon == 'UUU' or 'UUC':
# #         return 'Phenylalanine'
# #     elif codon == 'UUA' or 'UUA' or 'CUU' or 'CUC' or 'CUA' or 'CUG':
# #         return = 'Leucine'
# #     elif codon == 'AUU' or 'AUC' or 'AUA':
# #         return = 'Isoleucine'
# #     elif codon == 'GUU' or 'GUC' or 'GUA' or 'GUG':
# #         return ='Valine'
# #     elif codon == 'UCU' or 'UCC' or 'UCA' or 'UCG':
# #         return = 'Serine'
# #     elif codon ==  'CCU' or 'CCC' or 'CCA' or 'CCG':
# #         return = 'Proline'
# #     elif codon == 'ACU' or 'ACC' or 'ACA' or 'ACG':
# #         return = 'Threonine'
# #     elif codon == 'GCU' or 'GCC' or 'GCA' or 'GCG':
# #         return = 'Alanine'
# #     elif codon == 'UAU' or 'UAC':
# #         return = 'Tyrosine'
# #     elif codon == 'CAU' or 'CAC':
# #         return = 'Histidine'
# #     elif codon == 'CAA' or 'CAG':
# #         return = 'Glutamine'
# #     elif codon == 'AAU' or 'AAC':
# #         return = 'Lysine'
# #     elif codon == 'GAU' or 'GAC':
# #         return = 'Glutamate'
# #     elif codon == 'UGU' or 'UGC':
# #         return = 'Cysteine'
# #     elif codon == 'UGG':
# #         return = 'Tryptophan'
# #     elif codon == 'CGU' or 'CGC' or ' CGA' or 'CGG' or 'AGA' or 'AGG':
# #         return = 'Arginine'
# #     elif codon == 'AGU' or 'AGC':
# #         return = 'Serine'
# #     elif codon == 'GGU' or 'GGC' or 'GGA' or 'GGG':
# #         return = 'Glycine'
# #     else:
# #         return 'Stop codon'
# =============================================================================
    