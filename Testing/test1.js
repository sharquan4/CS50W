let myImage = document.querySelector('img');

myImage.onclick = function () {
    let mySrc = myImage.getAttribute('src');
    if (mySrc === 'images/canyon1.jpg') {
        myImage.setAttribute('src', 'images/p3n1s.jpg');
    } else {
        myImage.setAttribute('src', 'images/canyon1.jpg');
    }
}