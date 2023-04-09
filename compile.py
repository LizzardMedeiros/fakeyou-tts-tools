import os
import speech_recognition as sr
from natural import insere_pontuacao

source_dir = "wavs"
output_file = "list.txt"
wav_files = []

for filename in os.listdir(source_dir):
  if filename.endswith(".wav"):
    # Extrair o número do arquivo de áudio
    file_num = filename.split(".")[0]
    
    # Salvar o nome do arquivo .wav na lista
    wav_files.append(f"{source_dir}/{file_num}.wav")

# Crie um objeto Recognizer
r = sr.Recognizer()

# Use o método recognize_google() para fazer a transcrição de fala em texto
try:
  with open(output_file, "w", encoding="utf-8") as f:
    for wav_file in wav_files:
      # Use o método AudioFile() do objeto Recognizer para carregar um arquivo de áudio
      print("transcrevendo " + wav_file + "...")
      with sr.AudioFile(wav_file) as source:
        audio = r.record(source)
        text = r.recognize_google(audio, show_all=True, language="pt-BR")
        text = text["alternative"][0]["transcript"]
        f.write(wav_file + "| " + insere_pontuacao(text) + "\n")

except sr.UnknownValueError:
    print("Não foi possível reconhecer a fala.")

except sr.RequestError as e:
    print("Não foi possível se conectar ao serviço de reconhecimento de fala: {0}".format(e))
