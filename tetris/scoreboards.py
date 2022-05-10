from random import randint



class Cell:
    def __init__(self, bpc: int):
        self.bpc = bpc
        
    def setblockpercell(self, block: int) -> None:
        self.bpc = block

            
class Block:
    def __init__(self, color: int, block: int, maxblocks: int, locked: int) -> None:
        self.color = color  
        self.block = block
        self.maxblocks = maxblocks
        self.locked = locked

class Current(Block):
    def __init__(self, color: int, block: int, next_block: int, hold_block: int, cell: int) -> None:
        super().__init__(color, block, 1, False)
        self.next = Next(next_block)
        self.hold = Hold(hold_block)
        self.cell = Cell(cell)
        self.block_list = []
        
    
    def currentblock(self):
        self.block = self.block_list[0]

    def nextblock(self):
        self.falling = self.block_list.pop(0)
        self.block_list.append(self.next.randomblock(7))
    
    def addblock(self, block: int) -> None:
        if len(self.block_list) < Next.maxblocks:
            self.block_list.append(block)

    def lockblock(self) -> None:
        if self.block_list < self.maxblocks:
            self.hold.holding(self.block)

    def oneblockpercell(self) -> None:
        Cell.setblockpercell(1)

    def lock(self) -> None:
        self.locked = True

    def unlock(self) -> None:
        self.locked = False



class Hold(Block):
    def __init__(self, color: int, block: int) -> None:
        super().__init__(color, block, 1, True)

    def holding(self, holdingblock: int) -> None:
        self.hold_block = holdingblock

    def lock(self) -> None:
        self.locked = True

    def unlock(self) -> None:
        self.locked = False


class Next(Block):
    def __init__(self, color: int, block: int) -> None:
        super().__init__(color, block, 5, True) 

    def randomblock(self, maxblocks: int) -> None:
        self.next_block = randint(0, maxblocks)
        
    def lock(self) -> None:
        self.locked = True

    def unlock(self) -> None:
        self.locked = False
        



class Level:
    def __init__(self, level: int) -> None:
        self._level = level
        self._current_level = level

    def addlvl(self, number: int) -> None:
        if number < 10:
            self._current_level += number
            
    def setlvl(self, number: int) -> None:
        if number < 0: 
            raise ValueError("You cannot go below level 0!")
            
        if number > 10:
            raise ValueError("Level 10 is the highest level!")

        self._current_level = number

    def get_current_level(self) -> int:
        return self._current_level
    
    def highestlevel(self) -> None:
        if self._level < self._current_level:
            self._level = self._current_level

    def get_highestlevelreached(self) -> int:
        return self._level
    

class Score:
    def __init__(self, points: int) -> None:
        self._points = points
        self._current_points = points


    def setpoints(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("The points value cannot be below 0!")
        self._current_points = amount

    def highscore(self) -> None:
        if self._points < self._current_points:
            self._points = self._current_points

    def get_current_points(self) -> int:
        return self._current_points

    def get_highscore(self) -> int:
        return self._points

    # def multiplier(self, multiplied: int) ->


#client code
t = Text(0, 0)


