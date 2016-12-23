
# coding: utf-8

# In[12]:

from pymongo import MongoClient
import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import datetime
import tweepy


consumer_key = ""
consumer_key_secret = ""
access_token = ""
access_token_secret = ""


connection = MongoClient('localhost', 27017)
db = connection.Desemprego
db.tweets.ensure_index("id", unique=True, dropDups=True)
collection = db.tweets


keyword_list = ['desempregos','desemprego','crise fiscal','crise social','desempregados','desempregado','economia','mercado de trabalho',
               'PIB','inflação','faliu','corte de despesas','desligamento','desligamentos','prejuizo','endividado','endividados',
               'imposto','impostos','desaceleramento','financeiras','déficit','instabilidade','financeira','incerteza',
               'incentivos fiscais','demitir','trt','remuneração','clt','assalariados','salários','inss','aposentadoria',
               'redução de quadro ','redução de quadro','MTE','mte','fgts','FGTS','fundo de garantia','desempregada',
               'desempregadas','aumento do desemprego','carteira assinada','desaceleração de vagas','crise econômica',
               'rendamédia','desemprego sobe','postos de trabalho','estabilidade', 'financeira','população empregada',
               'população ocupada','economicamente', 'crise política', 'crise politica', 'governo do brasil', 'governantes', 
               'vaga temporaria', 'perde o emprego','agência de empregos','causas do desemprego', 'taxa de desemprego','demitido',
               'mão de obra','procuraram emprego','procuram emprego', 'previdência','governo Temer', 'governo Michel Temer','Temer',
               'crise internacional', 'economia emergente','Organização Internacional do Trabalho','OIT','deterioração do mercado de trabalho',
               'corrupção','STF','Lula','Dilma','PT','reforma da previdência','curriculo','currículo','reforma previdenciaria',
               'O número de empregadores','desemprego atingiu','inss','INSS','IRRF','irrf','tributos','pt acabou com o brasil',
               'sem emprego','remunerado', 'reforma política', 'instabilidade do momento','brasil sofre com desemprego','#desemprego',
               'comissão de trabalho','retração econômica','desemprego crescente', 'efeitos da crise econômica', 'alta do desemprego']




class StdOutListener(StreamListener):
    def on_data(self, data):


        t = json.loads(data)

        tweet_id = t['id_str'] 
        text = t['text']  
        hashtags = t['entities']['hashtags']  
        time_stamp = t['created_at']  
        language = t['lang']  
         


        created = datetime.datetime.strptime(time_stamp, '%a %b %d %H:%M:%S +0000 %Y')

   
        tweet = {'id': tweet_id, 'text': text, 'hashtags': hashtags, 'language': language, 'created': created}


        collection.insert_one(tweet)

   
        return True
       
             
  
    def on_error(self, status):
          
        print(status)

l = StdOutListener(api=tweepy.API(wait_on_rate_limit=True))
auth = OAuthHandler(consumer_key, consumer_key_secret)
auth.set_access_token(access_token, access_token_secret)

stream = Stream(auth, listener=l)
stream.filter(track=keyword_list)


# In[ ]:



