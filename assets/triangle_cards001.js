document.addEventListener("DOMContentLoaded", function () {
  const loreMap = {
    "Wisdom": "Breath is the bridge between thought and form...",
    "Courage": "Fire transforms. It consumes illusion...",
    // Add more mappings
  };

  document.querySelectorAll(".triangle").forEach(tri => {
    tri.addEventListener("click", () => {
      const name = tri.getAttribute("data-name");
      const lore = loreMap[name] || "Lore not found.";
      document.getElementById("symbolic-card").innerHTML = `
        <h3>${name}</h3>
        <p>${lore}</p>
      `;
    });
  });
});
