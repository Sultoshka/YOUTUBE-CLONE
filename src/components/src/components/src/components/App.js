import React, { useState, useEffect } from 'react';
import Navbar from './components/Navbar';
import VideoList from './components/VideoList';
import VideoPlayer from './components/VideoPlayer';
import axios from 'axios';

const App = () => {
    const [selectedVideo, setSelectedVideo] = useState(null);
    const [videos, setVideos] = useState([]);

    useEffect(() => {
        const fetchVideos = async () => {
            const response = await axios.get('http://localhost:5000/videos');
            setVideos(response.data);
        };

        fetchVideos();
    }, []);

    return (
        <div>
            <Navbar />
            <div className="container">
                <VideoList videos={videos} onVideoSelect={setSelectedVideo} />
                <VideoPlayer video={selectedVideo} />
            </div>
        </div>
    );
};

export default App;