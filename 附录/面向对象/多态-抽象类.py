# encoding = utf-8
__author__ = "Ang Li"

class Document:
    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Pdf(Document):
    def show(self):
        print("show pdf document.")

class Word(Document):
    def show(self):
        print("show word document.")

pdf_obj = Pdf()
word_obj = Word()

objs = [pdf_obj,word_obj]

for i in objs:
    i.show()