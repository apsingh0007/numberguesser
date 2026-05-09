document.addEventListener('DOMContentLoaded', () => {
    const guessInput = document.getElementById('guess-input');
    const guessBtn = document.getElementById('guess-btn');
    const resetBtn = document.getElementById('reset-btn');
    const feedbackContainer = document.getElementById('feedback-container');
    const feedbackText = document.getElementById('feedback-text');
    const attemptsCount = document.getElementById('attempts-count');

    // Handle Enter key
    guessInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            guessBtn.click();
        }
    });

    guessBtn.addEventListener('click', async () => {
        const guess = guessInput.value;
        if (!guess) return;

        guessInput.value = '';
        guessInput.focus();

        try {
            const response = await fetch('/guess', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ guess: guess })
            });

            const data = await response.json();

            if (data.error) {
                showFeedback(data.error, 'low');
                return;
            }

            attemptsCount.textContent = data.attempts;
            showFeedback(data.message, data.status);

            if (data.status === 'correct') {
                guessBtn.disabled = true;
                guessInput.disabled = true;
                resetBtn.classList.remove('hidden');
                createConfetti();
            }

        } catch (error) {
            console.error('Error:', error);
            showFeedback('An error occurred. Please try again.', 'high');
        }
    });

    resetBtn.addEventListener('click', async () => {
        try {
            const response = await fetch('/reset', {
                method: 'POST'
            });
            const data = await response.json();
            
            attemptsCount.textContent = '0';
            feedbackContainer.classList.add('hidden');
            guessBtn.disabled = false;
            guessInput.disabled = false;
            guessInput.value = '';
            guessInput.focus();
            resetBtn.classList.add('hidden');
            
            // Remove confetti
            document.querySelectorAll('.confetti').forEach(e => e.remove());

        } catch (error) {
            console.error('Error resetting game:', error);
        }
    });

    function showFeedback(message, status) {
        feedbackContainer.className = 'feedback'; // reset classes
        feedbackContainer.classList.add(`status-${status}`);
        feedbackText.textContent = message;
        
        // Add a small bounce animation
        feedbackContainer.style.transform = 'scale(1.05)';
        setTimeout(() => {
            feedbackContainer.style.transform = 'scale(1)';
        }, 200);
    }

    // Simple confetti effect
    function createConfetti() {
        const colors = ['#ff4757', '#2ed573', '#1e90ff', '#ffeb3b', '#ff69b4'];
        for (let i = 0; i < 100; i++) {
            const confetti = document.createElement('div');
            confetti.classList.add('confetti');
            confetti.style.left = Math.random() * 100 + 'vw';
            confetti.style.top = -10 + 'px';
            confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
            confetti.style.transform = `rotate(${Math.random() * 360}deg)`;
            
            document.body.appendChild(confetti);

            const animation = confetti.animate([
                { transform: `translate3d(0,0,0) rotate(0deg)`, opacity: 1 },
                { transform: `translate3d(${Math.random()*200 - 100}px, ${window.innerHeight}px, 0) rotate(${Math.random()*720}deg)`, opacity: 0 }
            ], {
                duration: Math.random() * 2000 + 1500,
                easing: 'cubic-bezier(.37,0,.63,1)',
                fill: 'forwards'
            });

            animation.onfinish = () => confetti.remove();
        }
    }
});
