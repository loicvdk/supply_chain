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
# products_stage1 = [typeA, typeB]
# products_stage2 = [grade1, grade2, grade3]
stages = [stage1, stage2]

demand = {
    grade1: [1000 for x in range(T)],
    grade2: [1000 for x in range(T)],
    grade3: [1000 for x in range(T)]
}

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
        ((p, s, t) for p in products for s in stages for t in range(T)),
        lowBound=0, cat='Continuous'
    )

    is_produced = plp.LpVariable.dicts(
        'is_p_produced',
        ((p, s, t) for p in products for s in stages for t in range(T)),
        cat=plp.LpBinary
    )

    production_costs = plp.LpVariable('production_cost', lowBound=0)
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
        if p == typeA or p == typeB:
            prob += inventory[p, stages[0], 0] == p.inventory
        else:
            prob += inventory[p, stages[1], 0] == p.inventory

    # NEED TO DEFINE THE DEMAND FOR GRADE 1 2 3
    for p in products:
        for t in range(1, T):
            if p == typeA or p == typeB:
                if p == typeA:
                    prob += inventory[p, stages[0], t] == inventory[p, stages[0], t-1] + production[p,
                                                                                                    stages[0], t] - 0.9 * (production[grade1, stages[1], t] + production[grade2, stages[1], t])
                else:
                    prob += inventory[p, stages[0], t] == inventory[p, stages[0], t-1] + \
                        production[p, stages[0], t] - 0.9 * \
                        production[grade3, stages[1], t]
            else:
                prob += inventory[p, stages[1], t] == inventory[p, stages[1],
                                                                t-1] + production[p, stages[1], t] - demand[p][t]

    for s in stages:
        for p in products:
            for t in range(T):
                prob += inventory[p, s, t] <= [x.capacity if x.grade_stored ==
                                               p else print('') for x in s.storage_capacity]

    for s in stages:
        for t in range(T):
            binary = 0
            for p in products:
                binary += is_produced[p, s, t]
            prob += binary <= 1

    for p in products:
        for s in stages:
            for t in range(T):
                prob += production[p, s,
                                   t] <= (24 - s.lost_capacity) * p.production_rate

    for t in range(T):
        prob += production[grade1, stages[1], t] == 0.9 * \
            inventory[typeA, stages[0], t]

    for t in range(T):
        prob += production[grade2, stages[1], t] == 0.9 * \
            inventory[typeA, stages[0], t]

    for t in range(T):
        prob += production[grade3, stages[1], t] == 0.9 * \
            inventory[typeB, stages[0], t]

    prob += plp.lpSum([p.variable_costs*production[p, s, t]
                       for p in products for s in stages for t in range(T)]) == production_costs

    prob.solve()
    print(production_costs.varValue, holding_costs.varValue)
