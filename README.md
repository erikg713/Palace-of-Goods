# Palace of Goods

**Palace of Goods** is a Web3-based marketplace application where users can buy, sell, and trade goods. Built with React for the frontend and Flask for the backend, this application leverages Pi Network for secure transactions and decentralized data storage.

## Project Structure

Palace-of-Goods/
│
├── frontend/                # React frontend
│   ├── public/
│   ├── src/
│   │   ├── components/      # UI components
│   │   ├── pages/           # Views for pages like Home, Product, Profile
│   │   ├── services/        # API calls to Flask backend
│   │   ├── App.js           # Main App Component
│   │   └── index.js         # Entry point
│   └── package.json
│
├── backend/                 # Flask backend
│   ├── app/
│   │   ├── __init__.py      # App factory and Blueprint registration
│   │   ├── auth/            # Auth Blueprint for login/register
│   │   ├── products/        # Products Blueprint for CRUD operations
│   │   ├── config.py        # Configuration file (e.g., DB setup)
│   │   ├── models.py        # Database models (SQLAlchemy)
│   │   └── utils.py         # Helper functions (e.g., JWT, Pi Network)
│   ├── migrations/          # Database migrations
│   ├── Dockerfile
│   ├── requirements.txt     # Backend dependencies
│   └── wsgi.py              # WSGI entry point for deployment
├── docker-compose.yml       # For containerizing frontend/backend
└── README.md


- **Frontend**: React-based application providing the user interface for the marketplace.
- **Backend**: Flask-based API handling user authentication, product management, and transactions.
- **Docker**: Containerization for both frontend and backend.

## Features

- User authentication and profile management
- Product listing, creation, and retrieval
- Secure transactions with Pi Network integration
- Mobile-responsive design

## Prerequisites

- Node.js (version 16 or later)
- npm (or yarn, if preferred)
- Python 3.9 or later
- PostgreSQL
- Docker (for containerization)

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/erikg713/palace-of-goods.git
cd palace-of-goods
