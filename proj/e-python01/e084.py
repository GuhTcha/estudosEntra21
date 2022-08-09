#e084.py
from datetime import datetime
import time

def tempo():
    for contagem in range(10):
        agora = datetime.now()
        print(agora)
        time.sleep(1)

x = tempo()