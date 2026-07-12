# Assignment 17 – Text Cleaning, Preprocessing & NLP Pipeline

## Dataset

Source: Custom text dataset created for educational purposes.

The dataset contains 25 text samples featuring various forms of noisy and unstructured text, including:

* Uppercase and lowercase text
* Punctuation marks
* Numbers
* URLs
* Email addresses
* HTML tags
* Emojis
* Extra whitespace
* Slang words
* Repeated characters

These samples simulate real-world text collected from social media, websites, emails, and user-generated content.


## Technologies Used

* Python
* Pandas
* NLTK (Natural Language Toolkit)
* Regular Expressions (`re`)

## NLP Pipeline

The preprocessing pipeline follows these stages:

**Raw Text**
→ Lowercase Conversion
→ Remove URLs
→ Remove Emails
→ Remove HTML Tags
→ Remove Emojis
→ Remove Numbers
→ Remove Punctuation
→ Remove Extra Spaces
→ Slang Replacement
→ Normalize Repeated Characters
→ Tokenization
→ Stopword Removal
→ Stemming
→ Lemmatization
→ Final Clean Text*

## Conclusion

This assignment demonstrates the importance of text preprocessing in Natural Language Processing. By applying multiple cleaning and normalization techniques, raw textual data was successfully transformed into structured and meaningful text. The final output is well-prepared for NLP applications such as sentiment analysis, document classification, information retrieval, and machine learning models

install the requirements.txt and then proceed to the next
