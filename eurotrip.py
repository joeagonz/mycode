#!/usr/bin/env python3

import random

# dictionary of European countries and their capitals
european_capitals = {
    "Albania": "Tirana",
    "Andorra": "Andorra la Vella",
    "Austria": "Vienna",
    "Belarus": "Minsk",
    "Belgium": "Brussels",
    "Bosnia and Herzegovina": "Sarajevo",
    "Bulgaria": "Sofia",
    "Croatia": "Zagreb",
    "Cyprus": "Nicosia",
    "Czech Republic": "Prague",
    "Denmark": "Copenhagen",
    "Estonia": "Tallinn",
    "Finland": "Helsinki",
    "France": "Paris",
    "Germany": "Berlin",
    "Greece": "Athens",
    "Hungary": "Budapest",
    "Iceland": "Reykjavik",
    "Ireland": "Dublin",
    "Italy": "Rome",
    "Kosovo": "Pristina",
    "Latvia": "Riga",
    "Liechtenstein": "Vaduz",
    "Lithuania": "Vilnius",
    "Luxembourg": "Luxembourg",
    "Malta": "Valletta",
    "Moldova": "Chisinau",
    "Monaco": "Monaco",
    "Montenegro": "Podgorica",
    "Netherlands": "Amsterdam",
    "North Macedonia": "Skopje",
    "Norway": "Oslo",
    "Poland": "Warsaw",
    "Portugal": "Lisbon",
    "Romania": "Bucharest",
    "Russia": "Moscow",
    "San Marino": "San Marino",
    "Serbia": "Belgrade",
    "Slovakia": "Bratislava",
    "Slovenia": "Ljubljana",
    "Spain": "Madrid",
    "Sweden": "Stockholm",
    "Switzerland": "Bern",
    "Ukraine": "Kyiv",
    "United Kingdom": "London",
    "Vatican City": "Vatican City"
}

# randomize the order of the countries
countries = list(european_capitals.keys())
random.shuffle(countries)

# initialize counters for correct and incorrect responses
correct = 0
incorrect = 0

# loop to ask the user to guess the capital of each European country in random order
while len(countries) > 0:
    country = random.choice(countries)
    capital = european_capitals[country]
    guess = input("What is the capital of " + country + "? ")
    while guess.lower() != capital.lower():
        try:
            raise ValueError("That's not a European capital. Try again.")
        except ValueError as error:
            print(error)
            guess = input("What is the capital of " + country + "? ")
        # increment the incorrect counter if the user's guess is incorrect
        incorrect += 1
    # increment the correct counter if the user's guess is correct
    correct += 1
    print("Correct!")
    # remove the country from the list of countries so it's not asked again
    countries.remove(country)

# print the final results
print("You guessed the capitals of " + str(correct) + " European countries correctly!")
print("You guessed the capitals of " + str(incorrect) + " European countries incorrectly. Better luck next time!")
