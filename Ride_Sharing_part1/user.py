from abc import ABC, abstractmethod
from datetime import datetime


class Ride_sharing:
    def __init__(self,company_name) -> None:
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []

    def add_rider(self,rider):
        self.riders.append(rider)

    def add_driver(self,driver):
        self.drivers.append(driver)

    def __repr__(self) -> str:
        return f"{self.company_name} with riders: {len(self.riders)} and driver: {len(self.drivers)}"

class User(ABC):
    def __init__(self,name,email,nid) -> None:
        self.name = name
        self.email = email

        # ToDo: set user id dynamically
        self.__id = 0
        self.__nid = nid
        self.wallet = 0
    
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    


class Rider(User):
    def __init__(self, name, email, nid, current_location,initial_amount) -> None:
        super().__init__(name, email, nid)
        self.current_ride = None
        self.wallet = initial_amount
        self.current_location = current_location

    def display_profile(self):
        print(f"Rider name: {self.name} and email: {self.email}")
    
    def load_cash(self,amount):
        if(amount > 0):
            self.wallet += amount
    
    def update_location(self,current_location):
        self.current_location = current_location
    
    def request_ride(self,ride_sharing,destination):
        if not self.current_ride:
            ride_request = Ride_request(self,destination)
            ride_matcher = Ride_matching(ride_sharing.drivers)
            self.current_ride = ride_matcher.find_driver(ride_request)

    def show_current_ride(self):
        print(self.current_ride)

class Driver(User):
    def __init__(self, name, email, nid,current_location) -> None:
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet =0
    
    def display_profile(self):
        print(f"Driver with name: {self.name}  and email: {self.email}")

    def accept_ride(self,ride):
        ride.set_driver(self)

class Ride:
    def __init__(self,start_location,end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None


    
    def set_driver(self,driver):
        self.driver = driver
    
    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self,rider,amount):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare

    def __repr__(self) -> str:
        return f"Ride Details: Started: {self.start_location} to {self.end_location}"

class Ride_request:
    def __init__(self, rider, end_location) -> None:
        self.rider = rider
        self.end_location = end_location

class Ride_matching:
    def __init__(self,drivers) :
        self.available_drivers = drivers
    
    def find_driver(self,ride_request):
        if(len(self.available_drivers) > 0):
            # todo: find the closest driver of the rider
            driver = self.available_drivers[0]
            ride = Ride(ride_request.rider.current_location, ride_request.end_location)
            driver.accept_ride(ride)
            return ride

class Vehicle(ABC):
    speed = {
        'car': 50,
        'bike': 60,
        'cng': 15

    }
    def __init__(self,vehicle_type,license,rate) -> None:
        # super().__init__()
        self.vehicle_type = vehicle_type
        self.license = license
        self.rate = rate
        self.status = 'available'

    @abstractmethod
    def start_drive(self):
        pass

class Car(Vehicle):
    def __init__(self, vehicle_type, license, rate) -> None:
        super().__init__(vehicle_type, license, rate)

    def start_drive(self):
        self.status = 'unavailable'

class Bike(Vehicle):
    def __init__(self, vehicle_type, license, rate) -> None:
        super().__init__(vehicle_type, license, rate)
    
    def start_drive(self):
        self.status = 'unavailable'



# driver code

thapao = Ride_sharing("Niye Jao")
bhatija = Rider("cholen mama",'cholenmama@yahoo.com', 1235, 'fakirapool', 230)
thapao.add_rider(bhatija)
mama = Driver("oi mama",'oimam@yahoo.com', 1231, 'kakrail')
thapao.add_driver(mama)
print(thapao)
bhatija.request_ride(thapao,"wari")
bhatija.show_current_ride()
