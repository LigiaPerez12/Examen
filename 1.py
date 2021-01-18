import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "oHPnhtrKHK6GFlV57pdER7GEI"
csecret = "bG2PWWAwTyqXln3WSemte9W334qsGsO10QIjgVwM8Kq6bAnWSn"
atoken = "1340075672086130688-T2QpAtisN6EsduN4m8s0NZ8rc49ulj"
asecret = "HevHRl52FT4Dv4G6GrFkVsGpQiDgNYHMCZAKT9eb5937M"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://admin:burbuja02@localhost:5984/')  
try:
    db = server.create('covid')
except:
    db = server['cobidnuevayork']
    
'''===============LOCATIONS=============='''    

#twitterStream.filter(locations=[40.71427,-74.00597])  
twitterStream.filter(track=['USA', 'Covid'])