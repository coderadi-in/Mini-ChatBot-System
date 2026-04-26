// ==================================================
// ELEMENT REFERENCE
// ==================================================

const modes = document.querySelectorAll('.mode');
const signupForm = document.getElementById('signupForm');
const loginForm = document.getElementById('loginForm');

// ==================================================
// FUNCTIONS
// ==================================================

// * FUNCTION TO SWITCH BETWEEN LOGIN AND SIGNUP MODE
function switchMode(mode) {
    const selectedMode = document.getElementById(mode);
    selectedMode.classList.add('selected');

    if (mode === 'signup') {
        loginForm.style.display = 'none';
        signupForm.style.display = 'flex';
    } else {
        signupForm.style.display = 'none';
        loginForm.style.display = 'flex';
    }
}

// ==================================================
// EVENT LISTENERS
// ==================================================

// & EVENT LISTENER TO PRE-SELECT SIGNUP MODE
document.addEventListener('DOMContentLoaded', () => {
    switchMode('signup');
});

// & EVENT LISTENER FOR MODE SWITCHING
modes.forEach(mode => {
    mode.addEventListener('click', () => {
        modes.forEach(m => m.classList.remove('selected'));
        switchMode(mode.id);
    });
});