import logo from './logo.svg';
import './App.css';
import '../node_modules/xterm/css/xterm.css'

import { useEffect } from 'react';

const useScript = url => {
  useEffect(() => {
    const script = document.createElement('script');

    script.src = url;
    script.async = true;

    document.body.appendChild(script);

    return () => {
      document.body.removeChild(script);
    }
  }, [url]);
};

function App(props) {

  return (
    <div className="App">
        <iframe id="terminal" src="/xterm.html"></iframe>
    </div>
  );
}

export default App;
