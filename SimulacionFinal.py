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


# In[2]:


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
        moving_cars.condition = 10
        
        
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
            if(random.randint(0, 4) == 1):
                park_car.condition = 19
                
        
        # Space for banquetas
        banqueta = self.parking.agents[0:self.p.size, 0:9]
        banqueta.condition=1
        
        banqueta = self.parking.agents[0:3, 16:50]
        banqueta.condition=1
        
        banqueta = self.parking.agents[8:9, 16:50]
        banqueta.condition=1
        
        banqueta = self.parking.agents[14:16, 16:50]
        banqueta.condition=1
        
        banqueta = self.parking.agents[21:23, 16:50]
        banqueta.condition=1
        
        banqueta = self.parking.agents[27:29, 16:50]
        banqueta.condition=1
        
        banqueta = self.parking.agents[34:36, 16:50]
        banqueta.condition=1
        
        banqueta = self.parking.agents[41:42, 16:50]
        banqueta.condition=1
        
        banqueta = self.parking.agents[47:50, 16:50]
        banqueta.condition=1
        
        banqueta = self.parking.agents[0:self.p.size, 49]
        banqueta.condition=1
        
        
        #barreras invisibles
        barreras_invisibles = self.parking.agents[5, 15:48]
        barreras_invisibles.condition=2
        
        barreras_invisibles = self.parking.agents[11, 15:48]
        barreras_invisibles.condition=2
        
        barreras_invisibles = self.parking.agents[18, 15:48]
        barreras_invisibles.condition=2
        
        barreras_invisibles = self.parking.agents[24:26, 15:49]
        barreras_invisibles.condition=2
        
        barreras_invisibles = self.parking.agents[31, 15:48]
        barreras_invisibles.condition=2
        
        barreras_invisibles = self.parking.agents[38, 15:48]
        barreras_invisibles.condition=2
        
        barreras_invisibles = self.parking.agents[44, 15:48]
        barreras_invisibles.condition=2
        
        
        #Cruces peatonales
        cruce = self.parking.agents[1:3, 9:16]
        cruce.condition = 4
        
        cruce = self.parking.agents[8:9, 9:16]
        cruce.condition = 4
        
        cruce = self.parking.agents[14:16, 9:16]
        cruce.condition = 4
        
        cruce = self.parking.agents[21:23, 9:16]
        cruce.condition = 4
        
        cruce = self.parking.agents[27:29, 9:16]
        cruce.condition = 4
        
        cruce = self.parking.agents[34:36, 9:16]
        cruce.condition = 4
        
        cruce = self.parking.agents[41:42, 9:16]
        cruce.condition = 4
        
        cruce = self.parking.agents[47:49, 9:16]
        cruce.condition = 4
        
        
        
        #carriles con sentido 
        
        carril = self.parking.agents[0:self.p.size, 9]
        carril.condition = 2
        
        carril = self.parking.agents[0:self.p.size, 11]
        carril.condition = 2
        
        carril = self.parking.agents[0:self.p.size, 12]
        carril.condition = 2
        
        carril = self.parking.agents[0:self.p.size, 14]
        carril.condition = 2
        
        
        carril = self.parking.agents[4, 10:16]
        carril.condition = 0
        
        carril = self.parking.agents[6, 10:16]
        carril.condition = 0
        
        carril = self.parking.agents[10, 10:16]
        carril.condition = 0
        
        carril = self.parking.agents[12, 10:16]
        carril.condition = 0
        
        carril = self.parking.agents[17, 10:16]
        carril.condition = 0
        
        carril = self.parking.agents[19, 10:16]
        carril.condition = 0
        
        carril = self.parking.agents[30, 10:16]
        carril.condition = 0
        
        carril = self.parking.agents[32, 10:16]
        carril.condition = 0
        
        carril = self.parking.agents[37, 10:16]
        carril.condition = 0
        
        carril = self.parking.agents[39, 10:16]
        carril.condition = 0
        
        carril = self.parking.agents[43, 10:16]
        carril.condition = 0
        
        carril = self.parking.agents[45, 10:16]
        carril.condition = 0
        
        
        carril = self.parking.agents[3, 15:17]
        carril.condition=2
        
        carril = self.parking.agents[7, 15:17]
        carril.condition=2
        
        carril = self.parking.agents[9, 15:17]
        carril.condition=2
        
        carril = self.parking.agents[13, 15:17]
        carril.condition=2
        
        carril = self.parking.agents[16, 15:17]
        carril.condition=2
        
        carril = self.parking.agents[20, 15:17]
        carril.condition=2
        
        carril = self.parking.agents[29, 15:17]
        carril.condition=2
        
        carril = self.parking.agents[33, 15:17]
        carril.condition=2
        
        carril = self.parking.agents[36, 15:17]
        carril.condition=2
        
        carril = self.parking.agents[40, 15:17]
        carril.condition=2
        
        carril = self.parking.agents[42, 15:17]
        carril.condition=2
        
        carril = self.parking.agents[46, 15:17]
        carril.condition=2
        
        """
        carril = self.parking.agents[4, 12]
        carril.condition = 32
        
        carril = self.parking.agents[6, 12]
        carril.condition = 32
        
        carril = self.parking.agents[10, 12]
        carril.condition = 32
        
        carril = self.parking.agents[12, 12]
        carril.condition = 32
        
        carril = self.parking.agents[17, 12]
        carril.condition = 32
        
        carril = self.parking.agents[19, 12]
        carril.condition = 32
        
        carril = self.parking.agents[30, 12]
        carril.condition = 32
        
        carril = self.parking.agents[32, 12]
        carril.condition = 32
        
        carril = self.parking.agents[37, 12]
        carril.condition = 32
        
        carril = self.parking.agents[39, 12]
        carril.condition = 32
        
        carril = self.parking.agents[43, 12]
        carril.condition = 32
        
        carril = self.parking.agents[45, 12]
        carril.condition = 32
        """
        #banqueta invisible en crucero
        
        banqueta = self.parking.agents[1:3, 9]
        banqueta.condition = 5
        
        banqueta = self.parking.agents[1:3, 11:13]
        banqueta.condition = 5
        
        banqueta = self.parking.agents[1:3, 14]
        banqueta.condition = 5
        
        banqueta = self.parking.agents[8:9, 9]
        banqueta.condition = 5
        
        banqueta = self.parking.agents[8:9, 11:13]
        banqueta.condition = 5
        
        banqueta = self.parking.agents[8:9, 14]
        banqueta.condition = 5
        
        banqueta = self.parking.agents[14:16, 9]
        banqueta.condition = 5
        
        banqueta = self.parking.agents[14:16, 11:13]
        banqueta.condition = 5
        
        banqueta = self.parking.agents[14:16, 14]
        banqueta.condition = 5
        
        banqueta = self.parking.agents[21:23, 9]
        banqueta.condition = 5
        
        banqueta = self.parking.agents[21:23, 11:13]
        banqueta.condition = 5
        
        banqueta = self.parking.agents[21:23, 14]
        banqueta.condition = 5
        
        banqueta = self.parking.agents[27:29, 9]
        banqueta.condition = 5
        
        banqueta = self.parking.agents[27:29, 11:13]
        banqueta.condition = 5
        
        banqueta = self.parking.agents[27:29, 14]
        banqueta.condition = 5
        
        banqueta = self.parking.agents[34:36, 9]
        banqueta.condition = 5
        
        banqueta = self.parking.agents[34:36, 11:13]
        banqueta.condition = 5
        
        banqueta = self.parking.agents[34:36, 14]
        banqueta.condition = 5
        
        banqueta = self.parking.agents[41:42, 9]
        banqueta.condition = 5
        
        banqueta = self.parking.agents[41:42, 11:13]
        banqueta.condition = 5
        
        banqueta = self.parking.agents[41:42, 14]
        banqueta.condition = 5
        
        banqueta = self.parking.agents[47:49, 9]
        banqueta.condition = 5
        
        banqueta = self.parking.agents[47:49, 11:13]
        banqueta.condition = 5
        
        banqueta = self.parking.agents[47:49, 14]
        banqueta.condition = 5
       
        
        #des spawner de carros
        des_spawner = self.parking.agents[0, 13]
        des_spawner.condition = 31
        
        des_spawner = self.parking.agents[49, 13]
        des_spawner.condition = 30
        
        #spawner de carros
        spawner = self.parking.agents[0, 10]
        spawner.condition = 31
        
        spawner = self.parking.agents[49, 10]
        spawner.condition = 30
        
        
        #spawnear personas
        gentes = self.agents.select(self.agents.condition == 1)
        for gente in gentes:
            if(random.randint(0, 20) == 10):
                gente.condition = 20;
        
        
        
        self.random = self.model.random

        
    def step(self):
        
        # Select persons
        moving_persons = self.agents.select(self.agents.condition == 20)
        moving_persons_in_street = self.agents.select(self.agents.condition == 21)
        moving_persons_in_street_banqueta = self.agents.select(self.agents.condition == 22)

        # moving persons
        for person in moving_persons:
            neighbor = self.parking.neighbors(person)
            neighbor = random.choice(list(neighbor))
            
            cont = 0
            while(neighbor.condition != 1) and (neighbor.condition != 4):
                neighbor = self.parking.neighbors(person)
                neighbor = random.choice(list(neighbor))
                
                cont +=1
                if (cont == 20):
                    break
            
            if (cont != 20):
                if(neighbor.condition == 1):
                    neighbor.condition = 20
                    person.condition = 1
                else:
                    neighbor.condition = 21
                    person.condition = 1
                
            
        #personas en crucero        
        for person in moving_persons_in_street:
            neighbor = self.parking.neighbors(person)
            neighbor = random.choice(list(neighbor))
            
            cont = 0
            while(neighbor.condition != 1) and (neighbor.condition != 4) and (neighbor.condition != 5):
                neighbor = self.parking.neighbors(person)
                neighbor = random.choice(list(neighbor))
                
                cont +=1
                if (cont == 20):
                    break
            
            if(cont != 20):
                if(neighbor.condition == 1):
                    neighbor.condition = 20
                    person.condition = 4
                elif(neighbor.condition == 5):
                    neighbor.condition = 22
                    person.condition = 4
                else:
                    neighbor.condition = 21
                    person.condition = 4
        
        #personas en crucero en banqueta
        
        for person in moving_persons_in_street_banqueta:
            neighbor = self.parking.neighbors(person)
            neighbor = random.choice(list(neighbor))
            
            cont = 0
            while(neighbor.condition != 4) and (neighbor.condition != 5):
                neighbor = self.parking.neighbors(person)
                neighbor = random.choice(list(neighbor))
                
                cont +=1
                if (cont == 20):
                    break
            
            if(cont == 0):
                if(neighbor.condition == 5):
                    neighbor.condition = 22
                    person.condition = 5
                else:
                    neighbor.condition = 21
                    person.condition = 5
                
        # Select moving cars
        moving_cars = self.agents.select(self.agents.condition == 10)
        moving_cars_back = self.agents.select(self.agents.condition == 11)
        
        
        # movimiento de vehiculos que buscan estacionamiento
        for car in moving_cars:
            persona_cerca = True
            for vecino in self.parking.neighbors(car, 2):
                if(vecino.condition == 21 or vecino.condition == 20):
                    persona_cerca = False #asdsdfadsfasdf
                    
            if(persona_cerca):
                neighbor = self.parking.neighbors(car)
                if(random.randint(1,2) == 1):
                    neighbor = (list(neighbor)[4])
                else:
                    neighbor = random.choice(list(neighbor))
                cont = 0
                while((neighbor.condition != 0)  and 
                      (neighbor.condition != 3) and 
                      (neighbor.condition != 4)):
                    neighbor = self.parking.neighbors(car)
                    neighbor = random.choice(list(neighbor))

                    cont +=1
                    if (cont == 20):
                        break

                if(cont != 20):

                    #estacionarse
                    if(neighbor.condition == 3):
                        neighbor.condition = 19
                        car.condition = 0
                        for i in self.parking.neighbors(neighbor):
                            if(i.condition == 1):
                                i.condition = 20
                                break

                    else:

                        if(neighbor.condition == 4):#entra en un crucero
                            neighbor.condition = 12
                            car.condition = 11
                        else: #sigue un camino random
                            neighbor.condition = 10
                            car.condition = 11
      
        # movimiento de carros que ya se van
        moving_cars_out = self.agents.select(self.agents.condition == 14)
        moving_cars_out_crucero = self.agents.select(self.agents.condition == 15)
        
        for car in moving_cars_out:
            persona_cerca = True
            #revisa si hay una persona cerca
            for vecino in self.parking.neighbors(car, 2):
                if(vecino.condition == 21 or vecino.condition == 20):
                    persona_cerca = False #asdsdfadsfasdf
                    
            if(persona_cerca):
                for vecino in self.parking.neighbors(car):
                    if(vecino.condition == 4):
                        vecino.condition = 15
                        car.condition = 11
                        break
                    if(vecino.condition == 0):
                        vecino.condition = 14
                        car.condition = 11
                        break
            
                
        # movimiento de carros que ya se van en un crucero
        
        for car in moving_cars_out_crucero:
            neighbor_list = self.parking.neighbors(car)
            cont = 0
            for vecino in neighbor_list:
                if (vecino.condition == 31):
                    car.condition = 4
                    cont == 20
                    break
                
                if(vecino.condition == 0 or vecino.condition == 4):
                    neighbor = vecino
                    break
            
            
            
            if(cont == 0):
                persona_cerca = True
                #revisa si hay una persona cerca
                for vecino in self.parking.neighbors(car, 1): # aquiiiiiiiiiiiiiii
                    if(vecino.condition == 22 or vecino.condition == 21 or vecino.condition == 20):
                        persona_cerca = False

                if(persona_cerca):
                    if(neighbor.condition == 4):
                        neighbor.condition = 15
                        car.condition = 13
                    else:
                        neighbor.condition = 14
                        car.condition = 13
                
                
        # moving cars in crucero

        moving_cars_in_crucero = self.agents.select(self.agents.condition == 12)
        moving_cars_back_in_crucero = self.agents.select(self.agents.condition == 13)
        
        
        for car in moving_cars_in_crucero:
            neighbor = self.parking.neighbors(car)
            neighbor = random.choice(list(neighbor))
            cont = 0
            
            while(neighbor.condition != 0) and (neighbor.condition != 4):
                neighbor = self.parking.neighbors(car)
                neighbor = random.choice(list(neighbor))
                cont +=1
                if (neighbor.condition == 31):
                    car.condition = 4
                    cont == 20
                if (cont == 20):
                    break
            
            if (cont != 20):
                if(neighbor.condition == 4):
                    neighbor.condition = 12
                    car.condition = 13
                elif(neighbor.condition == 0):
                    neighbor.condition = 10
                    car.condition = 13
        
        # moving cars back
        for back in moving_cars_back:
            back.condition = 0
        
        for back in moving_cars_back_in_crucero:
            back.condition = 4
            
            
        # Select occupate parking spots
        parking_occupate = self.agents.select(self.agents.condition == 19)
        
        # parking spots out
        for car in parking_occupate:
            space_out=False
            Person_out=False
            
            if(random.randint(1,5) == 1):
                
                for neighbor in self.parking.neighbors(car):
                    if(neighbor.condition == 0):
                        space_out = True
                        
                    if(neighbor.condition == 20):
                        Person_out = True
                        
                if(Person_out and space_out):
                    car.condition = 3
                    for neighbor in self.parking.neighbors(car):
                        if(neighbor.condition == 20 and Person_out):
                            neighbor.condition = 1
                            Person_out = False
                        
                        if(neighbor.condition == 0 and space_out):
                            neighbor.condition = 14
                            space_out = False

                        
        # spawner de carros
        
        spawners = self.agents.select(self.agents.condition == 30)
        for new_car in spawners:
            if(random.randint(1,20) == 1):
                for i in self.parking.neighbors(new_car):
                    if(i.condition == 4):
                        i.condition = 12
                        break
        
        bug_morado= self.agents.select(self.agents.condition == 14)
        for i in bug_morado:
            salir = True
            for neighbor in self.parking.neighbors(i):
                if(neighbor != 1):
                    salir = False
            
            if(salir):
                i.condition = 20
            
            
            
        # Stop simulation if the car is in the parking spot
        #if len(moving_cars + moving_cars_in_crucero) == 0:
        #    self.stop()

    def end(self):

        # Document a measure at the end of the simulation
        parked_cars = len(self.agents.select(self.agents.condition == 1))
        self.report('Percentage of parked cars',
                    parked_cars / len(self.agents))


