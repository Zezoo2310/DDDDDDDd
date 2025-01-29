def read_line_by_line(fileName):
    with open(fileName) as f:
        # read content line by line 
        content_lst = f.readlines()
        print(content_lst)
