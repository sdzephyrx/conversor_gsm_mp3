import argparse
import subprocess
import shutil
import os

def converter_gsm_para_mp3(input_file, output_file):
    # Verifica se o arquivo de entrada existe
    try:
        with open(input_file, "r"):
            pass
    except FileNotFoundError:
        print(f"Arquivo de entrada '{input_file}' não encontrado.")
        return

    # Copia o arquivo .gsm para o diretório do script Python
    shutil.copy(input_file, "arquivo.gsm")

    # Executa o comando do FFmpeg para converter o arquivo de entrada para MP3
    try:
        subprocess.run(["ffmpeg", "-i", "arquivo.gsm", output_file])
        print(f"Conversão concluída! Arquivo de saída: '{output_file}'")
    except Exception as e:
        print(f"Erro durante a conversão: {e}")

    # Remove o arquivo temporário .gsm
    os.remove("arquivo.gsm")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script para converter arquivo .gsm para .mp3")
    parser.add_argument("input_file", help="Caminho do arquivo .gsm de entrada")
    parser.add_argument("output_file", help="Caminho do arquivo de saída (formato .mp3)")

    args = parser.parse_args()
    converter_gsm_para_mp3(args.input_file, args.output_file)
