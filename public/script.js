// Basic client-side check before the form is submitted to Flask
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    if (!form) return;

    form.addEventListener('submit', function (event) {
        const inputs = form.querySelectorAll('input, select');
        let allFilled = true;

        inputs.forEach(function (field) {
            if (!field.value.trim()) {
                allFilled = false;
                field.style.borderColor = 'red';
            } else {
                field.style.borderColor = '#ccc';
            }
        });

        if (!allFilled) {
            event.preventDefault();
            alert('Please fill in all the fields before predicting.');
        }
    });
});
