def search(str , sub):
    for i, c  in enumerate(str):
        if str[i: i+len(sub)] == sub:
            return True
    return False

print(search("yajat", "janvi"))
