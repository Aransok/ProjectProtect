document.addEventListener('DOMContentLoaded', function() {
    const sidebarToggle = document.getElementById('sidebar-toggle');
    const sidebar = document.getElementById('sidebar');

    sidebarToggle.addEventListener('click', function() {
        sidebar.classList.toggle('open');
        sidebarToggle.classList.toggle('open');
    });

    sidebarToggle.addEventListener('keydown', function(event) {
        if (event.keyCode === 13 || event.keyCode === 32) {
            sidebar.classList.toggle('open');
            sidebarToggle.classList.toggle('open');
        }
    });
});
