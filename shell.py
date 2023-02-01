import BxPP
import os
from CurrentVersion import *

def update():
  os.system('python3 updater.py')
    
def checker():
  url = VersionKey
  r = requests.get(url, allow_redirects=True)
  with open('CurrentVersion.py', 'wb') as f:
    f.write(r.content)
    f.close()
  if Key == version:
    print("Up To Date !")
  else:
    os.system('python3 update.py')

while True:
	text = input('BxPP > ')
	if text.strip() == "": continue
	result, error = basic.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))
