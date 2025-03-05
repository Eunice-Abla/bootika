function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('overlay');
    const content = document.getElementById('content');
  
    sidebar.classList.toggle('active');
    overlay.classList.toggle('active');
    content.classList.toggle('shifted');
  }
  