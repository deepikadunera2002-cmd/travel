
function openPopup(imageSrc){
    document.getElementById("popupImg").src = imageSrc;
    document.getElementById("imagePopup").style.display = "flex";
}

function closePopup(){
    document.getElementById("imagePopup").style.display = "none";
}

function toggleInfo(id){
    document.getElementById(id).classList.toggle("show");
}function openVideoPopup() {
    document.getElementById("videoPopup").style.display = "flex";
}

function closeVideoPopup() {
    document.getElementById("videoPopup").style.display = "none";
}function openVideoPopup() {
    document.getElementById("videoPopup").style.display = "flex";
}
let slides = document.querySelectorAll(".slide");
let current = 0;

setInterval(() => {
    slides[current].classList.remove("active");
    current = (current + 1) % slides.length;
    slides[current].classList.add("active");
}, 3000);