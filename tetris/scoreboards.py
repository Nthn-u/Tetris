from random import randint



class Cell:
    def __init__(self, hold_block: int, next_block: int, current_block: int, maxblocks: int):
        self.hold = Hold(hold_block)
        self.next = Next(next_block)
        self.current_block = current_block
        self.block_list = []
        self._maxblocks = maxblocks
        

    def lockblock(self) -> None:
        self.hold.holding(self.current_block)

    def nextblock(self) -> None:
        self.falling = self.block_list.pop(0)
        self.block_list.append(self.next.randomblock(7))

    def addblock(self, block: int) -> None:
        if len(self.block_list) < self._maxblocks:
            self.block_list.append(block)
            

class Hold:
    def __init__(self, block: int) -> None:
        self.block = block
        self.hold_block = block

    def holding(self, holdingblock: int) -> None:
        self.hold_block = holdingblock


class Next:
    def __init__(self, block: int) -> None:
        self.nblock = block
        self.next_block = block

    def randomblock(self, maxblocks: int) -> None:
        self.next_block = randint(0, maxblocks)
        
        






class Text:
    def __init__(self, game_points: int, game_lvl: int):
        self.score = Score(game_points)
        self.round = Level(game_lvl)

    def lvlincrease(self):
        self.round.addlvl(1)


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
cell1 = Cell(0, randint(0, 7), 0, 7)

