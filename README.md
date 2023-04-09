# FAKEYOU - TTS TOOLS

*Fakeyou TTS tools* é um conjunto de pequenas ferramentas em Python para auxiliar a criação de modelos

#### 1 **Dependencias**

- Python >= 3.11.2
- ffmpeg >= 6.0

#### 2 **Instalação**

- `pip install requirements.txt`
- `python -m spacy download pt_core_news_sm`
- `python -m textblob.download_corpora`

#### 3 **Iniciação**

- Leia a documentação [oficial do Fakeyou](https://docs.google.com/document/d/1U4KVrY817-X_pPP-VLJuQFNw3_qGBU6HvWUp-PX5JeU) para geração de modelos
- Crie ou baixe o áudio fonte em formato `mp3`, nomeado `source.mp3`, contendo algum monólogo com a voz que você deseja criar o modelo. Use áudios preferencialmente com mais de 30 minutos de duração.
- Coloque-o dentro da pasta raiz do projeto
- Rode o comando `python split.py` para dividir o arquivo em arquivos de 6 segundos, no formato correto.
- Rode o comando `python compile.py` para criar o arquivo `transcript.txt` necessário para o treinamento do [FakeYou](https://fakeyou.com/)

##### 4 **Créditos**

- [FakeYou](https://fakeyou.com/)
- [FakeYou - discord](https://discord.gg/fakeyou)
