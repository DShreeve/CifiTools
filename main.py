from modNode import ModNode, Algo
from utilMath import cifiTruncate

def main():
    level = 0
    testNode = ModNode("test", "A01", True, None, level, 50, Algo.BASE_ALGO, 0, 1,	1.2, 1.32, 0.04)

    for _ in range(10):
        print(f"CurrentLevel: {testNode.level}, upgradeCost: {testNode.current_cost}")
        testNode.buy()

    modBoosts = {
        "playerProfile" : 35.56,
        "junoCard" : 1.25,
        "store" : 1.40,
        "daily" : 1.07, 
        "loopMod" : 26.00,
        "shard2" : 5.11,
        "ship1" : 6.62,
        "ship2" : 3.55,
        "milestone" : 1.05
    }
    modTotal = 1
    for name, boost in modBoosts.items():
        modTotal = modTotal * boost
    print(f"ModTotalBoost: {modTotal}")

    shardBoosts = {
        "playerProfile" : 1.42,
        "junoCard" : 1.45,
        "lyraCard" : 1.50,
        "loopMod" : 3.07,
        "shard5" : 1.34,
        "operations" : 1.13,

    }
    shardTotal = 1
    for name, boost in shardBoosts.items():
        shardTotal = cifiTruncate(cifiTruncate(shardTotal) * cifiTruncate(boost))
    print(f"shardTotalBoost: {shardTotal}")
if __name__ == "__main__":
    main()