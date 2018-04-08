class Singleton(object):
    dictionary = None

    __instance = None

    def __init__(self):
        print 1
        if(Singleton.__instance is not None):
            print 2
            raise Exception("An instance already exists")
        else:
            print 3
            Singleton.__instance = self
            self.dictionary = 1

    @staticmethod
    def getInstance():
        print 4
        if (Singleton.__instance == None):
            print 5
            Singleton()

        return Singleton.__instance



s = Singleton.getInstance()
print s, s.dictionary

s2 = Singleton.getInstance()
print s2, s2.dictionary

s3 = Singleton()
