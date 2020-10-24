class BookingSystem:
    current_user = None
    personnel = []
    appointment_types = []
    bookings = []

    def add_new_personnel(self, personnel):
        self.personnel.append(personnel)

    def set_current_user(self, user):
        self.current_user = user


class Personnel:
    def __init__(self, personnel_type, name, availability_dates):
        self.personnel_type = personnel_type
        self.name = name
        self.availability_dates = availability_dates


class AvailabilityPeriod:
    def __init__(self, from_date, to_date):
        self.from_date = from_date
        self.to_date = to_date
