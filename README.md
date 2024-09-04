# Palace-of-goods
It's time to develop #Web3 applications on #PiNetwork and get ready for the upcoming Open Mainnet.

palace-of-goods-backend/
├── app.py                 # Main application entry point
├── config.py              # App configuration settings
├── Dockerfile             # Dockerfile for containerizing the backend
├── .env                   # Environment variables
├── requirements.txt       # Python dependencies
├── blueprints/            # Application routes/blueprints
│   ├── __init__.py        # Blueprint initialization
│   ├── auth.py            # Authentication routes (register/login)
│   ├── marketplace.py     # Product listing, buying, and selling routes
│   └── transaction.py     # Web3-based transaction handling
├── models/                # Database models
│   ├── __init__.py        # Initialize the database
│   ├── user.py            # User model
│   └── product.py         # Product model
├── migrations/            # Database migration files
└── utils/                 # Utility functions (e.g., security, encryption)
    └── security.py        # Functions for password hashing, validation
