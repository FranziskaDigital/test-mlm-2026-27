const map = L.map("map").setView([51.3397, 12.3731], 13);

L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  attribution: "&copy; OpenStreetMap contributors"
}).addTo(map);

let objects = [];
let markers = [];
let activeGeoLayer = null;

fetch("data/media.json")
  .then(response => {
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    return response.json();
  })
  .then(data => {
    objects = data;
    showObjects(objects);
  })
  .catch(error => {
    document.getElementById("detail").innerHTML =
      `<h2>Fehler</h2><p>Metadaten konnten nicht geladen werden: ${error.message}</p>`;
  });

function clearMarkers() {
  markers.forEach(marker => map.removeLayer(marker));
  markers = [];
}

function showObjects(data) {
  clearMarkers();

  data.forEach(object => {
    const marker = L.marker([object.location.lat, object.location.lon]).addTo(map);
    marker.bindPopup(`<strong>${escapeHtml(object.title)}</strong><br>${escapeHtml(object.type)}`);
    marker.on("click", () => showObject(object));
    markers.push(marker);
  });
}

function viewerFor(object) {
  const src = object.representations.access;
  const mime = object.representations.mime;

  switch (object.type) {
    case "image":
      return `<img src="${src}" alt="${escapeHtml(object.title)}">`;
    case "audio":
      return `<audio controls><source src="${src}" type="${mime}"></audio>`;
    case "video":
      return `<video controls><source src="${src}" type="${mime}"></video>`;
    case "3d":
      return `<model-viewer src="${src}" camera-controls auto-rotate></model-viewer>`;
    case "geo":
      showGeoData(object);
      return `<p>Die Geodaten werden auf der Karte dargestellt.</p>`;
    default:
      return `<p>Für diesen Medientyp ist noch kein Viewer definiert.</p>`;
  }
}

function showObject(object) {
  if (activeGeoLayer) {
    map.removeLayer(activeGeoLayer);
    activeGeoLayer = null;
  }

  const detail = document.getElementById("detail");
  const license = object.rights?.license ?? "nicht angegeben";
  const rightsHolder = object.rights?.rightsHolder ?? "nicht angegeben";

  detail.innerHTML = `
    <article>
      <h2>${escapeHtml(object.title)}</h2>
      ${viewerFor(object)}
      <p>${escapeHtml(object.description)}</p>
      <dl class="metadata">
        <dt>Identifier</dt><dd>${escapeHtml(object.id)}</dd>
        <dt>Medientyp</dt><dd>${escapeHtml(object.type)}</dd>
        <dt>Ort</dt><dd>${escapeHtml(object.location.name)}</dd>
        <dt>Access-MIME</dt><dd>${escapeHtml(object.representations.mime)}</dd>
        <dt>Lizenz</dt><dd>${escapeHtml(license)}</dd>
        <dt>Rechteinhaber</dt><dd>${escapeHtml(rightsHolder)}</dd>
      </dl>
    </article>
  `;
}

function showGeoData(object) {
  fetch(object.representations.access)
    .then(response => response.json())
    .then(data => {
      activeGeoLayer = L.geoJSON(data).addTo(map);
      const bounds = activeGeoLayer.getBounds();
      if (bounds.isValid()) map.fitBounds(bounds);
    });
}

document.querySelectorAll("#filters button").forEach(button => {
  button.addEventListener("click", () => {
    document.querySelectorAll("#filters button").forEach(b => b.classList.remove("active"));
    button.classList.add("active");

    const type = button.dataset.type;
    showObjects(type === "all" ? objects : objects.filter(object => object.type === type));
  });
});

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}
