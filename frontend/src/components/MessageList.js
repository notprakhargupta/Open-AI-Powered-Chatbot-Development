import React from 'react';

const MessageList = ({ messages, loading }) => {
    return (
        <div>
            {/* Show loading state */}
            {loading && <p>Loading...please wait</p>}
            
            {/* Show "No messages" if the message list is empty */}
            {messages.length === 0 ? (
                <p>No messages yet. Try sending a prompt</p>
            ) : (
                // Map through the messages and display each one
                messages.map((message, index) => (
                    <div key={index}>
                            {message.is_from_user ? 'You' : 'Chatbot Assistant'}:

                    </div>
                ))
            )}
        </div>
    );
};

export default MessageList;
