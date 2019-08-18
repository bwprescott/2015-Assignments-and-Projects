#!/usr/bin/python3
#
#
# Nicolas Renet, 10/2015
#
# digital_circuit.py: a digital circuit simulator
#
# The following is a Python interpretation of the 'Digital Circuit Simulator' presented by 
# Harold Abelson and Gerald Sussman in their acclaimed Scheme textbook (Structure and 
# Interpretation of Computer Programs, MIT Press, 1998). Python's functional features made it
# easy to stay close to the original program's pattern, where logic gates are just
# functions to be applied to the wires: these maintain an internal state, mostly a list of
# delayed procedures that run when the signal changes.

import unittest
import collections


class OverflowException( Exception): pass
class UnderflowException( Exception): pass

class Queue():

	def __init__(self,size=None):
		if size is None:
			size=100	
		self.tail=0
		self.head=0
		self.array=[None]*size


	def is_empty(self):
		return self.head==self.tail
		

	def enqueue(self, x):
		if (self.head==0 and self.tail==len(self.array)-1) or (self.tail+1==self.head):
			raise OverflowException()
			
		self.array[self.tail] = x
		if self.tail == len(self.array)-1:
			self.tail = 0
		else:
			self.tail = self.tail + 1

	def dequeue(self):
		if (self.head==self.tail):
			raise UnderflowException()
		x = self.array[self.head]
		# just for clarity
		if self.head == len( self.array)-1:
			self.head=0
		else:
			self.head = self.head+1

		return x

	def peek(self):
		if self.is_empty():
			return None
		return self.array[ self.head ]

	def __str__(self):
		output = ''
		# no wrap-around
		#print( 'H:{} T:{}'.format(self.head, self.tail))
		if self.tail is self.head:
			return ''
		if self.tail==0 or self.head < self.tail:
			for el in self.array[self.head:self.tail]:
				output += (' -> '+ str(el))
			return output
		# wrap-around
		for el in self.array[self.head:]:
			output += (' -> '+str(el))
		for el in self.array[0:self.tail]:
			output += (' -> '+str(el))
			#if self.simulator is not None:
			#	output +=('(' + self.simulator.get_function_parameter(el)  + ')')
		return output


TimeSegment = collections.namedtuple( "TimeSegment", "time queue" )
Action = collections.namedtuple("Action","function object value") 

VERBOSE = False

def trace(s):
	global VERBOSE
	if VERBOSE: print(s)

class Agenda(object):
	""" The agenda: store the delayed procedures.

	 Actions stored on the wire populate the agenda, when the signal changes.""" 
	
	def __init__(self, simul=None):
		self.current_time=0
		self.segments = []
		self.simulator=simul
	

	def is_empty(self):
		return len(self.segments)==0


	def add( self, time, action ):
		""" Insert an action into the agenda, in the proper time segment
		    (and create the segment, if needed)
		:param	time: time
		:param  action: a tuple (function, <name of the wire on which it is called>)
		:type time: int
		:type action: Action
		 """
		
		trace('Agenda.add({}, {})'.format( time, action.function ))
			
		if not self.segments :
			q = Queue()
			q.enqueue(action)
			self.segments.append( TimeSegment(time, q))
			return
		
		insert_location=-1
		for s in self.segments:
			insert_location+=1
			# before potential location: skipping positions
			if time > s.time and insert_location < (len(self.segments)-1):
				continue
			# found matching segment
			elif s.time == time:
				s.queue.enqueue(action)
				break
			# found a location, new segment required
			elif (time < s.time):
				q = Queue()
				q.enqueue(action)
				self.segments.insert(insert_location, TimeSegment(time, q))
				break
			# end of list: append new segment
			else:
				q = Queue()
				q.enqueue(action)
				self.segments.insert(insert_location+1, TimeSegment(time, q))
					
	def remove_first( self ):
		""" Suppress an action from agenda, and, if needed, the containing time segment """

		if self.is_empty() or self.segments[0].queue.is_empty():
			return
		action = self.segments[0].queue.dequeue()
		trace('Agenda.remove_first() '.format())
		if self.segments[0].queue.is_empty():
			trace("Agenda.remove_first(): deleting empty segment (time {})".format(self.segments[0].time))
			del self.segments[0]
			trace(self)

	def get_first( self ):
		""" Return the first function to be executed in the agenda """

		if not self.segments:
			raise UnderflowException
		first = self.segments[0].queue.peek()
		self.current_time = self.segments[0].time

		trace('Agenda.get_first() --> {}'.format(first.function))
		trace('Agenda.current_time <-- {}'.format(self.current_time))

		return first.function

	def __str__(self):
		""" Agenda in printable form """

		str_arr=['']*5
		str_arr[0]='current: '+str(self.current_time)
		str_arr[1]= '-----------------------------'
		str_arr[2]= ' TIME |     PROCEDURES'
		str_arr[3]= '-----------------------------'
		for ts in self.segments:
			str_arr.insert(len(str_arr), '|  ' + str(ts.time) + '  | '+ str(ts.queue))
			str_arr.insert(len(str_arr),'-----------------------------')
		return '\n'.join(str_arr)
			
		
		
	
