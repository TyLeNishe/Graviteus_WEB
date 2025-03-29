function openModal(title, event) {
    event.stopPropagation();
    const modal = document.getElementById('modal');
    const modalTitle = document.getElementById('modal-title');
    modalTitle.textContent = title;
    modal.style.display = 'flex';
    document.body.classList.add('modal-open');
}

const modal = document.getElementById('modal');
modal.addEventListener('click', (event) => {
    if (event.target === modal) {
        modal.style.display = 'none';
        document.body.classList.remove('modal-open');
    }
});

const accordionItems = document.querySelectorAll('.accordion-item');

accordionItems.forEach(item => {
    const header = item.querySelector('.accordion-header');
    header.addEventListener('click', () => {
        accordionItems.forEach(otherItem => {
            if (otherItem !== item && otherItem.classList.contains('active')) {
                otherItem.classList.remove('active');
            }
        });
        item.classList.toggle('active');
    });
});

function handleAvatarChange(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const avatarPreview = document.getElementById('avatar-preview');
            avatarPreview.src = e.target.result;
        };
        reader.readAsDataURL(file);

        document.getElementById('avatar-form').submit();
    }
}

function toggleEmailEdit() {
    const emailValue = document.getElementById('email-value');
    const emailInput = document.getElementById('email-input');

    if (emailValue.style.display !== 'none') {
        emailValue.style.display = 'none';
        emailInput.style.display = 'inline';
        emailInput.value = emailValue.textContent;
        emailInput.focus();
    } else {
        emailValue.style.display = 'inline';
        emailInput.style.display = 'none';
    }
}

function saveEmail() {
    const emailValue = document.getElementById('email-value');
    const emailInput = document.getElementById('email-input');
    const newEmail = emailInput.value.trim();

    if (newEmail) {
        const form = document.createElement('form');
        form.method = 'POST';
        form.action = document.getElementById('update-email-url').dataset.url; 
        form.style.display = 'none';

        const csrfInput = document.createElement('input');
        csrfInput.type = 'hidden';
        csrfInput.name = 'csrfmiddlewaretoken';
        csrfInput.value = document.getElementById('csrf-token').dataset.csrf; 
        form.appendChild(csrfInput);

        const emailInputForm = document.createElement('input');
        emailInputForm.type = 'hidden';
        emailInputForm.name = 'email';
        emailInputForm.value = newEmail;
        form.appendChild(emailInputForm);

        document.body.appendChild(form);
        form.submit();
    }
}

function cancelEmailEdit() {
    const emailValue = document.getElementById('email-value');
    const emailInput = document.getElementById('email-input');

    emailValue.style.display = 'inline';
    emailInput.style.display = 'none';
}

document.getElementById('email-input').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        saveEmail();
    } else if (event.key === 'Escape') {
        cancelEmailEdit();
    }
});

function toggleUsernameEdit() {
    const usernameValue = document.getElementById('username-value');
    const usernameInput = document.getElementById('username-input');

    if (usernameValue.style.display !== 'none') {
        usernameValue.style.display = 'none';
        usernameInput.style.display = 'inline';
        usernameInput.value = usernameValue.textContent;
        usernameInput.focus();
    } else {
        usernameValue.style.display = 'inline';
        usernameInput.style.display = 'none';
    }
}

function saveUsername() {
    const usernameValue = document.getElementById('username-value');
    const usernameInput = document.getElementById('username-input');
    const newUsername = usernameInput.value.trim();

    if (newUsername) {
        const form = document.createElement('form');
        form.method = 'POST';
        form.action = document.getElementById('update-username-url').dataset.url; 
        form.style.display = 'none';

        const csrfInput = document.createElement('input');
        csrfInput.type = 'hidden';
        csrfInput.name = 'csrfmiddlewaretoken';
        csrfInput.value = document.getElementById('csrf-token').dataset.csrf; 
        form.appendChild(csrfInput);

        const usernameInputForm = document.createElement('input');
        usernameInputForm.type = 'hidden';
        usernameInputForm.name = 'username';
        usernameInputForm.value = newUsername;
        form.appendChild(usernameInputForm);

        document.body.appendChild(form);
        form.submit();
    } else {
        alert('Имя пользователя не может быть пустым.');
    }
}

function cancelUsernameEdit() {
    const usernameValue = document.getElementById('username-value');
    const usernameInput = document.getElementById('username-input');

    usernameValue.style.display = 'inline';
    usernameInput.style.display = 'none';
}

document.getElementById('username-input').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        saveUsername();
    } else if (event.key === 'Escape') {
        cancelUsernameEdit();
    }
});

