Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:16:59) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> def circuit_3_2(x, y):
	a1 = not x
	a2 = not y
	return int(bool(not(a1 and a2)))

def circuit_3_4(x, y, z)
        a1 = xy
        a2 = (not z) + x
        a3 = (not a1) + a2
        return int(bool(a3))

class circuits_unit_tests( unittest.TestCase ):

        def test_circuit_3_2(self):
                self.assertEqual(circuit_3_2(0,0), 1)
                self.assertEqual(circuit_3_2(0,1), 1)
                self.assertEqual(circuit_3_2(1,0), 1)
                self.assertEqual(circuit_3_2(1,1), 0)

        def test_circuit_3_4_000(self):
                self.assertEqual(circuit_3_4(0,0,0), 1)

        def test_circuit_3_4_001(self):
                self.assertEqual(circuit_3_4(0,0,1), 1)

        def test_circuit_3_4_010(self):
                self.assertEqual(circuit_3_4(0,1,0), 1)

        def test_circuit_3_4_011(self):
                self.assertEqual(circuit_3_4(0,1,1), 0)

        def test_circuit_3_4_100(self):
                self.assertEqual(circuit_3_4(1,0,0), 1)

        def test_circuit_3_4_101(self):
                self.assertEqual(circuit_3_4(1,0,1), 0)

        def test_circuit_3_4_110(self):
                self.assertEqual(circuit_3_4(1,1,0), 1)

        def test_circuit_3_4_111(self):
                self.assertEqual(circuit_3_4(1,1,1), 1)

def main():
        unittest.main()

if __name__ == '__main__':
        main()
        

