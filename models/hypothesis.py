class Hypothesis:
    def __init__(self, disease, cid):
        self.disease = disease
        self.cid = cid

    def show_hypothesis_cid(self):
        print(f"{self.disease} || CID: {self.cid}")
