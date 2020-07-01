import React, { Component } from 'react';
import fetch from 'isomorphic-fetch'
import logo from './logo.svg';
import './App.css';

class App extends Component {
  
    componentWillMount() {
    this.getJSON();
  }
  
  getJSON() {
    fetch('http://localhost:8080/sample.json')
    .then(response => {
      if(response.ok) return response.json();
      throw new Error('Request failed.');
    })
    .then(data => console.log(data))
    .catch(error => {
      console.log(error);
    });
  }
  
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div>
    );
  }
}

export default App;