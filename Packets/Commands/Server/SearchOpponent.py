import time

from Utils.Writer import Writer


class SearchOpponent(Writer):
    def __init__(self, client, pvp):
        super().__init__(client)
        self.pvp = pvp
        self.id = 24101

    def encode(self):
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0) #Troop
        self.writeInt(1) #Spell
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        
        #WinorLose?
        
        self.writeInt(0) #unk
        self.writeInt(0) #Win
        self.writeInt(1) #Lose
        self.writeInt(0)
        self.writeInt(1)
        
        self.writeByte(0) #unk boolean
        
        self.writeByte(0) #unk boolean
        
        self.writeInt(0)
        
        self.writeInt(1000000) #array 1, Place Barbarian
        
        self.writeInt(143996) #array 2, Place Archer
        
        self.writeInt(1000015) #array 3, Place Goblin
        
        self.writeInt(1000014) #array 4, Place Wall Breaker
        
        self.writeInt(1000002) #array 5, Place Dragon
        
        self.writeInt(1000003) #array 6, Place Witch
        
        self.writeInt(1000005) #array 7, Wizard
        
        self.writeInt(1000006) #array 8, Valkyrie
        
        self.writeInt(1000008) #array 9, Ice Golem
        
        self.writeInt(1000007) #array 10, Golem
        
        self.writeInt(1000010) #array 11 Hog Rider
        
        self.writeInt(1000011) #array 12 Minions
        
        self.writeInt(8000006) #array 13, Electro Dragon
        
        self.writeInt(277200) #array 14, Spell Heal
        
        self.writeInt(12000005) #array 15, Spell Rage
        
        self.writeInt(561881117) #array 16, Spell Clone
