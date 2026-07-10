Assignment 19: Word2Vec Text Embeddings


Kaggle Dataset Link:

https://www.kaggle.com/code/ishansoni/sms-spam-collection-dataset
https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

SMS Spam Collection Dataset
spam dataset
- Used the `final_clean_text` column created in the previous assignment.

Libraries Used

- Pandas
- NumPy
- NLTK
- Gensim
- Scikit-learn
- Matplotlib

What I Implemented

- Studied the basics of word embeddings.
- Understood how Word2Vec works.
- Learned the difference between CBOW and Skip-Gram.
- Prepared the cleaned text for Word2Vec training.
- Trained both CBOW and Skip-Gram models.
- Compared their training time and output.
- Found similar words using the trained model.
- Performed word vector operations.
- Visualized word embeddings using PCA.
- Recorded observations and limitations.

Key Learnings

- Word2Vec captures semantic relationships between words.
- CBOW is faster, while Skip-Gram performs better for rare words.
- Word embeddings are more meaningful than traditional techniques like TF-IDF because they preserve semantic similarity.
- Context plays an important role in understanding language, which is why modern NLP models use contextual embeddings.

Conclusion

This assignment helped me understand how Word2Vec learns word representations from text. I trained both CBOW and Skip-Gram models and explored how word embeddings can capture relationships between words, making them useful for various NLP applications