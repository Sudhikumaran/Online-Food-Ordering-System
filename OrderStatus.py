from enum import Enum

class OrderStatus(Enum):
    CREATED = "CREATED"
    CONFIRMED = "CONFIRMED"
    PAID = "PAID"
    CANCELLED = "CANCELLED"
