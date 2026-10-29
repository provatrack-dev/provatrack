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

        

class Prova(models.Model):
    class Modalidade(models.TextChoices):
        CICLISMO = 'ciclismo', 'Ciclismo'
        ATLETISMO = 'atletismo', 'Atletismo'

    class Status(models.TextChoices):
        ABERTA = 'aberta', 'Aberta'
        ANDAMENTO = 'andamento', 'Em andamento'
        ENCERRADA = 'encerrada', 'Encerrada'

    nome = models.CharField(max_length=150)
    modalidade = models.CharField(max_length=10, choices=Modalidade.choices)
    data = models.DateField()
    local = models.CharField(max_length=150)
    distancia_km = models.DecimalField('distância (km)', max_digits=6, decimal_places=2)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ABERTA)
    descricao = models.TextField('descrição', blank=True)

    class Meta:
        ordering = ['-data']

    def __str__(self):
        return self.nome


class Resultado(models.Model):
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE, related_name='resultados')
    prova = models.ForeignKey(Prova, on_delete=models.CASCADE, related_name='resultados')
    posicao = models.PositiveIntegerField('posição')
    tempo = models.DurationField()
    pontos = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['prova', 'posicao']
        constraints = [
            # Um atleta só pode ter um resultado por prova.
            models.UniqueConstraint(fields=['atleta', 'prova'], name='resultado_unico_por_atleta_e_prova'),
        ]

    def __str__(self):
        return f'{self.atleta} em {self.prova}: {self.posicao}º lugar'