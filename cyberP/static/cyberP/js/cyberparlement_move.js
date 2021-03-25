import {getCookie} from './modules/cookies.js'

let submit = document.getElementById("cp-move-submit")
if(submit != null) {
    submit.addEventListener('click', function () {
    /*
    fonction appelé lorsque la confirmation du déplacement est cliqué
    appelant la fonction envoyant l'id du cyberparlement en POST
     */
        submitCyberparlementSelected(cyberparlementID)
    })
}

function submitCyberparlementSelected(cyberparlementSelectedID) {
    /*
    fonction envoyant l'id du cyberparlement à déplacer en POST
    et charge la page de la liste des cyberparlements
     */
    location.replace('http://127.0.0.1:8000/cyberparlements/')
    fetch(location.href, {
        method: 'POST',
        body: JSON.stringify({
            cyberparlement_selected_id: cyberparlementSelectedID
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