

class Sports:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def start():
        pass

class Baseball(Sports):

    def start(self):
        print('Play ball!!')

class Soccer(Sports):

    def start(self):
        print('Kick off!!')

class Basketball(Sports):

    def start(self):
        print('Tip off!!')

sports_list = [
    Baseball('baseball'),
    Soccer('soccer'),
    Basketball('basketball'),
]

def sports_start(sports_list: list):
    for sports in sports_list:
        sports.start()

sports_start(sports_list)


"""
バスケットボールを追加するときどうする？
バスケットポールの開始は、ティップオフ(tip off)です。
"""