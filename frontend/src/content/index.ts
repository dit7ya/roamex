import App from "./App.svelte";

console.log("[roamex]  Content-script loaded.");

const roamex = document.createElement("div");
roamex.className = "roamex-sidebar-container";
roamex.id = "roamex-app";

document.body.appendChild(roamex);

const roamexShadowRoot = roamex.attachShadow({ mode: "open" });
new App({ target: roamexShadowRoot });
