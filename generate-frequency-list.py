
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

WIKI_URLS = [
  "https://en.wiktionary.org/wiki/Appendix:Mandarin_Frequency_lists/1-1000",
  "https://en.wiktionary.org/wiki/Appendix:Mandarin_Frequency_lists/1001-2000",
  "https://en.wiktionary.org/wiki/Appendix:Mandarin_Frequency_lists/2001-3000",
  "https://en.wiktionary.org/wiki/Appendix:Mandarin_Frequency_lists/3001-4000",
  "https://en.wiktionary.org/wiki/Appendix:Mandarin_Frequency_lists/4001-5000",
  "https://en.wiktionary.org/wiki/Appendix:Mandarin_Frequency_lists/5001-6000",
  "https://en.wiktionary.org/wiki/Appendix:Mandarin_Frequency_lists/6001-7000",
  "https://en.wiktionary.org/wiki/Appendix:Mandarin_Frequency_lists/7001-8000",
  "https://en.wiktionary.org/wiki/Appendix:Mandarin_Frequency_lists/8001-9000",
  "https://en.wiktionary.org/wiki/Appendix:Mandarin_Frequency_lists/9001-10000",
]

def get_part_of_list(wiki_url, starts_from):
  soup = BeautifulSoup(urlopen(wiki_url), "html.parser")
  words = soup.select(".mw-parser-output li")
  parsed = []

  for i, word in enumerate(words):
    anchors = word.find_all("a")
    parsed.append({
      "frequency": i + starts_from + 1,
      "traditional": anchors[0].text,
      "simplified": anchors[1].text,
      "pinyin": anchors[2].text,
      "definition": anchors[2].next_sibling.replace(") - ", "")
    })
  
  return parsed

def get_word_frequency_list():
  freq_list = []

  for i, wiki_url in enumerate(WIKI_URLS):
    freq_list = freq_list + get_part_of_list(wiki_url, i * 1000)

  return freq_list
    

if __name__ == "__main__": 
  print(json.dumps(get_word_frequency_list(), ensure_ascii=False))