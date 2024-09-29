# Palace of Goods

**Palace of Goods** is a Web3-based marketplace application where users can buy, sell, and trade goods. Built with React for the frontend and Flask for the backend, this application leverages the Pi Network for secure transactions and decentralized data storage.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [File Structure](#file-structure)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication and profile management
- Product listing, creation, and retrieval
- Secure transactions with Pi Network integration
- Mobile-responsive design
- Modular and maintainable codebase using Flask Blueprints
- Error handling and input validation for security

## Technologies

- **Frontend**: React.js
- **Backend**: Flask (with Blueprints for modularity)
- **Database**: PostgreSQL
- **Authentication**: JWT (JSON Web Tokens)
- **Containerization**: Docker
- **Security**: Input validation, rate limiting, HTTPS headers, encryption, etc.

## Installation

### Prerequisites

Ensure you have the following installed on your machine:

- Python 3.x
- Node.js (version 14.x or later)
- npm (Node Package Manager)
- PostgreSQL (latest version)
- Docker (optional, for containerization)

### Clone the Repository

Open your terminal and run the following commands:

```bash
git clone https://github.com/erikg713/Palace-of-goods.git
cd Palace-of-goods
```

### Backend Setup

1. **Navigate to the backend directory:**

    ```bash
    cd backend
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    pip install virtualenv
    virtualenv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your PostgreSQL database:**

   - Create a new PostgreSQL database named `palace_of_goods`.
   - Update your database configuration in `app/config.py` as follows:

    ```python
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/palace_of_goods'
    ```

   Replace `username` and `password` with your PostgreSQL credentials.

5. **Run database migrations:**

    ```bash
    flask db upgrade
    ```

### Frontend Setup

1. **Navigate to the frontend directory:**

    ```bash
    cd frontend
    ```

2. **Install dependencies:**

    ```bash
    npm install
    ```

3. **Start the React application:**

    ```bash
    npm start
    ```

### Docker Setup (Optional)

If you want to run the application using Docker, ensure you have Docker installed. You can start the services using the following command in the root directory of the project:

```bash
docker-compose up
```

## Usage

- **To run the backend server:**

    ```bash
    flask run
    ```

- **The application can be accessed at:**
  - Frontend: `http://localhost:3000`
  - Backend: `http://localhost:5000`

## Configuration

### Environment Variables

Create a `.env` file in the backend directory to manage sensitive information. Here’s an example configuration:

```plaintext
FLASK_ENV=development
FLASK_APP=manage.py
DATABASE_URL=postgresql://username:password@localhost/palace_of_goods
JWT_SECRET_KEY=your_jwt_secret_key
```

## File Structure

```plaintext
Palace-of-goods/
├── backend/
│   ├── app/
│   │   ├── __init__.py         # Initializes the Flask app
│   │   ├── config.py           # Configuration settings
│   │   ├── models.py           # Database models
│   │   ├── routes/             # Blueprint routes
│   │   │   ├── __init__.py     # Initializes the routes package
│   │   │   ├── auth.py         # Authentication routes
│   │   │   ├── products.py      # Product-related routes
│   │   │   └── transactions.py   # Transaction-related routes
│   │   ├── services/           # Business logic and services
│   │   └── migrations/         # Database migrations
│   ├── requirements.txt         # Python dependencies
│   └── manage.py                # Entry point for running the app
├── frontend/
│   ├── public/                 # Static files (index.html, favicon, etc.)
│   ├── src/                    # React app source files
│   │   ├── components/         # Reusable React components
│   │   ├── pages/              # Page components
│   │   ├── utils/              # Utility functions
│   │   ├── App.js              # Main app component
│   │   └── index.js            # Entry point for React app
├── docker-compose.yml           # Docker configuration
└── README.md                   # Project documentation
```

## API Endpoints

### Authentication

- `POST /api/auth/login` - Log in a user
- `POST /api/auth/register` - Register a new user

### Products

- `GET /api/products` - Get all products
- `POST /api/products` - Create a new product

### Transactions

- `GET /api/transactions` - Get transaction history
- `POST /api/transactions` - Create a new transaction

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/YourFeature`.
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to modify any sections or code snippets according to your specific project requirements. Let me know if there's anything else you would like to add or change!