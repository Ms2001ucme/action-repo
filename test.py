import random
import datetime

quotes = [
    "Believe in yourself and all that you are.",
    "The only way to do great work is to love what you do.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Your limitation—it’s only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Don’t watch the clock; do what it does. Keep going."
]

def get_quote_of_the_day():
    random.seed(datetime.date.today().toordinal())  # Ensure the quote changes daily
    return random.choice(quotes)

if __name__ == "__main__":
    print("✨ Quote of the Day ✨")
    print(get_quote_of_the_day())
