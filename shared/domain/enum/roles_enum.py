from enum import Enum


class Role(str, Enum):
    ADMIN = "ADMIN"
    DOCTOR = "DOCTOR"
    NURSE = "NURSE"
    LAB_TECHNICIAN = "LAB_TECHNICIAN"