#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 10:13:22 2018

@author: suliat16

Test cases
"""

import unittest
#import fastaReader

class TestFasta(unittest.TestCase):
    def setUp(self):
        self.fasta=FastaRead('1dpx.fasta.txt')
        self.titin=FastaRead('titin.fasta')
        self.multi=FastaRead('multiFasta.fasta')
        
    blockstr = ">AT1G01140.1 (version 1)\nAACCGGTT\n>AT1G01140.1 (version 2)\nTTGGCCAA\n>AT1G01140.2 (version 1)\nCCGGAATT"
    blck=">1DPX:A|PDBID|CHAIN|SEQUENCE\nKVFGRCELAAAMKRHGLDNYRGYSLGNWVCAAKFESNFNTQATNRNTDGSTDYGILQINSRWWCNDGRTPGSRNLCNIPC\nSALLSSDITASVNCAKKIVSDGNGMNAWVAWRNRCKGTDVQAWIRGCRL"
        
    
    def test_get_sequence_lysozyme(self):
        self.assertEqual(self.fasta.get_sequence(),'KVFGRCELAAAMKRHGLDNYRGYSLGNWVCAAKFESNFNTQATNRNTDGSTDYGILQINSRWWCNDGRTPGSRNLCNIPCSALLSSDITASVNCAKKIVSDGNGMNAWVAWRNRCKGTDVQAWIRGCRL')
    
    def test_get_sequence_multi_v2(self):
        self.assertEqual(self.multi.get_sequence(index=1), 'TTGGCCAA')
        
    def test_indv_block(self):
        self.assertEqual(len(self.multi.indv_block(self.blockstr)), 3)
        
    def test_indv_block_multi(self):
        self.assertEqual(self.multi.indv_block(self.blockstr), [">AT1G01140.1 (version 1)\nAACCGGTT\n",">AT1G01140.1 (version 2)\nTTGGCCAA\n", ">AT1G01140.2 (version 1)\nCCGGAATT"])
    
    def test_indv_block_sin(self):
        self.assertEqual(self.fasta.indv_block(self.blck), ['>1DPX:A|PDBID|CHAIN|SEQUENCE\nKVFGRCELAAAMKRHGLDNYRGYSLGNWVCAAKFESNFNTQATNRNTDGSTDYGILQINSRWWCNDGRTPGSRNLCNIPC\nSALLSSDITASVNCAKKIVSDGNGMNAWVAWRNRCKGTDVQAWIRGCRL'])
        
    def test_head(self):
        self.assertEqual(self.multi.get_head(), ['AT1G01140.1', 'AT1G01140.1', 'AT1G01140.2'])
        
    def test_head_single(self):
        self.assertEqual(self.titin.get_head(), ['CAA62188.1'])
        
    def test_head_single2(self):
        self.assertEqual(self.fasta.get_head(), ['1DPX:A'])

    