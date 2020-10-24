from enum import Enum
from typing import List


class User(Enum):
    administrator = 1
    client = 2


class Personnel:
    def __init__(self, personnel_type, name, availability_dates):
        self.personnel_type = personnel_type
        self.name = name
        self.availability_dates = availability_dates


class AvailabilityPeriod:
    def __init__(self, from_date, to_date):
        self.from_date = from_date
        self.to_date = to_date


class Appointment:
    def __init__(self, appointment_type, required_personnel, required_resources):
        self.appointment_type = appointment_type
        self.required_personnel = required_personnel
        self.required_resources = required_resources


class BookingSystem:
    current_user: User = None
    personnel: List[Personnel] = []
    appointment_types = []
    bookings = []

    def add_new_appointment(self, appointment):
        self.appointment_types.append(appointment)

    def add_new_personnel(self,
                          personnel: Personnel) -> None:
        if self.current_user == User.administrator:
            self.personnel.append(personnel)
        else:
            raise PermissionError(f"User with role {self.current_user} can not create new personnel.")

    def set_current_user(self,
                         user: User) -> None:
        self.current_user = user
