############################
########## IMPORT ##########
############################
import pulp as plp
from materials import typeA, typeB, grade1, grade2, grade3
from stages import stage1, stage2

#################################
########## MAIN SCRIPT ##########
#################################

T = 20  # days
products = [typeA, typeB, grade1, grade2, grade3]
stages = [stage1, stage2]


if __name__ == "__main__":
    #############################
    ########## PROBLEM ##########
    #############################
    prob = plp.LpProblem('SCA_production_probleme', plp.LpMinimize)

    ###############################
    ########## VARIABLES ##########
    ###############################
    production = plp.LpVariable.dicts(
        'production',
        ((p, s, t) for p in products for s in stages for t in range(T)),
        lowBound=0, cat='Continuous'
    )

    inventory = plp.LpVariable.dicts(
        'inventory',
        ((p, t) for p in products for t in range(T)),
        lowBound=0, cat='Continuous'
    )

    is_produced = plp.LpVariable.dicts(
        'is_p_produced',
        ((p, s, t) for p in products for s in stages for t in range(T)),
        cat=plp.LpBinary
    )

    production_costs = plp.LpVariable.dicts('production_cost', lowBound=0)
    holding_costs = plp.LpVariable('holding_cost', lowBound=0)

    ########################################
    ########## OBJECTIVE FUNCTION ##########
    ########################################
    prob += (production_costs + holding_costs)

    #################################
    ########## CONSTRAINTS ##########
    #################################
    # Inventory for product p in time 0 = p.inventory
    # since at t=0 no production yet and no demand yet
    for p in products:
        prob += inventory[p, 0] == p.inventory
