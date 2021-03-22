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

    def __init__(self, capacity, grade_stored):
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
storage_type_A = Silo(12000, typeA)
storage_type_B = Silo(6000, typeB)

#--- Tanks for stage 2 ---#
storage_grade1 = Silo(8000, grade1)
storage_grade2 = Silo(4000, grade2)
storage_grade3 = Silo(6000, grade3)


#--- Stages ---#
stage1 = Stage((typeA, typeB), (storage_type_A, storage_type_B),
               8)
stage2 = Stage((grade1, grade2, grade3), (storage_grade1, storage_grade2,
                                          storage_grade3),
               20)
