// Flipping the card
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".flip-card").forEach(function (card) {
        const viewBtn = card.querySelector(".view-btn");
        const backBtn = card.querySelector(".back-btn");

        viewBtn.addEventListener("click", function () {
            card.classList.add("flipped");
        });

        backBtn.addEventListener("click", function () {
            card.classList.remove("flipped");
        });
    });
});





// hamburger js
document.addEventListener("DOMContentLoaded", function() {
    const toggler = document.querySelector(".custom-toggler");

    toggler.addEventListener("click", function() {
        this.classList.toggle("open"); // Toggle 'X' animation
    });
});


// side navbar
function toggleSidebar() {
    let sidebar = document.getElementById("mySidebar");
    let toggleBtn = document.getElementById("sidebarToggle");

    sidebar.classList.toggle("active");
    toggleBtn.classList.toggle("hidden"); // Hide button when sidebar is active
}


// for feedbacks
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".toggle-reply").forEach(button => {
    button.addEventListener("click", function () {
        let replyBox = this.nextElementSibling;
        replyBox.classList.toggle("d-none");
    });
    });

    document.getElementById("add-feedback").addEventListener("click", function () {
    document.getElementById("feedback-form").classList.toggle("d-none");
    });
});




// modal for zooming in 
function openImageModal(imageSrc) {
    // Get the modal elements
    let modal = document.getElementById("imageModal");
    let modalImg = document.getElementById("modalImage");

    // Check if modal elements exist
    if (modal && modalImg) {
        modalImg.src = imageSrc; // Set the image source
        modal.style.display = "block"; // Show the modal
    } else {
        console.error("Modal elements not found. Make sure the modal is included in the HTML.");
    }
}

// Close modal function
function closeModal() {
    document.getElementById("imageModal").style.display = "none";
}

// messages here
$(document).ready(function () {
    $("#messages-container").hide().slideDown(500).delay(3000).slideUp(500);
});