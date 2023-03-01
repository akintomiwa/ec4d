
# 15-02-2023 Attempt to nest EV agent step function

#  def step(self):
#         # Block A - Transitions SM:

#         # Transition Case 1: Start travelling. idle -> travel
#         if self.machine.state == 'Idle':
#             if self.odometer < self._distance_goal:
#                 self.machine.start_travel()
            
#         if self.machine.state == 'Travel':
#             self.travel()
#             self.machine.continue_travel()
#             print(f"Vehicle id: {self.unique_id} is {self.machine.state}. This vehicle has travelled: {self.odometer} miles. Battery: {self.battery} kWh")
#             # EV travelling or travelling low, checking for Charge Station at each checkpoint
#             if self.odometer in self.checkpoint_list:
#                 print("EV has arrived at Charge Station but is not yet low on battery")
        
#         # Transition Case 2: Still travelling, battery low. Travel -> travel_low  
#             if self.battery <= self._soc_usage_thresh:
#                 self.machine.get_low()
#                 print("Current EV state: " + str(self.machine.state))
#                 print(f"EV: {self.unique_id}. This vehicle has travelled: {str(self.odometer)} miles and is low on battery. This vehicle's current charge level is: {self.battery} kwh")

#             # Transition Case 7: Journey Complete. travel -> idle
#             if self.odometer >= self._distance_goal:
#                 self.machine.end_travel()
#                 print(f"Vehicle {self.unique_id} has completed its journey. State: {self.machine.state}. This vehicle has travelled: {self.odometer} miles. Battery: {self.battery} kWh")
            
        
#         # Transition Case 3: EV with low battery does not arrive at charge station. Travel_low -> Battery_dead
#         # condition self.battery < 10 because 10 is the minimum expenditure of energy to move the vehicle in one timestep
#         if self.machine.state == 'Travel_low':
        
#             # Transition Case 4: EV with low battery is on lookout for Charge station. Notification.
#             if self.odometer < self._distance_goal:
#                 if self.battery > 10:
#                     print(f"EV {self.unique_id} is low on charge and is seeking a charge station. Current charge: {self.battery} kWh")
#                     self.travel()

#                 if self.battery < 10:
#                     self.machine.deplete_battery()
#                     print(f"EV {self.unique_id} is now in state: {self.machine.state} and is out of charge.")

#                 # if self.battery <= 0:
#                 #     self.machine.deplete_battery()
#                 #     print(f"EV {self.unique_id} is out of charge and can no longer travel. State: {self.machine.state}. Current charge: {self.battery} kWh")
#                 if self.odometer in self.checkpoint_list:
#                     self.machine.seek_charge_queue()
#                     print(f"EV {self.unique_id} is low on battery and is at a station. Seeking charge queue. Current EV state: {self.machine.state}")
#                     self.select_cp()
#                     self.machine.join_charge_queue()


#             # Transition Case 8: Joutney complete, battery low. travel_low -> idle
#             if self.odometer >= self._distance_goal:
#                 self.machine.end_travel_low()
#                 print(f"Vehicle {self.unique_id} has completed its journey. State: {self.machine.state}. This vehicle has travelled: {self.odometer} miles. Battery: {self.battery} kWh")
                
#             # # experimental - limit queue size to limit defined in charge station
#             # if (len(self._chosen_cp.queue_1) == self._chosen_cp._max_queue_size) and (len(self._chosen_cp.queue_2) == self._chosen_cp._max_queue_size):
#             #     print("Queue 1 and 2 are full. EV travelling under stress.")
#             # self.machine.join_charge_queue()
#             # # notification handled in charge station step method
       
#         # Transition Case 5: Start charging. in_queue -> charge
#         if self.machine.state == 'In_queue':
#             self.machine.start_charge()

