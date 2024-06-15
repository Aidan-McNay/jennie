"""A representation of a specialty concert.

A specialty concert is special request, where a single Chimesmaster signs up to play

Author: Aidan McNay
Date: June 15th, 2024
"""

from dataclasses import dataclass
from datetime import datetime
from enum import IntEnum
from typing import Optional


class SpecialtyConcertType(IntEnum):
    """The type of a specialty concert."""

    QUARTER_HOUR = 1
    HALF_HOUR = 2
    HALF_HOUR_SPLIT = 3


@dataclass
class Contact:
    """The type of a contact for a concert."""

    name: str
    email: Optional[str]
    phone: Optional[str]


class SpecialtyConcert:
    """A Specialty Concert represents a one-off request, played by one Chimesmaster.

    Attributes:
     - `name`: Name of the concert (str)
     - `type`: Type of the concert (SpecialtyConcertType)
     - `start`: The start time of the concert (datetime)
     - `end`: The end time of the concert (datetime)
     - `contact`: The person to contact (Contact)
     - `cm`: The Chimesmaster signed up to play (if any), indicated by
           their Slack ID (Optional str)
     - `note`: Any other notes about the concert (Optional str)

    Other Attributes (not in __init__):
     - `id`: The unique internal ID of the concert
    """

    def __init__(
        self,
        name: str,
        type: SpecialtyConcertType,
        start: datetime,
        end: datetime,
        contact: Contact,
        cm: Optional[str],
        note: Optional[str],
    ):
        """Initializes a new SpecialtyConcert."""
        self.name = name
        self.type = type
        self.start = start
        self.end = end
        self.contact = contact
        self.cm = cm
        self.note = note
