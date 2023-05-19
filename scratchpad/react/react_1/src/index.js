import React from 'react';
// import ReactDOM from 'react-dom/client';
import ReactDOM from 'react-dom';
import HelloWorld from './hello-app';

// const root = ReactDOM.createRoot(document.getElementById('root'));
// root.render(
//   <React.StrictMode>
//     <App />
//   </React.StrictMode>
// );
ReactDOM.render(
    <HelloWorld />,
    document.getElementById('root')
);

