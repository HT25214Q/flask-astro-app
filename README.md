.kundli-input {
    width: 100%;
    padding: 14px 16px;
    background: rgba(31, 41, 55, 0.85); /* गहरा बैकग्राउंड */
    color: #f9fafb; /* हल्का text */
    font-size: 1rem;
    font-weight: 500;
    border: 2px solid transparent;
    border-radius: 12px;
    outline: none;
    transition: all 0.3s ease;
    box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.3);
}

/* Placeholder styling */
.kundli-input::placeholder {
    color: #9ca3af;
    font-style: italic;
}

/* Focus effect */
.kundli-input:focus {
    border-color: #f59e0b; /* Golden border */
    background: rgba(55, 65, 81, 0.95); /* थोड़ा और highlighted */
    box-shadow: 0 0 12px rgba(245, 158, 11, 0.7);
    transform: scale(1.02);
}

/* Hover effect */
.kundli-input:hover {
    border-color: #6366f1; /* Indigo border */
    box-shadow: 0 0 8px rgba(99, 102, 241, 0.5);
}

/* Date/Time picker icon styling */
.kundli-input[type="date"],
.kundli-input[type="time"] {
    cursor: pointer;
}
