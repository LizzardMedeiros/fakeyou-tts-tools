import spacy
import re
from spacy.lang.pt import Portuguese

nlp = spacy.load("pt_core_news_sm")

def extrai_sentiment(frase):
  doc = nlp(frase)
  # Extrai a polaridade e a subjetividade da frase a partir dos atributos "sentiment" e "is_subjective" do objeto Doc
  polaridade = doc.sentiment
  return polaridade

def insere_pontuacao(frase):
  # Adiciona espaços antes e depois de pontuações para facilitar o processo de adicionar vírgulas
  frase = re.sub(r"([^\w\s])", r" \1 ", frase)

  # Divide a frase em palavras
  palavras = frase.split()

  # Lista de tags gramaticais que podem ser seguidas por vírgula
  # "NOUN", "VERB" - verbo, "ADJ" - adjetivo, "ADV", "PRON" - pronome, "DET" - artigo, "NUM"
  pos_tags_virgula = ["NOUN", "ADV", "PRON"]
  pos_tags_exclamacao = ["INTJ"]

  # Percorre a lista de palavras e adiciona vírgula se necessário
  resultado = []
  for i in range(len(palavras)):
      # Adiciona a palavra atual ao resultado
      resultado.append(palavras[i])

      # Verifica se a palavra atual é uma tag gramatical que pode ser seguida por vírgula
      if i < len(palavras) - 1 and palavras[i+1] != "," and palavras[i+1] != ".":
        tag_atual = nlp(palavras[i])[0].pos_
        tag_seguinte = nlp(palavras[i+1])[0].pos_
        interjeicao_list = ["né", "hein", "quê", "ah"]

        if palavras[i] in interjeicao_list:
            resultado.append("? ")
        elif tag_atual in pos_tags_virgula and tag_seguinte in pos_tags_virgula:
          resultado.append(", ")
        elif tag_atual in pos_tags_exclamacao and tag_seguinte in pos_tags_exclamacao:
          resultado.append("! ")
        else:
          polaridade = extrai_sentiment("".join(resultado))
          # Adiciona ponto de exclamação se a frase for positiva ou entusiástica
          if abs(polaridade) > 0.5 and i == len(palavras) - 1:
            resultado.append("! ")
          else:
            resultado.append(" ")

  # Concatena as palavras de volta para formar a sentença completa
  resultado = "".join(resultado)
  polaridade = extrai_sentiment(resultado)

  # Adiciona ponto de exclamação se a frase for positiva ou entusiástica
  if abs(polaridade) > 0.5:
    resultado += "!"
  else:
    resultado += "."

  return resultado

