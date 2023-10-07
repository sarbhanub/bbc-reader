// script.js

const sortButton = document.querySelector('#sort-button');
const sortHover = document.querySelector('#sort-hover');
const continentsButton = document.querySelector('#continents-button');
const continentsHover = document.querySelector('#continents-hover');

sortButton.addEventListener('mouseover', () => {
	sortHover.style.display = 'block';
});

sortButton.addEventListener('mouseout', () => {
	sortHover.style.display = 'none';
});

sortHover.addEventListener('mouseover', () => {
	sortHover.style.display = 'block';
});

sortHover.addEventListener('mouseout', () => {
	sortHover.style.display = 'none';
});

continentsButton.addEventListener('mouseover', () => {
	continentsHover.style.display = 'block';
});

continentsButton.addEventListener('mouseout', () => {
	continentsHover.style.display = 'none';
});

continentsHover.addEventListener('mouseover', () => {
	continentsHover.style.display = 'block';
});

continentsHover.addEventListener('mouseout', () => {
	continentsHover.style.display = 'none';
});

window.addEventListener('scroll', function() {
	var navbar = document.querySelector('ul.navbar');
	var logoPane = document.querySelector('.logo-pane');
	var logoHeight = logoPane.offsetHeight;

	if (window.scrollY > logoHeight) {
		navbar.classList.add('navbar-fixed');
	} else {
		navbar.classList.remove('navbar-fixed');
	}
});

function handleSortChange(sortValue) {
	const currentUrl = new URL(window.location.href);
	currentUrl.searchParams.set('sort', sortValue);
	window.location.href = currentUrl.toString();
}