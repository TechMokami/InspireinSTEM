#!/usr/bin/python

##################################
#       Subject: CLASSES
#       Name:    Joan Mokami
#       Date:    03/06/2022
##################################
 
class Vehicles:
    def __init__(vehicle,max_speed,mileage):
        vehicle.max_speed=max_speed
        vehicle.mileage=mileage
        
Toyota=Vehicles(str(180)+"km/hr",str(150000)+"km")
Mercedees=Vehicles(str(240)+"km/hr",str(100)+"km")
print(Toyota.max_speed,Toyota.mileage)

    
