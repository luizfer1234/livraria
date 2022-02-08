
from django.contrib.auth.models import User
from django.db import models

class Consumidor(models.Model):
	usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	nome = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.nome

class Livro(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.FloatField()
    digital = models.BooleanField(default=False,null=True, blank=True)
    imagem = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.nome
    
    @property
    def URLimagem(self):
        try:
            url = self.imagem.url
        except:
            url = ''
        return url





class Ordem(models.Model):
	consumidor = models.ForeignKey(Consumidor, on_delete=models.SET_NULL, null=True, blank=True)
	data_ordem = models.DateTimeField(auto_now_add=True)
	completada = models.BooleanField(default=False)
	id_transacao = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

class Enderecoenvio(models.Model):
	consumidor = models.ForeignKey(Consumidor, on_delete=models.SET_NULL, null=True)
	ordem = models.ForeignKey(Ordem, on_delete=models.SET_NULL, null=True)
	endereco = models.CharField(max_length=200, null=False)
	cidade = models.CharField(max_length=200, null=False)
	estado = models.CharField(max_length=200, null=False)
	cep = models.CharField(max_length=200, null=False)
	data_adicionado = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.endereco

class ItemOrdem(models.Model):
	produto = models.ForeignKey(Livro, on_delete=models.SET_NULL, null=True)
	ordem = models.ForeignKey(Ordem, on_delete=models.SET_NULL, null=True)
	quantidade = models.IntegerField(default=0, null=True, blank=True)
	data_adicionado = models.DateTimeField(auto_now_add=True)