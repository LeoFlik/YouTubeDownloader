from customtkinter import filedialog
import customtkinter
from tkinter import *
from tkinter import ttk
from threading import Thread
from downloader import download_file


customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class CTKWindow(customtkinter.CTk):
  def __init__(self):
    super().__init__()

# main window setting
    self.title('YouTube Video Downloader')
    self.geometry(f'{500}x{350}')
    self.message =""
    

# instructions Label
    self.instruction_label = customtkinter.CTkLabel(
      self,
      anchor="e",
      text="Insira o endereço do link no espaço abaixo.\nClique no botão e escolha a pasta onde o video será salvo",
      font=customtkinter.CTkFont(size=15, weight="normal",slant="roman")
      )
    self.instruction_label.grid(row=0,column=0,columnspan = 1,padx=20,pady=20,sticky="nsew")

#url input
    self.entry_url = customtkinter.CTkEntry(
      self,
      height= 35,
      border_width=1,
    )
    self.entry_url.grid(row=1,column=0,columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

  # file manager button
    self.download_button = customtkinter.CTkButton(
      self,
      text="Download",
      font=customtkinter.CTkFont(size=15, weight="bold",slant="roman"),
      border_width=1,
      border_color="blue",
      command= self.askdir
    )
    self.download_button.grid(row=2,column=0,columnspan=2,padx=10,pady=10,sticky="nsew")

   # file status message
    
    self.label_status= customtkinter.CTkLabel(
      self,
      anchor="e",
      text="",
      font=customtkinter.CTkFont(size=10, weight="normal",slant="roman")
    )
    self.label_status.configure(text= self.message)
    self.label_status.grid(row=4,column=0,pady =10,padx= 10)



  def askdir(self):
        self.file_path = filedialog.askdirectory(title='Selecione um pasta')
        if self.file_path:
            progress_var = DoubleVar()
            progress_bar = ttk.Progressbar(variable=progress_var, maximum=100)
            progress_bar.grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

            def progress_callback(stream, chunk, remaining):
                total_size = stream.filesize
                bytes_downloaded = total_size - remaining
                progress = (bytes_downloaded / total_size) * 100
                progress_var.set(progress)
                self.label_status.configure(text=f"Downloading: {progress:.2f}%")

                

            download_thread = Thread(target=download_file, args=(self.entry_url.get(), self.file_path, progress_callback))
            download_thread.start()
            

if __name__ == '__main__':
  app = CTKWindow()
  app.mainloop()
