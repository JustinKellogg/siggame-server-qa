__author__ = 'Rory/Justin'

import math
import unittest
import random
import Test

bob = Test.Creature(33,2,2,0,120,10,2,1,4,4,4,1,30)
marv = Test.Creature(35,2,3,1,120,40,20,4,2,2,2,7,31)
sally = Test.Creature(37,0,3,1,120,90,20,4,2,2,2,7,31)
plant = Test.Plant(22,0,2,2,33,1)
Test.grid[2][2].append(bob)
Test.grid[2][3].append(marv)
Test.grid[0][3].append(sally)
Test.grid[0][2].append(plant)

class TestSequenceFunctions(unittest.TestCase):
    def setUp(self):
        pass

    #Preconditions:
        #Sally can eat, is in range of the plant
    #Postcondtions:
        #Sally gains health, the plant size is decremented
    def test_eat_a_plant(self):
        self.assertEqual(sally.canEat,True)
        self.assertGreater(plant.size,0)
        rest=sally.eat(plant.x,plant.y)
        print (rest)
        self.assertEqual(sally.currentHealth,90+1*10)
        self.assertEqual(plant.size,2-1)

    #Pre Conditions:
      #Marv can eat, Bob is in range of Marv, Bob is at low health, Marv is at low health
    #Post Conditions:
      #Marv can not eat again, Bob is killed, Marv regains some health
    def test_eat_creature(self):
        self.assertEqual(marv.canEat,True)
        marv.eat(bob.x,bob.y)
        self.assertEqual(marv.canEat,False)
        self.assertEqual(bob.currentHealth,10-(4-1)*Test.damageMul)
        self.assertEqual(marv.currentHealth,40+4*10)

    #Pre Conditions:
      #Marv is moving to a valid locationMarv has movement left, Marv has movement left
    #Post Conditions
      #Marv's location is updated, Marv's health is decremented
    def test_move(self):
        self.assertEqual(Test.getObject(marv.x-1,marv.y),None)
        self.assertGreater(marv.movementLeft,0)
        res = marv.move(marv.x-1,marv.y)
        print (res)
        self.assertEqual([marv.x,marv.y],[1,3])
        self.assertEqual(marv.currentHealth,80-Test.healthPerMove)

    #Pre condition:
        #both sally and marv can breed, both sally and marv have enough health to breed
    #Post condition:
        #neither sally nor marv can breed or eat, sally and marv's health is decremented
        #a new creature is added to Player 2's breeding list
    def test_zbreed(self):
        print (sally.x,sally.y)
        print (marv.x,marv.y)
        self.assertEqual(sally.canBreed,True)
        self.assertEqual(marv.canBreed,True)
        self.assertGreater(marv.currentHealth,Test.healthPerBreed)
        self.assertGreater(sally.currentHealth,Test.healthPerBreed)
        marv.breed(sally)
        self.assertEqual(sally.canEat,False)
        self.assertEqual(marv.canEat,False)
        self.assertEqual(sally.canBreed,False)
        self.assertEqual(marv.canBreed,False)
        self.assertEqual(sally.currentHealth,100-Test.healthPerBreed)
        self.assertEqual(marv.currentHealth,77-Test.healthPerBreed)
        self.assertEqual(len(Test.Player2.breeding),1)


if __name__ == '__main__':
    unittest.main()
