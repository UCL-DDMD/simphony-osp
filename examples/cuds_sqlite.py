"""An example on how to work with SimPhoNy wrappers.

> In SimPhoNy, assertional knowledge is stored in sessions. You may think of a
> session as a “box” were ontology individuals can be placed. But sessions go
> beyond just storing assertional knowledge. Sessions can be connected to
> SimPhoNy Wrappers. Each wrapper is a piece of software that seamlessly
> translates the assertional knowledge to a form that is compatible with a
> specific simulation engine, database, data repository or file format.
-- [Introduction (to sessions) - SimPhoNy documentation]
   (https://simphony.readthedocs.io/en/v4.0.0/usage/sessions
   /introduction.html)

This example demonstrates the use of teh SQLite wrapper, which is included with
SimPhoNy.

Before running this example, make sure that the city ontology is
installed. If it is not the case, install them running the following code:
>>> from simphony_osp.tools.pico import install
>>> install("city")
>>> install("boe")
"""

from simphony_osp.namespaces import city
from simphony_osp.namespaces import boe
from simphony_osp.tools import pretty_print
from simphony_osp.wrappers import SQLite

# instantiate some individuals directly in an SQLite database
with SQLite("water_sim.db", create=True) as water_sim:
    water_sim.clear()  # just in case you already ran this example
    O_atom = boe.OxygenAtom()
    H1_Atom  =boe.HydrogenAtom()
    H2_Atom  =boe.HydrogenAtom()
    # This assumes we are not interested in teh electronic chaege distribution,
    # hence we talk about atoms as if there is no distincition between them and
    # an isolated one. 

    water_mol  =  boe.Molecule()
    water_mol(boe.Has, O_atom) # in boe, has is a holistic hast_part
    water_mol(boe.Has, H1_atom) # in boe, has is a holistic hast_part
    water_mol(boe.Has, H2_atom) # in boe, has is a holistic hast_part

    # here we have semantically encoded the information about the composition
    # of the water molecue, but not its internal structure. 

    water_mol2 = boe.WaterMolecule() # in this case, we rely on the information
    #already in the ontology class of WaterMolecule, which may or may not have
    #any information about the composition. 


    # note, that water_mol itself is not necessarily a water molcule at all
    # times, as there is no assertion to that extent! we simply added 2H and O
    # to it, any one can do so later for example: 
    water_mol (boe.Has, boe.CarbonAtom())
    # this water_mol happens to be a molecule that is called by "accident" a
    # water_mol, whence it is anything but. 

    # We need more assertsion that this molecule is indeed water!

    # assume we have support for all point groups in the pgs ontology
    water_mol(boe.Has, pgr.C2v())

# this is much better, now we know that probably it is water, but we can never be 100%, as no assertion is made. At point one can still do: 

    water_mol (boe.Has, boe.CarbonAtom())
    # this is probably (is axctually) not correct, but we do not want to create
    # a semantic environemtn that limits people by our current understanding of
    # physics (even though this example is trivial, it makes the point). 


    # conclusion 1: while a water_mol defined as above (sans the carbon line), is
    # merely a promise that it is a water molecule (or a molecule that has 2H and O
    # with a C2V symmetry). There is no assertion that this is INDEED the case in
    # the world described but THIS ontology. Which may be modtl approprieate for a
    # specific application: (fast, easy to use,simple).  

    # Example 3 (inspired from ASE)
    water_mol  =  boe.Molecule()
    water_mol(boe.Has, O_atom) # in boe, has is a holistic hast_part
    water_mol(boe.Has, H1_atom) # in boe, has is a holistic hast_part
    water_mol(boe.Has, H2_atom) # in boe, has is a holistic hast_part
    O_atom( boe.Has, CUDS.coordinate( [0,0,0])     )
    H1_atom(boe.Has, CUDS.coordinate( [0.96,0,0])  )
    H2_atom(boe.Has, CUDS.coordinate( [-0.96,0,0]) )


# lets make a XXX holistic approach for a water molecule which is a bit more safe:

    water_mol2 = boe.WaterMolecule() # here this HAS to be water molecule
                                     #  accorsing to the convention which is
                                     #  the ontology itself. 

   # This is in fact, a corsed grained model of a water molecule, as we do not
   # see the actual atoms. 

    # in this perspective, there is no need to add a H, or O2 to the water moleucle as this 
    # is something already defined in the level of the ontology itself. 

    # we can then use the iformation in the ontology (the assertion of the
    # description logic part) that is can have only exactly one O and exactly
    # only 2 H, and you can also have : it has exactly one C2V symmetry...

let us add the bonds now and then also the property (observation) that it has a C2V symmetry, 


    H1_atom(boe.isBondedTo, O_atom)
    H2_atom(boe.isBondedTo, O_atom)

    C2v = boe.C2v()    # this is a sign, i.e., a property. 
    
    water_mol(hasProperty, C2v)   # synonym to hassign, and symmtry (C2v) is the sign.  
    C2v(hasInterpreter, boe.Gaussian()) # the way Gaussian internally represent
                                        #C2v, is the interpretant, which does not interest us here at all.

    Poly1 =  boe.Polymer()
    Mono1= boe.CarboHydrate()
    Mono2= boe.CarboXyl()
    Poly1[boe.Has] +=Mono1, Mono2
    water_sim.commit()





# retrieve the saved individuals and show them using pretty_print
with SQLite("database.db", create=False) as sqlite:
    pretty_print(sqlite.get(oclass=city.City).one())
