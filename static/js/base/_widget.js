// ==================================================
// ELEMENT REFERENCE
// ==================================================

const widgets = document.querySelectorAll('.widget');
const widgetCloseBtn = document.querySelectorAll('.closeWidget');

const widgetTriggers = {
    profileBtn: profileWidget,
    settingsBtn: settingsWidget,
};

// ==================================================
// FUNCTIONS
// ==================================================

// * FUNCTION TO TOGGLE WIDGET VISIBILITY
function toggleWidget(widget) {
    widget.classList.toggle('active');
}

// * FUNCTION TO ADD EVENT LISTENERS TO WIDGET TRIGGERS
function addWidgetEventListeners() {
    for (const trigger in widgetTriggers) {
        const triggerElement = document.getElementById(trigger);
        const widget = widgetTriggers[trigger];

        triggerElement.addEventListener('click', () => {
            toggleWidget(widget);
        });
    }
}

// * FUNCTION TO ADD EVENT LISTENERS TO WIDGET CLOSE BUTTONS
function addWidgetCloseEventListeners() {
    widgetCloseBtn.forEach((btn) => {
        btn.addEventListener('click', () => {
            const widget = btn.closest('.widget');
            toggleWidget(widget);
        });
    });
}

// * FUNCTION TO ADD EVENT LISTENERS TO CLOSE WIDGETS WHEN CLICKING OUTSIDE
function addOutsideClickEventListeners() {
    widgets.forEach((widget) => {
        widget.addEventListener('click', (event) => {
            if (event.target === widget) {
                toggleWidget(widget);
            }
        });
    });
}

// * FUNCTION TO ADD EVENT LISTENER TO CLOSE WIDGETS WHEN PRESSING ESCAPE KEY
function addEscapeKeyEventListener() {
    document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape') {
            widgets.forEach((widget) => {
                if (widget.classList.contains('active')) {
                    toggleWidget(widget);
                }
            });
        }
    });
}

// ==================================================
// EVENT LISTENERS
// ==================================================

// & INITIALIZE WIDGET EVENT LISTENERS
document.addEventListener('DOMContentLoaded', () => {
    addWidgetEventListeners();
    addWidgetCloseEventListeners();
    addOutsideClickEventListeners();
    addEscapeKeyEventListener();
});