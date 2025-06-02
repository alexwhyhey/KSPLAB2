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
            document.getElementById('modalLogo').src = this.dataset.logoUrl;     // исправлено на coverUrl
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

