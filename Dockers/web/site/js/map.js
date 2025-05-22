

let map, marker;
function initMap() {
// Coordenadas iniciais (ex: São Paulo, Brasil)
const initialLocation = {lat: -23.5505, lng: -46.6333};
map = L.map('map').setView([initialLocation.lat, initialLocation.lng], 13);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);
marker = L.marker([initialLocation.lat, initialLocation.lng]).addTo(map);
marker.bindPopup("<b>Sua Localização</b>").openPopup();
}

document.getElementById('getLocationButton').addEventListener('click', () => {
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
        (position) => {
            const pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };

            // Atualiza a posição do marcador
            marker.setLatLng([pos.lat, pos.lng]);

            // Centraliza o mapa na nova localização
            map.setView([pos.lat, pos.lng], 15);
        },
        () => {
            alert('Erro ao obter a localização. Verifique se a permissão está ativa.');
        }
    );
} else {
    alert('Geolocalização não suportada pelo navegador.');
}
});
initMap();

