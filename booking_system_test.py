import unittest
from booking_system import BookingSystem, Personnel, AvailabilityPeriod, User
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


def joe():
    return Personnel(
                "teacher", "Joe",
                [AvailabilityPeriod(datetime(2020, 2, 2, 10), datetime(2020, 2, 2, 13)),
                 AvailabilityPeriod(datetime(2020, 2, 4, 14), datetime(2020, 2, 4, 18))]
            )


if __name__ == '__main__':
    unittest.main()
