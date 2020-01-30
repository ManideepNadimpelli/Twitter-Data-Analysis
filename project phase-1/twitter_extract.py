from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

# Sign-in to twitter developer account and create app.
# Then Consumer key, Consumer secret, Access token and Access token secret keys will be generated.
consumer_key = "RiAljDExhBmC58Iqh0fyv3Kia"
consumer_secret_key = "4Bo2UzGErfBGJARHVBA0zkrA3pLCxgj916MwDJzwbdp3PwVUFn"
access_token = "391206417-Ws9xmwz1zfJBGD6dlj7RNej8EroI3e26kRpwov5d"
access_token_secret = "LDbm2pGU7IMQ0QiACTmnokPLePxfSW01eR5K8R64YNTQy"


class StdOutListener(StreamListener):
    # This code creates output files and data created is collected in those files.

    def on_data(self, data):
        try:
            with open('data1.json', 'a') as output1:
                json.dump(data, output1)
            with open('data2.json', 'a') as output2:
                output2.write(data)
            with open('tweets.txt', 'a') as tweets:
                tweets.write(data)
                tweets.write('\n')
            output1.close()
            tweets.close()
            output2.close()
        except BaseException as e:
            print('File execution is stopped', str(e))
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    # This code handles the twitter authentication and connections.

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    # Here it will retrieve the twitter data based on this filter.
    stream.filter(track=['WHO', 'WebMD', 'Cigna', 'Aetna', 'Cerner', 'Highmark', 'Anthem', 'AHA', 'Mayo Clinic'])