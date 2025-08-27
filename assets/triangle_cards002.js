document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".triangle").forEach(tri => {
    tri.addEventListener("click", () => {
      const name = tri.getAttribute("data-name");
      const element = tri.getAttribute("data-element");
      const symbol = tri.getAttribute("data-symbol");
      const lore = tri.getAttribute("data-lore");

      document.getElementById("symbolic-card").innerHTML = `
        <h3>${symbol} (${element})</h3>
        <h4>${name}</h4>
        <p>${lore}</p>
      `;
    });
  });
});
