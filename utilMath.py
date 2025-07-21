import math

def commonExpo(start_cost, cost_growth, start_base, base_growth, level):
    # Formula:
    #                  term1                    term2
    # upgradeCost = ((sc + level) * cg) * (((sb + level) * bg) ^ level)
    #
    # where:
    #   sc = Starting cost
    #   cg = Cost growth
    #   sb = start base
    #   bg = base growth
    #   level = the current level of node
    term1 = start_cost + (level * cost_growth)
    term2 = start_base + (level * base_growth)
    value = term1 * (term2 ** level)
    return value

def cifiTruncate(num):
    num = num * 100
    num = math.floor(num)
    num = num / 100
    return num

def commonExpo2(start_cost, cost_growth, start_base, base_growth, level):
    # sc_log+LOG10(1+level*POW(10,cg_log-sc_log))+level*LOG10(sb+level*bg))
    sc_log = math.log10(start_cost)
    cg_log = math.log10(cost_growth)

    term1 = sc_log + math.log10(1+(level* 10 **(cg_log -sc_log)))
    term2 = level*math.log10(start_base+level*base_growth)
    res = term1 + term2

