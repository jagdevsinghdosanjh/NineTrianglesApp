window.addEventListener("load", () => {
  setTimeout(() => {
    const loreContainer = document.getElementById("symbolic-card");
    const triangles = document.querySelectorAll(".triangle");

    if (!loreContainer || triangles.length === 0) {
      console.warn("⚠️ Lore container or triangles not found.");
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
  }, 500);
});

// function attachTriangleListeners() {
//   const loreContainer = document.getElementById("symbolic-card");
//   const triangles = document.querySelectorAll(".triangle");

//   if (!loreContainer || triangles.length === 0) {
//     console.warn("⚠️ Lore container or triangles not found.");
//     return;
//   }

//   triangles.forEach(tri => {
//     tri.addEventListener("click", () => {
//       const name = tri.getAttribute("data-name") || "Unknown";
//       const element = tri.getAttribute("data-element") || "Unknown";
//       const symbol = tri.getAttribute("data-symbol") || "";
//       const lore = tri.getAttribute("data-lore") || "Lore not available.";

//       loreContainer.innerHTML = `
//         <h3>${symbol} (${element})</h3>
//         <h4>${name}</h4>
//         <p>${lore}</p>
//       `;
//     });
//   });
// }

// // Delay execution to ensure DOM is ready
// window.addEventListener("load", () => {
//   setTimeout(attachTriangleListeners, 500);
// });
