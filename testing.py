"""
    Assignment 2 - Testing
    FIT2004: Algorithms and Data Structures
    Ahmad Abu-Shaqra
    20/10/2023

"""

import unittest
from EdmondKarps import allocate

# 1: Customized Auto-Complete

class TestingQ1(unittest.TestCase):

    def test_01(self):
        
        # initialising test
        prefix = 'a'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, 'aberr')
        self.assertEqual(definition, 'To wander; to stray. [Obs.] Sir T. Browne.')
        self.assertEqual(frequency, 3000)
    
    def test_02(self):
        
        # initialising test
        prefix = 'an'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, 'andantino')
        self.assertEqual(definition, 'Rather quicker than andante; between that allegretto.')
        self.assertEqual(frequency, 205)

    def test_03(self):
        
        # initialising test
        prefix = 'ana'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, 'analeptic')
        self.assertEqual(definition, 'Restorative; giving strength after disease. -- n.')
        self.assertEqual(frequency, 161)

    def test_04(self):
        
        # initialising test
        prefix = 'anac'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, 'anaclastic')
        self.assertEqual(definition, 'Produced by the refraction of light, as seen through water; as, anaclastic curves.')
        self.assertEqual(frequency, 24)

    def test_05(self):
        
        # initialising test
        prefix = 'anace'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, None)
        self.assertEqual(definition, None)
        self.assertEqual(frequency, 0)
    
    def test_06(self):
        
        # initialising test
        prefix = ''
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, 'aberr')
        self.assertEqual(definition, 'To wander; to stray. [Obs.] Sir T. Browne.')
        self.assertEqual(frequency, 3000)

    def test_07(self):
        
        # initialising test
        prefix = 'ba'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, None)
        self.assertEqual(definition, None)
        self.assertEqual(frequency, 0)

    def test_08(self):
        
        # initialising test
        prefix = 'xyz'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, None)
        self.assertEqual(definition, None)
        self.assertEqual(frequency, 0)

    def test_09(self):
        
        # initialising test
        prefix = 'abu'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, 'abutter')
        self.assertEqual(definition, 'One who, or that which, abuts. Specifically, the owner of a contiguous estate; as, the abutters on a street or a river.')
        self.assertEqual(frequency, 17)

    def test_10(self):
        
        # initialising test
        prefix = 'az'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, None)
        self.assertEqual(definition, None)
        self.assertEqual(frequency, 0)

    def test_11(self):
        
        # initialising test
        prefix = 'absurd'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, 'absurdly')
        self.assertEqual(definition, 'In an absurd manner.')
        self.assertEqual(frequency, 3)
    
    def test_12(self):
        
        # initialising test
        prefix = 'aware'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, None)
        self.assertEqual(definition, None)
        self.assertEqual(frequency, 0)

    def test_13(self):
        
        # initialising test
        prefix = 'aco'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, 'aconite')
        self.assertEqual(definition, 'The herb wolfsbane, or monkshood; -- applied to any plant of the genus Aconitum (tribe Hellebore), all the species of which are poisonous.')
        self.assertEqual(frequency, 32)

    def test_14(self):
        
        # initialising test
        prefix = 'acol'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, 'acold')
        self.assertEqual(definition, 'Cold. [Obs.] "Poor Tom\'s acold." Shak.')
        self.assertEqual(frequency, 8)

    def test_15(self):
        
        # initialising test
        prefix = 'abg'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, 'abgeordnetenhaus')
        self.assertEqual(definition, 'See Legislature, Austria, Prussia.')
        self.assertEqual(frequency, 1)

    def test_16(self):
        
        # initialising test
        prefix = 'asd'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, None)
        self.assertEqual(definition, None)
        self.assertEqual(frequency, 0)

    def test_17(self):
        
        # initialising test
        prefix = 'ay'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, None)
        self.assertEqual(definition, None)
        self.assertEqual(frequency, 0)

    def test_18(self):
        
        # initialising test
        prefix = 'ae'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, 'aerometric')
        self.assertEqual(definition, 'Of or pertaining to aërometry; as, aërometric investigations.')
        self.assertEqual(frequency, 97)

    def test_19(self):
        
        # initialising test
        prefix = 'and'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, 'andantino')
        self.assertEqual(definition, 'Rather quicker than andante; between that allegretto.')
        self.assertEqual(frequency, 10)

    def test_20(self):
        
        # initialising test
        prefix = 'ado'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, 'adorner')
        self.assertEqual(definition, 'He who, or that which, adorns; a beautifier.')
        self.assertEqual(frequency, 30)

    def test_21(self):
        
        # initialising test
        prefix = 'testverylongword'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, None)
        self.assertEqual(definition, None)
        self.assertEqual(frequency, 0)
    
    def test_22(self):
        
        # initialising test
        prefix = 'aja'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, 'ajava')
        self.assertEqual(definition, 'See Ajouan.')
        self.assertEqual(frequency, 2)

    def test_23(self):
        
        # initialising test
        prefix = 'ajav'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, 'ajava')
        self.assertEqual(definition, 'See Ajouan.')
        self.assertEqual(frequency, 1)

    def test_24(self):
        
        # initialising test
        prefix = 'ammon'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, 'ammonitiferous')
        self.assertEqual(definition, 'Containing fossil ammonites.')
        self.assertEqual(frequency, 8)

    def test_25(self):
        
        # initialising test
        prefix = 'amm'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, 'ammonitiferous')
        self.assertEqual(definition, 'Containing fossil ammonites.')
        self.assertEqual(frequency, 13)

    def test_26(self):
        
        # initialising test
        prefix = 'amba'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, 'ambagitory')
        self.assertEqual(definition, 'Ambagious. [R.]')
        self.assertEqual(frequency, 9)

    def test_27(self):
        
        # initialising test
        prefix = 'ac'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, 'acerbitude')
        self.assertEqual(definition, 'Sourness and harshness. [Obs.] Bailey.')
        self.assertEqual(frequency, 545)

    def test_28(self):
        
        # initialising test
        prefix = 'ab'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, 'aberr')
        self.assertEqual(definition, 'To wander; to stray. [Obs.] Sir T. Browne.')
        self.assertEqual(frequency, 380)

    def test_29(self):
        
        # initialising test
        prefix = 'ag'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, 'agileness')
        self.assertEqual(definition, 'Agility; nimbleness. [R.]')
        self.assertEqual(frequency, 170)

    def test_30(self):
        
        # initialising test
        prefix = 'af'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, 'aftward')
        self.assertEqual(definition, 'Toward the stern.')
        self.assertEqual(frequency, 160)

    def test_31(self):
        
        # initialising test
        prefix = 'afte'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, 'aftergame')
        self.assertEqual(definition, 'A second game; hence, a subsequent scheme or expedient. Wotton. Aftergame at Irish, an ancient game very nearly resembling backgammon. Beau. & Fl.')
        self.assertEqual(frequency, 21)

    def test_32(self):
        
        # initialising test
        prefix = 'restorative'
        word, definition, frequency = myTrie.prefix_search(prefix)
        
        # testing
        self.assertEqual(word, None)
        self.assertEqual(definition, None)
        self.assertEqual(frequency, 0)


