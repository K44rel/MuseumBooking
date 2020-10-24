import unittest
from booking_system import \
    BookingSystem, Personnel, AvailabilityPeriod, \
    User, Appointment, AppointmentType, Booking, PersonnelType
from datetime import datetime


class TestBookingSystem(unittest.TestCase):
    """
    Scenario: Administrator creates new personnel in the system

        Administrators should be able to create new personnel.
        Personnel shall be attached to appointment types.

        Given the administrator is signed in to the management view
        And the administrator navigates to the personnel creation view
        When the administrator enters "teacher" for the type of the personnel
        And the administrator enters "Joe" for the name of the personnel
        And the administrator enters availability dates for the personnel
        Then a new personnel is created in the system
    """

    def test_admin_creates_new_personnel(self):
        system = BookingSystem()

        # Current user has to be administrator
        system.set_current_user(User.administrator)

        personnel = joe()

        system.add_new_personnel(personnel)

        # Check if new personnel was added
        self.assertIn(personnel, system.personnel)

    """
    Scenario: Administrator creates a new appointment type in the system

        Administrators should be able to create new types of appointments.
        The appointments have rooms personnel and other resources attached.

        Given the administrator is signed in to the management view
        And the administrator navigates to the appointment creation view
        When the administrator enters "tour" for the type of the appointment
        And the administrator enters "guide" for the personnel required for the appointment
        And the administrator adds "microphone" for the resource required for the appointment
        Then a new appointment type is created in the system
    """
    def test_admin_creates_new_appointment(self):
        system = BookingSystem()

        # Current user has to be administrator
        system.set_current_user(User.administrator)

        personnel = joe()
        system.add_new_personnel(personnel)

        appointment = Appointment(
            AppointmentType.tour,   # Type of the appointment
            [personnel],            # Personnel required for the appointment
            ["microphone"]          # Resources required for the appointment
        )

        system.add_new_appointment(appointment)

        # Check if new appointment was added
        self.assertIn(appointment, system.appointments)

    """
    Scenario: Administrator approves booking

        Some bookings contain special requests by the clients.
        The administrator needs to approve these bookings manually.

        Given the administrator is signed in to the management view
        And there exists a pending booking with a special request attached
        When administrator approves the booking
        Then new appointment is created
        And the client is notified of the approval
    """
    def test_admin_approves_booking(self):
        system = BookingSystem()

        # Current user has to be administrator
        system.set_current_user(User.administrator)

        # Set up dummy booking to approve
        personnel = joe()
        system.add_new_personnel(personnel)

        appointment = Appointment(
            AppointmentType.tour, [personnel], ["microphone"]
        )
        system.add_new_appointment(appointment)

        system.bookings.append(
            Booking(
                appointment,
                "special request description",
                datetime(2020, 2, 2, 10)
            )
        )

        booking = system.get_pending_bookings()[0]
        booking.approve()

        self.assertTrue(booking.is_approved)


def joe():
    return Personnel(
                PersonnelType.teacher, "Joe",
                [AvailabilityPeriod(datetime(2020, 2, 2, 10), datetime(2020, 2, 2, 13)),
                 AvailabilityPeriod(datetime(2020, 2, 4, 14), datetime(2020, 2, 4, 18))]
            )


if __name__ == '__main__':
    unittest.main()