#         # Transition Case 6: Continue charging. Charge -> charge
#         if self.machine.state == 'Charge':
#             if self.battery >= self._soc_charging_thresh:
#                 print(f"Charge complete. Vehicle {self.unique_id} is {self.machine.state}. This vehicle has travelled: {self.odometer} miles. Battery: {self.battery} kWh")
#                 self.machine.end_charge()
#             if self.battery < self._soc_charging_thresh:
#                 self.machine.continue_charge()
#                 self._chosen_cp.charge_ev()
#                 print(f"Charging. Vehicle {self.unique_id} is {self.machine.state}. This vehicle has travelled: {self.odometer} miles. Battery: {self.battery} kWh")
        

# 21/02/23
# logic for 'Stay in queue'

# if self._in_queue == True:
#     if self._chosen_cs.active_ev_1 == self:
#         self.machine.charge()
#         self._charging = True
#         self._in_queue = False
#         print(f"EV {self.unique_id} is now charging at Charge Station {self._chosen_cs.unique_id}. Current charge: {self.battery} kWh")
#     elif self._chosen_cs.active_ev_2 == self:
#         self.machine.charge()
#         self._charging = True
#         self._in_queue = False
#         print(f"EV {self.unique_id} is now charging at Charge Station {self._chosen_cs.unique_id}. Current charge: {self.battery} kWh")
#     else:
#         print(f"EV {self.unique_id} is waiting in queue at Charge Station {self._chosen_cs.unique_id}. Current charge: {self.battery} kWh")
#         self.machine.wait_in_queue()
#         self._in_queue = True
#         self._charging = False


