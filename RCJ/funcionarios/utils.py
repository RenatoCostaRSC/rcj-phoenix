from .models import Gestor


def salva_gestor(nome, cargo):
    
    if cargo == 'SUPERVISOR':
        print('meu cargo é supervisor')
        gestor = Gestor(nome = nome)
        gestor.save()
