window.addEventListener('scroll', function() {
    const scrollBtn = document.getElementById('scrollToTopBtn');
    if (window.scrollY > 48) {
        scrollBtn.style.display = 'block';
    } else {
        scrollBtn.style.display = 'none';
    }
});

function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById('bookModal');
    const closeBtn = modal.querySelector('.close');

    document.querySelectorAll('.open-book-modal').forEach(btn => {
        btn.addEventListener('click', function (e) {
            e.preventDefault();

            document.getElementById('modalTitle').textContent = this.dataset.title;
            document.getElementById('modalAuthor').textContent = this.dataset.author;
            document.getElementById('modalPublisher').textContent = this.dataset.publisher;
            document.getElementById('modalDate').textContent = this.dataset.date;
            document.getElementById('modalCover').src = this.dataset.coverUrl;

            modal.style.display = 'block';
        });
    });

    closeBtn.onclick = () => modal.style.display = 'none';

    window.onclick = function (event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    };
});

document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById('authorModal');
    const closeBtn = modal.querySelector('.close');

    document.querySelectorAll('.open-author-modal').forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            
            document.getElementById('modalAuthorName').textContent = this.dataset.name;
            document.getElementById('modalAuthorPhoto').src = this.dataset.photoUrl;
            document.getElementById('modalAuthorBio').textContent = this.dataset.biography;

            modal.style.display = 'block';
        });
    });

    closeBtn.onclick = () => modal.style.display = 'none';

    window.onclick = function (event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    };
});



document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById('publisherModal');
    const closeBtn = modal.querySelector('.close');

    document.querySelectorAll('.open-publisher-modal').forEach(btn => {
        btn.addEventListener('click', function (e) {
            e.preventDefault();

            document.getElementById('modalName').textContent = this.dataset.name;
            document.getElementById('modalLogo').src = this.dataset.logoUrl;
            document.getElementById('modalAddress').textContent = this.dataset.address;

            modal.style.display = 'block';
        });
    });

    closeBtn.onclick = () => modal.style.display = 'none';

    window.onclick = function (event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    };
});

function showToast(message, type = 'info', duration = 3000) {
    const container = document.getElementById('toastContainer');
    const toast = document.createElement('div');
    
    toast.className = `toast ${type}`;
    toast.textContent = message;
    
    container.appendChild(toast);
    
    
    setTimeout(() => {
        toast.remove();
    }, duration + 500); 
}


function toggleSlidePanel() {
    const panel = document.getElementById('slidePanel');
    panel.classList.toggle('open');
}


document.addEventListener('DOMContentLoaded', function() {
    const panelTab = document.querySelector('.slide-panel-tab');
    if (panelTab) {
        panelTab.addEventListener('click', toggleSlidePanel);
    }
});

console.log("Скрипт main.js загружен!"); // Это должно появиться в консоли

document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM полностью загружен"); // Это второе сообщение
    
    const mainContainer = document.getElementById('mainContainer');
    if (!mainContainer) {
        console.error("Элемент mainContainer не найден!");
        return;
    }
    
    console.log("mainContainer найден");
    const backgrounds = [
        'url("/static/images/bg1.jpg")',
        'url("/static/images/bg2.jpg")',
        'url("/static/images/bg3.jpg")'
    ];
    
    if (mainContainer && backgrounds.length > 0) {
        console.log("Начинаем смену фонов");
        
        // Простая смена без анимации для теста
        let current = 0;
        mainContainer.style.backgroundImage = backgrounds[current];
        
        setInterval(() => {
            current = (current + 1) % backgrounds.length;
            console.log("Меняем фон на:", backgrounds[current]);
            mainContainer.style.backgroundImage = backgrounds[current];
        }, 5000);
}});