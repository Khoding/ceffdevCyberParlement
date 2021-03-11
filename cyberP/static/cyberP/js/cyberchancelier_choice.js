import {docReady} from './modules/docready.js'
import {getCookie} from './modules/cookies.js'

docReady(function () {
        let person_selected_id = null
        if (document.getElementById('cyberchancelier') != null) {
            document.getElementById('cyberchancelier').addEventListener('change', function () {
                person_selected_id = this.value
            })
        }

        if (document.getElementById('submit-cyberchancelier') != null) {
            document.getElementById('submit-cyberchancelier').addEventListener('click', function () {
                submitCyberchancelier(person_selected_id)
            })
        }

        function submitCyberchancelier(person_selected_id) {
            fetch(location.href, {
                method: 'POST',
                body: JSON.stringify({
                    person_selected_id: person_selected_id
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
    }
)
