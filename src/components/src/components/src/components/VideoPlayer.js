import React from 'react';

const VideoPlayer = ({ video }) => {
    if (!video) return <div>Loading...</div>;

    return (
        <div>
            <h2>{video.title}</h2>
            <video src={video.url} controls></video>
        </div>
    );
};

export default VideoPlayer;