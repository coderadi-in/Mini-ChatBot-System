// ==================================================
// ELEMENT REFERENCE
// ==================================================

var socket = io();

// ==================================================
// IMPORTS
// ==================================================

import { loaderView, appendMessage } from '../pages/index.js';

// ==================================================
// FUNCTIONS
// ==================================================

// * FUNCTION TO SEND A MESSAGE TO SERVER
export function sendMessage(event, message) {
    socket.emit(event, message);
}

// ==================================================
// EVENTS
// ==================================================

socket.on('recv', (message) => {
    loaderView.style.display = 'none';
    appendMessage(message, 'ai');
});