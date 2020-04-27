import React from 'react';
import './style/App.scss';
import Navbar from './components/Navbar';
import About from './components/About';
import Home from './components/Home';
import FooterNav from './components/FooteNav';
import Submit from './components/Submit';
import { BrowserRouter, Switch, Route } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <Navbar />
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/about" component={About} />
          <Route path="/submit" component={Submit} />
        </Switch>
        <FooterNav />
      </div>
    </BrowserRouter>
  );
}

export default App;
