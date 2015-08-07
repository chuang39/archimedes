from boto import sns

from django.forms import ModelForm

from contact.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'company', 'phone', 'email', 'message',)

    def save(self, commit=True):
        contact = super(ContactForm, self).save(commit=commit)
        self.send_contact_email(contact)
        return contact

    def send_contact_email(self, contact):
        sns_conn = sns.connect_to_region(
            'us-west-2',
            aws_access_key_id='AKIAJXN4QBOQO6TR7T5Q',
            aws_secret_access_key='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'
        )

        msg = """
            Name: {name}
            Company: {company}
            Phone: {phone}
            Email: {email}
            Message: {message}
        """.format(
            name=contact.name,
            company=contact.company,
            phone=contact.phone,
            email=contact.email,
            message=contact.message
        )
        sns_conn.publish(
            u'arn:aws:sns:us-west-2:451326512542:ArchimedesCustomerContactTopic',
            msg,
            '[New Message] Archimedes Controls website received new message',
        )