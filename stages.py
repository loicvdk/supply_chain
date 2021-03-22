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
    - the number of hour per week lost due to changeover (lost_capacity)"""

    def __init__(self, production, lost_capacity):
        self.production = production
        self.lost_capacity = lost_capacity


######################################
########## OBJECTS CREATION ##########
######################################
silo1_stage1 = Silo(6000, typeA)
silo2_stage1 = Silo(6000, typeA)
silo3_stage1 = Silo(6000, typeB)

stage1 = Stage((typeA, typeB), 8)
stage2 = None
