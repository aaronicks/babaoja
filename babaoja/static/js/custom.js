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
document.addEventListener("DOMContentLoaded", function () {
    const toggler = document.querySelector(".custom-toggler");
    const icon = toggler.querySelector("i"); // Get the icon inside the button

    toggler.addEventListener("click", function () {
        if (icon.classList.contains("bi-list")) {
            icon.classList.remove("bi-list");
            icon.classList.add("bi-x"); // Change to "X" icon
        } else {
            icon.classList.remove("bi-x");
            icon.classList.add("bi-list"); // Change back to hamburger
        }
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

// Notification here
$(document).ready(function () {
    $("#messages-container").hide().slideDown(500).delay(3000).slideUp(500);
});



document.addEventListener("DOMContentLoaded", function() {
    // Toggle Reply Form
    document.querySelectorAll(".toggle-reply").forEach(button => {
        button.addEventListener("click", function() {
            this.nextElementSibling.classList.toggle("d-none");
        });
    });


    // Show Feedback Form
    document.getElementById("add-feedback").addEventListener("click", function() {
        document.getElementById("feedback-form").classList.toggle("d-none");
    });
});




// SHow More and Show Lesss
document.addEventListener("DOMContentLoaded", function () {
    // Toggle Reply Form
    document.querySelectorAll(".toggle-reply").forEach(button => {
        button.addEventListener("click", function () {
            const replyBox = this.nextElementSibling;
            replyBox.classList.toggle("d-none");
        });
    });

    // Show More / Show Less Replies
    document.querySelectorAll(".replies-container").forEach(container => {
        const showMoreBtn = container.nextElementSibling; // The "Show More" button
        const extraReplies = showMoreBtn ? showMoreBtn.nextElementSibling : null;

        if (showMoreBtn && extraReplies) {
            showMoreBtn.addEventListener("click", function () {
                if (extraReplies.classList.contains("d-none")) {
                    // Expand replies
                    extraReplies.classList.remove("d-none");
                    this.textContent = "Show Less";
                    
                    // Move "Show Less" button to the bottom
                    extraReplies.appendChild(this);
                } else {
                    // Collapse replies
                    extraReplies.classList.add("d-none");
                    this.textContent = "Show More";

                    // Move "Show More" button back to its original place
                    container.insertAdjacentElement("afterend", this);
                }
            });

            // Hide extra replies initially
            extraReplies.classList.add("d-none");
        }
    });

    // Add Feedback Form Toggle
    const addFeedbackBtn = document.getElementById("add-feedback");
    const feedbackForm = document.getElementById("feedback-form");

    if (addFeedbackBtn) {
        addFeedbackBtn.addEventListener("click", function () {
            feedbackForm.classList.toggle("d-none");
        });
    }
});

// product image
$(document).ready(function(){
    $('.image-slider').slick({
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: true,
        dots: true
    });
});