# In[6]:


# Define parameters

parameters = {
    'Car density': 1, # Percentage of cars
    'size': 50,
    'steps': 50, # cambiar la cantidad de pasos
}


# In[7]:


# Crear Archivo
#  0  - 9  Tipo de mapa
#  10 - 19 agentes de vehiculo
#  20 - 29 agentes de personas
def animation_plot(model, ax):
    attr_grid = model.parking.attr_grid('condition')
    color_dict = {0:'green',   #calle
                  1:'gray',    #banqueta
                  2:'green',  #bannquetas invisibles #a5ffb1
                  3:'yellow',  #estacionamiento libre
                  4:'#e3e3e3', #crucero
                  5:'#e3e3e3', #banqueta invisible en crucero white
                  
                  10:'blue',   #carro
                  11:'#4692b2',#Back-car
                  12:'#ff6a00',#carro crucero
                  13:'#4692b2',#Back-car crucero
                  14:'purple', #carro que ya se va
                  15:'black', #carro que ya se va en un crucero
                  19:'red',    #estacionamiento ocupado
                  
                  20:'pink',   #persona
                  21:'pink',  #persona en crucero
                  22:'pink', #persona en banqueta de crucero
                  
                  30:'black', #spawner de carros
                  31:'black', #des spawner de carros
                  32:'black', #pasada solo para los que buscan estacionamiento
                  33:'white', #pasada solo para los que NO buscan estacionamiento
                  
                  None:'black'}
   
        
    ap.gridplot(attr_grid, ax=ax, color_dict=color_dict, convert=True)
    ax.set_title(f"Estacionamiento\n"
                 f"Time-step: {model.t}, Carros en movimiento: "
                 f"{len(model.agents.select(model.agents.condition == 10)) + len(model.agents.select(model.agents.condition == 12)) +len(model.agents.select(model.agents.condition == 14)) +len(model.agents.select(model.agents.condition == 15))} \n"
                 f"gente en movimiento: "
                 f"{len(model.agents.select(model.agents.condition == 20)) + len(model.agents.select(model.agents.condition == 21))}"
                 f" Carros estacionados: "
                 f"{len(model.agents.select(model.agents.condition == 19))}")


