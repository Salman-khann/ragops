import React, { useState } from 'react';
import './App.css';
import FileUpload from './components/FileUpload';
import ChatInterface from './components/ChatInterface';

function App() {
  const [uploadStatus, setUploadStatus] = useState('');

  return (
    <div className="App">
      <header className="App-header">
        <h1>🤖 RAG Knowledge Base</h1>
        <p>Upload documents and ask questions</p>
      </header>
      
      <div className="container">
        <div className="sidebar">
          <FileUpload 
            uploadStatus={uploadStatus}
            setUploadStatus={setUploadStatus}
          />
        </div>
        
        <div className="main-content">
          <ChatInterface />
        </div>
      </div>
    </div>
  );
}

export default App;
