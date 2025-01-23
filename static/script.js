// Get the modal and close button elements
var modal = document.getElementById("modal");
var closeModal = document.getElementsByClassName("close")[0];

// Show the modal initially
modal.style.display = "block";

// Hide the modal when the close button is clicked
closeModal.onclick = function() {
    modal.style.display = "none";
}

// Hide the modal when clicking outside of it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// Execute when the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {
    const infoSection = document.getElementById("info-section");
    const tips = document.querySelectorAll(".additional-info");
    
    // Display the additional info section with a delay
    setTimeout(() => {
        if (infoSection) {
            infoSection.classList.add("visible");
            let delay = 500;
            
            // Show each tip with a delay to create a typing effect
            tips.forEach((tip, index) => {
                setTimeout(() => {
                    tip.style.opacity = 1;
                    tip.classList.add("typing");
                }, delay * (index + 1));
            });
        }
    }, 1000);
});
