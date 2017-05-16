import os, pprint
pp=pprint.PrettyPrinter() # we'll use this later.
from epanettools.epanettools import EPANetSimulation, Node, Link, Network, Nodes,Links, Patterns, Pattern, Controls, Control # import all elements needed
from epanettools.examples import simple # this is just to get the path of standard examples
file = os.path.join(os.path.dirname(simple.__file__),'Net3.inp') # open an example
es=EPANetSimulation(file)