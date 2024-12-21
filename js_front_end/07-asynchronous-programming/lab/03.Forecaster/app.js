function attachEvents() {
    const baseUrl = 'http://localhost:3030/jsonstore/forecaster';
    const locationEl = document.getElementById('location');
    const submitButton = document.getElementById('submit');
    const forecastEl = document.getElementById('forecast')
    const currentEl = document.getElementById('current');
    const upcomingEl = document.getElementById('upcoming');

    const weatherSymbol = {
        'Sunny': '☀',
        'Partly sunny': '⛅',
        'Overcast': '☁',
        'Rain': '☂',
        'Degrees': '°',
    }

    function createForecastElement(day, forecastInfoEl) {
        console.log(day);

        const spanEl = document.createElement('span');
        spanEl.classList.add('upcoming');
        spanEl.innerHTML = `
            <span class="symbol">${weatherSymbol[day.condition]}</span>
            <span class="forecast-data">${day.low}${weatherSymbol.Degrees}/${day.high}${weatherSymbol.Degrees}</span>
            <span class="forecast-data">${day.condition}</span>
        `;

        forecastInfoEl.appendChild(spanEl);
    }

    submitButton.addEventListener('click', () => {
        fetch(`${baseUrl}/locations`)
            .then(res => res.json())
            .then(locations => {
                const location = locations.find(l => l.name === locationEl.value);
                const code = location.code;
                return Promise.all([
                    fetch(`${baseUrl}/today/${code}`),
                    fetch(`${baseUrl}/upcoming/${code}`)
                ]);
            })
            .then(res => Promise.all(res.map(r => r.json())))
            .then(([today, upcoming]) => {
                console.log(today);
                forecastEl.style.display = 'block';       

                const symbolSpanEl = document.createElement('span');
                symbolSpanEl.classList.add('condition');
                symbolSpanEl.classList.add('symbol');
                symbolSpanEl.textContent = weatherSymbol[today.forecast.condition];

                //Bad to do
                const anotherSpanEl = document.createElement('span');
                anotherSpanEl.innerHTML = `
                    <span class="condition">
                        <span class="forecast-data">${today.name}</span>
                        <span class="forecast-data">${today.forecast.low}${weatherSymbol.Degrees}/${today.forecast.high}${weatherSymbol.Degrees}</span>
                        <span class="forecast-data">${today.forecast.condition}</span>
                    </span>
                `;

                const forecastsEl = document.createElement('div');
                forecastsEl.classList.add('forecasts');
                forecastsEl.appendChild(symbolSpanEl);
                forecastsEl.appendChild(anotherSpanEl);

                currentEl.appendChild(forecastsEl);

                const forecastInfoEl = document.createElement('div');
                forecastInfoEl.classList.add('forecast-info');

                upcoming.forecast.forEach(f => createForecastElement(f, forecastInfoEl));

                upcomingEl.appendChild(forecastInfoEl);
            })
            .catch(err => {
                forecastEl.style.display = 'block';
                currentEl.textContent = 'Error';
                upcomingEl.style.display = 'none';
            });
    })
}

attachEvents();
