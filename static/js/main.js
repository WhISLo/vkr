// Анимация загрузки
document.addEventListener('DOMContentLoaded', function() {
  // Подсветка активного пункта меню
  const currentPath = window.location.pathname;
  document.querySelectorAll('.sidebar a').forEach(link => {
    if (link.getAttribute('href') === currentPath) {
      link.classList.add('active');
    }
  });

  // Динамическое обновление цены в форме заказа
  const quantityInputs = document.querySelectorAll('input[name="quantity"]');
  quantityInputs.forEach(input => {
    const pricePerItem = parseFloat(input.closest('form').querySelector('.price-per-item').textContent);
    const totalPriceElement = input.closest('form').querySelector('.total-price');
    
    input.addEventListener('input', function() {
      const total = pricePerItem * parseInt(this.value || 0);
      totalPriceElement.textContent = total.toFixed(2);
    });
  });

  // Плавная прокрутка
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      document.querySelector(this.getAttribute('href')).scrollIntoView({
        behavior: 'smooth'
      });
    });
  });

  // Уведомления
  setTimeout(() => {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
      alert.style.transition = 'opacity 0.5s';
      alert.style.opacity = '0';
      setTimeout(() => alert.remove(), 500);
    });
  }, 3000);
});

// Модальное окно
function openModal(modalId) {
  document.getElementById(modalId).style.display = 'block';
}

function closeModal(modalId) {
  document.getElementById(modalId).style.display = 'none';
}