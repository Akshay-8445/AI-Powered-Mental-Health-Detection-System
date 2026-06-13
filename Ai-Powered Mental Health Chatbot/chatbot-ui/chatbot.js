// FIX 1: API_URL used https:// for localhost → should be http://
// FIX 2: togglrChat() had a typo and used wrong variable name `Chat` (capital C)
// FIX 3: getElementById used 'chatcontainer' and 'chatbox'/'userinput'
//         but index.html uses 'chatWidget', 'chatBody', 'userInput'
//         Consolidated to match index.html IDs.

const API_URL = 'http://127.0.0.1:8000';
const session_id = "user_" + Math.floor(Math.random() * 10000);

function toggleChat() {
    const widget = document.getElementById('chatWidget');
    widget.style.display = widget.style.display === 'block' ? 'none' : 'block';
}

function appendMessage(role, text) {
    const chatBody = document.getElementById('chatBody');
    const message = document.createElement('div');
    message.innerHTML = `<strong>${role}:</strong> ${text}`;
    message.style.margin = "6px 0";
    chatBody.appendChild(message);
    chatBody.scrollTop = chatBody.scrollHeight;
}

async function sendMessage() {
    const input = document.getElementById('userInput');
    const text = input.value.trim();
    if (!text) return;

    appendMessage('You', text);
    input.value = '';

    try {
        const response = await fetch(`${API_URL}/chat`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ session_id, query: text })
        });
        const data = await response.json();
        appendMessage('MindEase', data.response);
    } catch (error) {
        appendMessage('MindEase', 'Sorry, something went wrong. Please try again later.');
    }
}
