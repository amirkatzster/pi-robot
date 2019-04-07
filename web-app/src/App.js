import React, { Component } from 'react';
import {
  BrowserView,
  MobileView,
  isBrowser,
  isMobile
} from "react-device-detect";

import MobileApp from './MobileApp';
import DesktopApp from './DesktopApp';

class App extends Component {


  constructor(props) {
	  super(props);
  }

  render() {
    return (
      
      <div className="App">
        <div>
          <BrowserView>
              <DesktopApp />
          </BrowserView>
          <MobileView>
              <MobileApp />
          </MobileView>
        </div>           
    </div>
    );
  }
}

export default App;
