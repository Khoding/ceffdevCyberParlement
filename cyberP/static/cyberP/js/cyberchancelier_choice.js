import {getCookie} from './modules/cookies.js'

let personSelectedID = null,
    cyberchancelier = document.getElementById('cyberchancelier'),
    cyberchancelierSubmit = document.getElementById('submit-cyberchancelier')

if (cyberchancelier != null) {
    cyberchancelier.addEventListener('change', function () {
        /*
        fonction remplissant une variable avec l'id de la personne sélectionnée
        et affichage du bouton d'enregistrement lorsque une personne est choisi
        pour devenir cyberchancelier
         */
        personSelectedID = this.value
        cyberchancelierSubmit.classList.remove('hidden')
    })
}

if (cyberchancelierSubmit != null) {
    cyberchancelierSubmit.addEventListener('click', function () {
        /*
        fonction appelant la fonction d'envoie de l'id de la personne
        en POST lorsque le bouton d'enregistrement est cliqué
         */
        submitCyberchancelier(personSelectedID)
    })
}

function submitCyberchancelier(personSelectedID) {
    /*
    fonction envoyant en POST l'id de la personne sélectionné
    et charge la page de la liste des cyberparlements
     */
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