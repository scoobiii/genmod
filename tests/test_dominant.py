#!/usr/bin/env python
# encoding: utf-8
"""
test_models_compound.py

Test the so that the genetic models behave as suspected.


Created by Måns Magnusson on 2013-03-07.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os
from ped_parser import family, individual
from genmod.models import genetic_models
from genmod.variants import genotype


class TestModelsCompound(object):
    """Test class for testing how the genetic models behave with a recessive variant"""

    def setup_class(self):
        """Setup a simple family with family id 1, sick son id 1,
         healthy father id 2, healthy mother id 3"""
        # Setup family with sick kid, sick father and healthy mother:
        self.dominant_family = family.Family(family_id = '1')
        sick_son = individual.Individual(ind='1', family='1',mother='3', father='2', sex=1, phenotype=2)
        sick_father = individual.Individual(ind='2', family='1',mother='0', father='0', sex=1, phenotype=2)
        healthy_mother = individual.Individual(ind='3', family='1',mother='0', father='0', sex=2, phenotype=1)
        
        self.dominant_family.add_individual(sick_father)
        self.dominant_family.add_individual(sick_son)
        self.dominant_family.add_individual(healthy_mother)
        
        self.dominant_variant = {'CHROM':'1', 'POS':'5', 'ALT':'A', 'REF':'C', 'ID':'rs2230749', '1':'0/1', '2':'0/1', '3':'0/0'}
        
        self.dominant_missing = {'CHROM':'1', 'POS':'10', 'ALT':'C', 'REF':'T', 'ID':'.', '1':'0/1', '2':'./.', '3':'0/0'}
        
        self.not_dominant = {'CHROM':'1', 'POS':'15', 'ALT':'C', 'REF':'T', 'ID':'.', '1':'0/1', '2':'0/1', '3':'0/1'}

        
        #This batch simulates two genes, one variant is present in both genes
        batch = {'ABC':{'1_5_A_C':self.dominant_variant, '1_10_C_T':self.dominant_missing, '1_15_C_T':self.not_dominant}}
        
        genetic_models.check_genetic_models(batch_1, self.dominant_family, verbose=True)

            
    def test_dominant_variant(self):
        """Check if the genetic models are followed for the heterozygote variant"""
        assert not self.dominant_variant['Inheritance_model']['AR_hom']
        assert not self.dominant_variant['Inheritance_model']['AR_hom_denovo']
        assert self.dominant_variant['Inheritance_model']['AD']
        assert not self.dominant_variant['Inheritance_model']['AD_denovo']
        assert not self.dominant_variant['Inheritance_model']['X']
        assert not self.dominant_variant['Inheritance_model']['X_dn']
        # assert not self.dominant_variant['Inheritance_model']['AR_compound']
    
    def test_dominant_missing(self):
        """docstring for test_not_dominant_comp"""
        assert not self.dominant_missing['Inheritance_model']['AR_hom']
        assert not self.dominant_missing['Inheritance_model']['AR_hom_denovo']
        assert self.dominant_missing['Inheritance_model']['AD']
        assert self.dominant_missing['Inheritance_model']['AD_denovo']
        assert not self.dominant_missing['Inheritance_model']['X']
        assert not self.dominant_missing['Inheritance_model']['X_dn']
        # assert not self.dominant_missing['Inheritance_model']['AR_compound']
    
    def test_not_dominant(self):
        """docstring for test_dominant_comp_missing"""
        assert not self.not_dominant['Inheritance_model']['AR_hom']
        assert not self.not_dominant['Inheritance_model']['AR_hom_denovo']
        assert not self.not_dominant['Inheritance_model']['AD']
        assert not self.not_dominant['Inheritance_model']['AD_denovo']
        assert not self.not_dominant['Inheritance_model']['X']
        assert not self.not_dominant['Inheritance_model']['X_dn']
        # assert not self.not_dominant['Inheritance_model']['AR_compound']
            


def main():
    pass


if __name__ == '__main__':
    main()

