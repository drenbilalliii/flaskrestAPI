import string
import random


#helperss
def generateUniqueID(chars=string.ascii_lowercase + string.digits,madhesia = 12):
      return ''.join(random.choice(chars) for _ in range(madhesia))