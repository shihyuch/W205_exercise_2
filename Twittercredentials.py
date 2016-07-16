import tweepy

consumer_key = "Qctjq0TeFPuc33SL959CrCOFG"

consumer_secret = "20YFhQsAd6xnp1ElzfpsQAIvmTcXaYbXvzFWHyRGfIZQUhRn1k";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "746816918229655554-9gf8rw1pUnEkopohezwD9MXYl0eMaPN";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "dr9ydx0yPJe60jwuMn3dwUZxlJcuSryP3dxyFWTiKR7Bs";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



