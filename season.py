import sys
import inflect
from datetime import date

p = inflect.engine()


def main():
    print(Duration.Birthday())
    
class Duration():
    def __init__(self, DOB):
        self.DOB = DOB
        self.Date = date.today()

    @classmethod
    def Birthday(cls):
        try:
            return cls(date.fromisoformat(input("Date of Birth: ")))
    
        except ValueError: # Invalid format
            sys.exit("Invalid date")

    
    def Cal_duration_min(self):
        
        today_date = self.Date
        duration_second = (today_date - self.DOB).total_seconds() # Operator overload
        total_min = round(duration_second / 60) #Round to nearest integer
       # print(total_min,"Working")
        return total_min 


    def __str__(self):
        duration_min = self.Cal_duration_min()
        duration_text = p.number_to_words(duration_min)

        return duration_text


if __name__ == "__main__":
    main()