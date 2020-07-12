from bs4 import BeautifulSoup
import requests
import random
import time

welcome= input("Welcome to Guess Who Said That! You start with 4 guesses. Let's play! Hit enter to continue.")

url= "http://quotes.toscrape.com"
base_page= "/page/1/"


while base_page: 
	website= requests.get(f"{url}{base_page}")
	soup= BeautifulSoup(website.text, "html.parser")
	quotes= soup.find_all(class_= "quote")
	#Create an empty list
	quote_bank= []

	for q in quotes:
		quote_bank.append({
			"quote": q.find(class_="text").get_text(),
			"author": q.find(class_="author").get_text(),
			"about": q.find("a")["href"]
		})

# #Next button needs to be iterated over
	nextbutton= soup.find(class_="next")
# 		#continue to look for base page if there's a next button on the web page, if not then return None
	print("Scraping a quote for you. Please wait...")
	base_page= nextbutton.find("a")["href"] if nextbutton else None
	time.sleep(0.5)


play_again = str('Y').lower()
while play_again == 'y':
	quote_pick= random.choice(quote_bank)
	thechosenquotetext = quote_pick["quote"]
	print(f"Who said this? {thechosenquotetext}")
	
	player_guess= input()
	guesses = 4

	#Use .lower or .upper because of case sensitivity in Python. This makes answers consistent
	while player_guess.lower() != quote_pick["author"].lower():
		author_link = quote_pick["about"]
		author_hyperlink = requests.get(f"{url}{author_link}")
		soup= BeautifulSoup(author_hyperlink.text, "html.parser")
		
		if True and guesses == 4: 
			guesses -= 1
			print(f"Try again! Remaining guesses: {guesses}")
			hint1 = soup.find(class_= "author-born-location").get_text()
			print(f"Here's a hint: The author was born {hint1}")
			player_guess = input()

		elif True and guesses == 3:
			guesses -= 1
			print(f"Try again! Remaining guesses: {guesses}")
			hint2 = soup.find(class_= "author-born-date").get_text()
			print(f"Here's another hint: The author was born on {hint2}")
			player_guess = input()

		elif True and guesses == 2:
			guesses -= 1
			print(f"Try again! Remaining guesses: {guesses}")
			hint3= quote_pick["author"][0]
			print(f"Here's your last hint: The first letter of the author's first name is {hint3}")
			player_guess = input()

		elif True and guesses == 1:
			answer = quote_pick["author"]
			print(f"You ran out of guesses! The answer was {answer}.")
			play_again= input("Do you want to play again? Y or N?")
			break

	if player_guess.lower() == quote_pick["author"].lower():
		print("You got it!")
		play_again= input("Do you want to play again? Y or N?")

if play_again == str('N').lower():
	print ("See you next time!")

	 




