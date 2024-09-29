# Palace of Goods - Frontend

## Overview

The Palace of Goods is a Web3 marketplace application that enables users to interact with the Pi Network. This frontend is built using React and allows users to authenticate, view products, make transactions, and manage their accounts in a decentralized environment.

## Features

- **User Authentication**: Users can sign up and log in using their Pi Network accounts.
- **Product Management**: Users can view a list of products available for sale.
- **Transaction Handling**: Users can view their transaction history and perform transactions using Pi tokens.
- **Dashboard**: A dedicated dashboard for user-related activities.
- **Responsive Design**: The application is designed to be mobile-friendly.

## Technologies Used

- **React**: Frontend framework for building user interfaces.
- **React Router**: For managing routing within the application.
- **Axios**: For making HTTP requests to the backend API.
- **CSS**: For styling the application.

## Getting Started

### Prerequisites

- Node.js (v14 or higher)
- npm (v6 or higher)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/erikg713/Palace-of-goods.git
   ```

2. Navigate to the frontend directory:

   ```bash
   cd Palace-of-goods/frontend
   ```

3. Install the dependencies:

   ```bash
   npm install
   ```

### Running the Application

To start the application in development mode, run:

```bash
npm start
```

This will start the React application, and you can access it at `http://localhost:3000`.

### Building for Production

To build the application for production, use:

```bash
npm run build
```

This creates a `build` directory with a production build of your app.

### API Integration

The frontend communicates with the backend API hosted at the specified endpoint. Ensure the backend is running before using the frontend.

### Directory Structure

```
frontend/
│
├── public/                 # Static files
├── src/
│   ├── components/         # React components
│   ├── context/            # React Context API for global state management
│   ├── services/           # Services for API calls
│   ├── utils/              # Utility functions
│   └── App.js              # Main application component
│
├── package.json            # Project dependencies and scripts
└── README.md               # Project documentation
```

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For inquiries or feedback, please contact the project maintainer:

- Name: Erik G.
- Email: [erikgordon985@gmail.com]
```