// Инициализируем Swiper
new Swiper('.image-slider', {
    // Стрелки
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev'
    },
    // Текущее положение
    pagination: {
        el: '.swiper-pagination',
        // Фракция
        type: 'fraction',
        renderFraction: function (currentClass, totalClass) {
            return 'Изображение <span class="' 
                   + currentClass + '"></span>' 
                   + ' из ' + '<span class="' 
                   + totalClass + '"></span>'
        },
        
    },
    // Бесконечный слайдер
    loop: true,
});
