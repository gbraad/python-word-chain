from requests import get
import re

url = 'https://gist.githubusercontent.com/gbraad/cae1b0ca2748db7e91627ced04f02589/raw/603c2480c32376102b2ce399ac260fdedd3bda91/5letter.html'


# load file
def load_words_file(url):
  filecontent = get(url).text
  return re.findall(r'<pre>(.*?)</pre>', filecontent, re.S)[0].replace('\n', ' ').strip().split(' ')

if __name__ == "__main__":
  words = load_words_file(url);
  print(words)
