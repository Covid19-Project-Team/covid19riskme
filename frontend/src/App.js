import React from 'react';
import logo from './logo.svg';gi
import './App.css';

function tick() {
  const element = (
    <div>
      <h1>Hello, world!</h1>
      <h2>It is {new Date().toLocaleTimeString()}.</h2>
    </div>
  );
  // highlight-next-line
  ReactDOM.render(element, document.getElementById('root'));
}



function App() {
  
setInterval(tick, 1000);

}

export default App;
