let zipGraphs = [
    "97222.png",
    "98101.png",
    "98102.png",
    "98103.png",
    "98104.png",
    "98105.png",
    "98106.png",
    "98107.png",
    "98108.png",
    "98109.png",
    "98112.png",
    "98115.png",
    "98116.png",
    "98117.png",
    "98118.png",
    "98119.png",
    "98121.png",
    "98122.png",
    "98125.png",
    "98126.png",
    "98133.png",
    "98134.png",
    "98136.png",
    "98144.png",
    "98146.png",
    "98177.png",
    "98178.png",
    "98199.png",
];

let zipGallery = document.getElementById("zip-gallery");

for(let i = 0; i < zipGraphs.length; i++){
    let img = document.createElement("img");
    img.src = "plots/zips/" + zipGraphs[i];
    img.alt = "Image " + (i+1);
    zipGallery.appendChild(img);
}