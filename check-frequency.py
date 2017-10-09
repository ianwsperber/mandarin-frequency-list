
from optparse import OptionParser
import json

FREQ_LIST = "mandarin-10000-freq-list.json"

def lookup(character):
  freq_list = json.loads(open(FREQ_LIST).read())

  for word in freq_list:
    if word["traditional"] == character or word["simplified"] == "character":
      return word["frequency"]

  return -1

if __name__ == "__main__": 
  parser = OptionParser()
  (options, args) = parser.parse_args()
  print(lookup(args[0]))