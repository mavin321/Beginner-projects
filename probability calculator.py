import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents=[key for key, value in kwargs.items() for _ in range(value)]
        self.popped_items=[]

    def draw(self,num_of_balls_to_draw):

        if num_of_balls_to_draw >= len(self.contents):
            self.popped_items+=self.contents
            self.contents=[]
            return self.popped_items

        i=0
        while i < num_of_balls_to_draw:
            self.popped_items.append(self.contents.pop(random.randint(0, len(self.contents)-1)))
            i+=1
        return self.popped_items


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    i=0
    m=0
    while i < num_experiments:
        copied_hat = copy.deepcopy(hat)
        copied_hat.popped_items=[]
        copied_hat.draw(num_balls_drawn)
        counts={}
        for word in copied_hat.popped_items:
            counts[word] = counts.get(word, 0) + 1
        if all(counts.get(key, 0) >= value for key, value in expected_balls.items()):
            m+=1
        i+=1
    return m/num_experiments






hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, expected_balls={'red':2,'green':1}, num_balls_drawn=5,num_experiments=2000)
print(probability)
hat.draw(6)
hat.draw(20)
print(hat.contents)