class UnknownOperationException(Exception): pass
class InvalidSignalException(Exception): pass


class _WireObject(object):
	""" This class implements a wire: a wire can be assigned an value, and be 
    	used as an input to, or an output from a logical gate """
	
	wire_id=0

	def __init__(self, agenda=None, name=''):
		self.signal_value = 0
		self.action_procedures = []

		# the name is useful for the log trace
		self.name = name
		if name != '':
			_WireObject.wire_id+=1
			self.name = 'wire-'+str(_WireObject.wire_id)
			#print("_WireObject.name={}".format(self.name))
		self.agenda = agenda
			


	def set_signal(self, value):
		""" Test whether the new signal value changes the signal on the wire
		    and runs each of the action procedures

		:param value: a Boolean value (0 or 1)
		:type value: int
		"""

		if value != self.signal_value:
			self.signal_value = value
			for proc in self.action_procedures:
				trace('{}.set_signal({}): running {} (computing new output value,  and insert corresponding output setting function into the agenda)'.format(self.name,value, proc))
				proc()
			return 'done'
	
	def get_signal(self):
		""" Returns the Boolean value carried by the wire.

		:returns: 0 or 1
		:rtype: int
		"""
		trace('{}.get_signal() --> {}'.format(self.name, self.signal_value))
		return self.signal_value

	def _add_action(self, proc):
		""" Add the given procedure to the list of procedures and then then run the new procedure once """

		self.action_procedures.insert(0, proc)
		trace('{}._add_action({}): running {} once (computing new output value, and insert corresponding output setting function into the agenda)'.format(self.name,proc, proc))
		proc()

	def probe(self, name):
		def display():
			print('')
			print('{} {} new_value={}'.format(name, self.agenda.current_time,self.get_signal()))
		self._add_action( display )
			


