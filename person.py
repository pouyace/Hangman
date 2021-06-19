class person:
    username = ""
    highscore = ""
    current_score = 0
    wrong_inputs = 0
    correct_inputs = 0
    def __init__(self,name,score):
        self.username = name
        self.highscore = score