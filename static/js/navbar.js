const nav = document.querySelector("nav"); //PEga a tag nav

document.addEventListener("scroll", (e) => {
	if (scrollY > 100) {
		if (scrollY > window.innerHeight) {
			nav.classList.add("invisible");
		} else {
			nav.classList.add("navbar-bg");
			nav.classList.remove("invisible");
		}
	} else {
		nav.classList.remove("navbar-bg");
		nav.classList.remove("invisible");
	}
});
