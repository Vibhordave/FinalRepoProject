# read the index.txt and prepare documents, vocab , idf

import chardet,os

current_dir = os.path.dirname(os.path.abspath(__file__))
sibling_dir = os.path.join(current_dir, "..", "Qdata")
txt_dir = os.path.join(current_dir, "..", "Text_files")

index_path=os.path.join(sibling_dir,"index.txt")
data_path=os.path.join(current_dir,"..","TF_IDF_DATA")

vocab_file=os.path.join(data_path,"vocab.txt")
idf_file=os.path.join(data_path,"idf-values.txt")
doc_file=os.path.join(data_path,"documents.txt")
inverted_file=os.path.join(data_path,"inverted-index.txt")

def provide_quspecific_path(x):
    x=str(x)
    child=os.path.join(sibling_dir,"data")
    qu_folder=os.path.join(child,x)
    qu_txt=os.path.join(qu_folder,x + ".txt")
    return qu_txt
    
def find_encoding(fname):
    r_file = open(fname, 'rb').read()
    result = chardet.detect(r_file)
    charenc = result['encoding']
    return charenc

my_encoding = find_encoding(index_path)

with open(index_path, 'r', encoding=my_encoding) as f:
    lines = f.readlines()

def preprocess(document_text):
    # remove the leading numbers from the string, remove not alpha numeric characters, make everything lowercase
    terms = [term.lower() for term in document_text.strip().split()[1:]]
    return terms

def preprocess_body(doc_txt):
    terms=[term.lower() for term in doc_txt.strip().split()]
    return terms
vocab = {}
documents = []
for index, line in enumerate(lines):
    # read statement and add it to the line and then preprocess
    tokens = []
    try:
        fold_path=provide_quspecific_path(index+1)
        with open(fold_path,'r',encoding=my_encoding) as new:
            qlines=new.readlines()
        for qindex,qline in enumerate(qlines):
            tokens.extend(preprocess_body(qline))
    except:
        pass
    # print(tokens)
    # break
    tokens = list(set(tokens))
    for i in range(5):
        tokens.extend(preprocess(line))
    
    # print(tokens)
    # break
    documents.append(tokens)
    for token in tokens:
        if token not in vocab:
            vocab[token] = 1
        else:
            vocab[token] += 1

# reverse sort the vocab by the values
vocab = dict(sorted(vocab.items(), key=lambda item: item[1], reverse=True))

print('Number of documents: ', len(documents))
print('Size of vocab: ', len(vocab))
print('Sample document: ', documents[0])

# save the vocab in a text file
with open(vocab_file, 'w',encoding=my_encoding) as f:
    for key in vocab.keys():
        f.write("%s\n" % key)

# save the idf values in a text file
with open(idf_file, 'w',encoding=my_encoding) as f:
    for key in vocab.keys():
        f.write("%s\n" % vocab[key])

# save the documents in a text file
with open(doc_file, 'w',encoding=my_encoding) as f:
    for document in documents:
        f.write("%s\n" % ' '.join(document))


inverted_index = {}
for index, document in enumerate(documents):
    for token in document:
        if token not in inverted_index:
            inverted_index[token] = [index]
        else:
            inverted_index[token].append(index)

# save the inverted index in a text file
with open(inverted_file, 'w',encoding=my_encoding) as f:
    for key in inverted_index.keys():
        f.write("%s\n" % key)
        f.write("%s\n" % ' '.join([str(doc_id) for doc_id in inverted_index[key]]))