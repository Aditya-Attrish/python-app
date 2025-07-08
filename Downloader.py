from tkinter import Tk,mainloop,Label,Entry,Button
from tkinter import ttk,filedialog
import requests
class Downloader(Tk):
	def __init__(self):
		super().__init__()
		self.lab=Label(text="Download file from URL.")
		self.lab.pack()
		self.lab2=Label(text="Enter URL's file.")
		self.lab2.pack()
		self.entry=Entry(self)
		self.entry.pack()
		self.entry.insert(0,"")
		self.but=Button(text="Download",bg="lightgreen",command=self.download)
		self.but.pack()
		self.progressBar=ttk.Progressbar(self,orient="horizontal",maximum=100,length=300,mode="determinate")
		self.dow=Label(text="Downloading")
		self.dow.place(x=167,y=200)
		self.progressBar.place(x=92,y=240)
		self.mainloop()
	def download(self):
		name=filedialog.asksaveasfilename(initialfile="image.jpg")
		size=1000
		self.progressBar['value']=0
		try:
			r=requests.get(self.entry.get(),stream=True)
			bytes=int(r.headers.get('content-length'))
			with open(name,"wb") as f:
				for d in r.iter_content(size):
					f.write(d)
					self.progressBar['value']+=(100*size)/bytes
					self.update()
			self.dow.configure(text="File Downloaded")
		except Exception as e:
			self.dow.configure(text="Error")
	
if __name__ == "__main__":
	Downloader()