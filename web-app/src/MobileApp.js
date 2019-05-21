import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import Button from '@material-ui/core/Button';
import { scaleRotate as Menu } from 'react-burger-menu'


class MobileApp extends Component {

    constructor(props) {
        super(props);
        this.state = {value: ''};
        this.handleChange = this.handleChange.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
      this.action = this.action.bind(this);
      this.domain = this.getDomain();
    }
  
    handleChange(event) {
            this.setState({value: event.target.value});
    }

    isDev() {
        if (window.location.hostname === 'localhost' || window.location.hostname == '192.168.0.104') {
          return true;
        }
        return false;
    }
    getDomain() {
        var domain = window.location.hostname;
        if (this.isDev()) {
          domain = "192.168.0.103";
        }
        return domain;
    }
  
    handleSubmit(event) {
    event.preventDefault();
      axios.get('http://'+ this.domain +':8080/say/' + this.state.value)
        .then(res => console.log(res));	
    }
  
    action(actionName) {
        axios.get('http://' + this.domain +':8080/action/' + actionName + '%7C')
        .then(res => console.log(res));	
    }
    
    liveCam() {
      if (this.isDev()) {
        return "resources/pic.jpg";
      }
        return 'http://' + this.domain + ':8081/?action=stream';
    }

    showSettings (event) {
        event.preventDefault();
      }

    render() {
        return (
            <div id="outer-container">
                <Menu width={ '30%' } pageWrapId={ "page-wrap" } outerContainerId={ "outer-container" } >
                    <a id="home" className="menu-item" href="/">Home</a>
                    <a id="about" className="menu-item" href="/about">About</a>
                    <a id="contact" className="menu-item" href="/contact">Contact</a>
                    <a onClick={ this.showSettings } className="menu-item--small" href="">Settings</a>
                </Menu>
                <main id="page-wrap">
                    <img src={this.liveCam()} alt="cam" width='100%' height='100%' />
                    <Button style={{position:'absolute',top:0,right:280}}  onClick={() => this.action('MoveFw')} variant="contained" color="primary">
                    ⇧
                    </Button>
                    <Button style={{position:'absolute',bottom:0,right:280}}  onClick={() => this.action('MoveBw')} variant="contained" color="primary">
                    ⇩
                    </Button>
                    <Button style={{position:'absolute',top:150,right:0}}  onClick={() => this.action('TurnRight')} variant="contained" color="primary">
                    ⇨
                    </Button>
                    <Button style={{position:'absolute',top:150,left:0}}  onClick={() => this.action('TurnLeft')} variant="contained" color="primary">
                    ⇦  
                    </Button>
                    <Button style={{position:'absolute',top:150,left:280}}  onClick={() => this.action('Stop')} variant="contained" color="primary">
                    ⏹  
                    </Button>
                </main>
            </div>
        );
    }

    
}

export default MobileApp;