#MadLib.py
#Name: Grant Schaeffer
#Date: 8/31/25
#Assignment: Lab 1

def main():
  print("Madlib")
  #Ask user for words
  location1 = input("Enter a location: ")
  verb1 = input("Enter a verb: ")
  noun1 = input("Enter a noun: ")
  color1 = input("Enter a color: ")
  clothing1 = input("Enter an article of clothing: ")
  food1= input("Enter a food: ")
  verb2 = input("Enter a verb: ")

  #Print the story with the user supplied words.
  print("This summer, I visited "+ location1 + ".")
  print("It was amazing! While I was there, I learned how to " + verb1 + ".")
  print("During a walk around the town I was in, I saw a poster for a " + noun1 + " museum. So I decided to pay it a visit.")
  print("When I got to the museum, I learned that the main display was of a " + color1 + noun1 + ".")
  print("After the museum, I visted a market where I bought, a " + clothing1 + " and a " + food1 + ".")
  print("I really enjoyed my time in " + location1 + ".")
  print("My favorite part of the trip was " + verb2 + "ing with the locals!")

#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
