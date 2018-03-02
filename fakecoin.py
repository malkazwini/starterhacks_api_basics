import hug

@hug.get()
def fakecoin():
    data = {'USD':10022341243.21}
    return data
