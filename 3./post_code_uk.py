
'''
Write a library that supports validating and formatting post codes for UK.\
The details of which post codes are valid and which are the parts they consist\
of can be found at https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting.\
The API that this library provides is your choice.
'''

import re

class PostCodeUk:
    _pattern = re.compile(r"^[A-Z]{1,2}[0-9][A-Z0-9]? ?[0-9][A-Z]{2}$")

    def __init__(self, code: str):
        self.code = self._normalize(code)
        if not self._validate(self.code):
            raise ValueError(f"Invalid UK postcode: {code}")

    @staticmethod
    def _normalize(code: str) -> str:
        return code.replace(" ", "").upper()

    @classmethod
    def _validate(cls, code: str) -> bool:
        return bool(cls._pattern.match(code))

    def formatted(self) -> str:
        outward_code, inward_code = self.code[:-3], self.code[-3:]
        return f"{outward_code} {inward_code}"

    def __str__(self) -> str:
        return self.formatted()
