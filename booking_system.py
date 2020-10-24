from datetime import datetime
from typing import List
from enum import Enum


class User(Enum):
    administrator = 1
    client = 2


class PersonnelType:
    teacher = 1
    guide = 2


class AppointmentType:
    tour = 1
    workshop = 2


class AvailabilityPeriod:
    def __init__(self,
                 from_date: datetime,
                 to_date: datetime):
        self.from_date = from_date
        self.to_date = to_date


class Personnel:
    def __init__(self,
                 personnel_type: PersonnelType,
                 name: str,
                 availability_dates: List[AvailabilityPeriod]):
        self.personnel_type = personnel_type
        self.name = name
        self.availability_dates = availability_dates


class Appointment:
    def __init__(self,
                 appointment_type: AppointmentType,
                 required_personnel: List[Personnel],
                 required_resources: List[str]):
        self.appointment_type = appointment_type
        self.required_personnel = required_personnel
        self.required_resources = required_resources


class Booking:
    def __init__(self,
                 appointment: Appointment,
                 special_request: str,
                 time: datetime):
        self.appointment = appointment
        self.special_request = special_request
        self.time = time
        self.is_approved = False if special_request is not None else True

    def approve(self) -> None:
        self.is_approved = True


class BookingSystem:
    current_user: User = None
    personnel: List[Personnel] = []
    appointments: List[Appointment] = []
    bookings: List[Booking] = []

    def add_new_appointment(self,
                            appointment: Appointment) -> None:
        if self.current_user == User.administrator:
            self.appointments.append(appointment)
        else:
            raise PermissionError(f"User with role {self.current_user} can not create new appointment types.")

    def add_new_personnel(self,
                          personnel: Personnel) -> None:
        if self.current_user == User.administrator:
            self.personnel.append(personnel)
        else:
            raise PermissionError(f"User with role {self.current_user} can not create new personnel.")

    def set_current_user(self,
                         user: User) -> None:
        self.current_user = user

    def get_pending_bookings(self) -> List[Booking]:
        return [booking for booking in self.bookings if booking.is_approved is False]