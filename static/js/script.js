// Dark mode toggle
const darkModeToggle = document.getElementById('darkModeToggle');
darkModeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    const isDark = document.body.classList.contains('dark-mode');
    localStorage.setItem('darkMode', isDark);
    darkModeToggle.textContent = isDark ? '☀️ Light Mode' : '🌙 Dark Mode';
});

// Load dark mode preference
if (localStorage.getItem('darkMode') === 'true') {
    document.body.classList.add('dark-mode');
    darkModeToggle.textContent = '☀️ Light Mode';
}

// Load pinned services from localStorage
function loadPinnedServices() {
    const pinned = JSON.parse(localStorage.getItem('pinnedServices') || '[]');
    pinned.forEach(serviceId => {
        const serviceItem = document.querySelector(`[data-service-id="${serviceId}"]`);
        if (serviceItem) {
            serviceItem.classList.add('pinned');
            const pinButton = serviceItem.querySelector('.pin-button');
            if (pinButton) {
                pinButton.classList.add('active');
            }
        }
    });
    sortServicesByPinned();
}

// Sort services so pinned ones appear first
function sortServicesByPinned() {
    document.querySelectorAll('.services-grid').forEach(grid => {
        const services = Array.from(grid.children);
        services.sort((a, b) => {
            const aPinned = a.classList.contains('pinned');
            const bPinned = b.classList.contains('pinned');
            return bPinned - aPinned;
        });
        services.forEach(service => grid.appendChild(service));
    });
}

// Toggle pin status
function togglePin(event, serviceId) {
    event.preventDefault();
    event.stopPropagation();

    const serviceItem = document.querySelector(`[data-service-id="${serviceId}"]`);
    const pinButton = event.target.closest('.pin-button');

    let pinned = JSON.parse(localStorage.getItem('pinnedServices') || '[]');

    if (pinned.includes(serviceId)) {
        pinned = pinned.filter(id => id !== serviceId);
        serviceItem.classList.remove('pinned');
        pinButton.classList.remove('active');
    } else {
        pinned.push(serviceId);
        serviceItem.classList.add('pinned');
        pinButton.classList.add('active');
    }

    localStorage.setItem('pinnedServices', JSON.stringify(pinned));
    sortServicesByPinned();
}

// Search and filter logic
document.addEventListener('DOMContentLoaded', function() {
    const search = document.getElementById('search');
    const envRadios = document.querySelectorAll('input[name="env"]');

    function filterServices() {
        const query = search.value.toLowerCase();
        const selectedEnv = document.querySelector('input[name="env"]:checked').value;

        document.querySelectorAll('.env-section').forEach(section => {
            const envName = section.getAttribute('data-env');
            const isSelectedEnv = selectedEnv === 'all' || envName === selectedEnv;
            section.style.display = isSelectedEnv ? 'block' : 'none';

            if (isSelectedEnv) {
                const services = section.querySelectorAll('.service-item');
                services.forEach(service => {
                    const name = service.querySelector('.service-name').textContent.toLowerCase();
                    const url = service.querySelector('.service-url').textContent.toLowerCase();
                    const matches = name.includes(query) || url.includes(query);
                    service.style.display = matches ? 'flex' : 'none';
                });
            }
        });
    }

    // Event listeners
    search.addEventListener('input', filterServices);
    envRadios.forEach(radio => radio.addEventListener('change', filterServices));

    // Load pinned services and filter
    loadPinnedServices();
    filterServices();
});