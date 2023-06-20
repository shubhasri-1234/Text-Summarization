import bs4
import urllib.request as url
import re
import nltk
from nltk import sent_tokenize
from nltk.corpus import stopwords
from nltk import word_tokenize
import string
import heapq
from youtube_transcript_api import YouTubeTranscriptApi as yta

nltk.download('punkt')
nltk.download('stopwords')
stop_word = stopwords.words('english')

def geturl(url_name, numofsentences):
  if 'youtube.com' in url_name:
    video_id = url_name.split('v=')[-1]
    try:
      data=yta.get_transcript(video_id)
      trans=''
      for value in data:
        for key,val in value.items():
          if key=='text':
            trans+=val
      l=trans.splitlines()
      s=" ".join(l)
      summary = process(s, numofsentences)
      return summary
    except:
      summary = "Sorry, the transcript couldn't be retrieved."
      return summary
  else:
    web = url.urlopen(url_name)
    try:
      page = bs4.BeautifulSoup(web,'html.parser')
      elements = page.find_all('p')
      if len(elements)==0:
        summary = "Sorry, this site couldn't be summarized."
        return summary
      else:
        article = ''
        for i in elements:
          article+= (i.text)
        summary = process(article,numofsentences)
        return summary
    except:
      summary = "Please enter a valid URL."
      return summary

def process(article,numofsentences):
  processed = article.replace(r'^\s+|\s+?$','')
  processed = processed.replace('\n',' ')

  processed = processed.replace("\\",'')
  processed = processed.replace(",",'')
  processed = processed.replace('"','')
  processed = re.sub(r'\[[0-9]*\]','',processed)

  sentences = sent_tokenize(processed)
  
  frequency = {}

  processed1 = processed.lower()

  for word in word_tokenize(processed1):

    if word not in stop_word and word not in string.punctuation:

        if word not in frequency.keys():

            frequency[word]=1

        else:

            frequency[word]+=1

  max_fre = max(frequency.values())
  
  for word in frequency.keys():

    frequency[word]=(frequency[word]/max_fre)

  frequency
  sentence_score = {}


  for sent in sentences:

    for word in word_tokenize(sent):

      if word in frequency.keys():

        if len(sent.split(' '))<30:

            if sent not in sentence_score.keys():

              sentence_score[sent] = frequency[word]

            else:
              sentence_score[sent]+=frequency[word]
  sentence_score

  summary = heapq.nlargest(numofsentences,sentence_score,key = sentence_score.get)

  summary = ' '.join(summary)

  return summary
