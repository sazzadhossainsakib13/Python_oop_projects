# 🏛️ Python Object-Oriented Programming (OOP) Systems

A collection of interactive console-based applications modeling real-world business domains using Object-Oriented Programming (OOP) principles in Python.

[![Python: 3.x](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Overview

This repository contains domain-driven object-oriented systems implementing core software design paradigms including abstraction, inheritance, composition, and role-based access control.

---

## Included Applications

### 1. 🚌 Bus Reservation & Fleet Management System (`Bus_sysytem.py`)
A transportation management system handling fleet administration and passenger seat reservations.
- **Bus & Route Modeling**: Dynamic bus registration with unique identifiers, route assignments, and capacity tracking.
- **Seat Allocation & Booking Engine**: Automated availability checks and real-time seat reservation.
- **Passenger Registry**: Links booked seats with passenger profiles and contact details.
- **Administrative Control**: Role-gated management for bus registration and fleet inspection.

### 2. 🍽️ Restaurant Management & Billing System (`Resturent_Management.py`)
A food service system modeling customer ordering workflows and restaurant administration.
- **Abstract Base User Contract**: Standardizes profile data using Python's `abc.ABC` for `Customer`, `Employee`, and `Admin`.
- **Menu & Food Item Modeling**: Item creation with dynamic pricing, stock bounds, and deletion capabilities.
- **Order & Cart Aggregation**: Composition-driven cart managing item counts with dynamic total calculation via `@property`.
- **Role-Based Workflows**: Separate execution loops for customer ordering and back-office staff management.

---

## Key OOP Concepts Demonstrated

- **Abstraction**: Encapsulating domain logic into self-contained methods and abstract base classes.
- **Inheritance & Polymorphism**: Reusing shared attributes across specialized user types.
- **Composition**: Building complex models (`BusSystem` composing `Bus` and `Passenger`; `Restaurent` composing `Menu` and `Employee`).
- **Encapsulation & Validation**: Enforcing input constraints, available seat thresholds, and inventory boundaries.

---

## Project Structure

```text
Python_oop_projects/
├── Bus_sysytem.py           # Bus ticketing and fleet management application
├── Resturent_Management.py  # Restaurant catalog, cart, and administration application
└── README.md                # Documentation
```

---

## Installation & Running Locally

### Prerequisites
- Python 3.8 or higher

### Clone the Repository
```bash
git clone https://github.com/sazzadhossainsakib13/Python_oop_projects.git
cd Python_oop_projects
```

### Run the Applications
```bash
# Run Bus Reservation System
python Bus_sysytem.py

# Run Restaurant Management System
python Resturent_Management.py
```

---

## Author

**Sazzad Hossain Sakib**  
- GitHub: [@sazzadhossainsakib13](https://github.com/sazzadhossainsakib13)
