import React, { useState } from 'react';
import axios from 'axios';
import './FileUpload.css';

const BACKEND_URL = 'http://localhost:8080';

function FileUpload({ uploadStatus, setUploadStatus }) {
  const [selectedFile, setSelectedFile] = useState(null);
  const [isUploading, setIsUploading] = useState(false);
  const [uploadedFiles, setUploadedFiles] = useState([]);

  const handleFileSelect = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
    setUploadStatus('');
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      setUploadStatus('Please select a file first');
      return;
    }

    setIsUploading(true);
    setUploadStatus('');

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      const response = await axios.post(`${BACKEND_URL}/upload`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      setUploadStatus(`✅ ${selectedFile.name} uploaded successfully!`);
      setUploadedFiles([...uploadedFiles, { 
        name: selectedFile.name, 
        id: response.data.vector_id,
        timestamp: new Date().toLocaleTimeString()
      }]);
      setSelectedFile(null);
      
      // Clear file input
      document.getElementById('fileInput').value = '';
    } catch (error) {
      setUploadStatus(`❌ Upload failed: ${error.response?.data?.detail || error.message}`);
    } finally {
      setIsUploading(false);
    }
  };

  const handleDrop = (event) => {
    event.preventDefault();
    const file = event.dataTransfer.files[0];
    setSelectedFile(file);
    setUploadStatus('');
  };

  const handleDragOver = (event) => {
    event.preventDefault();
  };

  return (
    <div className="file-upload">
      <h2>📁 Upload Documents</h2>
      <p className="upload-description">
        Upload text files to add to your knowledge base
      </p>

      <div 
        className="drop-zone"
        onDrop={handleDrop}
        onDragOver={handleDragOver}
      >
        <div className="drop-zone-icon">📄</div>
        <p>Drag & drop your file here</p>
        <p className="or-text">or</p>
        <label htmlFor="fileInput" className="file-input-label">
          Choose File
        </label>
        <input
          id="fileInput"
          type="file"
          onChange={handleFileSelect}
          accept=".txt,.md,.csv,.json"
          className="file-input"
        />
      </div>

      {selectedFile && (
        <div className="selected-file">
          <span>📎 {selectedFile.name}</span>
          <span className="file-size">
            ({(selectedFile.size / 1024).toFixed(2)} KB)
          </span>
        </div>
      )}

      <button 
        onClick={handleUpload}
        disabled={!selectedFile || isUploading}
        className="upload-button"
      >
        {isUploading ? '⏳ Uploading...' : '🚀 Upload to Knowledge Base'}
      </button>

      {uploadStatus && (
        <div className={`upload-status ${uploadStatus.includes('❌') ? 'error' : 'success'}`}>
          {uploadStatus}
        </div>
      )}

      {uploadedFiles.length > 0 && (
        <div className="uploaded-files">
          <h3>📚 Uploaded Files</h3>
          <ul>
            {uploadedFiles.map((file, index) => (
              <li key={index}>
                <span className="file-name">{file.name}</span>
                <span className="file-time">{file.timestamp}</span>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default FileUpload;
