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
// const to_top_btn = $("#toTopBtn");
// // When the user scrolls down 20px from the top of the document, show the button
// window.onscroll = function () {
//   if (document.body.scrollTop > 40 || document.documentElement.scrollTop > 40) {
//     to_top_btn.removeClass("hidden");
//     to_top_btn.addClass("block");
//   } else {
//     to_top_btn.removeClass("block");
//     to_top_btn.addClass("hidden");
//   }
// };

// // When the user clicks on the button, scroll to the top of the document
// function toTop() {
//   document.body.scrollTop = 0;
//   document.documentElement.scrollTop = 0;
// }

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
document.getElementById("defaultOpen").click();

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
