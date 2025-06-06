import json
from car import Car
import os
class User:
    def __init__(self,username,email,password,firstname,lastname,balance,role,address,rentedcarid = None):
        self.username = username
        self.email = email
        self.password = password
        self.firstName = firstname
        self.lastName = lastname
        self.balance = balance
        self.role = role
        self.address = address
##################3 Umers part ################
        if rentedcarid == "null" or rentedcarid is None:
                    self.rented_car_id = None
        else:
                    self.rented_car_id = rentedcarid
    def to_dict(self):
            return {
                'Username':self.username,
                'Email':self.email,
                'Password': self.password,
                'FirstName':self.firstName,
                'LastName':self.lastName,
                'Balance':self.balance,
                'Role':self.role,
                'Address':self.address,
                'RentedCarID': self.rented_car_id
                }
    def save_to_JSON(self,fileName):
            try:
                with open('data/'+fileName,'r') as f:
                    data = json.load(f)
            except (FileNotFoundError,json.JSONDecodeError):
                data = []
            data.append(self.to_dict())
            with open('data/'+fileName,'w') as f:
                json.dump(data, f, indent=4)
                
##################3 Umers part ################
    def has_rented_a_car(self):
        if self.rented_car_id is not None:
            return True
        else:
            return False
    def rent_a_car(self, car_id):
        self.rented_car_id = car_id

    def return_car(self):
        self.rented_car_id = None
