######################################
########## CLASSES CREATION ##########
######################################
class Material:
    """Initialise materials with a name, an hourly production rate and 
    the unit variable cost in EUR/ton"""

    def __init__(self, name, production_rate, variable_costs, inventory):
        self.name = name
        self.production_rate = production_rate
        self.variable_costs = variable_costs
        self.inventory = inventory


class Grade(Material):
    """Initialise Grade based on Material, this allows us to use the raw material needed
    which will be either typeA or typeB and the amount of type needed, in our case 0.9 ton/ton
    """

    def __init__(self, name, production_rate, variable_costs, raw_material, raw_material_needed):
        super().__init__(name, production_rate, variable_costs)
        self.raw_material = raw_material
        self.raw_material_needed = raw_material_needed


######################################
########## OBJECTS CREATION ##########
######################################
typeA = Material('type A', 75, 1.48, 2513)
typeB = Material('type B', 62, 1.62, 5973)

grade1 = Grade('grade 1', 91, 1.63, typeA, 0.9, 5602)
grade2 = Grade('grade 2', 76, 1.69, typeA, 0.9, 1203)
grade3 = Grade('grade 3', 83, 1.74, typeB, 0.9, 4118)
