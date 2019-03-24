import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import Button from '@material-ui/core/Button';
import ReactPlayer from 'react-player'

class App extends Component {


  constructor(props) {
	  super(props);
	  this.state = {value: ''};
	  this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.action = this.action.bind(this);
  }

  handleChange(event) {
	      this.setState({value: event.target.value});
  }

  handleSubmit(event) {
	event.preventDefault();
	axios.get('http://192.168.0.103:8080/say/' + this.state.value)
	  .then(res => console.log(res));	
  }

  action(actionName) {
	  axios.get('http://192.168.0.103:8080/action/' + actionName + '%7C')
	  .then(res => console.log(res));	
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
	    
	    <img src='http://192.168.0.103:8081/?action=stream' width='300' height='200' />
            בוב
          </p>
	  <form onSubmit={this.handleSubmit}>
       <input type="text" value={this.state.value} onChange={this.handleChange} />
       <label>
            תגיד 
	     </label>
       <Button variant="contained" color="primary">
	        <input type="submit" value="שלח" />
       </Button>
	  </form>
      <Button onClick={() => this.action('RaiseRightHand')} variant="contained" color="secondary">
	        הרם יד ימין
      </Button>
      <Button onClick={() => this.action('RaiseLeftHand')} variant="contained" color="primary">
	        הרם יד שמאל
      </Button>
      <Button onClick={() => this.action('SayYes')} variant="contained" color="secondary">
	       כן
      </Button>
      <Button onClick={() => this.action('SayNo')} variant="contained" color="primary">
	       לא
      </Button>
      <Button onClick={() => this.action('TurnLightOn')} variant="contained" color="secondary">
	       פתח אור
      </Button>
      <Button onClick={() => this.action('TurnLightOff')} variant="contained" color="primary">
	       סגור אור
      </Button>
      <Button onClick={() => this.action('MoveFw')} variant="contained" color="secondary">
	       קדימה
      </Button>
      <Button onClick={() => this.action('MoveBw')} variant="contained" color="primary">
	       אחורה
      </Button>
      <Button onClick={() => this.action('TurnRight')} variant="contained" color="secondary">
	       ימינה
      </Button>
      <Button onClick={() => this.action('TurnLeft')} variant="contained" color="primary">
	    שמאל
      </Button>
      <Button onClick={() => this.action('Stop')} variant="contained" color="primary">
	    עצור
      </Button>
        </header>
        
      </div>
    );
  }
}

export default App;
