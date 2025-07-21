from dataclasses import dataclass
from typing import Optional
from enum import Enum
from utilMath import commonExpo, cifiTruncate

class Algo(Enum):
    BASE_ALGO = 1
    OTHER_ALGO = 2



@dataclass
class ModNode:
    name: str
    code: str
    unlocked: bool
    parent: Optional['ModNode'] 
    level: int
    max_level: int
    algo: Algo
    current_cost: float
    start_cost: float
    cost_growth: float
    start_base: float
    base_growth: float

    def buy(self):
        self.levelUp()
        self.update_current_cost()
        

    def update_current_cost(self):
        print(f"{self.name} updated cost to: {self.current_cost}")
        self.current_cost = cifiTruncate(self.getNextUpgradeCost())

    def getNextUpgradeCost(self):
        value = 0
        if (self.algo == Algo.BASE_ALGO):
            value = commonExpo(self.start_cost, self.cost_growth,
                                self.start_base, self.base_growth, self.level)
        return value
    
    def levelUp(self):
        self.level += 1
        print(f"{self.name} leveled up to {self.level}!")
        return self.level