# 22/02/23
# post successful tests, clean up EV class and remove redundant code



    # Working with issues
    # def step(self):

    #     ############
    #     # Travelling #
    #     ############

    #     # Block A - Transitions SM:

    #     # Transition Case 1: Start travelling. idle -> travel
    #     if self.machine.state == 'Idle' and self.odometer < self._distance_goal:
    #         self.machine.start_travel()

    #     # # 1b    
    #     # if self.machine.state == 'Travel' and self.odometer < self._distance_goal:
    #     #     self.machine.continue_travel()
    #     #     self.travel()
    #     #     print(f"Vehicle id: {self.unique_id} is {self.machine.state}. This vehicle has travelled: {self.odometer} miles. Battery: {self.battery} kWh")
        
    #     # Transition Case 2: Still travelling, battery low. Travel -> travel_low  
    #     if self.machine.state == 'Travel' and self.battery <= self._soc_usage_thresh:
    #         self.machine.get_low()
    #         # print(f"EV: {self.unique_id} has travelled: {str(self.odometer)} miles and is now {self.machine.state}. Current charge level is: {self.battery} kwh")


    #     ######################
    #     # Locating a Station #
    #     ######################
    #     # 21/02/23 - new flow for locating a station
    #     # Combo of 1b and 4

    #     if (self.machine.state == 'Travel' or self.machine.state == 'Travel_low') and self.odometer < self._distance_goal:
    #         if self.machine.state == 'Travel':
    #             self.travel()
    #             self.machine.continue_travel()
    #             print(f"EV {self.unique_id}  has travelled: {self.odometer} miles. State: {self.machine.state}. Battery: {self.battery} kWh")
    #         elif self.machine.state == 'Travel_low':
    #             if self.battery > 0:
    #                 print(f"EV {self.unique_id} is low on charge and is seeking a charge station. Current charge: {self.battery} kWh")
    #                 self.travel()
    #             elif self.battery <= 0:
    #                 self.machine.deplete_battery()
    #                 print(f"EV {self.unique_id} is out of charge and can no longer travel. State: {self.machine.state}. Current charge: {self.battery} kWh")

        

    #     # # Transition Case 4: EV with low battery is on lookout for Charge station. Notification.
    #     # if self.machine.state == 'Travel_low' and self.odometer < self._distance_goal:
    #     #     if self.battery > 0:
    #     #         print(f"EV {self.unique_id} is low on charge and is seeking a charge station. Current charge: {self.battery} kWh")
    #     #         self.travel()
    #     #     elif self.battery <= 0:
    #     #         self.machine.deplete_battery()
    #     #         print(f"EV {self.unique_id} is out of charge and can no longer travel. State: {self.machine.state}. Current charge: {self.battery} kWh")
        
    #     # 21/02/23 - new flow for recognising a charge station (CS), choosing a CS and charge queue.
    #     # combine both below for stopping at charge station:
    #     if self.odometer in self.checkpoint_list:
    #         if self.machine.state == 'Travel':
    #             print(f"EV {self.unique_id} has arrived at Charge Station but is in state: {self.machine.state}. Not travelling low.")
    #         elif self.machine.state == 'Travel_low':
    #             self._at_station = True
    #             print(f"EV {self.unique_id} is low on battery and is at a station. Seeking charge queue. Current EV state: {self.machine.state}")
    #             # self.select_cp()
    #             self.choose_charge_station()
    #             self.machine.seek_charge_queue()
    #             self.choose_cs_queue()
    #             # at this point EV has arrived at CS, joined one of the two queues and is waiting to become the active ev, and get charged.
    #             self.machine.join_charge_queue()
    #             self._in_queue = True

    #             # # experimental - limit queue size to limit defined in charge station
    #             # if (len(self._chosen_cs.queue_1) + len(self._chosen_cs.queue_2)) >= self._chosen_cs.queue_limit:
    #             #     print(f"EV {self.unique_id} has arrived at Charge Station but the queue is full. EV is not in queue.")
    #             #     self._in_queue = False
    #             # else:
    #             #     self.choose_cs_queue()
    #             #     self.machine.join_charge_queue()
    #             #     self._in_queue = True

    #     # Transition Case 3: EV with low battery does not arrive at charge station. Travel_low -> Battery_dead
    #     # condition self.battery < 10 because 10 is the minimum expenditure of energy to move the vehicle in one timestep
    #     if self.machine.state == 'Travel_low' and self.battery < 10:
    #         self.machine.deplete_battery()
    #         print(f"EV {self.unique_id} is now in state: {self.machine.state} and is out of charge.")

    #     # # old flow for recognising a charge station (CS), choosing a CS and charge queue.
    #     # # EV travelling or travelling low, checking for Charge Station at each checkpoint
    #     # if self.machine.state == 'Travel' and self.odometer in self.checkpoint_list:
    #     #     print(f"EV {self.unique_id} has arrived at Charge Station but is in state: {self.machine.state}. Not travelling low.")

    #     # if self.machine.state == 'Travel_low' and self.odometer in self.checkpoint_list:
    #     #     self._at_station = True
    #     #     print(f"EV {self.unique_id} is low on battery and is at a station. Seeking charge queue. Current EV state: {self.machine.state}")
    #     #     # self.select_cp()
    #     #     self.choose_charge_station()
    #     #     self.machine.seek_charge_queue()
    #     #     self.choose_cs_queue()
    #     #     self.machine.join_charge_queue()
    #     #     self._in_queue = True

    #     #     # # experimental - limit queue size to limit defined in charge station
    #     #     # if (len(self._chosen_cs.queue_1) == self._chosen_cs._max_queue_size) and (len(self._chosen_cs.queue_2) == self._chosen_cs._max_queue_size):
    #     #     #     print("Queue 1 and 2 are full. EV travelling under stress.")
    #     #     # self.machine.join_charge_queue()
    #     #     # # notification handled in charge station step method

        

        
        

    #     ############
    #     # Charging #
    #     ############

    #     # # Transition Case 6: Continue charging. Charge -> charge
    #     # if self.machine.state == 'Charge':
    #     #     self._at_station = True
    #     #     if self.battery >= self._soc_charging_thresh:
    #     #         print(f"Charge complete. EV {self.unique_id} is {self.machine.state}. This EV has travelled: {self.odometer} miles. Battery: {self.battery} kWh")
    #     #         self.machine.end_charge()
    #     #         self._is_charging = False
    #     #         self._at_station = False
    #     #         self._chosen_cs.finish_charge_ev() #??? untested, may break things
    #     #     if self.battery < self._soc_charging_thresh:
    #     #         # self.machine.continue_charge() # this is a redundant state, but it's here for completeness. may be responsible for some of the re-charging in same timestep issues
    #     #         self._chosen_cs.charge_evs()
    #     #         # self._chosen_cs.charge_ev_1()
    #     #         self._is_charging = True
    #     #         print(f"Charging. EV {self.unique_id} is {self.machine.state}. This EV has travelled: {self.odometer} miles. Battery: {self.battery} kWh")
        

    #     for ev in self.model.evs:
    #         if ev.machine.state == 'In_queue' and (ev == ev._chosen_cs.active_ev_1 or ev == ev._chosen_cs.active_ev_2):
    #             if ev.battery < ev._soc_charging_thresh:
    #                 try:
    #                     self.machine.start_charge()
    #                     self._chosen_cs.charge_evs()
    #                 except MachineError:
    #                     print(f"EV {self.unique_id} is in state: {self.machine.state}. Cannot start charging.")
    #         if ev.machine.state == 'Charge' and (ev == ev._chosen_cs.active_ev_1 or ev == ev._chosen_cs.active_ev_2):
    #             if ev.battery < ev._soc_charging_thresh:
    #                 self.machine.continue_charge()
    #                 self._chosen_cs.charge_evs()

    #                 # if this causes multiple charges in Timestep, move to separate elif block.
    #         if ev.machine.state == 'In_queue' and (ev != ev._chosen_cs.active_ev_1 or ev != ev._chosen_cs.active_ev_2):
    #             self.machine.wait_in_queue()
    #             print(f"EV {self.unique_id} is in state: {self.machine.state}. Waiting in queue.")

        

        
    #     # under work

    #     # # For chosen CS, if EV is active_ev at CS, start charging. If EV is not active_ev, wait in queue.
    #     # # Transition Case 5: Start charging. in_queue -> charge
    #     # if self.machine.state == 'In_queue' and self.ev == self._chosen_cs.active_ev:
    #     #     if self._chosen_cs.active_ev_1.battery >= self._chosen_cs.active_ev_1._soc_charging_thresh:
    #     #         print(f"Charge complete. EV {self.unique_id} is {self.machine.state}. This EV has travelled: {self.odometer} miles. Battery: {self.battery} kWh")
    #     #         self._chosen_cs.active_ev_1.machine.end_charge()
    #     #         self._is_charging = False
    #     #         self._at_station = False
    #     #         self._chosen_cs.finish_charge_ev() #??? untested, may break things
    #     #     if self.battery < self._soc_charging_thresh:
    #     #         # self.machine.continue_charge() # this is a redundant state, but it's here for completeness. may be responsible for some of the re-charging in same timestep issues
    #     #         self._chosen_cs.charge_evs()
    #     #         # self._chosen_cs.charge_ev_1()
    #     #         self._is_charging = True
    #     #         print(f"Charging. EV {self.unique_id} is {self.machine.state}. This EV has travelled: {self.odometer} miles. Battery: {self.battery} kWh")
    #     #     self.machine.start_charge()
    #     #     self._chosen_cs.charge_evs()
    #     #     # self._in_queue = False

    #     # # Transition Case 6: Continue charging. Charge -> charge
    #     # if self.machine.state == 'Charge':
    #     #     self._at_station = True
    #     #     if self.battery >= self._soc_charging_thresh:
    #     #         print(f"Charge complete. EV {self.unique_id} is {self.machine.state}. This EV has travelled: {self.odometer} miles. Battery: {self.battery} kWh")
    #     #         self.machine.end_charge()
    #     #         self._is_charging = False
    #     #         self._at_station = False
    #     #         self._chosen_cs.finish_charge_ev() #??? untested, may break things
    #     #     if self.battery < self._soc_charging_thresh:
    #     #         # self.machine.continue_charge() # this is a redundant state, but it's here for completeness. may be responsible for some of the re-charging in same timestep issues
    #     #         self._chosen_cs.charge_evs()
    #     #         # self._chosen_cs.charge_ev_1()
    #     #         self._is_charging = True
    #     #         print(f"Charging. EV {self.unique_id} is {self.machine.state}. This EV has travelled: {self.odometer} miles. Battery: {self.battery} kWh")
                
    #     # Transition Case 7: Journey Complete. travel -> idle
    #     if self.machine.state == 'Travel' and self.odometer >= self._distance_goal:
    #         self.machine.end_travel()
    #         print(f"EV {self.unique_id} has completed its journey. State: {self.machine.state}. This EV has travelled: {self.odometer} miles. Battery: {self.battery} kWh")

    #     # Transition Case 8: Journey complete, battery low. travel_low -> idle
    #     if self.machine.state == 'Travel_low' and self.odometer >= self._distance_goal:
    #         self.machine.end_travel_low()
    #         print(f"EV {self.unique_id} has completed its journey. State: {self.machine.state}. This EV has travelled: {self.odometer} miles. Battery: {self.battery} kWh")
    





    #     # # Transition Case 5: Start charging. in_queue -> charge
    #     # if self.machine.state == 'In_queue':
    #     #     self.machine.start_charge()
    #     #     # self._in_queue = False

    #     # # Transition Case 6: Continue charging. Charge -> charge
    #     # if self.machine.state == 'Charge':
    #     #     self._at_station = True
    #     #     if self.battery >= self._soc_charging_thresh:
    #     #         print(f"Charge complete. EV {self.unique_id} is {self.machine.state}. This EV has travelled: {self.odometer} miles. Battery: {self.battery} kWh")
    #     #         self.machine.end_charge()
    #     #         self._is_charging = False
    #     #         self._at_station = False
    #     #         self._chosen_cs.finish_charge_ev() #??? untested, may break things
    #     #     if self.battery < self._soc_charging_thresh:
    #     #         # self.machine.continue_charge() # this is a redundant state, but it's here for completeness. may be responsible for some of the re-charging in same timestep issues
    #     #         self._chosen_cs.charge_evs()
    #     #         # self._chosen_cs.charge_ev_1()
    #     #         self._is_charging = True
    #     #         print(f"Charging. EV {self.unique_id} is {self.machine.state}. This EV has travelled: {self.odometer} miles. Battery: {self.battery} kWh")
                
    #     # # Transition Case 7: Journey Complete. travel -> idle
    #     # if self.machine.state == 'Travel' and self.odometer >= self._distance_goal:
    #     #     self.machine.end_travel()
    #     #     print(f"EV {self.unique_id} has completed its journey. State: {self.machine.state}. This EV has travelled: {self.odometer} miles. Battery: {self.battery} kWh")

    #     # # Transition Case 8: Journey complete, battery low. travel_low -> idle
    #     # if self.machine.state == 'Travel_low' and self.odometer >= self._distance_goal:
    #     #     self.machine.end_travel_low()
    #     #     print(f"EV {self.unique_id} has completed its journey. State: {self.machine.state}. This EV has travelled: {self.odometer} miles. Battery: {self.battery} kWh")
    


