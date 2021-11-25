#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Model design
import agentpy as ap

# Visualization
import matplotlib.animation as plt
import matplotlib.pyplot as pl
import matplotlib as plss
import seaborn as sns
import IPython

import random


# In[73]:


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
        moving_cars = self.parking.agents[25, 15]
        moving_cars.condition = 1
        
        
        # Space for parking
        
        estacionamiento = self.parking.agents[3, 17:49]
        estacionamiento.condition=3
        
        estacionamiento = self.parking.agents[7, 17:49]
        estacionamiento.condition=3
        
        estacionamiento = self.parking.agents[9, 17:49]
        estacionamiento.condition=3
        
        estacionamiento = self.parking.agents[13, 17:49]
        estacionamiento.condition=3
        
        estacionamiento = self.parking.agents[16, 17:49]
        estacionamiento.condition=3
        
        estacionamiento = self.parking.agents[20, 17:49]
        estacionamiento.condition=3
        
        estacionamiento = self.parking.agents[29, 17:49]
        estacionamiento.condition=3
        
        estacionamiento = self.parking.agents[33, 17:49]
        estacionamiento.condition=3
        
        estacionamiento = self.parking.agents[36, 17:49]
        estacionamiento.condition=3
        
        estacionamiento = self.parking.agents[40, 17:49]
        estacionamiento.condition=3
        
        estacionamiento = self.parking.agents[42, 17:49]
        estacionamiento.condition=3
        
        estacionamiento = self.parking.agents[46, 17:49]
        estacionamiento.condition=3
        
        parking_cars = self.agents.select(self.agents.condition == 3)
        for park_car in parking_cars:
            if(random.randint(0, 10) == 1):
                park_car.condition = 4;
        
        # Space for banquetas
        banqueta = self.parking.agents[0:self.p.size, 0:8]
        banqueta.condition=2
        
        banqueta = self.parking.agents[0:3, 16:50]
        banqueta.condition=2
        
        banqueta = self.parking.agents[8:9, 16:50]
        banqueta.condition=2
        
        banqueta = self.parking.agents[14:16, 16:50]
        banqueta.condition=2
        
        banqueta = self.parking.agents[21:23, 16:50]
        banqueta.condition=2
        
        banqueta = self.parking.agents[27:29, 16:50]
        banqueta.condition=2
        
        banqueta = self.parking.agents[34:36, 16:50]
        banqueta.condition=2
        
        banqueta = self.parking.agents[41:42, 16:50]
        banqueta.condition=2
        
        banqueta = self.parking.agents[47:50, 16:50]
        banqueta.condition=2
        
        banqueta = self.parking.agents[0:self.p.size, 49]
        banqueta.condition=2
        
        
        
        #barreras invisibles
        estacionamiento = self.parking.agents[5, 17:49]
        estacionamiento.condition=6
        
        estacionamiento = self.parking.agents[11, 17:49]
        estacionamiento.condition=6
        
        estacionamiento = self.parking.agents[18, 17:49]
        estacionamiento.condition=6
        
        estacionamiento = self.parking.agents[24:26, 17:49]
        estacionamiento.condition=6
        
        estacionamiento = self.parking.agents[31, 17:49]
        estacionamiento.condition=6
        
        estacionamiento = self.parking.agents[38, 17:49]
        estacionamiento.condition=6
        
        estacionamiento = self.parking.agents[44, 17:49]
        estacionamiento.condition=6
        
        #spawnear personas
        gentes = self.agents.select(self.agents.condition == 2)
        for gente in gentes:
            if(random.randint(0, 20) == 1):
                gente.condition = 5;
        
        
        
        self.random = self.model.random

    def step(self):

        # Select moving cars
        moving_cars = self.agents.select(self.agents.condition == 1)
        moving_cars_back = self.agents.select(self.agents.condition == 9)
        
        # Select occupate parking spots
        parking_occupate = self.agents.select(self.agents.condition == 4)
        
        # Select persons
        moving_persons = self.agents.select(self.agents.condition == 5)
        
        # moving cars
        for car in moving_cars:
            neighbor = self.parking.neighbors(car)
            neighbor = random.choice(list(neighbor))
            
            while((neighbor.condition == 2) or (neighbor.condition == 9) or (neighbor.condition == 4) or (neighbor.condition == 5) or (neighbor.condition == 6)):
                neighbor = self.parking.neighbors(car)
                neighbor = random.choice(list(neighbor))
            
            if(neighbor.condition == 3):
                neighbor.condition = 4
                car.condition = 0
            else:
                neighbor.condition = 1
                car.condition = 9
      
            
        
        # moving cars back
        for back in moving_cars_back:
            back.condition=0

        # parking spots out
        for car in parking_occupate:
            space_out=False
            if(random.randint(0,20) == 1):
                
                for neighbor in self.parking.neighbors(car):
                    if(neighbor.condition == 0):
                        space_out = True
                        break
                if(space_out):
                    neighbor.condition = 1
                    car.condition = 3
                
            #if(space_out):
                #if(random.randint(0, 20) == 1): # 5% de que un lugar se desocupe
                    #car.condition = 3
                    #neighbor.condition = 1

        # moving persons
        for person in moving_persons:
            neighbor = self.parking.neighbors(person)
            neighbor = random.choice(list(neighbor))
            
            while(neighbor.condition != 2):
                neighbor = self.parking.neighbors(person)
                neighbor = random.choice(list(neighbor))
    
            neighbor.condition = 5
        
            person.condition = 2
        
        
        # Stop simulation if the car is in the parking spot
        if len(moving_cars) == 0:
            self.stop()

    def end(self):

        # Document a measure at the end of the simulation
        parked_cars = len(self.agents.select(self.agents.condition == 2))
        self.report('Percentage of parked cars',
                    parked_cars / len(self.agents))


# In[74]:


# Define parameters

parameters = {
    'Car density': 1, # Percentage of cars
    'size': 50,
    'steps': 50,
}


# In[77]:


# Create single-run animation with custom colors

def animation_plot(model, ax):
    attr_grid = model.parking.attr_grid('condition')
    color_dict = {0:'green', 1:'blue', 2:'gray', 3:'yellow', 4:'red', 5:'pink', 6:'purple', 9:'#8cfffb', 10:'black', None:'black'}
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




