from src.GameLogic.GenericGameLogic import GenericGameLogic


class CreateCharacter(GenericGameLogic):
    
    def __init__(self,channel):
        super(self, channel)
        

        
#    def messageReceive(self,message):
        
    def createCharacter(race,occupation):
        hp = 120
        spd = 15
        attk = 10
        mp = 15
        crt = 2

        if race == 'elf': 
            spd += 10
            attk += 5
            mp +=10
            crt +=2
       
        elif race == 'dwarf':
            spd -= 5
            hp += 90
            mp -= 5

        elif race == 'troll':
            hp += 90
            attk += 10
            spd -= 10
            mp -=15
            
        elif race == 'gnome':
            hp -=20
            spd +=20
            attk += 5
            crt+=5
        elif race == 'human':
            hp += 20
            attk +=10
            mp +=5
            spd +=5
            
        if occupation == 'thief':
            spd += 10
            hp -=10
            attk += 5
            crt +=1

        elif occupation == 'smith':
            hp += 20
        
        elif occupation == 'drunk':
            attk -= 4
            crt += 4
        elif occupation == 'librarian':
            hp += 5
            mp += 10

        elif occupation == 'hunter':
            attk += 5
            crt +=5

        


