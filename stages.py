############################
########## IMPORT ##########
############################
from materials import typeA, typeB, grade1, grade2, grade3


######################################
########## CLASSES CREATION ##########
######################################
class Silo:
    """Initialise Silo which will have different attributes:
    - a grade stored 
    - capacity
    Then those silos will be assigned to a stage"""

    def __init__(self):
        self.capacity = capacity
        self.grade_stored = grade_stored


class Stage:
    """Initalise Stage which will have different attributes
    - a tuple containing what we can product at that stage 
    - a tuple containing the storage capacity and how it is composed
    - the number of hour per week lost due to changeover (lost_capacity)"""

    def __init__(self, production, storage_capacity, lost_capacity):
        self.production = production
        self.storage_capacity = storage_capacity
        self.lost_capacity = lost_capacity


######################################
########## OBJECTS CREATION ##########
######################################

#--- Silos for stage1 ---#
silo1_stage1 = Silo(6000, typeA)
silo2_stage1 = Silo(6000, typeA)
silo3_stage1 = Silo(6000, typeB)

#--- Tanks for stage 2 ---#
tank1_stage2 = Silo(4000, grade1)
tank2_stage2 = Silo(4000, grade2)
tank3_stage2 = Silo(4000, grade3)
tank4_stage2 = Silo(2000, grade3)
tank5_stage2 = Silo(2000, grade1)
tank6_stage2 = Silo(2000, grade1)

#--- Stages ---#
stage1 = Stage((typeA, typeB), (silo1_stage1, silo2_stage1,
                                silo3_stage1), 8)
stage2 = Stage((grade1, grade2, grade3), (tank1_stage2, tank2_stage2,
                                          tank3_stage2, tank4_stage2, tank5_stage2, tank6_stage2),
               20)
