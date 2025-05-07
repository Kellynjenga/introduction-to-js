// Change text content dynamically
document.getElementById("change-text-btn").addEventListener("click", () => {
    const description = document.getElementById("description");
    description.textContent = "The text has been dynamically updated!";
});

// Add a new element
document.getElementById("add-element-btn").addEventListener("click", () => {
    const container = document.getElementById("dynamic-container");
    const newElement = document.createElement("p");
    newElement.textContent = "This is a dynamically added paragraph.";
    newElement.style.color = "blue"; // Modify CSS styles dynamically
    container.appendChild(newElement);
});

// Remove the last added element
document.getElementById("remove-element-btn").addEventListener("click", () => {
    const container = document.getElementById("dynamic-container");
    if (container.lastChild) {
        container.removeChild(container.lastChild);
    }
});
