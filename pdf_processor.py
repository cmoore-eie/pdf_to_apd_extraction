""" The main processing module

The import file defined in the configuration is read in and processed.
Once tokenised the information is handed off to the generation of the
mind map.
"""
import spacy
from spacy.matcher import Matcher
from spacypdfreader import pdf_reader
from spacy.lang.en.stop_words import STOP_WORDS
import config
import rules
from constants import coverage_words
from utility import wise_monkey_says, to_title
from xmind_generate import generate_xmind


def remove_cover_words():
    """Remove the coverage term from the identified coverage name

    Depending on the naming convention used in the policy wording coverages may be described as
    XXX Coverage, the word coverage adds clutter to the generated mind map. If the option
    remove_coverage_from_label is set to Yes or True the coverage clutter will be removed.

    :param config_dict The configuration file dictionary representation
    :return bool
    """
    remove_words = False
    check_words = config.config_dict['Process']['remove_coverage_from_label'].lower()
    if check_words == 'yes' or check_words == 'true':
        remove_words = True
    return remove_words


def read_document(nlp):
    """Processes the PDF identified in the configuration

    Reads the PDF identified in the configuration file Base Information -> input_document

    :param nlp The loaded nlp object
    :param config_dict The configuration file dictionary representation
    :return spaCy Doc
    """
    wise_monkey_says('Reading Document, this will take a few moments')
    input_document = config.config_dict['Base Information']['input_document']
    doc = pdf_reader(input_document, nlp)
    return doc


def apply_rules(nlp, doc):
    wise_monkey_says('Building and applying Matcher Rules')
    new_matcher = Matcher(nlp.vocab)
    rules.build_matcher_rules(new_matcher)

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
                if not (remove_cover_words() and t.text.lower() in coverage_words):
                    final_text = final_text + t.text_with_ws

        coverages[string_label] = to_title(final_text.strip())
    return coverages


def process():
    product_shape = config.config_dict['Product Information']['product_shape']
    if not ('input_document' in config.config_dict['Base Information']):
        wise_monkey_says(f'No Input file given, generating only the shape for {product_shape}')
        coverages = dict()
    else:
        nlp = spacy.load("en_core_web_sm")
        spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
        spacy_punctuation = spacy.lang.en.punctuation
        spacy_hyphens = spacy_punctuation.HYPHENS.split('|')

        doc = read_document(nlp)

        output_tokens = config.config_dict['Process']['output_tokens'].lower()
        if output_tokens == 'yes' or output_tokens == 'true':
            with open(config.config_dict['Process']['token_file'], 'w') as file:
                for token in doc:
                    line = f'{token.text} | {token.lemma_} | {token.pos_} | {token.tag_} | {token.dep_} | ' \
                           f'{token.shape_} | {token.is_alpha} | {token.is_stop} |  {token.is_title} | ' \
                           f'{token.is_sent_start} | {token.morph} | {token.has_dep()} | {token.right_edge.text} \n'
                    file.write(line)

        coverages = apply_rules(nlp, doc)
    wise_monkey_says(f'Generating the {product_shape} Mind Map')

    generate_xmind(coverages)

    wise_monkey_says('All done and you are welcome, it is always a pleasure to help')
    wise_monkey_says('Please deposit one banana for services rendered')
