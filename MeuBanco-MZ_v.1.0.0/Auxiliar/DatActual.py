from datetime import datetime

def datactual():

    now = datetime.now()

    dia = now.strftime('%d%m%y')
    hora = now.strftime('%H%M%S')

    return dia, hora