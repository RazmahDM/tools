var categorySwiper = new Swiper(".category__carousel", {
  slidesPerView: 6,
  spaceBetween: 10,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});

var imgSwiper = new Swiper(".img__carousel", {
  pagination: {
    el: ".swiper-pagination",
    type: "progressbar",
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});

// var newToolSwiper = new Swiper(".newtools__carousel", {
//   slidesPerView: 4,
//   spaceBetween: 30,
//   navigation: {
//     nextEl: ".swiper-button-next",
//     prevEl: ".swiper-button-prev",
//   },
// });

// var promotionSwiper = new Swiper(".promotion__carousel", {
//   slidesPerView: 4,
//   spaceBetween: 30,
//   navigation: {
//     nextEl: ".swiper-button-next",
//     prevEl: ".swiper-button-prev",
//   },
// });





let products = document.querySelector('.products')
let summ = document.querySelector('.summ')
let total = 0

if (products) {
  

  let product_list = document.querySelectorAll('.product')

  product_list.forEach(item => {
    let pr = item.querySelector('.cena')
    let str = ''
    str = pr.innerHTML.slice(0, -3)
    console.log(pr.innerHTML)

    total += +str
  })

  summ.innerHTML = total

}