

class Sports:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


sports_list = [
    Sports('baseball'),
    Sports('soccer'),
]

def sports_start(sports_list: list):
    for sports in sports_list:
        if sports.name == 'baseball':
            print('Play ball!!')

        elif sports.name == 'soccer':
            print('Kick off!!')

sports_start(sports_list)


"""
バスケットボールを追加するときどうする？
バスケットポールの開始は、ティップオフ(tip off)です。
"""