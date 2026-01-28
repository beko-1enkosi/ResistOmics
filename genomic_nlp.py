
def get_kmers(sequence, k=4):
    kmers = []

    num_of_chunks = len(sequence) - k + 1

    for i in range(num_of_chunks):
        kmer = sequence[i : i+k]
        kmers.append(kmer)
    
    return kmers

class ResistanceModel:

    def __init__(self):
        pass

    def train(self, data_file):
        pass

    def predict(self, dna_sequence):
        pass