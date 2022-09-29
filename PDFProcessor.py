import re

import spacy
from spacy.matcher import Matcher
from spacypdfreader import pdf_reader
from spacy.lang.en.stop_words import STOP_WORDS

import Rules
from Constants import coverage_words
from XmindGenerate import generate_xmind


def to_title(string):
    regex = re.compile("[a-z]+('[a-z]+)?", re.I)
    return regex.sub(lambda grp: grp.group(0)[0].upper() + grp.group(0)[1:].lower(),
                     string)


def remove_cover_words(config_dict):
    remove_words = False
    check_words = config_dict['Process']['remove_coverage_from_label'].lower()
    if check_words == 'yes' or check_words == 'true':
        remove_words = True
    return remove_words


def read_document(nlp, config_dict):
    print('*** Reading Document, this will take a few moments ***')
    input_document = config_dict['Base Information']['input_document']
    doc = pdf_reader(input_document, nlp)
    return doc


def apply_rules(nlp, doc, config_dict):
    print('*** Building and applying Matcher Rules ***')
    new_matcher = Matcher(nlp.vocab)
    Rules.build_matcher_rules(new_matcher, config_dict)

    coverages = {}
    matches = new_matcher(doc)
    for match_id, start, end in matches:
        string_label = nlp.vocab.strings[match_id]
        matched_text = doc[start:end]
        final_text = ''
        for t in matched_text:
            if t.is_punct or t.pos_ == 'PART':
                ...
            else:
                if not (remove_cover_words(config_dict) and t.text.lower() in coverage_words):
                    final_text = final_text + t.text_with_ws

        coverages[string_label] = to_title(final_text.strip())
    return coverages


def process(config_dict):
    nlp = spacy.load("en_core_web_sm")
    spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
    spacy_punctuation = spacy.lang.en.punctuation
    spacy_hyphens = spacy_punctuation.HYPHENS.split('|')

    doc = read_document(nlp, config_dict)

    # for token in doc:
    #     print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
    #           token.shape_, token.is_alpha, token.is_stop, token.is_title, token.is_sent_start,
    #           token.morph, token.has_dep(), token.right_edge.text)

    coverages = apply_rules(nlp, doc, config_dict)
    print('*** Generating Mind Map ***')

    generate_xmind(coverages, config_dict)

    print("*** All complete and you are welcome ***")
