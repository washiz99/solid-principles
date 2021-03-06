# SRPに準拠した例

class User:
    """
    ユーザ情報を保持するという役割
    """

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def __str__(self):
        return "{}, {}, {}".format(
            self.name, self.age, self.address
        )


class Company:
    """
    会社情報を保持するという役割
    """
    
    def __init__(self, name, since, address):
        self.name = name
        self.since = since
        self.address = address

    def __str__(self):
        return "{}, {}, {}".format(
            self.name, self.since, self.address
        )


class FileManager:

    @staticmethod
    def write_to_file(obj, filename):
        with open(filename, mode='w') as fh:
            fh.write(str(obj))


user = User('Taro', 30, 'Osaka')
print(str(user))
FileManager.write_to_file(user, 'srp_good.txt')
