import React, { useState } from 'react';

const MessageInput = ({ onSendMessage, disabled }) => {
    const [message, setMessage] = useState('');

    const handleInputChange = (event) => {
        setMessage(event.target.value);
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        if (message.trim() !== '') {
            onSendMessage(message);
            setMessage(''); // Clear the input after sending the message
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                value={message}
                onChange={handleInputChange}
                placeholder="Type a message..."
                disabled={disabled}
            />
            <button type="submit" disabled={disabled}>
                Send
            </button>
        </form>
    );
};

export default MessageInput;
