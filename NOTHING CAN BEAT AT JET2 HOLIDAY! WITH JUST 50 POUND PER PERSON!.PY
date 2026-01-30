class Student:
    name="Long"
    scores={
        "Math":80,
        "English":80,
        "Science":85,
        "HistoryandGeography":100,
        "CitizenTeaching": 95,
    }
    rank="First"
    def scores_average(self):
        avg = (self.scores["Math"] + self.scores["English"] + self.scores["Science"] + self.scores["HistoryandGeography"] + self.scores["CitizenTeaching"])/5
        return avg
    def show_info(self):
        print(f"Name: {self.name}")
        for subject, score in self.scores.items():
            print(f"{subject}: {score}")
        print(f"Average Score: {self.scores_average()}")
    def show_rank(self):
        if self.scores_average >= 90:
            self.rank = "First"
        elif self.scores_average >= 80:
            self.rank = "Second"
        elif self.scores_average >= 70:
            self.rank = "Third"
        else:
            self.rank = "Fail"
        return self.rank
    print(f"Rank: {self.show_rank()}")
    
Long=Student()
Long.show_info()

