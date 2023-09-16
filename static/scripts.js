//  navbbar dropdown button mechanism ----------------------------------------------
function toggleDropdown(e) {
  e.name === "dropdownBtn"
    ? ((e.name = "close"), dropdownMenu.classList.remove("hidden"))
    : ((e.name = "dropdownBtn"), dropdownMenu.classList.add("hidden"));
}

//  menu button mechanism ----------------------------------------------
function toggleMenu(e) {
  e.name === "menu"
    ? ((e.name = "close"), navlinks.classList.remove("hidden"))
    : ((e.name = "menu"), navlinks.classList.add("hidden"));
}

//  notifier button mechanism ----------------------------------------------
function toggleNotifier(e) {
  console.log("notify me");
  e.name === "bellBtn"
    ? ((e.name = "close"), notifications.classList.remove("hidden"))
    : ((e.name = "bellBtn"), notifications.classList.add("hidden"));
}

//  back to top button mechanism ---------------------------------------------------
const to_top_btn = $("#toTopBtn");
// When the user scrolls down 20px from the top of the document, fadein the button
window.onscroll = function () {
  if (document.body.scrollTop > 30 || document.documentElement.scrollTop > 30) {
    to_top_btn.removeClass("hidden");
    to_top_btn.addClass("block");
  } else {
    to_top_btn.removeClass("block");
    to_top_btn.addClass("hidden");
  }
};
// When the user clicks on the button, scroll to the top of the document
function toTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

//  tabs control ---------------------------------------------------
function openTab(evt, cityName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}

/* client folder scripts ---------------------------------------------------------------------------------------------------- */

// Get the element with id="defaultOpen" and click on it
// document.getElementById("defaultOpen").click();

// Récupérer tous les éléments de l'accordéon
const accordionItems = document.querySelectorAll(".accordion-item");

// Ajouter un gestionnaire d'événement pour chaque en-tête
accordionItems.forEach((item) => {
  const header = item.querySelector(".accordion-header");

  header.addEventListener("click", () => {
    // Bascule la classe "active" pour afficher/masquer le contenu
    item.classList.toggle("active");
  });
});

// comment ça marche

const tabLinks = document.querySelectorAll(".tab-links a");
const tabPanes = document.querySelectorAll(".tab-pane");

tabLinks.forEach((link, index) => {
  link.addEventListener("click", (e) => {
    e.preventDefault();
    tabLinks.forEach((l) =>
      l.classList.remove("text-blue-500", "border-blue-500")
    );
    link.classList.add("text-blue-500", "border-blue-500");
    tabPanes.forEach((pane) => pane.classList.add("hidden"));
    tabPanes[index].classList.remove("hidden");
  });
});

/* school rating ---------------------------------------------------------------------------------------------------- */
const ratingStars = [...document.getElementsByClassName("rating_star")];

function executeRating(stars) {
  const starClassActive =
    "rating_star fa-solid  fa-star text-sky-400 cursor-pointer";
  const starClassInactive =
    "rating_star fa-regular fa-star text-sky-400 cursor-pointer";

  const starsLength = stars.length;
  let i;
  stars.map((star) => {
    star.onclick = () => {
      i = stars.indexOf(star);
      console.log(i + 1);

      if (star.className === starClassInactive) {
        for (i; i >= 0; --i) stars[i].className = starClassActive;
      } else {
        for (i; i < starsLength; ++i) stars[i].className = starClassInactive;
      }
    };
  });
}
executeRating(ratingStars);

/* carousels ---------------------------------------------------------------------------------------------------- */
const carousel = document.querySelector(".carousel");
const slider = document.querySelector(".carousel-slider");
const prev = document.querySelector(".prev");
const next = document.querySelector(".next");
var carousel_direction = 0;

prev.addEventListener("click", function () {
  if (carousel_direction < 0) {
    slider.appendChild(slider.firstElementChild);
    carousel_direction = 1;
  }
  carousel.style.justifyContent = "flex-end";
  slider.style.transform = "translate(+20%)";
});

next.addEventListener("click", function () {
  if (carousel_direction > 0) {
    slider.appendChild(slider.lastElementChild);
    carousel_direction = -1;
  }
  carousel.style.justifyContent = "flex-start";
  slider.style.transform = "translate(-20%)";
});

slider.addEventListener("transitionend", function () {
  if (carousel_direction > 0) {
    slider.prepend(slider.lastElementChild);
  } else {
    slider.appendChild(slider.firstElementChild);
  }

  slider.style.transition = "none";
  slider.style.transform = "translate(0)";
  setTimeout(function () {
    slider.style.transition = "all 0.5s";
  });
});
/* animations ---------------------------------------------------------------------------------------------------- */

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    console.log(entry);
    if (entry.isIntersecting) {
      entry.target.classList.add("fadein");
    } else {
      entry.target.classList.remove("fadein");
    }
    if (entry.isIntersecting) {
      entry.target.classList.add("slidein");
    } else {
      entry.target.classList.remove("slidein");
    }
    if (entry.isIntersecting) {
      entry.target.classList.add("stagerin");
    } else {
      entry.target.classList.remove("stagerin");
    }
  });
});
const fadingElements = document.querySelectorAll(".fadeout");
fadingElements.forEach((e) => observer.observe(e));
const slidingElements = document.querySelectorAll(".slideout");
slidingElements.forEach((e) => observer.observe(e));
const stageringElements = document.querySelectorAll(".stagerout");
stageringElements.forEach((e) => observer.observe(e));
