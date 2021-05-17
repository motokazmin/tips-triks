from nltk.tokenize import word_tokenize, sent_tokenize
import pymorphy2
import networkx as nx
from wiki_ru_wordnet import WikiWordnet

# lemmatize_normalize: разворачивает предложения в одно, нормализует слова. Может заменять
# человеческие имена на пол. Возможно применить фильтр по частям речи
# include_part_speech - список частей речи, которые учитываются в результате
# names_to_gender - преобразовывать имена в пол или нет.
# save_sent - сохранить предложения или нет.
def lemmatize_normalize(text, morph, include_part_speech = ['NOUN', 'VERB', 'ADJF'], names_to_gender = True, save_sent = False):
  s = ''
  for sent in sent_tokenize(text):
    for word in word_tokenize(sent):
      p = morph.parse(word)[0]
      if (names_to_gender) & ('Name' in p.tag):
        if p.tag.gender == 'femn':
          s += ' женщина' 
        else:
          s += ' мужчина'
      elif p.tag.POS in include_part_speech:
        s += ' ' + p.normal_form
    if save_sent:
      s += ' . '

  return s

# get_synsets_graph: конструирует словарь синонимов, заменяя группу одним из значений. Также может возвратить ненаправленный граф синонимов.
def get_synsets_dict(texts, return_graph = True):
  wikiwordnet = WikiWordnet()
  G=nx.Graph()

  for text in texts:
    s = set()
    synsets = wikiwordnet.get_synsets(text)
    for synset in synsets:
      for w in synset.get_words():
        if (text != w.lemma()) & (w.lemma() in texts.values):
          G.add_edge(text, w.lemma())

  d = {}
  for g in nx.connected_components(G):
    default_lemma = g.pop()
    d.update(dict.fromkeys(g, default_lemma))
    d[default_lemma] = default_lemma

  if return_graph:
    return d, G
  else:
    return d

