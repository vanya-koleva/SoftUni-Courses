function getInfo() {
    const baseUrl = 'http://localhost:3030/jsonstore/bus/businfo';

    const stopIdEl = document.querySelector('#stopId');
    const stopNameEl = document.querySelector('#stopName');
    const busesEl = document.querySelector('#buses');

    const stopId = stopIdEl.value;
    fetch(`${baseUrl}/${stopId}`)
        .then(res => res.json())
        .then(data => {
            stopNameEl.textContent = data.name;
            for (const bus in data.buses) {
                const liElement = document.createElement('li');
                liElement.textContent = `Bus ${bus} arrives in ${data.buses[bus]} minutes`;
                busesEl.appendChild(liElement);
            }
        })
        .catch(() => {
            stopNameEl.textContent = 'Error';
        });
}
