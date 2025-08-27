document.addEventListener("DOMContentLoaded", function () {
  const triangles = document.querySelectorAll(".triangle");
  const loreContainer = document.getElementById("symbolic-card");

  if (!loreContainer || triangles.length === 0) {
    console.warn("Symbolic card container or triangles not found.");
    return;
  }

  triangles.forEach(tri => {
    tri.addEventListener("click", () => {
      const name = tri.getAttribute("data-name") || "Unknown";
      const element = tri.getAttribute("data-element") || "Unknown";
      const symbol = tri.getAttribute("data-symbol") || "";
      const lore = tri.getAttribute("data-lore") || "Lore not available.";

      loreContainer.innerHTML = `
        <h3>${symbol} (${element})</h3>
        <h4>${name}</h4>
        <p>${lore}</p>
      `;
    });
  });
});



// document.addEventListener("DOMContentLoaded", function () {
//   document.querySelectorAll(".triangle").forEach(tri => {
//     tri.addEventListener("click", () => {
//       const name = tri.getAttribute("data-name");
//       const element = tri.getAttribute("data-element");
//       const symbol = tri.getAttribute("data-symbol");
//       const lore = tri.getAttribute("data-lore");

//       const loreContainer = document.getElementById("symbolic-card");
//       if (loreContainer) {
//         loreContainer.innerHTML = `
//           <h3>${symbol} (${element})</h3>
//           <h4>${name}</h4>
//           <p>${lore}</p>
//         `;
//       } else {
//         console.warn("⚠️ Could not find #symbolic-card container.");
//       }
//     });
//   });
// });
