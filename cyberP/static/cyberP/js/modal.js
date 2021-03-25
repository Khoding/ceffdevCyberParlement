let modalBtn = document.querySelector('.modal-btn'),
    modalBg = document.querySelector('.modal-bg'),
    modalClose = document.querySelector('.modal-close'),
    modalSave = document.querySelector('.modal-save')


modalBtn.addEventListener('click', function () {
    /*
    fonction pemettant d'afficher la modal lors que
    l'on clique sur le bouton d'affichage de la modal
     */
    modalBg.classList.add('bg-active')
})

modalClose.addEventListener('click', function () {
    /*
    fonction pemettant de cacher la modal lorsque
    l'on clique sur le bouton d'annulation
     */
    modalBg.classList.remove('bg-active')
})

modalSave.addEventListener('click', function () {
    /*
    fonction pemettant de cacher la modal lorsque
    l'on clique sur le bouton d'enregistrement
     */
    modalBg.classList.remove('bg-active')
})