import pickle

with open('File130', 'rb') as f:
    data_new = pickle.load(f)
    
key = 70
answer = data_new.get(key)
print('Значение с ключом 70: ', answer)

print('Содержание словаря целиком: ', data_new)
