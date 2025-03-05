    // Script pour faire défiler les vidéos
    const videos = document.querySelectorAll('.video-container video');
    let currentVideo = 0;

    setInterval(() => {
      videos[currentVideo].classList.remove('active');
      currentVideo = (currentVideo + 1) % videos.length;
      videos[currentVideo].classList.add('active');
    }, 15000); // Change de vidéo toutes les 10 secondes