import shutil

f1 = open("test1.txt", encoding="utf-8")
f2 = open("test2.txt", 'w', encoding="utf-8")

# shutil.copyfileobj(f1, f2)

# shutil.copyfile("test1.txt", "test3.txt")
shutil.make_archive("test.tar", "zip", root_dir=".")