# 2: A Weekend Getaway

class TestingQ2(unittest.TestCase):

    def test_01(self):

        # initialising test
        preferences = [[0], [1], [0,1], [0, 1], [1, 0], [1], [1, 0], [0, 1], [1]]
        licences = [1, 4, 0, 5, 8]
        cars = allocate(preferences, licences)

        # testing
        expected = [[[0, 4, 2, 3 ,6], [1, 5, 8, 7]],
                    [[0, 4, 2, 3, 7], [1, 5, 8, 6]],
                    [[0, 4, 2, 6, 7], [1, 5, 8, 3]],
                    [[0, 4, 3, 6, 7], [1, 5, 8, 2]],
                    [[0, 4, 2, 3], [1, 5, 8, 6, 7]],
                    [[0, 4, 2, 6], [1, 5, 8, 3, 7]],
                    [[0, 4, 2, 7], [1, 5, 8, 3, 6]],
                    [[0, 4, 3, 6], [1, 5, 8, 2, 7]],
                    [[0, 4, 3, 7], [1, 5, 8, 2, 6]],
                    [[0, 4, 6, 7], [1, 5, 8, 2, 3]]]
        self.assertEqual(len(cars), len(expected[0]))
        output = find_chosen_output(cars, expected)
        for i in range(len(cars)):
            self.assertCountEqual(cars[i], expected[output][i])

    def test_02(self):

        # initialising test
        preferences = [[], [], [], [], [], [], [], []]
        licences = [4, 2, 0]
        cars = allocate(preferences, licences)

        # testing
        self.assertEqual(cars, None)

    def test_03(self):

        # initialising test
        preferences = [[1, 0], [0, 1], [1, 0], [], [1], [0], [1]]
        licences = [6, 5, 2]
        cars = allocate(preferences, licences)

        # testing
        self.assertEqual(cars, None)

    def test_04(self):

        # initialising test
        preferences = [[0], [0], [0], [0], [0]]
        licences = [0, 4, 3, 2, 1]
        cars = allocate(preferences, licences)

        # testing
        expected = [[0, 1, 2, 3, 4]]
        self.assertEqual(len(cars), len(expected))
        for i in range(len(cars)):
            self.assertCountEqual(cars[i], expected[i])

    def test_05(self):

        # initialising test
        preferences = [[0], [0], [0], [0], [0]]
        licences = [0]
        cars = allocate(preferences, licences)

        # testing
        self.assertEqual(cars, None)

    def test_06(self):

        # initialising test
        preferences = [[0], [0], [0], [0], [0]]
        licences = []
        cars = allocate(preferences, licences)

        # testing
        self.assertEqual(cars, None)

    def test_07(self):

        # initialising test
        preferences = [[0], [0], [0], [0], [0], [1]]
        licences = [5, 4, 3, 2, 1, 0]
        cars = allocate(preferences, licences)

        # testing
        self.assertEqual(cars, None)

    def test_08(self):

        # initialising test
        preferences = [[0]]
        licences = [0]
        cars = allocate(preferences, licences)

        # testing
        self.assertEqual(cars, None)
    
    def test_09(self):

        # initialising test
        preferences = [[0], [0], [0], [0], [0], [0]]
        licences = [1, 4, 3]
        cars = allocate(preferences, licences)

        # testing
        self.assertEqual(cars, None)

    def test_10(self):

        # initialising test
        preferences = [[0], [0, 1], [0], [1, 0], [1], [1]]
        licences = [4, 2, 0, 5]
        cars = allocate(preferences, licences)

        # testing
        expected = [[[0, 1, 2, 3], [4, 5]],
                    [[0, 1, 2], [3, 4, 5]],
                    [[0, 2, 3], [1, 4, 5]],
                    [[0, 2], [1, 3, 4, 5]]]
        self.assertEqual(len(cars), len(expected[0]))
        output = find_chosen_output(cars, expected)
        for i in range(len(cars)):
            self.assertCountEqual(cars[i], expected[output][i])
        
    def test_11(self):

        # initialising test
        preferences = [[0, 1], [0, 1], [1, 0], [0, 1], [0, 1], [0, 1], [1, 0], [1, 0], [0, 1], [0, 1], [0, 1]]
        licences = [10, 1, 7, 3, 5, 0]
        cars = allocate(preferences, licences)

        # testing
        self.assertEqual(cars, None)

    def test_12(self):

        # initialising test
        preferences = [[0, 1, 2], [0, 2], [0], [0, 1], [2, 1], [0, 1], [0], [2], [1, 2], [0], [0, 2], [1]]
        licences = [4, 2, 0, 1]
        cars = allocate(preferences, licences)

        # testing
        self.assertEqual(cars, None)
    
    def test_13(self):

        # initialising test
        preferences = [[1], [0], [0, 1], [1, 0], [0, 1], [1, 0], [1], [1], [0], [0, 1]]
        licences = [6, 3, 4, 9, 1]
        cars = allocate(preferences, licences)

        # testing
        expected = [[[1, 8, 4, 5, 9], [0, 6, 7, 2, 3]],
                    [[1, 8, 3, 5, 9], [0, 6, 7, 2, 4]],
                    [[1, 8, 3, 4, 5], [0, 6, 7, 2, 9]],
                    [[1, 8, 2, 5, 9], [0, 6, 7, 3, 4]],
                    [[1, 8, 2, 4, 9], [0, 6, 7, 3, 5]],
                    [[1, 8, 2, 4, 5], [0, 6, 7, 3, 9]],
                    [[1, 8, 2, 3, 9], [0, 6, 7, 4, 5]],
                    [[1, 8, 2, 3, 5], [0, 6, 7, 4, 9]],
                    [[1, 8, 2, 3, 4], [0, 6, 7, 5, 9]]]
        self.assertEqual(len(cars), len(expected[0]))
        output = find_chosen_output(cars, expected)
        for i in range(len(cars)):
            self.assertCountEqual(cars[i], expected[output][i])

    def test_14(self):

        # initialising test
        preferences = [[0], [0], [0], [0], [0], [1], [1], [1], [1], [1], [2], [2]]
        licences =  [0, 1, 5, 6, 10, 11]
        cars = allocate(preferences, licences)

        # testing
        expected = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11]]
        self.assertEqual(len(cars), len(expected))
        for i in range(len(cars)):
            self.assertCountEqual(cars[i], expected[i])

    def test_15(self):

        # initialising test
        preferences = [[0], [1], [0,1], [0], [1, 0], [1], [1], [0, 1], [1]]
        licences = [1, 4, 0, 5, 8]
        cars = allocate(preferences, licences)

        # testing
        expected = [[[0, 4, 2, 3], [1, 5, 8, 6, 7]],
                    [[0, 4, 3, 7], [1, 5, 8, 6, 2]],
                    [[0, 4, 2, 3, 7], [1, 5, 8, 6]],
                    [[0, 4, 3], [1, 5, 8, 6, 2, 7]]]
        self.assertEqual(len(cars), len(expected[0]))
        output = find_chosen_output(cars, expected)
        for i in range(len(cars)):
            self.assertCountEqual(cars[i], expected[output][i])

    def test_16(self):

        # initialising test
        preferences = [[1], [0, 1], [0], [1, 0], [0], [0]]
        licences = [0, 1, 2, 4]
        cars = allocate(preferences, licences)

        # testing
        expected = [[[2, 3, 4, 5], [0, 1]],
                    [[2, 4, 5], [0, 1, 3]]]
        self.assertEqual(len(cars), len(expected[0]))
        output = find_chosen_output(cars, expected)
        for i in range(len(cars)):
            self.assertCountEqual(cars[i], expected[output][i])
    
    def test_17(self):

        # initialising test
        preferences = [[0], [0]]
        licences = [1, 0]
        cars = allocate(preferences, licences)

        # testing
        expected = [[0, 1]]
        self.assertEqual(len(cars), len(expected))
        for i in range(len(cars)):
            self.assertCountEqual(cars[i], expected[i])

    def test_18(self):

        # initialising test
        preferences = [[0], [0], []]
        licences = [2]
        cars = allocate(preferences, licences)

        # testing
        self.assertEqual(cars, None)

    def test_19(self):

        # initialising test
        preferences = [[0], [0], [0], [0], [0]]
        licences = [2, 1, 4]
        cars = allocate(preferences, licences)

        # testing
        expected = [[0, 1, 2, 3, 4]]
        self.assertEqual(len(cars), len(expected))
        for i in range(len(cars)):
            self.assertCountEqual(cars[i], expected[i])

    def test_20(self):

        # initialising test
        preferences = [[0], [], [0], [0]]
        licences = [0, 2, 1]
        cars = allocate(preferences, licences)

        # testing
        self.assertEqual(cars, None)
    
    def test_21(self):

        # initialising test
        preferences = [[0], [1], [1, 0], [1], [0], [1], [0]]
        licences = [3, 4, 1, 2]
        cars = allocate(preferences, licences)

        # testing
        expected = [[0, 4, 2, 6], [1, 3, 5]]
        self.assertEqual(len(cars), len(expected))
        for i in range(len(cars)):
            self.assertCountEqual(cars[i], expected[i])

    def test_22(self):

        # initialising test
        preferences = [[]]
        licences = []
        cars = allocate(preferences, licences)

        # testing
        self.assertEqual(cars, None)

    def test_23(self):

        # initialising test
        preferences = [[0], [0], [0], [0]]
        licences = [0, 2]
        cars = allocate(preferences, licences)

        # testing
        expected = [[0, 1, 2, 3]]
        self.assertEqual(len(cars), len(expected))
        for i in range(len(cars)):
            self.assertCountEqual(cars[i], expected[i])

    def test_24(self):

        # initialising test
        preferences = [[0], [0], [0]]
        licences = [2, 0, 1]
        cars = allocate(preferences, licences)

        # testing
        expected = [[0, 1, 2]]
        self.assertEqual(len(cars), len(expected))
        for i in range(len(cars)):
            self.assertCountEqual(cars[i], expected[i])
    
    def test_25(self):

        # initialising test
        preferences = [[0], [0], [0], [0], [0, 1], [1]]
        licences = [0, 1, 4, 5]
        cars = allocate(preferences, licences)

        # testing
        expected = [[0, 1, 2, 3], [4, 5]]
        self.assertEqual(len(cars), len(expected))
        for i in range(len(cars)):
            self.assertCountEqual(cars[i], expected[i])

    def test_26(self):

        # initialising test
        preferences = [[0], [0], [0], [0], [0, 1], [1]]
        licences = [0, 1, 5]
        cars = allocate(preferences, licences)

        # testing
        self.assertEqual(cars, None)

    def test_27(self):

        # initialising test
        preferences = [[0, 2], [1], [1, 0], [0], [0], [1], [0], [2], [2], [2], [2, 1], [1]]
        licences = [0, 3, 2, 5, 10, 9]
        cars = allocate(preferences, licences)

        # testing
        expected = [[[0, 3, 4, 6], [2, 5, 1, 11], [10, 9, 8, 7]], 
	                [[2, 3, 4, 6], [10, 5, 1, 11], [0, 9, 8, 7]]]
        self.assertEqual(len(cars), len(expected[0]))
        output = find_chosen_output(cars, expected)
        for i in range(len(cars)):
            self.assertCountEqual(cars[i], expected[output][i])

    def test_28(self):

        # initialising test
        preferences = [[3, 0, 1], [3, 1, 2, 0], [0, 3, 2, 1], [2, 1, 3, 0], [3, 2, 1, 0], [3, 1, 0, 2], [3, 2, 0, 1], [2, 3, 0], [0, 3, 1, 2], [2, 0, 3, 1], [1, 2, 0, 3], [2, 3, 1, 0], [1, 2, 3, 0], [3, 2, 0], [3, 2], [3, 2, 0], [0, 2, 1, 3], [2, 0, 3, 1]]
        licences = [0, 5, 10, 15, 7, 11, 2]
        cars = allocate(preferences, licences)

        # testing
        self.assertEqual(cars, None)
    
    def test_29(self):

        # initialising test
        preferences = [[0], [1], [0], [0, 1], [1], [0], [1, 0]]
        licences = [1, 3, 2, 6]
        cars = allocate(preferences, licences)

        # testing
        expected = [[[0, 2, 5, 3], [1, 4, 6]],
	                [[0, 2, 5, 6], [1, 4, 3]]]
        self.assertEqual(len(cars), len(expected[0]))
        output = find_chosen_output(cars, expected)
        for i in range(len(cars)):
            self.assertCountEqual(cars[i], expected[output][i])

    def test_30(self):

        # initialising test
        preferences = [[0, 1], [1, 0], [0, 1], [0, 1], [0], [1, 0]]
        licences = [5, 3]
        cars = allocate(preferences, licences)

        # testing
        self.assertEqual(cars, None)

    def test_31(self):

        # initialising test
        preferences = [[1, 0], [0, 1], [0], [0], [0], [1], [1], [0, 1], [1], [1, 2], [2], [2]]
        licences = [0, 1, 5, 6, 9, 10]
        cars = allocate(preferences, licences)

        # testing
        expected = [[0, 1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11]]
        self.assertEqual(len(cars), len(expected))
        for i in range(len(cars)):
            self.assertCountEqual(cars[i], expected[i])

    def test_32(self):

        # initialising test
        preferences = [[1, 0, 2], [0], [0], [0], [0], [2, 1, 0], [1], [1], [1], [0, 1, 2], [2], [2]]
        licences = [0, 1, 5, 6, 9, 10]
        cars = allocate(preferences, licences)

        # testing
        expected = [[[0, 1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11]],
                    [[5, 1, 2, 3, 4], [9, 6, 7, 8], [0, 10, 11]],
                    [[9, 1, 2, 3, 4], [0, 6, 7, 8], [5, 10, 11]],
                    [[0, 1, 2, 3, 4], [9, 6, 7, 8], [5, 10, 11]],
                    [[5, 1, 2, 3, 4], [0, 6, 7, 8], [9, 10, 11]],
                    [[9, 1, 2, 3, 4], [5, 6, 7, 8], [0, 10, 11]]]
        self.assertEqual(len(cars), len(expected[0]))
        output = find_chosen_output(cars, expected)
        for i in range(len(cars)):
            self.assertCountEqual(cars[i], expected[output][i])


# Helper Functions

def load_dictionary(filename):
    infile = open(filename, encoding = 'utf-8')
    word, frequency = "", 0
    aList = []
    for line in infile:
        line.strip()
        if line[0:4] == "word":
            line = line.replace("word: ","")
            line = line.strip()
            word = line            
        elif line[0:4] == "freq":
            line = line.replace("frequency: ","")
            frequency = int(line)
        elif line[0:4] == "defi":
            index = len(aList)
            line = line.replace("definition: ","")
            definition = line.replace("\n","")
            aList.append([word,definition,frequency])
    return aList

def find_chosen_output(cars, expected):
    for i in range(len(expected)):
        is_output = True
        for j in range(len(expected[i])):
            if set(cars[j]) != set(expected[i][j]):
                is_output = False
        if is_output:
            return i
    return 0


# Run Tests

if __name__ == '__main__':
    Dictionary = load_dictionary("Dictionary.txt")
    myTrie = Trie(Dictionary)
    unittest.main()
    