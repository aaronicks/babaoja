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


