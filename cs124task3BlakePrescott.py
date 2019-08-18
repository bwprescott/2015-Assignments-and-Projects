#!/usr/bin/python3

import unittest
from digital_circuit_core import *

class MyPrettySimulator( Simulator ):
	""" A class skeleton for the digital circuit implementation of
		Blake Prescott - CS124
		
		The class extends the Simulator class, that contains the core simulation code.
		It inherits the following methods:
			- Wire( [name] ): creates a Wire object, that can be passed as an input
				to logic gates functions
			- AndGate(a1, a2, out): connect 3 wires a1, a2 and out in an AND gate
			- OrGate(o1, o2, out): connect 3 wires o1, o2 and out in an OR gate
			- Inverter(in, out): connect 2 wires in and out in an inverter gate
			- propagate(): propagate a signal along the wires; usually used after 
				changing the value carried by one of the input wires

		A Wire object defines the following methods:
			- set_signal( <boolean value> )
			- get_signal()
		A newly created Wire object carries the value 0 by default.

	"""

	
	def MajorityVoting(self, x, y, z, o):
		""" An example: implementing Majority Voting circuit (Rosen, 12.3, Example 2,
			- Figure 5, p. 825)

			F(x, y, z) = xy + xz + yz

			Since the simulator's OrGate() function takes only 2 inputs, we must
			rewrite F(x, y, z) as a combination of 2 sums: F(x,y,z) = (xy + xz) + yz
		"""
		# All wires that enter/exit the circuit need to be visible outside of the 
		# function: they are to be created in the enclosing scope and passed 
		# as parameters.
		# However, wires that connect the AND gates to the OR gates are 
		# _internal wires_, visible only inside the circuit: they need to be created
		xy = self.Wire('xy')
		xz = self.Wire('xz')
		yz = self.Wire('yz')
		xy_or_xz = self.Wire('xy_or_xz')
		
		self.AndGate(x, y, xy)	
		self.AndGate(x, z, xz)	
		self.Andgate(y, z, yz)

		# OR(xy,xz,yz) = OR( OR(xy,xz),  yz)
		self.OrGate(xy, xz, xy_or_xz)
		self.OrGate(xy_or_xz, yz, o)
		
		return 'ok'

	def TwoSwitches(self, x, y, o):
		""" An example: light controlled by 2 switches (Rosen, 12.3, Example 3,
			- Figure 6, p. 825)
			
			F(x, y) = xy + !x.!y
		"""
		# Wires x, y, and o are passed as parameters.
		# Only the internal wires need to be created:
		xy = self.Wire('xy')
		not_x = self.Wire('not_x')
		not_y = self.Wire('not_y')
		notx_noty = self.Wire('notx_noty')

		self.AndGate(x,y,xy)
		self.Inverter(x, not_x)
		self.Inverter(y, not_y)
		self.AndGate(not_x, not_y, notx_noty)
		self.OrGate(xy, notx_noty, o)		
	
		return 'ok'
	
        # This function needs to be defined: parameter, body definition
	def HalfAdder(self, x, y, s, c):
		x_or_y = self.Wire('x_or_y')
		not_c = self.Wire('not_c')
		
		self.OrGate(x, y, x_or_y)
		self.AndGate(x, y, c)
		self.Inverter(c, not_c)
		self.AndGate(x_or_y, not_c, s)
                
		pass
		


	def FullAdder(self, a, b, c_in, s, c_out):
                
		s1c_in = self.Wire('s1c_in')
		c1 = self.Wire('c1')
		s1 = self.Wire('s1')
		
		self.HalfAdder(a, b, s1, c1)
		self.HalfAdder(s1, c_in, s, s1c_in)
		self.OrGate(c1, s1c_in, c_out)
		
		
		pass



