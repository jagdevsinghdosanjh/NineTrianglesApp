document.querySelectorAll("polygon").forEach(poly => {
    poly.addEventListener("click", () => {
        const symbol = poly.getAttribute("title");
        const card = document.getElementById("symbolic-card");
        card.innerHTML = `<h3>${symbol}</h3><p>${getLore(symbol)}</p>`;
    });
});

document.addEventListener("DOMContentLoaded", function() {
    if (!CSS.supports("backdrop-filter", "blur(5px)")) {
        document.querySelectorAll(".symbolic-card").forEach(card => {
            card.style.backgroundColor = "rgba(255,255,255,0.2)";
        });
    }
});


function getLore(symbol) {
    const loreMap = {
        "Wisdom": "Clarity of thought and the breath of insight.",
        "Courage": "The spark that ignites transformation.",
        "Harmony": "Flowing unity and emotional resonance.",
        "Structure": "Foundation, form, and sacred geometry.",
        "Vision": "The unseen pattern behind all things.",
        "Balance": "Precision, reflection, and inner alignment.",
        "Flow": "Growth, adaptability, and creative expansion.",
        "Truth": "Illumination, revelation, and integrity.",
        "Mystery": "The unknown, the hidden, the fertile void."
    };
    return loreMap[symbol] || "Unknown symbol.";
}
