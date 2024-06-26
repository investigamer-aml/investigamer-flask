document.addEventListener('DOMContentLoaded', function() {
    const useCaseContainer = document.querySelector('.use-case-container');
    const useCaseDataElement = document.querySelector('#use-case-data'); // Correctly reference the use-case-data element
    let totalUseCases = parseInt(useCaseDataElement.dataset.totalUseCases, 10);
    let completedUseCases = parseInt(useCaseDataElement.dataset.completedUseCases, 10);
    console.log('COMPLETED CASES', completedUseCases)

    // Event delegation for form submission
    useCaseContainer.addEventListener('submit', async function(event) {
      if (event.target.tagName === 'FORM') {
        event.preventDefault();
        const form = event.target;
        const formData = new FormData(form);
        const data = {
          use_case_id: formData.get('use_case_id'),
          answers: []
        };
        formData.forEach((value, key) => {
          if (key.startsWith('answer[')) {
            const questionId = key.match(/\[(.*?)\]/)[1];
            data.answers.push({ questionId, answer: value });
          }
        });
        try {
          const response = await fetch('/submit-answer', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data),
          });
          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }
          const responseData = await response.json();
          console.log('Response data:', responseData);


          if (responseData.isCorrect) {
            completedUseCases++;
            completedUseCases = parseFloat(completedUseCases);
            updateProgressBar();
            updateRemainingUseCases();
            displayFeedback(true); // Show success message
          } else {
            displayFeedback(false); // Show error message
          }

          if (responseData.nextUseCase) {
            loadNextUseCase(responseData.nextUseCase);
          } else {
            useCaseContainer.innerHTML = '<p>All use cases completed!</p>';
          }
        } catch (error) {
          console.error('Error:', error);
          displayFeedback(false, error.message); // Show error with message
        }
      }
    });



    function updateProgressBar() {
      const progressBar = document.getElementById('progress-bar');
      let progressPercentage = (completedUseCases / totalUseCases) * 100;
      progressBar.style.width = `${progressPercentage}%`;
      progressBar.textContent = `${progressPercentage.toFixed(0)}%`;
    }

    function updateRemainingUseCases() {
      const remainingCount = document.getElementById('remaining-count');
      let remaining = totalUseCases - completedUseCases;
      remainingCount.textContent = remaining;
    }



    function displayFeedback(isCorrect, message = '') {
      const feedback = document.getElementById('answer-feedback');
      if (isCorrect) {
        feedback.textContent = 'Correct answer!';
        feedback.className = 'bg-green-500 text-center py-2 px-4 rounded text-white';
        playSound('sounds/correct.mp3'); // Assuming you have this audio file
      } else {
        feedback.textContent = message || 'Incorrect answer!';
        feedback.className = 'bg-red-500 text-center py-2 px-4 rounded text-white';
        playSound('sounds/wrong.mp3'); // Assuming you have this audio file
      }
      feedback.classList.remove('hidden');
      setTimeout(() => feedback.classList.add('hidden'), 3000);
    }

    function generateQuestionHTML(question) {
      if (!question) return '';
      return `
        <div class="mb-6">
          <p class="font-bold mb-2">${question.text}</p>
          ${question.options.map(option => `
            <label class="block mb-2">
              <input type="radio" name="answer[${question.questionId}]" value="${option.id}" class="mr-2">
              ${option.text}
            </label>
          `).join('')}
        </div>
      `;
    }

  });