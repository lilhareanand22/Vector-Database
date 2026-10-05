from chromadb.utils.embedding_functions import DefaultEmbeddingFunction

default_ef = DefaultEmbeddingFunction()

name = "Anand"
emb = default_ef([name])

print(emb)