class Simulator(object):
	""" The simulation framework: this class contains the functions that create wires and apply operations on them (logic gates)
	"""

	class _Simulator(object):
		""" Singleton """
		def __init__(self):
			self.agenda = Agenda( self )
			self.inverter_delay = 2
			self.and_gate_delay = 3
			self.or_gate_delay = 5
	instance = None

	def __init__(self):
		if not Simulator.instance:
			Simulator.instance = Simulator._Simulator()
	
	def __getattr__(self, name):
		return getattr( self.instance, name)

	
	def _after_delay(self,  delay, action ):
		trace('Simulator._after_delay({}, {})'.format(delay, action))
		trace('Simulator._after_delay: calling Agenda.add({}+{}, {})'.format(delay,self.agenda.current_time, action))
		self.agenda.add( delay + self.agenda.current_time, action )
		
	def Wire(self, name=''):
		""" Creates a Wire object.

		:param name: name (optional)
		:type name: string
		:rtype: _WireObject
		"""
		return _WireObject(self.agenda, name)

	def WireArray(self, n):
		""" Create an array of n _WireObjects.

		:param n: number of wires to create
		:type n: int
		:rtype: list
		"""
		wire_arr=[]
		for i in range(0,n):
			wire_arr.append( self.Wire() )
		return wire_arr

	def OrGate(self, o1_wire, o2_wire, output_wire):
		"""  Connects 2 input wires and 1 output wire through an OR gate.

		:param o1_wire: first input wire 
		:param o2_wire: second input wire 
		:param output_wire: output wire
		:type o1_wire: _WireObject
		:type o2_wire: _WireObject
		:type output_wire: _WireObject

		.. note:: Use a functional style: an OR gate is not an object, with an internal state (where input and output wires would be typically represented as instance properties), but a *procedure*, that itself generates a procedure from the parameters passed in, and stores it on the wires
		"""
		
		def or_action_procedure():
			trace('In or_action_procedure(): {}.get_signal()'.format(o1_wire.name))
			trace('In or_action_procedure(): {}.get_signal()'.format(o2_wire.name))
			new_value = self._logical_or( o1_wire.get_signal(), o2_wire.get_signal())
			def set_or_output():
				trace('In set_or_output(): {}.set_signal( {} )'.format(output_wire.name,  new_value))
				output_wire.set_signal( new_value)

			self._after_delay(
				self.or_gate_delay,
				#(lambda : output_wire.set_signal( new_value )))
				Action (set_or_output, output_wire.name, new_value))
		trace('In OrGate(): {}._add_action( <delayed action on {}> )'.format(o1_wire.name, output_wire.name))
		o1_wire._add_action( or_action_procedure )

		trace('In OrGate(): {}._add_action( <delayed action on {}> )'.format(o2_wire.name, output_wire.name))
		o2_wire._add_action( or_action_procedure )
		return 'ok'
	
	def AndGate(self, a1_wire, a2_wire, output_wire):
		""" Connects 2 input wires and 1 output wire through an AND gate.
		
		:param a1_wire: first input wire 
		:param a2_wire: second input wire 
		:param output_wire: output wire
		:type a1_wire: _WireObject
		:type a2_wire: _WireObject
		:type output_wire: _WireObject

		.. note:: Use a functional style: an OR gate is not an object, with an internal state (where input and output wires would be typically represented as instance properties), but a *procedure*, that itself generates a procedure from the parameters passed in, and stores it on the wires
		"""
		def and_action_procedure():
			trace('In and_action_procedure(): {}.get_signal()'.format(a1_wire.name))
			trace('In and_action_procedure(): {}.get_signal()'.format(a2_wire.name))
			new_value = self._logical_and( a1_wire.get_signal(), a2_wire.get_signal())
			def set_and_output():
				trace('In set_and_output(): {}.set_signal( {} )'.format(output_wire.name,  new_value))
				output_wire.set_signal( new_value)

			self._after_delay(
				self.and_gate_delay,
				#(lambda : output_wire.set_signal(new_value)))
				Action(set_and_output, output_wire.name, new_value))

		trace('In AndGate(): {}._add_action( <delayed action on {}> )'.format(a1_wire.name, output_wire.name))
		trace('In AndGate(): {}._add_action( <delayed action on {}> )'.format(a2_wire.name, output_wire.name))
		a1_wire._add_action( and_action_procedure )
		a2_wire._add_action( and_action_procedure )
		return 'ok'
			
	def Inverter(self, input_wire, output_wire):
		""" Connects 1 input wire and 1 output wire through an Inverter Gate.

		:param input_wire: first input wire 
		:param output_wire: output wire
		:type input_wire: _WireObject
		:type output_wire: _WireObject
		"""

		def invert_input():
			trace('In invert_input(): {}.get_signal()'.format(input_wire.name))
			new_value = self._logical_not( input_wire.get_signal())
			def set_inverter_output():
				trace('In set_inverter_output(): {}.set_signal( {} )'.format(output_wire.name, new_value))
				output_wire.set_signal( new_value )

			self._after_delay(
				self.inverter_delay,
				#(lambda : output_wire.set_signal( new_value )))
				Action(set_inverter_output, output_wire.name, new_value))
		trace('In Inverter(): {}._add_action( <delayed action on {}> )'.format(input_wire.name, output_wire.name))
		input_wire._add_action( invert_input )
		return 'ok'

	def _logical_not(self, s):
		trace('_logical_not({})'.format(s))
		if (s==0): return 1
		elif (s==1): return 0
		else: raise InvalidSignalException


	def _logical_and(self, s1, s2):
		trace('_logical_and({}, {})'.format(s1, s2))
		if (s1==1 and s2==1): return 1
		return 0
		
		
	def _logical_or(self, s1, s2):
		trace('_logical_or({}, {})'.format(s1, s2))
		if (s1==1 or s2==1): return 1
		return 0

	
	def propagate(self, interactive=False):
		""" Propagate a signal along a circuit.

		:param interactive: if True, prompt user before computing the next cycle (optional)
		:type interactive: bool
		 """

		if self.agenda.is_empty():
			return 'done'
		first_item = self.agenda.get_first()
		trace('propagate(): running first item = {}()'.format(first_item))
		first_item()	
		self.agenda.remove_first()
		if interactive:
			go = input("Validate for next step.")
		return (self.propagate())
	

	def set_wires(self, wire_array, value):
		""" Utility function initializes an array of wires from an integer : first index in the wire array carries the LSB

		:param wire_array: an array of _WireObject objects
		:param value: an integer
		:type wire_array: list
		:type value: an integer
		"""
		if value > 2**len(wire_array)-1:
			raise InputLengthException
		for pos in range(0, len(wire_array)):
			remainder = value % 2
			value = value // 2
			wire_array[pos].set_signal( remainder )
			

	def display_wires(self, wire_arr):	
		""" Display signals carried by an array of wires

		:param wire_arr: an array of _WireObject objects
		:type wire_arr: list
		:rtype: str
		"""
		x_wires_values = []
		for w in wire_arr:
			x_wires_values.append( w.get_signal())
						
		return '{}'.format(x_wires_values)

	def wires_to_integer(self, wire_arr):
		""" Read the signals carried by an array of wires as an integer

		:param wire_arr: an array of _WireObject objects, with LSB in leftmost position
		:type wire_arr: list
		:rtype: int
		"""
		out_value = 0
		pos = 0
		for pos  in range(0,  len(wire_arr)):
			out_value += (wire_arr[pos].get_signal() << pos)
		return out_value
			


		
