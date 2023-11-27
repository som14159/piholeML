import re
import string
import nltk
from symspellpy.symspellpy import SymSpell
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer
import joblib
import sys
def preprocess_text(text):
    # Add your text preprocessing steps here
    text = ''.join([char for char in text if char not in string.punctuation])
    return sym_spell.word_segmentation(text).corrected_string

def predict_ads(domain):
    preprocessed_domain = preprocess_text(domain)
    tokenized_domain = nltk.word_tokenize(preprocessed_domain)
    vectorized_domain = vectorizer.transform([" ".join(tokenized_domain)]).toarray()
    prediction = clf.predict(vectorized_domain)
    return prediction[0]

if __name__ == "__main__":
    # Load the model and other components
    sym_spell = SymSpell(max_dictionary_edit_distance=0, prefix_length=7)
    sym_spell.load_dictionary("frequency_dictionary_en_82_765.txt", term_index=0, count_index=1)

    vectorizer = joblib.load('count_vectorizer.joblib')  # Load your CountVectorizer
    clf = joblib.load('decision_tree_model.joblib')  # Load your Decision Tree model

    # Example usage
    domain_to_predict = sys.argv[1]
    result = predict_ads(domain_to_predict)
    print(f"Prediction for {domain_to_predict}: {result}")
