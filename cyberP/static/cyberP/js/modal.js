let modalBtn = document.querySelector('.modal-btn')
let modalBg = document.querySelector('.modal-bg')
let modalClose = document.querySelector('.modal-close')
let modalSave = document.querySelector('.modal-save')

modalBtn.addEventListener('click', function () {
    modalBg.classList.add('bg-active')
})

modalClose.addEventListener('click', function () {
    modalBg.classList.remove('bg-active')
})

modalSave.addEventListener('click', function () {
    modalBg.classList.remove('bg-active')
})