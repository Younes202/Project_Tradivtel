from django.db import models


class users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class Specialite(models.Model):
    class Meta:
        db_table = 'specialite'

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Equipe(models.Model):
    class Meta:
        db_table = 'equipe'

    name = models.CharField(max_length=255)
    technicians = models.ManyToManyField('Technician', related_name='equipes', blank=True)

    def __str__(self):
        return self.name


class Technician(models.Model):
    class Meta:
        db_table = 'technician'

    fullname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    specialite = models.ForeignKey(Specialite, on_delete=models.CASCADE)
    equipe = models.OneToOneField(Equipe, on_delete=models.CASCADE, related_name='team_member', null=True, blank=True)

    def __str__(self):
        return self.fullname


