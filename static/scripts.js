function stars() {
    const count = 300;
    const stars = document.getElementById('stars');
    const starElements = []; // Array to store the created star elements
    var i = 0;
    while(i < count) {
      const star = document.createElement('i');
      const x = Math.floor(Math.random() * window.innerWidth);
      const y = Math.floor(Math.random() * window.innerHeight);
      const size = Math.random() * 5;
      star.style.left = x+'px';
      star.style.top = y+'px';
      star.style.height = 1+size+'px';
      star.style.width = 1+size+'px';
      const duration = Math.random() * 2;
      star.style.animationDuration = 2+duration+'s';
      stars.appendChild(star);
      starElements.push(star); // Add the star element to the array
      i++;
    }
    return starElements; // Return the array of star elements
}

const starElements = stars(); // Get the array of star elements

const scene = document.querySelector('#scene');

function createDiv(starElements) {
    starElements.forEach(star => {
        const div = document.createElement('div');
        // Use the same style for div as the star
        div.style.left = star.style.left;
        div.style.top = star.style.top;
        div.style.position = 'absolute'; // this is important for correct positioning
        div.style.height = star.style.height;
        div.style.width = star.style.width;
        scene.appendChild(div);
    });
}

createDiv(starElements);