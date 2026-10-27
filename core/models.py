from django.db import models


class Equipe(models.Model):
    MODALIDADES = [
        ('ciclismo', 'Ciclismo'),
        ('atletismo', 'Atletismo'),
        ('ambas', 'Ambas'),
    ]

    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    uf = models.CharField('UF', max_length=2, blank=True)
    modalidade = models.CharField(max_length=10, choices=MODALIDADES, default='ambas')

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Atleta(models.Model):
    SEXOS = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    MODALIDADES = [
        ('ciclismo', 'Ciclismo'),
        ('atletismo', 'Atletismo'),
    ]

    nome = models.CharField(max_length=150)
    data_nascimento = models.DateField('data de nascimento', null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=SEXOS)
    cidade = models.CharField(max_length=100, blank=True)
    modalidade = models.CharField(max_length=10, choices=MODALIDADES)
    # Atleta avulso: sem equipe. Se a equipe for apagada, o atleta continua existindo.
    equipe = models.ForeignKey(
        Equipe,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='atletas',
    )

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome