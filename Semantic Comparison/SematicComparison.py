# -*- coding: utf-8 -*-
"""Copy of word_embeddings_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1f62AhmA5xBnhkNhSmtUl7yNHtiEkKVvW
"""

!pip install numpy pandas sentence-transformers scikit-learn matplotlib seaborn --quiet

import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import seaborn as sns
import inspect
import textwrap

model = SentenceTransformer('all-MiniLM-L6-v2')

def embedding_heatmap_demo(txt1,txt2,txt3,txt4) -> None:
    # Initialize the model


    texts = [txt1,txt2,txt3,txt4]
    embeddings = model.encode(texts)
    similarity_matrix = cosine_similarity(embeddings)

    #Plot heat map
    sns.set_context('talk')
    plt.figure(figsize=(8, 6))
    truncated_texts = [text[:20] for text in texts]
    sns.heatmap(similarity_matrix, annot=True, cmap='coolwarm', xticklabels=truncated_texts,
                yticklabels=truncated_texts,annot_kws={"size": 18, "weight": "bold"})
    plt.xticks(rotation=45, ha='right', fontsize=16)
    plt.yticks(fontsize=16)
    plt.title("Cosine Similarity Heatmap")
    plt.show()

    # Show embeddings
    df = pd.DataFrame(embeddings)
    df.insert(0, "Text", texts)
    return df

embedding_heatmap_demo("kitten hospital","cat clinic","animal hospital","zoom class on AI")