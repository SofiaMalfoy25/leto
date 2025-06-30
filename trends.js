document.addEventListener('DOMContentLoaded', function() {
    // Инициализация графиков
    initCharts();
    
    // Обработка фильтров
    document.getElementById('apply-trend-filters').addEventListener('click', function() {
        updateCharts();
    });
});

function initCharts() {
    // График популярных регионов
    const regionsCtx = document.getElementById('popularRegionsChart').getContext('2d');
    const regionsChart = new Chart(regionsCtx, {
        type: 'bar',
        data: {
            labels: ['Карелия', 'Байкал', 'Камчатка', 'Золотое кольцо', 'Сочи', 'Алтай'],
            datasets: [{
                label: 'Количество туристов',
                data: [1250, 980, 870, 760, 680, 520],
                backgroundColor: [
                    'rgba(42, 95, 143, 0.7)',
                    'rgba(58, 127, 191, 0.7)',
                    'rgba(74, 159, 239, 0.7)',
                    'rgba(231, 76, 60, 0.7)',
                    'rgba(243, 156, 18, 0.7)',
                    'rgba(46, 204, 113, 0.7)'
                ],
                borderColor: [
                    'rgba(42, 95, 143, 1)',
                    'rgba(58, 127, 191, 1)',
                    'rgba(74, 159, 239, 1)',
                    'rgba(231, 76, 60, 1)',
                    'rgba(243, 156, 18, 1)',
                    'rgba(46, 204, 113, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // График сезонности
    const seasonalityCtx = document.getElementById('seasonalityChart').getContext('2d');
    const seasonalityChart = new Chart(seasonalityCtx, {
        type: 'line',
        data: {
            labels: ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек'],
            datasets: [{
                label: 'Активность туристов',
                data: [15, 20, 35, 55, 80, 95, 100, 98, 75, 50, 30, 20],
                fill: true,
                backgroundColor: 'rgba(42, 95, 143, 0.1)',
                borderColor: 'rgba(42, 95, 143, 1)',
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            }
        }
    });

    // График бюджетов
    const budgetCtx = document.getElementById('budgetChart').getContext('2d');
    const budgetChart = new Chart(budgetCtx, {
        type: 'doughnut',
        data: {
            labels: ['До 20 тыс.', '20-50 тыс.', '50-100 тыс.', 'Более 100 тыс.'],
            datasets: [{
                data: [25, 45, 20, 10],
                backgroundColor: [
                    'rgba(42, 95, 143, 0.7)',
                    'rgba(58, 127, 191, 0.7)',
                    'rgba(74, 159, 239, 0.7)',
                    'rgba(231, 76, 60, 0.7)'
                ],
                borderWidth: 0
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom'
                }
            }
        }
    });

    // График типов путешественников
    const travelersCtx = document.getElementById('travelerTypesChart').getContext('2d');
    const travelersChart = new Chart(travelersCtx, {
        type: 'pie',
        data: {
            labels: ['Семьи', 'Пары', 'Соло', 'Друзья'],
            datasets: [{
                data: [40, 30, 15, 15],
                backgroundColor: [
                    'rgba(42, 95, 143, 0.7)',
                    'rgba(231, 76, 60, 0.7)',
                    'rgba(243, 156, 18, 0.7)',
                    'rgba(46, 204, 113, 0.7)'
                ],
                borderWidth: 0
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom'
                }
            }
        }
    });

    // Сохраняем ссылки на графики для обновления
    window.trendCharts = {
        regions: regionsChart,
        seasonality: seasonalityChart,
        budget: budgetChart,
        travelers: travelersChart
    };
}

function updateCharts() {
    const period = document.getElementById('time-period').value;
    const travelerType = document.getElementById('traveler-type').value;
    
    // Здесь должен быть реальный запрос к API с фильтрами
    // Для демо просто обновим данные случайным образом
    
    // Обновляем график популярных регионов
    const newRegionsData = Array(6).fill().map(() => Math.floor(Math.random() * 500) + 500);
    window.trendCharts.regions.data.datasets[0].data = newRegionsData;
    window.trendCharts.regions.update();
    
    // Обновляем график сезонности
    const newSeasonData = Array(12).fill().map(() => Math.floor(Math.random() * 50) + 50);
    window.trendCharts.seasonality.data.datasets[0].data = newSeasonData;
    window.trendCharts.seasonality.update();
    
    // Показываем загрузку
    document.getElementById('apply-trend-filters').textContent = 'Загрузка...';
    setTimeout(() => {
        document.getElementById('apply-trend-filters').textContent = 'Применить';
    }, 800);
}