// reload_animation.js

// Function to show loading overlay during page reload
function showReloadAnimation() {
    const loadingOverlay = document.createElement('div');
    loadingOverlay.className = 'loading-overlay';
    const loadingSpinner = document.createElement('div');
    loadingSpinner.className = 'loading-spinner';
    loadingOverlay.appendChild(loadingSpinner);
    document.body.appendChild(loadingOverlay);
}

// Event listener for page reload
window.addEventListener('beforeunload', function () {
    showReloadAnimation();
});