# def exit_charge_station(self) -> None:
    #     """EV exits the charge station. Removes EV from queue and sets charge station to inactive."""
    #     if self._chosen_cs.active_ev_1 == self:
    #         self._chosen_cs = None
    #     elif self._chosen_cs.active_ev_2 == self:
    #         self._chosen_cs = None
    #     print(f"EV {(self.unique_id)} exited charge point at Charge Station {(self._chosen_cs.unique_id)}")


  # # Approach 1: use a link, index calculated by journey goal/by distance tick
    # def _set_checkpoint(self, factor) -> float:
    #     distance = self._distance_goal * factor
    #     return distance
    # # next step, do checkpointing using a link, index calculated by journey goal/by distance tick
    

# From ChargeStation class 
 # def charge_ev_1(self):
    #     """Charge the EV at the Charge Station.
    #     The EV is charged at the Chargepoint's charge rate.
    #     """
    #     # Transition Case: EV is charging at CP.
    #     if self.active_ev_1 is not None:
    #         print(f"EV {self.unique_id} is in state; {self.active_ev_1.machine.state}")
    #         self.active_ev_1.battery += self._charge_rate
    #         print(f"EV {self.active_ev_1.unique_id} at CP {self.unique_id} is in state: {self.active_ev_1.machine.state}, Battery: {self.active_ev_1.battery}")
    
    # def charge_ev_2(self):
    #     """Charge the EV at the Charge Station.
    #     The EV is charged at the Chargepoint's charge rate.
    #     """
    #     # Transition Case: EV is charging at CP.
    #     if self.active_ev_2 is not None:
    #         print(f"EV {self.unique_id} is in state; {self.active_ev_2.machine.state}")
    #         self.active_ev_2.battery += self._charge_rate
    #         print(f"EV {self.active_ev_2.unique_id} at CP {self.unique_id} is in state: {self.active_ev_2.machine.state}, Battery: {self.active_ev_2.battery}")
    
    # def charge_evs(self):
    #     self.charge_ev_1()
    #     self.charge_ev_2()

    # def charge_ev(self):
    #     """Charge the EV at the Charge Station.
    #     The EV is charged at the Chargepoint's charge rate.
    #     """
    #     # Transition Case: EV is charging at CP.
    #     if self.active_ev_1:
    #         print(f"EV {self.unique_id} is in state; {self.active_ev_1.machine.state}")
    #         self.active_ev_1.battery += self._charge_rate
    #         print(f"EV {self.active_ev_1.unique_id} at CP {self.unique_id} is in state: {self.active_ev_1.machine.state}, Battery: {self.active_ev_1.battery}")

    #     if self.active_ev_2:
    #         self.active_ev_2.battery += self._charge_rate
    #         print(f"EV {str(self.active_ev_2.unique_id)} at CP {(self.unique_id)} is in state: {self.active_ev_2.machine.state}, Battery: {self.active_ev_2.battery}")
       
    #     # # problem zone
    #     # if self.active_ev_1 is not None:
    #     #     print(f"EV {self.unique_id} is in state; {self.active_ev_1.machine.state}")
    #     #     self.active_ev_1.battery += self._charge_rate
    #     #     print(f"EV {self.active_ev_1.unique_id} at CP {self.unique_id} is in state: {self.active_ev_1.machine.state}, Battery: {self.active_ev_1.battery}")
    #     #     # print(f"The length of the queue 1 is now: {len(self.queue_1)}")
    #     # if self.active_ev_2 is not None:
    #     #     self.active_ev_2.battery += self._charge_rate
    #     #     print(f"EV {str(self.active_ev_2.unique_id)} at CP {(self.unique_id)} is in state: {self.active_ev_2.machine.state}, Battery: {self.active_ev_2.battery}")
    #     #     # print(f"The length of the queue 2 is now: {len(self.queue_2)}")


