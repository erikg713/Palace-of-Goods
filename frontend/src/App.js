import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './components/Navbar';
import HomePage from './pages/HomePage';
import ProductPage from './pages/ProductPage';
import SellProduct from './components/SellProduct';
import Login from './components/Login';
import Register from './components/Register';
import Profile from './components/Profile';

function App() {
  return (
    <Router>
      <Navbar />
      <Switch>
        <Route path="/" exact component={HomePage} />
        <Route path="/product/:id" component={ProductPage} />
        <Route path="/sell" component={SellProduct} />
        <Route path="/login" component={Login} />
        <Route path="/register" component={Register} />
        <Route path="/profile" component={Profile} />
      </Switch>
    </Router>
  );
}

export default App;

