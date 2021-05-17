import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import multidict as multidict

def getFrequencyDictForText(sentence):
    fullTermsDict = multidict.MultiDict()
    tmpDict = {}

    # making dict for counting frequencies
    for text in sentence.split(" "):
        val = tmpDict.get(text, 0)
        tmpDict[text.lower()] = val + 1
    for key in tmpDict:
        fullTermsDict.add(key, tmpDict[key])
    return fullTermsDict

def plot_category(text, figsize=(18, 10)):
    if isinstance(text, str) == False:
        print('text should have str type')
        return
    
    plt.figure(figsize=figsize)
    wordcloud = WordCloud(max_font_size=40)
    
    wordcloud.generate_from_frequencies(getFrequencyDictForText(text))
    
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
 