#ajustar las banquetas con los caminos invisibles
#que los carros no puedan salirse
#que las personas si puedan caminar
#agente de persona en estas banquetas
#que los carros tambien detecten a estar personas

#ponerle direccion o controlador a los carriles en caso de que choquen de frente
#poner algo de orden en las personas



fig, ax = pl.subplots()
model = ParkingModel(parameters)
animation = ap.animate(model, fig, ax, animation_plot)
IPython.display.HTML(animation.to_jshtml(fps=15))


# In[21]:


# Crear Archivo
#  0  - 9  Tipo de mapa
#  10 - 19 agentes de vehiculo
#  20 - 29 agentes de personas
report = open('arrayy.txt', 'w')
def animation_plot(model, ax):
    attr_grid = model.parking.attr_grid('condition')
    color_dict = {0:'green',   #calle
                  1:'gray',    #banqueta
                  2:'#a5ffb1',  #bannquetas invisibles #a5ffb1
                  3:'yellow',  #estacionamiento libre
                  4:'#e3e3e3', #crucero
                  5:'#e3e3e3', #banqueta invisible en crucero white
                  
                  10:'blue',   #carro
                  11:'#4692b2',#Back-car
                  12:'#ff6a00',#carro crucero
                  13:'#4692b2',#Back-car crucero
                  14:'purple', #carro que ya se va
                  15:'black', #carro que ya se va en un crucero
                  19:'red',    #estacionamiento ocupado
                  
                  20:'pink',   #persona
                  21:'pink',  #persona en crucero
                  22:'pink', #persona en banqueta de crucero
                  
                  30:'black', #spawner de carros
                  31:'black', #des spawner de carros
                  32:'black', #pasada solo para los que buscan estacionamiento
                  33:'white', #pasada solo para los que NO buscan estacionamiento
                  
                  None:'black'}
    
    #print(attr_grid)
    listToStr = '\n'.join(map(str, attr_grid.tolist()))
    #print(listToStr)
    ##report.write(listToStr + '\n' + '\n')
    lista = []
    x = 0
    
    #report.write("{")
    for i in attr_grid.tolist():
        y=0
        #report.write("{")
        si = False
        for j in i:
            if(j == 10.0 or j == 12.0 or j == 14.0 or j == 19.0):
                #print("{", x,",", y,"},")
                si = True
                report.write(str(x)+","+ str(y))
                if(j+1 != i):
                    report.write(" ")
                
                aux = [x, y, 0]
                lista.append(aux)
            y+=1
        
        
        x+=1
        
        
    report.write("\n")
    #print(lista)
    #x = 0
    #for i in attr_grid.tolist():
    #    y=0
    #    for j in i:
    #        if(j == 20.0 or j == 21.0 or j == 22.0):
    #            #print("{", x,",", y,"},")
    #            report.write("{"+ str(x)+","+ str(y)+"},")
    #        y+=1
    #    report.write('\n')
    #    x+=1
    #
    #report.write('\n')
   
        
    ap.gridplot(attr_grid, ax=ax, color_dict=color_dict, convert=True)
    ax.set_title(f"Estacionamiento\n"
                 f"Time-step: {model.t}, Carros en movimiento: "
                 f"{len(model.agents.select(model.agents.condition == 10)) + len(model.agents.select(model.agents.condition == 12)) +len(model.agents.select(model.agents.condition == 14)) +len(model.agents.select(model.agents.condition == 15))} \n"
                 f"gente en movimiento: "
                 f"{len(model.agents.select(model.agents.condition == 20)) + len(model.agents.select(model.agents.condition == 21))}"
                 f" Carros estacionados: "
                 f"{len(model.agents.select(model.agents.condition == 19))}")


#ajustar las banquetas con los caminos invisibles
#que los carros no puedan salirse
#que las personas si puedan caminar
#agente de persona en estas banquetas
#que los carros tambien detecten a estar personas

#ponerle direccion o controlador a los carriles en caso de que choquen de frente
#poner algo de orden en las personas



fig, ax = pl.subplots()
model = ParkingModel(parameters)
animation = ap.animate(model, fig, ax, animation_plot)
IPython.display.HTML(animation.to_jshtml(fps=15))
report.close()

