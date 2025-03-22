// Flipping the card
document.querySelectorAll('.flip-btn').forEach(button => {
    button.addEventListener('click', function() {
        this.closest('.flip-card').classList.toggle('flipped');
    });
});