from django.template.loader import render_to_string
from django_q.tasks import async_task


def send_reset_password_email(cyberchancelier, member):
    template = render_to_string(template_name='cyberparlementProject/mail/poll_vote_validation.html',
                                context={
                                    'member': member
                                })

    async_task('django.core.mail.send_mail',
               subject='[Cyberparlement] Réinitialisation de votre mot de passe',
               message="template",
               html_message=template,
               from_email='no-reply@cyberparlement.ch',
               recipient_list=[member.email, cyberchancelier.email],
               )
