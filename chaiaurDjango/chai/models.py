from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ChaiVariety(BaseModel):
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELACHI')
    ]
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='chais/')
    type = models.CharField(choices=CHAI_TYPE_CHOICE)
    description = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name

class ChaiReview(BaseModel):
    REVIEW_RATINGS = [(1,1), (2,2), (3,3), (4,4), (5,5)]

    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=REVIEW_RATINGS)
    comment = models.CharField()

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'


class Store(BaseModel):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVariety, related_name='stores')

    def __str__(self):
        return self.name

class ChaiCertificate(BaseModel):
    chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.IntegerField()
    valid_untill = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.chai.name}'
    