# def dequeue(self) -> None:
    #     """Remove the first EV from each queue. FIFO fom queue."""
    #     try:
    #         self.active_ev_1 = self.queue_1.pop(0)
    #         self.active_ev_2 = self.queue_2.pop(0)
    #         print(f"EV {(self.active_ev_1.unique_id)} dequeued at CP {self.unique_id} at Queue 1 and is in state: {self.active_ev_1.machine.state}")
    #         print(f"EV {(self.active_ev_2.unique_id)} dequeued at CP {self.unique_id} at Queue 2 and is in state: {self.active_ev_2.machine.state}")
    #         print(f"Queue 1 size: {len(self.queue_1)}, Queue 2 size: {len(self.queue_2)}")
    #     except:
    #         pass

# def step(self):
    #     # if self.active_ev_1 or self.active_ev_2 is None:
    #     #     self.dequeue()
    #     # # else:
    #     #     self.charge_ev()
    #     # step_1
    #     if self.active_ev_1 is None:
    #         self.dequeue_1()
    #     if self.active_ev_2 is None:
    #         self.dequeue_2()
    #     # pass

    #     # step2
    #     # for CS in self.model.chargestations:
    #     # active_ev 2
    #     if self.active_ev_1.battery < self.active_ev_1._soc_usage_thresh:
    #         self.active_ev_1.charge_ev_1()
    #     else:
    #         self.active_ev_1.finish_charge_ev_1()
    #     # active_ev 2
    #     if self.active_ev_2.battery < self.active_ev_2._soc_usage_thresh:
    #         self.active_ev_2.charge_ev_2()
    #     else:
    #         self.active_ev_2.finish_charge_ev_2()


