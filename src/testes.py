import jogovelha
import sys
erroInicializar = False
jogo = jogovelha.inicializar()
if len(jogo) != 3:
erroInicializar = False
else:
for linha in jogo:
if len(linha) != 3:
erroInicializar = False
else:
for elemento in linha:
if elemento != '.':
erroInicializar = False
if erroInicializar:
sys.exit(1)
else:
sys.exit(0)
