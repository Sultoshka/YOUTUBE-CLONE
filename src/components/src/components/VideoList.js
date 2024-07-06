import React from 'react';

const VideoList = ({ videos, onVideoSelect }) => {
    return (
        <div>
            {videos.map((video) => (
                <div key={video.id} onClick={() => onVideoSelect(video)}>
                    <h3>{video.title}</h3>
                </div>
            ))}
        </div>
    );
};

export default VideoList;