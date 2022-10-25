# concatenate several context managers within the parenthesis
with (open("test_file1.txt", "w") as test,
      open("test_file2.txt", "w") as test2):
    pass

with (open("test_file1.txt", "w"),
      open("test_file2.txt", "w")):
    pass

with (open("test_file1.txt", "w") as test,
      open("test_file2.txt", "w")):
    pass

with (open("test_file1.txt", "w"),
      open("test_file2.txt", "w") as test2):
    pass
