import React, { useState } from 'react';
import axios from 'axios';
import MessageList from './MessageList';
import MessageInput from './MessageInput';

const ChatThread = () => {
    const [messages, setMessages] = useState([]);
    const [loading, setLoading] = useState(false);

    const handleSendMessage = async (message) => {
        setLoading(true); // Set loading to true while the message is being sent

        try {
            if (messages.length === 0) {
                // First message: Create a new chat thread
                const response = await axios.post(
                    'http://127.0.0.1:8000/api/chat-thread/'
                );

                setMessages([
                    {
                        id: response.data.id,
                        prompt: message,
                        response: '',
                        is_from_user: true,
                    },
                ]);
            } else {
                // Add a message to the existing thread
                const threadId = messages[0].id; // Get the thread ID from the first message
                const response = await axios.post(
                    'http://127.0.0.1:8000/api/messages/',
                    {
                        thread_id: threadId,
                        prompt: message,
                    }
                );

                setMessages((prevMessages) => [
                    ...prevMessages,
                    {
                        id: response.data.id,
                        prompt: message,
                        response: '',
                        is_from_user: true,
                    },
                ]);
            }
        } catch (error) {
            alert('Error sending message');
            console.error('Error sending message:', error.response?.data || error);
        } finally {
            setLoading(false); // Set loading back to false after the request completes
        }
    };

    return (
        <div>
            <MessageList messages={messages} loading={loading} />
            <MessageInput onSendMessage={handleSendMessage} disabled={loading} />
        </div>
    );
};

export default ChatThread;
