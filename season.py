import sys
import inflect
from datetime import date

p = inflect.engine()

    
class Duration():
    def __init__(self, DOB):
        self.DOB = DOB
        self.Date = date.today()   

     
    @classmethod
    def DOB_Date(cls, DOB):
        try: return cls(date.fromisoformat(DOB))
        except ValueError: sys.exit("Invalid date") # Invalid format


    def Cal_duration_min(self):
        today_date = self.Date
        duration_second = (today_date - self.DOB).total_seconds() # Operator overload
        total_min = round(duration_second / 60) #Round to nearest integer

        return total_min 


    def __str__(self):
        duration_min = self.Cal_duration_min()
        duration_text = p.number_to_words(duration_min)

        return duration_text


def main():

    print(Duration.DOB_Date("2006-06-09"))
    

if __name__ == "__main__":
    main()