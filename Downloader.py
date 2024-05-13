import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

# Função para baixar vídeo do YouTube
def baixar_video():
    url = url_entry.get()

    try:
        # Crie um objeto YouTube com a URL fornecida
        video = YouTube(url)

        # Selecione a melhor qualidade disponível
        video_stream = video.streams.get_highest_resolution()

        # Baixe o vídeo para o diretório atual
        file_path = video_stream.download()
        messagebox.showinfo("Download Concluído", f"O vídeo foi baixado com sucesso!\n\nSalvo em: {file_path}")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")


# Configuração da janela principal
root = tk.Tk()
root.title("Baixar Vídeo do YouTube")

# Frame para conter widgets
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Label e Entry para inserir a URL do vídeo
url_label = tk.Label(frame, text="URL do Vídeo:")
url_label.grid(row=0, column=0, sticky="w")

url_entry = tk.Entry(frame, width=40)
url_entry.grid(row=0, column=1, padx=5)

# Botão para iniciar o download
download_button = tk.Button(frame, text="Baixar Vídeo", command=baixar_video)
download_button.grid(row=1, columnspan=2, pady=10)

# Executar o loop da aplicação
root.mainloop()
