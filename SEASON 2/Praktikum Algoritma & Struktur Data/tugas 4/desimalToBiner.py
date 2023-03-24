class desimalToBiner:
    def __init__(self, desimal):
        self.desimal = desimal
        self.arrayBiner = []
        self.explanation = []

    def convert(self):
        temp = self.desimal
        prev_temp = self.desimal
        if self.desimal == 0:
            self.arrayBiner.append(0)
        if self.desimal == 1 or self.desimal == 0:
            self.explanation.append("Desimal 1 dan 0 tidak perlu dikonvesi")
        while temp > 0:
            self.arrayBiner.insert(0, temp % 2)
            temp = temp // 2
            if temp >= 1:
                remainder = prev_temp % 2
                self.explanation.append(f"{prev_temp} / 2 = {temp}, sisa {remainder}")
            prev_temp = temp

        while len(self.arrayBiner) % 4 != 0:
            self.arrayBiner.insert(0, 0)
        return self.arrayBiner

    def get_explanation(self):
        for step in self.explanation:
            print(step)    