class SimulatorUnitTest( unittest.TestCase ):
	""" A testing class for your simulator. It includes complete tests for the half- and full-adders."""

	
	def testTwoSwitches_1(self):
		""" Input (1,0) --> 1  """
		sim = MyPrettySimulator()
		x = sim.Wire('x')
		y = sim.Wire('y')
		o = sim.Wire('o')
		
		sim.TwoSwitches(x, y, o)

		x.set_signal(1)
		sim.propagate()
		
		self.assertEqual( o.get_signal(), 0)		
		

	def testTwoSwitches_2(self):
		""" Input (0,1) --> 1  """
		sim = MyPrettySimulator()
		x = sim.Wire('x')
		y = sim.Wire('y')
		o = sim.Wire('o')
		
		sim.TwoSwitches(x, y, o)

		y.set_signal(1)
		sim.propagate()
		
		self.assertEqual( o.get_signal(), 0)		
		
	def testTwoSwitches_3(self):
		""" Input (1,1) --> 1  """
		sim = MyPrettySimulator()
		x = sim.Wire('x')
		y = sim.Wire('y')
		o = sim.Wire('o')
		
		sim.TwoSwitches(x, y, o)

		x.set_signal(1)
		y.set_signal(1)
		sim.propagate()
		
		self.assertEqual( o.get_signal(), 1)		
		
	def testTwoSwitches_4(self):
		""" Input (0,0) --> 1  """
		sim = MyPrettySimulator()
		x = sim.Wire('x')
		y = sim.Wire('y')
		o = sim.Wire('o')
		
		sim.TwoSwitches(x, y, o)

		sim.propagate()
		
		self.assertEqual( o.get_signal(), 1)		
		

	def testHalfAdder_1(self):
		" Input(0,1) --> (0,1)"""
		sim = MyPrettySimulator()

		a = sim.Wire('a')
		b = sim.Wire('b')

		s = sim.Wire('s')
		c = sim.Wire('c')

		sim.HalfAdder(a, b, s, c)

		a.set_signal(1)
		
		sim.propagate()
		
		self.assertEqual( s.get_signal(), 1)
		self.assertEqual( c.get_signal(), 0)
		
		

	def testHalfAdder_2(self):
		" Input(1,0) --> (0,1)"""

		sim = MyPrettySimulator()

		a = sim.Wire('a')
		b = sim.Wire('b')

		s = sim.Wire('s')
		c = sim.Wire('c')

		sim.HalfAdder(a, b, s, c)

		b.set_signal(1)
		
		sim.propagate()
		
		self.assertEqual( s.get_signal(), 1)
		self.assertEqual( c.get_signal(), 0)
		
		

	def testHalfAdder_3(self):
		" Input(1,1) --> (1,0)"""

		sim = MyPrettySimulator()

		a = sim.Wire('a')
		b = sim.Wire('b')

		s = sim.Wire('s')
		c = sim.Wire('c')

		sim.HalfAdder(a, b, s, c)

		a.set_signal(1)
		b.set_signal(1)
		
		sim.propagate()
		
		self.assertEqual( s.get_signal(), 0)
		self.assertEqual( c.get_signal(), 1)


		
	def testFullfAdder_1(self):
		" Input(0,0,1) --> (0,1)"""

		sim = MyPrettySimulator()

		a = sim.Wire('a')
		b = sim.Wire('b')
		c_in = sim.Wire('c_in')
		

		s = sim.Wire('s')
		c_out = sim.Wire('c_out')

		sim.FullAdder(a, b, c_in, s, c_out)

		a.set_signal(1)
		
		sim.propagate()
		
		self.assertEqual( s.get_signal(), 1)
		self.assertEqual( c_out.get_signal(), 0)

	def testFullfAdder_2(self):
		" Input(0,1,0) --> (0,1)"""

		sim = MyPrettySimulator()

		a = sim.Wire('a')
		b = sim.Wire('b')
		c_in = sim.Wire('c_in')
		

		s = sim.Wire('s')
		c_out = sim.Wire('c_out')

		sim.FullAdder(a, b, c_in, s, c_out)

		b.set_signal(1)
		
		sim.propagate()
		
		self.assertEqual( s.get_signal(), 1)
		self.assertEqual( c_out.get_signal(), 0)
		
	def testFullfAdder_3(self):
		" Input(0,1,1) --> (1,0)"""

		sim = MyPrettySimulator()

		a = sim.Wire('a')
		b = sim.Wire('b')
		c_in = sim.Wire('c_in')
		

		s = sim.Wire('s')
		c_out = sim.Wire('c_out')

		sim.FullAdder(a, b, c_in, s, c_out)

		a.set_signal(1)
		b.set_signal(1)
		
		sim.propagate()
		
		self.assertEqual( s.get_signal(), 0)
		self.assertEqual( c_out.get_signal(), 1)
		

	def testFullfAdder_4(self):
		" Input(1,0,1) --> (1,0)"""

		sim = MyPrettySimulator()

		a = sim.Wire('a')
		b = sim.Wire('b')
		c_in = sim.Wire('c_in')
		

		s = sim.Wire('s')
		c_out = sim.Wire('c_out')

		sim.FullAdder(a, b, c_in, s, c_out)

		a.set_signal(1)
		c_in.set_signal(1)
		
		sim.propagate()
		
		self.assertEqual( s.get_signal(), 0)
		self.assertEqual( c_out.get_signal(), 1)
		
	def testFullfAdder_5(self):
		" Input(1,1,0) --> (1,0)"""

		sim = MyPrettySimulator()

		a = sim.Wire('a')
		b = sim.Wire('b')
		c_in = sim.Wire('c_in')
		

		s = sim.Wire('s')
		c_out = sim.Wire('c_out')

		sim.FullAdder(a, b, c_in, s, c_out)

		b.set_signal(1)
		c_in.set_signal(1)
		
		sim.propagate()
		
		self.assertEqual( s.get_signal(), 0)
		self.assertEqual( c_out.get_signal(), 1)
		

	def testFullfAdder_6(self):
		" Input(1,1,1) --> (1,1)"""

		sim = MyPrettySimulator()

		a = sim.Wire('a')
		b = sim.Wire('b')
		c_in = sim.Wire('c_in')
		

		s = sim.Wire('s')
		c_out = sim.Wire('c_out')

		sim.FullAdder(a, b, c_in, s, c_out)

		a.set_signal(1)
		b.set_signal(1)
		c_in.set_signal(1)
		
		sim.propagate()
		
		self.assertEqual( s.get_signal(), 1)
		self.assertEqual( c_out.get_signal(), 1)
		

def main():
      unittest.main()

if __name__ == '__main__':
       main()

