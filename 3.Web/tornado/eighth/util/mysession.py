from uuid import uuid4

from eighth.util.myutil import myuuid

s={}

class Session:
    def __init__(self,handler):
       self.handler = handler

    def __getitem__(self, key):
        #找到＇凭证＇的值
        c = self.handler.get_cookie('uid')
        if c:
            d = s.get(c,None)
            if d:
                return d.get(key,None)
            else:
                return None
        else:
            return None

    def __setitem__(self, key, value):
        c = self.handler.get_cookie('uid')
        if c:
            d = s.get(c,None)
            if d:
                d[key] = value
            else:
                d = {}
                d[key]=value
                s[c] = d
        else:
           #Expected bytes, unicode, or None;
           # got <class 'uuid.UUID'>
           u = myuuid(uuid4())
           d = {}
           d[key]=value
           s[u]=d
           self.handler.set_cookie('uid',u,expires_days=10)






