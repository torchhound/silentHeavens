import requests
from bs4 import BeautifulSoup, SoupStrainer

flip = True

def starName():
	try:
		r = requests.get("https://donjon.bin.sh/scifi/name/#type=space;space=Star")
		response = r.content
		soup = BeautifulSoup(response, "lxml")
		name = soup.find("textarea", {"id": "list"})
		print(name)
		result = "".join([i for i in name if not i.isdigit()])
		return result
	except Exception as e:
		print(e)
		return False

def planetName():
	global flip
	try:
		if flip == True:
			responseSF = requests.get("http://www.scifiideas.com/planet-generator/")
			response = responseSF.content
			soup = BeautifulSoup(response, "lxml")

			flip = not flip
			return result
		else:
			responseDJ = requests.get("https://donjon.bin.sh/scifi/name/#type=space;space=SciFi%20World")
			response = responseDJ.content
			soup = BeautifulSoup(response, "lxml")

			result = "".join([i for i in name if not i.isdigit()])
			flip = not flip
			return result
	except Exception as e:
		print(e)
		return False

def starSystemName():
	try:
		r = requests.get("http://www.scifiideas.com/star-system-name-generator/")
		response = r.content
		soup = BeautifulSoup(response, "lxml")

	except Exception as e:
		print(e)
		return False

def main():
	print(starName())

if __name__ == "__main__":
	main()
