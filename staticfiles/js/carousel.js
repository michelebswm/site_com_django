const controls = document.querySelectorAll(".control");
let currentItem = 0;
const items = document.querySelectorAll(".item");
const maxItems = items.length;

controls.forEach((control) => {
	control.addEventListener("click", () => {
		const isLeft = control.classList.contains("arrow-left");

		if (isLeft) {
			currentItem -= 1;
		} else {
			currentItem += 1;
		}

		if (currentItem >= maxItems) {
			currentItem = 0;
		}
		// currentItem não pode ser < 0
		if (currentItem < 0) {
			currentItem = maxItems - 1;
		}

		items.forEach((item) => item.classList.remove("current-item"));
		items[currentItem].scrollIntoView({
			inline: "center",
			behavior: "smooth",
		});

		items[currentItem].classList.add("current-item");
	});
});

const controls2 = document.querySelectorAll(".control2");
let currentItem2 = 0;
const items2 = document.querySelectorAll(".item2");
const maxItems2 = items2.length;

controls2.forEach((control2) => {
	control2.addEventListener("click", () => {
		const isLeft2 = control2.classList.contains("arrow-left2");

		if (isLeft2) {
			currentItem2 -= 1;
		} else {
			currentItem2 += 1;
		}

		if (currentItem2 >= maxItems2) {
			currentItem2 = 0;
		}
		// currentItem não pode ser < 0
		if (currentItem2 < 0) {
			currentItem2 = maxItems2 - 1;
		}

		items2.forEach((item2) => item2.classList.remove("current-item2"));
		items2[currentItem2].scrollIntoView({
			inline: "center",
			behavior: "smooth",
		});

		items2[currentItem2].classList.add("current-item2");
	});
});

const controls3 = document.querySelectorAll(".control3");
let currentItem3 = 0;
const items3 = document.querySelectorAll(".item3");
const maxItems3 = items3.length;

controls3.forEach((control3) => {
	control3.addEventListener("click", () => {
		const isLeft3 = control3.classList.contains("arrow-left3");

		if (isLeft3) {
			currentItem3 -= 1;
		} else {
			currentItem3 += 1;
		}

		if (currentItem3 >= maxItems3) {
			currentItem3 = 0;
		}
		// currentItem não pode ser < 0
		if (currentItem3 < 0) {
			currentItem3 = maxItems3 - 1;
		}

		items3.forEach((item3) => item3.classList.remove("current-item3"));
		items3[currentItem3].scrollIntoView({
			inline: "center",
			behavior: "smooth",
		});

		items3[currentItem3].classList.add("current-item3");
	});
});
