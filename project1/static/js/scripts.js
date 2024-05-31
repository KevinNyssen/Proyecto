// static/js/gifControl.js

document.addEventListener("DOMContentLoaded", function() {
    const sections = [
        { id: 'to-do-img', png: 'images/td.png', gif: 'images/to-do.gif' },
        { id: 'doing-img', png: 'images/ding.png', gif: 'images/doing.gif' },
        { id: 'done-img', png: 'images/de.png', gif: 'images/done.gif' }
    ];

    sections.forEach(section => {
        const img = document.getElementById(section.id);
        img.addEventListener('mouseover', () => {
            img.src = `{% static '${section.gif}' %}`;
        });
        img.addEventListener('mouseout', () => {
            img.src = `{% static '${section.png}' %}`;
        });
    });
});
