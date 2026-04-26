// ==================================================
// ELEMENT REFERENCE
// ==================================================

const messageInput = document.getElementById('prompt');
const sendBtn = document.getElementById('sendMessageBtn');
const chatContainer = document.querySelector('.chats .section');
export const loaderView = document.querySelector('.loader-view');

// ==================================================
// IMPORTS
// ==================================================

import { sendMessage } from '../base/_chat.js';

// ==================================================
// FUNCTIONS
// ==================================================

// * FUNCTION TO CHECK IS THE MESSAGE BOX IS EMPTY OR NOT AND ENABLE OR DISABLE THE SEND BUTTON
function toggleSendButton() {
    if (messageInput.value.trim() === '') { sendBtn.disabled = true; }
    else { sendBtn.disabled = false; }
}

// * FUNCTION TO APPEND A MESSAGE TO THE CHAT CONTAINER
export function appendMessage(message, sender = 'user') {
    const messageElement = document.createElement('pre');
    messageElement.classList.add('para', 'message', 'pv-8', 'ph-12', 'rounded-4', sender);
    messageElement.textContent = message;
    chatContainer.appendChild(messageElement);
}

// ==================================================
// EVENT LISTENERS
// ==================================================

// & EVENT LISTENER FOR MESSAGE INPUT
messageInput.addEventListener('input', toggleSendButton);

// & EVENT LISTENER FOR SEND BUTTON
sendBtn.addEventListener('click', () => {
    // GET THE MESSAGE AND TRIM IT
    const message = messageInput.value.trim();
    if (message === '') return;

    // APPEND THE MESSAGE TO THE CHAT CONTAINER
    appendMessage(message, 'user');
    sendMessage('send', message);
    loaderView.style.display = 'block';

    // CLEAR THE MESSAGE INPUT AND DISABLE THE SEND BUTTON
    messageInput.value = '';
    toggleSendButton();
});

// & EVENT LISTENER FOR CTRL + ENTER KEY PRESS IN MESSAGE INPUT
messageInput.addEventListener('keydown', (event) => {
    if (event.ctrlKey && event.key === 'Enter') {
        sendBtn.click();
    }
});
