import os
import subprocess
import uuid

output_dir = "wavs"
ffmpeg_command = ["ffmpeg", "-i", "source.mp3", "-f", "segment", "-segment_time", "6", "-c", "copy", output_dir + "/%d.mp3"]
subprocess.call(ffmpeg_command)

for filename in os.listdir(output_dir):
  if filename.endswith(".mp3"):
    # Define os caminhos dos arquivos de entrada e saída
    mp3_path = os.path.join(output_dir, filename)
    wav_path = os.path.join(output_dir, str(uuid.uuid4()) + ".wav")
    
    # Executa o comando ffmpeg para converter o arquivo MP3 para WAV
    subprocess.run(["ffmpeg", "-i", mp3_path, "-acodec", "pcm_s16le", "-ar", "22050", "-ac", "1", wav_path])

    # Apagar o arquivo .mp3 convertido
    os.remove(mp3_path)
