function Toggle_mobile_menu() {
  let menus = document.getElementById("mobile_navigation");
  if (menus.style.display === "block") {
    menus.style.display = "none"
  } else {
    menus.style.display = "block"
  }
}
