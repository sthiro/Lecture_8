import sys
import inflect
from datetime import date

p = inflect.engine()

def birthday_date():
    return date.fromisoformat(input("Date of Birth: ")) 

def duration():
    try:
        today_date = date.today()
        duration_second = (today_date - birthday_date()).total_seconds() # Operator overload
        total_min = round(duration_second / 60) #Round to nearest integer

        return duration_second 

    except ValueError: # Invalid format
        sys.exit("Invalid date")

def main():

    duration_min = duration()
    duration_text = p.number_to_words(duration_min)
    print(duration_text)


if __name__ == "__main__":
    main()