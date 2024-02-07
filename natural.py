import spacy
import re

nlp = spacy.load("pt_core_news_sm")

def insere_pontuacao(frase):
  doc = nlp(frase)

  sentenceList = list()
  text = ""
  interjeicao_list = ["né", "hein", "quê", "ah"]

  for sent in doc.sents:
    sentenceList.append(sent.text)

  for i in range(len(sentenceList)):
    d = nlp(sentenceList[i])

    for j in range(len(d)):
      text += d[j].text
      if j == len(d) - 1:
        continue

      if d[j].text in interjeicao_list:
        text += "? "
      elif d[j].tag_ == "NOUN" and d[j + 1].tag_ == "ADV":
        text += ", "
      elif d[j].tag_ == "NOUN" and d[j + 1].tag_ == "PRON":
        text += ", "
      elif d[j].tag_ == "CCONJ":
        text += ", "
      elif d[j].tag_ == "INTJ":
        text += "! "
      else:
        text += " "

    if i == len(sentenceList) - 1:
      text += "."
    else:
      text += ", "

  return text
