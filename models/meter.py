#!/usr/bin/python3
""" Module for energy meters"""
from models.base import Base


class Meter(Base):
    """Class for management of meters"""
    def __init__(self, account, cp_no, location="kenha", id=None):
        """Constructor"""
        self.account = account
        self.cp_no = cp_no
        self.location = location
        super().__init__(id)

        @property
        def account(self):
            return self.__account

        @property
        def cp_no(self):
            return self.__cp_no

        @property
        def location(self):
            return self.__location

        @account.setter
        def account(self, value):
            if not isinstance(value, int):
                raise TypeError('Account Number invalid')
            if len(str(value)) < 6:
                raise ValueError('Account Number too short')
            self.__account = value

        @cp_no.setter
        def cp_no(self, value):
            if not isinstance(value, int):
                raise TypeError('CP must be a number')
            if value < 0:
                raise ValueError('Can not be negative')
            self.__cp_no = value

        @location.setter
        def location(self, value):
            if not isinstance(value, str):
                raise TypeError('location must be string')
            self.__location = value

        def __str__(self):
            """Return the meter description"""
            return('[Meter no:] {} at CP No: {} with Account {} Location: {}'
                   .format(self.id, self.cp_no, self.account, self.location))
