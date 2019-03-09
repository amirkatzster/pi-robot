import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';

class App extends Component {


  constructor(props) {
	  super(props);
	  this.state = {value: ''};
	  this.handleChange = this.handleChange.bind(this);
          this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
	      this.setState({value: event.target.value});
  }

  handleSubmit(event) {
	alert('A name was submitted: ' + this.state.value);
	event.preventDefault();
	axios.get('http://192.168.0.103:8080/say/' + this.state.value)
	  .then(res => console.log(res));
	
  }


  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            בוב
          </p>
	  <form onSubmit={this.handleSubmit}>
	     <label>
	       תגיד:
	          <input type="text" value={this.state.value} onChange={this.handleChange} />
	     </label>
	     <input type="submit" value="שלח" />
	  </form>
        </header>
      </div>
    );
  }
}

export default App;
