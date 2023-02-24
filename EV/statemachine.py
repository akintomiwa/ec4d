from random import choice
import warnings
from transitions import Machine
from transitions.extensions import GraphMachine

"""A state machine for managing status of EV agent in AB model."""


class TModel:
    def clear_state(self, deep=False, force=False):
        print("Clearing State ... ")
        return True

model = TModel()
machine = GraphMachine(model=model, states=['Idle', 'Travel', 'Seek_queue', 'In_queue', 'Charge', 'Travel_low', 'Battery_dead'],
                        transitions= [
                        {'trigger': 'start_travel', 'source': 'Idle', 'dest': 'Travel'},
                        {'trigger': 'get_low', 'source': 'Travel', 'dest': 'Travel_low'},
                        {'trigger': 'seek_charge_queue', 'source': 'Travel_low', 'dest': 'Seek_queue'},
                        {'trigger': 'deplete_battery', 'source': 'Travel_low', 'dest': 'Battery_dead'},
                        {'trigger': 'join_charge_queue', 'source': 'Seek_queue', 'dest': 'In_queue'},
                        {'trigger': 'start_charge', 'source': 'In_queue', 'dest': 'Charge'},
                        {'trigger': 'wait_in_queue', 'source': 'In_queue', 'dest': 'In_queue'},
                        {'trigger': 'continue_charge', 'source': 'Charge', 'dest': 'Charge'},
                        {'trigger': 'end_charge', 'source': 'Charge', 'dest': 'Travel'},
                        {'trigger': 'continue_travel', 'source': 'Travel', 'dest': 'Travel'},
                        {'trigger': 'end_travel', 'source': 'Travel', 'dest': 'Idle'},
                        {'trigger': 'end_travel_low', 'source': 'Travel_low', 'dest': 'Idle'},
                        ], 
                        initial = 'Idle', show_conditions=True)

model.get_graph().draw('my_state_diagram_nu.png', prog = 'dot')


class EVSM(Machine):
    """A state machine for managing status of EV agent in AB model.
    Can be deployed as EvState object.

States:
    Idle, Travel, Seek_queue, Travel_low, In_queue, Charge
Transitions:
    start_travel: Idle -> Travel
    get_low: Travel -> Travel_low
    seek_charge_queue: Travel_low -> Seek_queue
    deplete_battery: Trav`el_low -> Battery_dead
    join_charge_queue: Seek_queue -> In_queue
    wait_in_queue: In_queue -> In_queue
    start_charge: In Queue -> Charge
    end_charge: Charge -> Travel
    continue_travel: Travel -> Travel
    continue_charge: Charge -> Charge
    end_travel: Travel -> Idle
    end_travel_low: Travel_low -> Idle
    """

states = ['Idle', 'Travel', 'Seek_queue', 'In_queue', 'Charge', 'Travel_low', 'Battery_dead']
transitions = [
    {'trigger': 'start_travel', 'source': 'Idle', 'dest': 'Travel'},
    {'trigger': 'get_low', 'source': 'Travel', 'dest': 'Travel_low'},
    {'trigger': 'seek_charge_queue', 'source': 'Travel_low', 'dest': 'Seek_queue'},
    {'trigger': 'deplete_battery', 'source': 'Travel_low', 'dest': 'Battery_dead'},
    {'trigger': 'join_charge_queue', 'source': 'Seek_queue', 'dest': 'In_queue'},
    {'trigger': 'wait_in_queue', 'source': 'In_queue', 'dest': 'In_queue'},
    {'trigger': 'start_charge', 'source': 'In_queue', 'dest': 'Charge'},
    {'trigger': 'continue_charge', 'source': 'Charge', 'dest': 'Charge'},
    {'trigger': 'end_charge', 'source': 'Charge', 'dest': 'Travel'},
    {'trigger': 'continue_travel', 'source': 'Travel', 'dest': 'Travel'},
    {'trigger': 'end_travel', 'source': 'Travel', 'dest': 'Idle'},
    {'trigger': 'end_travel_low', 'source': 'Travel_low', 'dest': 'Idle'},
]


