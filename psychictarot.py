import random
#Welcome Statement
print("Hi, welcome to your tarot card reading!")
print("Madame Lieselle Sparkelle will tell you about your past, present, and future.")
print("")

#Past Card Output
int_past = random.randint(1, 5)
past_card = ""
past_card_meaning = ""
#print(int_past)
if int_past == 1:
    past_card = "The World Card"
    past_card_meaning = "fulfillment, harmony, completion"
if int_past == 2:
    past_card = "The Queen of Wands Card"
    past_card_meaning = "courage, determination, joy"
if int_past == 3:
    past_card = "The Ace of Cups Card"
    past_card_meaning == "new feelings, spirituality, intuition"
if int_past == 4:
    past_card = "The Two of Swords Card"
    past_card_meaning = "difficult choices, indecision, stalemate"
if int_past == 5:
    past_card = "The Judgement Card"
    past_card_meaning= "reflection, reckoning, awakening"

print("First I will turn over the card that represents your past.") 
print("You got " + past_card)
print("Very interesting... this means that your past was shrouded in feelings of " + past_card_meaning + ".")
print("")

#Present Card Output
int_present = random.randint(1, 5)
#print(int_present)
present_card = ""
present_card_meaning = ""
if int_present == 1:
    present_card = "The Sun Card"
    present_card_meaning = "joy, success, celebration, positivity"
if int_present == 2:
    present_card = "The Queen of Cups Card"
    present_card_meaning = "compassion, calm, comfort"
if int_present == 3:
    present_card = "The Nine of Pentacles Card"
    present_card_meaning = "fruits of labor, rewards, luxury"
if int_present == 4:
    present_card = "The King of Swords Card"
    present_card_meaning = "head over heart, discipline, truth"
if int_present == 5:
    present_card = "The Moon Card"
    present_card_meaning= "unconscious, illusions, intuition"

print("Next I will turn over the card that represents your present.") 
print("You got " + present_card)
print("I see... this means that your present is marked by feelings of " + present_card_meaning + ".")
print("")

#Future Card Output
int_future = random.randint(1, 5)
#print(int_future)
future_card = ""
future_card_meaning = ""
if int_future == 1:
    future_card = "The Star Card"
    future_card_meaning = "hope, faith, rejuvenation"
if int_future == 2:
    future_card = "The King of Wands Card"
    future_card_meaning = "big picture, leadership, overcoming challenges"
if int_future == 3:
    future_card = "The Six of Wands Card"
    future_card_meaning = "victory, success, public reward"
if int_future == 4:
    future_card = "The Chariot Card"
    future_card_meaning = "direction, control, willpower"
if int_future == 5:    
    future_card = "The Tower Card"
    future_card_meaning= "sudden upheaval, broken pride, disaster"

print("Finally, I will turn over the card that represents your future.") 
print("You got " + future_card)
print("Oh wow, Madame Lieselle doesn't see this too often... this means that your future might be defined by feelings of " + future_card_meaning + ".")
print("")

print("But, always remember, the future is not set in stone. It is yours to create.")
print("Madame Lieselle Sparkelle wishes you a beautiful future... enjoy!")
