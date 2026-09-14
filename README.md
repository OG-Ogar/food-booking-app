                    CUSTOMER
                       │
                       ▼
                    app.py
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
      food_service.py     booking_service.py
             │                   │
             ▼                   ▼
        models/food.py      models/booking.py
             │                   │
             └─────────┬─────────┘
                       ▼
                    data/
                       │
                       ▼
                  Food records




                                      CUSTOMER
                       │
                       ▼
                    app.py
                       │
                       ▼
                  AI Assistant
                       │
                       ▼
                Application Services
                       │
              ┌────────┴────────┐
              ▼                 ▼
        Food Service      Booking Service
              │                 │
              ▼                 ▼
           Food Model       Booking Model
              │                 │
              └────────┬────────┘
                       ▼
                    Database


                    food-booking-app/
│
├── app.py
│
├── models/
│   ├── food.py
│   ├── customer.py
│   └── booking.py
│
├── services/
│   ├── food_service.py
│   ├── customer_service.py
│   ├── auth_service.py
│   └── booking_service.py
│
├── data/
│   ├── foods.py
│   ├── customers.py
│   └── bookings.py
│
├── utils/
│   └── validation.py
│
├── ai/
│   └── assistant.py
│
└── tests/
    ├── test_food.py
    ├── test_customer.py
    ├── test_auth.py
    └── test_booking.py