#!/usr/bin/python3

import unittest
from digital_circuit_core import *

class InputLengthException( Exception ): pass

class MyPrettySimulator( Simulator ):
	""" A class skeleton for the digital circuit implementation of
		<Blake Prescott> - <CS124>
		
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

	
	def HalfAdder(self, a, b, s, c):
		""" The half-adder (see Rosen, figure 8, p. 827). Other, equivalent circuits are
			possible -f.i. involving an XOR gate-, but this is the most straightforward
			one.
		"""
		# internal wires
		d = self.Wire('d-wire')
		e = self.Wire('e-wire')

		self.OrGate(a, b, d)
		self.AndGate(a, b, c)
		self.Inverter(c, e)
		self.AndGate(d, e, s)
		
		return 'ok'
			

	def FullAdder(self, a, b, c_in, s, c_out):
		""" The full-adder (see Rosen, figure 9, p. 827)."""

		# internal wires
		d = self.Wire()
		c1 = self.Wire()
		c2 = self.Wire()

		self.HalfAdder(b, c_in, d, c1)
		self.HalfAdder(a, d, s, c2)
		self.OrGate(c1, c2, c_out) 		
		
		return 'ok'

	def RippleCarryAdder_5_bits(self, x_array, y_array, s_array ):
		"""
		A fixed-sized adder: each operand is passed as an array of 5 wires; there are 5+1=6 wires for the sum.
		This is a proof of concept. It lacks genericity: what about 6-bits, 7-bits, ..., n-bits integers?
		See below for a better solution.

		:param x_array: first operand, (LSB in first position)
		:param y_array: second operand, (LSB in first position)
		:param s_arr: sum (LSB in first position)
		:type x_array: list
		:type y_array: list
		:type s_array: list
		"""
		#  x0 y0   x1 y1   x2 y2   x3 y3   x4 y4  
		#  |__|    |__|    |__|    |  |    |  |
		#  |HA|-c0-|FA|-c1-|FA|-c2-|FA|-c3-|FA|--s5
		#  |       |       |       |       | 
		#  s0      s1      s2      s3      s4	


		############# YOUR CODE HERE ###############
##		x_array = [ self.Wire(), self.Wire(), self.Wire(), self.Wire(), self.Wire() ]
##		y_array = [ self.Wire(), self.Wire(), self.Wire(), self.Wire(), self.Wire() ]
##		s_array = [ self.Wire(), self.Wire(), self.Wire(), self.Wire(), self.Wire(), self.Wire() ]

		
		c0 = self.Wire('c0')
		c1 = self.Wire('c1')
		c2 = self.Wire('c2')
		c3 = self.Wire('c3')
		c4 = self.Wire('c4')
		
		self.HalfAdder(x_array[0], y_array[0], s_array[0], c0)
		self.FullAdder(x_array[1], y_array[1], c0, s_array[1], c1)
		self.FullAdder(x_array[2], y_array[2], c1, s_array[2], c2)
		self.FullAdder(x_array[3], y_array[3], c2, s_array[3], c3)
		self.FullAdder(x_array[4], y_array[4], c3, s_array[4], s_array[5])
		

		return 'ok'  

	def RippleCarryAdder(self, x_arr, y_arr, s_arr):
		""" The n-bit ripple carry adder:
			- it is passed arrays of wire instead of separate wires
			- it accepts inputs of any length, up to 16 bits
		A loop is used to create the internal wires (c0, c1, ..., c_n-1),
		and the adders.

		:param x_arr: first operand, a n-wire array (LSB on the left)
		:param y_arr: second operand, a n-wire array (LSB on the left)
		:param s_arr: sum, a n+1-wire array (LSB on the left)
		:type x_arr: list
		:type y_arr: list
		:type s_arr: list
		""" 
		
		#  x0 y0   x1 y1   x2 y2   x3 y3  ... x_n y_n
		#  |__|    |__|    |__|    |__|        |__|
		#  |HA|-c0-|FA|-c1-|FA|-c2-|FA|-- ... -|FA|--s_n+1
		#  |       |       |       |           |
		#  s0      s1      s2      s3          s_n

		############ YOUR CODE HERE ############
		c_array = len(x_arr) * [self.Wire('')]
		self.HalfAdder(x_arr[0], y_arr[0], s_arr[0], c_array[0])
		
		z = 1
		if z < len(x_arr):
			self.FullAdder(x_arr[z], y_arr[z], c_array[z-1], s_arr[z], c_array[z])
			z += 1
##		self.FullAdder(x_arr[len(x_arr)], y_arr[len(x_arr)], c_array[len(x_arr) - 1], s_arr[len(x_arr)], s_arr[len(x_arr) + 1])

		return 'ok'



class SimulatorUnitTest( unittest.TestCase ):
	""" A testing class for your simulator. It includes complete tests for the half- and full-adders."""

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
		c_in = sim.Wire('c-in')
		

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
		c_in = sim.Wire('c-in')
		

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
		c_in = sim.Wire('c-in')
		

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
		c_in = sim.Wire('c-in')
		

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
		c_in = sim.Wire('c-in')
		

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
		c_in = sim.Wire('c-in')
		

		s = sim.Wire('s')
		c_out = sim.Wire('c_out')

		sim.FullAdder(a, b, c_in, s, c_out)

		a.set_signal(1)
		b.set_signal(1)
		c_in.set_signal(1)
		
		sim.propagate()
		
		self.assertEqual( s.get_signal(), 1)
		self.assertEqual( c_out.get_signal(), 1)
		
	def testRippleCarryAdder_5_bits(self):
		"""
		A fixed-sized adder: each operand is passed as an array of 5 wires; there are 5+1=6 wires for the sum.
		This is a proof of concept. It lacks genericity: what about 6-bits, 7-bits, ..., n-bits integers?
		See next test for a better solution.
		"""

		sim = MyPrettySimulator()

		# note: since x and y have 5 bits each, the resulting sum is 6-bit long
		# 
		# Initializing arrays of wires this way is not convenient: the next test
		# use a Simulator's convenience method to do the same task
		x_arr = [ sim.Wire(), sim.Wire(), sim.Wire(), sim.Wire(), sim.Wire() ]
		y_arr = [ sim.Wire(), sim.Wire(), sim.Wire(), sim.Wire(), sim.Wire() ]
		s_arr = [ sim.Wire(), sim.Wire(), sim.Wire(), sim.Wire(), sim.Wire(), sim.Wire() ]

		sim.RippleCarryAdder_5_bits( x_arr, y_arr, s_arr )
		
		# note: leftmost wire carries the LSB!
		sim.set_wires( [x_arr[0], x_arr[1], x_arr[2], x_arr[3], x_arr[4] ], 0b10110) # x0=0, x1=1, x2=1, ...
		sim.set_wires( [y_arr[0], y_arr[1], y_arr[2], y_arr[3], y_arr[4] ], 0b11101) # y0=1, y1=0, y2=1, ...

		sim.propagate()

		self.assertEqual( sim.wires_to_integer( s_arr ), 0b110011)	

	def testRippleCarryAdder_1(self):
		""" The ripple carry adder, much improved:
			- it is passed arrays of wire instead of separate wires
			- it accepts inputs of any length, up to 16 bits
		""" 

		sim = MyPrettySimulator()
		
		x_wires = sim.WireArray( 8 )
		y_wires = sim.WireArray( 8 )
		out_wires = sim.WireArray( 9 )

		sim.RippleCarryAdder(x_wires, y_wires, out_wires)
	
		sim.set_wires(x_wires, 0b10111010)
		sim.set_wires(y_wires, 0b10101110)
		
		sim.propagate()

		# rightmost wire carries LSB
		self.assertEqual( sim.wires_to_integer( out_wires ), 0b101101000) 

	def testRippleCarryAdder_2(self):
		"""Special case: 1-bit operands"""

		sim = MyPrettySimulator()
		
		x_wires = sim.WireArray( 1 )
		y_wires = sim.WireArray( 1 )
		out_wires = sim.WireArray( 2 )

		sim.RippleCarryAdder(x_wires, y_wires, out_wires)
	
		sim.set_wires(x_wires, 0b1)
		sim.set_wires(y_wires, 0b1)
		
		sim.propagate()

		# rightmost wire carries LSB
		self.assertEqual( sim.wires_to_integer( out_wires ), 0b10) 
		
	
	def testRippleCarryAdder_3(self):
		"""Special case: 2-bit operands"""

		sim = MyPrettySimulator()
		
		x_wires = sim.WireArray( 2 )
		y_wires = sim.WireArray( 2 )
		out_wires = sim.WireArray( 3 )

		sim.RippleCarryAdder(x_wires, y_wires, out_wires)
	
		sim.set_wires(x_wires, 0b10)
		sim.set_wires(y_wires, 0b11)
		
		sim.propagate()
		
		# rightmost wire carries LSB
		self.assertEqual( sim.wires_to_integer( out_wires ), 0b101) 
		
	
		
	
def main():
      unittest.main()

if __name__ == '__main__':
       main()