# Explore for model
    #  if self.schedule.steps >= self.ticks:
            # self.running = False
            # print("Simulation finished.")
            # print(self.datacollector.get_agent_vars_dataframe())
            # print(self.datacollector.get_model_vars_dataframe())
            # print(self.datacollector.get_agent_vars_dataframe().columns)
            # print(self.datacollector.get_model_vars_dataframe().columns)
            # print(self.datacollector.get_agent_vars_dataframe().index)
            # print(self.datacollector.get_model_vars_dataframe().index)
            # print(self.datacollector.get_agent_vars_dataframe().index.names)
            # print(self.datacollector.get_model_vars_dataframe().index.names)
            # print(self.datacollector.get_agent_vars_dataframe().index.levels)
            # print(self.datacollector.get_model_vars_dataframe().index.levels)
            # print(self.datacollector.get_agent_vars_dataframe().index.levels[0])
            # print(self.datacollector.get_model_vars_dataframe().index.levels[0])
            # print(self.datacollector.get_agent_vars_dataframe().index.levels[1])
            # print(self.datacollector.get_model_vars_dataframe().index.levels[1])
            # print(self.datacollector.get_agent_vars_dataframe().index.levels[2])
            # print(self.datacollector.get_model_vars_dataframe().index.levels[2])
            # print(self.datacollector.get_agent_vars_dataframe().index.levels[3])
            # print(self.datacollector.get_model_vars_dataframe().index.levels[3])
            # print(self.datacollector.get_agent_vars_dataframe().index.levels[4])
            # print(self.datacollector.get_model_vars_dataframe().index.levels[4])
            # print(self.datacollector.get_agent_vars_dataframe().index.levels[5])
            # print(self.datacollector.get_model_vars_dataframe().index.levels[5])
            # print(self.datacollector.get_agent_vars_dataframe().index.levels[6])
            # print(self.datacollector.get_model_vars_dataframe().index.levels[6])
            # print(self.datacollector.get_agent_vars_dataframe().index.levels[7])
            # print(self.datacollector.get_model_vars_dataframe().index.levels[7])
            # print(self.datacollector.get_agent_vars_dataframe().index.levels[8])
            # print(self.datacollector.get_model_vars_dataframe().index.levels[8])
            # print(self.datacollector.get_agent_vars_dataframe().index.levels[9])
            # print(self.datacollector.get_model_vars_dataframe().index.levels[9])
            # print(self.datacollector.get_agent_vars_dataframe().index.levels[10])
            # print(self.datacollector.get_model_vars_dataframe().index.levels[10])


# def unpack_and_join(df, column_name):
#     # Get the column values as a list of strings
#     column_values = df[column_name].tolist()

#     # Strip the square brackets from the strings
#     column_values = [s.strip("[]") for s in column_values]

#     # Split the strings on commas and create a list of lists
#     split_values = [s.split(",") for s in column_values]

#     # Get the number of columns needed
#     num_cols = max([len(row) for row in split_values])

#     # Create the new columns in the output dataframe
#     column_names = [column_name+"_unpacked_"+str(i) for i in range(num_cols)]
#     new_df = pd.DataFrame(columns=column_names)

#     # Loop over the original column values and add the unpacked values to the new dataframe
#     for vals in split_values:
#         row_data = {}
#         for i in range(num_cols):
#             if i < len(vals):
#                 row_data[column_name+"_unpacked_"+str(i)] = vals[i].strip()
#             else:
#                 row_data[column_name+"_unpacked_"+str(i)] = ""
#         new_df = new_df.append(row_data, ignore_index=True)

#     # Join all values in the same position per row
#     new_df = new_df.apply(lambda x: ','.join(x.astype(str)), axis=1)

#     # Replace the original column with the unpacked and joined values
#     df[column_name] = new_df

#     return df