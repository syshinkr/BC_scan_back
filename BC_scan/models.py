from django.db import models
import uuid

class BusinessCard(models.Model):
    """
    id: uuid [PK]
    user: user who added this business card
    name: Owner's name
    mobile_tell: Owner's Mobile phone number
    email: Owner's email [nullable]
    fax: Owner's fax [nullable]
    company: company
    company_address: company address [nullable]
    company_tell: Company's Representative call number [nullable]
    com_extension_tell: Owner's call number In company [nullable]
    created_at: Automatically set the field to now(datetime) when the object is first created
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='id for PK to this Business Card')
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    name = models.CharField(max_length=8, help_text='name')
    mobile_tell = models.CharField(max_length=20, help_text='mobile tell')
    email = models.EmailField(max_length=50, help_text='email', null=True)
    fax = models.CharField(max_length=20, help_text='fax', null=True)
    company = models.CharField(max_length=20, help_text='company')
    company_address = models.CharField(max_length=100, help_text='company address', null=True)
    company_tell = models.CharField(max_length=20, help_text='company tell', null=True)
    com_extension_tell = models.CharField(max_length=20, help_text='company extension tell', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Metadata
    class Meta:
        ordering = ['name']

    # def get_absolute_url(self):
    #     """Returns the url to access a particular instance of MyModelName."""
    #     return reverse('bc-detail-view', args=[str(self.id)]) 

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return f"{self.name} {self.company} {self.mobile_tell}"


class User(models.Model):
    """
    id: id [PK]
    email: user email [UK]
    name: user name
    access_token: access token to access to social (Only Google)
    refresh_token: refresh token to get new access token
    created_at: Automatically set the field to now(date) when the object is first created
    
    If user don't have a id, email will be PK. 
    But, email is too long to use as PK.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID for PK to user')
    email = models.EmailField(max_length=50, help_text='email', unique=True)
    name = models.CharField(max_length=8, help_text="user name")
    access_token = models.CharField(primary_key=True, help_text='access token to access to social')
    refresh_token = models.CharField(help_text='refresh token to get new access token', null=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['email']

    # def get_absolute_url(self):
    #     return reverse('user-detail-view', args=[str(self.id)])

    def __str__(self):
        return f"{self.name} {self.email}"

