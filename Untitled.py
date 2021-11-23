#!/usr/bin/env python
# coding: utf-8

# In[72]:


# Model design
import agentpy as ap

# Visualization
import matplotlib.animation as plt
import matplotlib.pyplot as pl
import matplotlib as plss
import seaborn as sns
import IPython


# In[246]:


class ParkingModel(ap.Model):

    def setup(self):

        # Create agents (cars)
        n_cars = int(self.p.size**2)
        cars = self.agents = ap.AgentList(self, n_cars)

        # Create grid (Parking lot)
        self.parking = ap.Grid(self, [self.p.size]*2, track_empty=True)
        self.parking.add_agents(cars, random=True, empty=True)

        # Initiate a dynamic variable for all cars
        # Condition 0: street, 1: car, 2: sidewalk, 3: parking spot
        self.agents.condition = 0

        # Start a car in one entry
        moving_cars = self.parking.agents[5, 12]
        moving_cars.condition = 1
        
        
        # Space for parking
        
        estacionamiento = self.parking.agents[8:12, 17:50]
        estacionamiento.condition=3
        
        estacionamiento = self.parking.agents[16:20, 17:50]
        estacionamiento.condition=3
        
        estacionamiento = self.parking.agents[28:32, 17:50]
        estacionamiento.condition=3
        
        estacionamiento = self.parking.agents[38:42, 17:50]
        estacionamiento.condition=3
        
        
        # Space for banquetas
        banqueta = self.parking.agents[0:self.p.size, 0:8]
        banqueta.condition=2
        
        banqueta = self.parking.agents[0:8, 16:50]
        banqueta.condition=2
        
        banqueta = self.parking.agents[20:28, 16:50]
        banqueta.condition=2
        
        banqueta = self.parking.agents[42:50, 16:50]
        banqueta.condition=2
        
        banqueta = self.parking.agents[0:1,0:40]
        banqueta.condition=2
        
        banqueta = self.parking.agents[8:12, 16]
        banqueta.condition=2
        
        banqueta = self.parking.agents[16:20, 16]
        banqueta.condition=2
        
        banqueta = self.parking.agents[28:32, 16]
        banqueta.condition=2
        
        banqueta = self.parking.agents[38:42, 16]
        banqueta.condition=2
        
        banqueta = self.parking.agents[0:50, 49]
        banqueta.condition=2
        
        
        
        
        
        
        self.random = self.model.random

    def step(self):

        # Select moving cars
        moving_cars = self.agents.select(self.agents.condition == 1)
        
        # moving cars
        for car in moving_cars:
            for neighbor in self.parking.neighbors(car):
                if neighbor.condition == 0:
                    if(self.random.randint(0,1) == 1):
                        neighbor.condition = 1 # Neighbor starts
                        break
            car.condition = 0 # Tree burns out

        # Stop simulation if the car is in the parking spot
        if len(moving_cars) == 0:
            self.stop()

    def end(self):

        # Document a measure at the end of the simulation
        parked_cars = len(self.agents.select(self.agents.condition == 2))
        self.report('Percentage of parked cars',
                    parked_cars / len(self.agents))


# In[247]:


# Define parameters

parameters = {
    'Car density': 1, # Percentage of cars
    'size': 50,
    'steps': 100,
}


# In[249]:


# Create single-run animation with custom colors

def animation_plot(model, ax):
    attr_grid = model.parking.attr_grid('condition')
    color_dict = {0:'green', 1:'blue', 2:'gray', 3:'yellow', None:'black'}
    ap.gridplot(attr_grid, ax=ax, color_dict=color_dict, convert=True)
    ax.set_title(f"Estacionamiento\n"
                 f"Time-step: {model.t}, Carros en movimiento: "
                 f"{len(model.agents.select(model.agents.condition == 1))} \n"
                 f"gente en movimiento: "
                 f"{len(model.agents.select(model.agents.condition == 4))}")
    
    

fig, ax = pl.subplots()
model = ParkingModel(parameters)
animation = ap.animate(model, fig, ax, animation_plot)
IPython.display.HTML(animation.to_jshtml(fps=15))


# In[ ]:




