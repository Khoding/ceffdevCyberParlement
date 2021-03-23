import {docReady} from './modules/docready.js'
import {getCookie} from './modules/cookies.js'

docReady(function () {
    let personSelectedID = null
    if (document.getElementById('cyberchancelier') != null) {
        document.getElementById('cyberchancelier').addEventListener('change', function () {
            personSelectedID = this.value
        })
    }

    if (document.getElementById('submit-cyberchancelier') != null) {
        document.getElementById('submit-cyberchancelier').addEventListener('click', function () {
            submitCyberchancelier(personSelectedID)
        })
    }

    function submitCyberchancelier(personSelectedID) {
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
})