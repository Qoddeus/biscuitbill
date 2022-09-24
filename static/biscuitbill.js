// OPEN SECTIONS
function open_section(name) {
	var i, section;
	
	section = document.getElementsByClassName("section");
	for (i=0; i<section.length; i++) { section[i].style.display = "none"; }
	document.getElementById(name).style.display = "flex";
}

document.getElementById("default").click();

// TOGGLE MODE
let lightMode = localStorage.getItem("lightMode");
const lightModeToggle = document.querySelector("#light-mode-toggle");

const enableLightMode = () => {
	document.body.classList.add("light");
	localStorage.setItem("lightMode", "enabled");
}

const disableLightMode = () => {
	document.body.classList.remove("light");
	localStorage.setItem("lightMode", null);
}

if (lightMode === "enabled") { enableLightMode(); }

lightModeToggle.addEventListener("click", () => {
	lightMode = localStorage.getItem("lightMode");

	if (lightMode !== "enabled") { enableLightMode(); }
	else { disableLightMode(); }
});

// TIMO
function timo() {
	var timo = new Audio("static/sounds/timo.mp3");
	timo.play();
}
