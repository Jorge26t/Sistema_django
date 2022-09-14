from config.wsgi import *

#importo el modelo typo
from erp.models import Type

llamar = Type.objects.all()
print(llamar)
print("aa")


