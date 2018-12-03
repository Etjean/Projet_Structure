
# coding: utf-8

from modeller import *
from modeller.automodel import *




log.verbose()    # request verbose output


# # Inward open modelling



env = environ()  # create a new MODELLER environment to build this model in




env.io.atom_files_directory = ['.', './data/structures/inward_open']




a = automodel(env,
              alnfile  = './data/sequences/inward_open/inward_align.pir', # alignment filename
              knowns   = ('4YB9','5EQI', '5EQH','5EQG','4PYP'),     # codes of the templates ,
              sequence = 'Q9NRM0')               # code of the target
a.starting_model= 1                 # index of the first model
a.ending_model  = 1                 # index of the last model
                                    # (determines how many models to calculate)
a.make()                            # do the actual comparative modeling


# # Outward open modelling


env2 = environ()  # create a new MODELLER environment to build this model in




env2.io.atom_files_directory = ['.', './data/structures/outward_open']




b = automodel(env2,
              alnfile  = './data/sequences/outward_open/outward_align.pir', # alignment filename
              knowns   = ('4YBQ','5C65', '4ZWC','4ZWB','4ZW9'),     # codes of the templates ,
              sequence = 'Q9NRM0')               # code of the target
b.starting_model= 1                 # index of the first model
b.ending_model  = 1                 # index of the last model
                                    # (determines how many models to calculate)
b.make()