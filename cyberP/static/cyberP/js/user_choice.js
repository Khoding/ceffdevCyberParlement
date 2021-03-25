import {getCookie} from './modules/cookies.js'

let personSelectedID = null,
    user = document.getElementById('user'),
    userSubmit = document.getElementById('submit-user')

if (user != null) {
    user.addEventListener('change', function () {
        /*
        fonction remplissant une variable avec l'id de la personne sélectionnée
        et affichage du bouton d'enregistrement lorsque une personne est choisi
         */
        personSelectedID = this.value
        userSubmit.classList.remove('hidden')
    })
}

if (userSubmit != null) {
    userSubmit.addEventListener('click', function () {
        /*
        fonction appelant la fonction d'envoie de l'id de la personne
        en POST lorsque le bouton d'enregistrement est cliqué
         */
        submitUser(personSelectedID)
    })
}

function submitUser(personSelectedID) {
    /*
    fonction envoyant en POST l'id de la personne sélectionné
    et charge la page de la liste des cyberparlements
     */
    location.replace('http://127.0.0.1:8000/cyberparlements/')
    fetch(location.href, {
        method: 'POST',
        body: JSON.stringify({
            person_selected_id: personSelectedID
        }),
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json'
        }
    }).then(function (response) {
        if (response.ok) {
            return response.json()
        }
    })
}