import pandas


class Definition:

    def __init__(self, term):
        self.term = term

    def get(self):
        df = pandas.read_csv("data.csv")
        return tuple(df.loc[df['word']==self.term]['definition'])


# d = Definition(term="sun")
# print(d.get())