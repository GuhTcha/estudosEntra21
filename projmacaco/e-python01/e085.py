#e085.py
'85. Crie um programa que exibe a versão atual do Python instalada em seu sistema: (import sys)'
import sys
w = (sys.version)
x = (sys.version_info)
y = (sys.base_prefix)
z = (sys.getwindowsversion())
print(f'version: {w}\nVersion_info: {x}\nBase_prefix: {y}\ngetwindowsversion: {z}')