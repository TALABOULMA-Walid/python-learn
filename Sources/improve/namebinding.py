import datetime
import imp
#datetime.datetime.now()
#datetime.datetime(2013, 02, 14, 02, 53, 59, 608842)
class PartyTime():
    def __init__(self):
        print("initcustom")
        return super().__init__()

    def __call__(self, *args):
        imp.reload(datetime)
        value = datetime.datetime(*args)
        datetime.datetime = self
        return value
     
    def __getattr__(self, value):
        if value == 'now':
            return lambda: print('Party Time!')
        else:
            imp.reload(datetime)
            value = getattr(datetime.datetime, value)
            datetime.datetime = self
            return value
    
q = PartyTime()
datetime.datetime.now() 
qq = PartyTime
qq.vv = 'hello'
today = datetime.datetime(2013, 2, 14)
print(today)