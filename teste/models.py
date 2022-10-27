from django.db import models


class Animal(models.Model):
    Nome = models . CharField ( max_length =50)
    Raça = models . CharField ( max_length =50)
    Porte= models . CharField ( max_length =50)
    Idade_Aproximada = models . IntegerField ()
    Cor_do_Pelo = models . CharField ( max_length =50)
    Observações = models . CharField ( max_length =300)

class func(models.Model):
    Usuário = models . CharField ( max_length =50)
    Senha = models . CharField ( max_length = 20)
