from Veiculo import Veiculo
from HashTable import HashTable

hashtable = HashTable()

print("\n########## INSERINDO REGISTROS ##########")
veiculo1 = Veiculo('NEX-0196', 2020, 'honda', 'preto')
hashtable.__setitem__(veiculo1.placa, veiculo1.__str__())

veiculo2 = Veiculo('JFS-7272', 2009, 'fiat', 'preto')
hashtable.__setitem__(veiculo2.placa, veiculo2.__str__())

veiculo3 = Veiculo('NAL-7556', 2010, 'fiat', 'branco')
hashtable.__setitem__(veiculo3.placa, veiculo3.__str__())

veiculo4 = Veiculo('ANX-1565', 2012, 'fiat/strada', 'preto')
hashtable.__setitem__(veiculo4.placa, veiculo4.__str__())

veiculo5 = Veiculo('IAL-0831', 2022, 'ford', 'preto')
hashtable.__setitem__(veiculo5.placa, veiculo5.__str__())

veiculo6 = Veiculo('MXY-7202', 2022, 'peugeot', 'branco')
hashtable.__setitem__(veiculo6.placa, veiculo6.__str__())

veiculo7 = Veiculo('KEE-6341', 2010, 'peugeot', 'vermelho')
hashtable.__setitem__(veiculo7.placa, veiculo7.__str__())

veiculo8 = Veiculo('NAK-4280', 2015, 'fiat', 'vermelho')
hashtable.__setitem__(veiculo8.placa, veiculo8.__str__())

veiculo9 = Veiculo('ASL-1246', 2015, 'renault', 'preto')
hashtable.__setitem__(veiculo9.placa, veiculo9.__str__())

veiculo10 = Veiculo('ALV-4461', 2019, 'renault', 'branco')
hashtable.__setitem__(veiculo10.placa, veiculo10.__str__())

print("\n########## SITUAÇÃO DA HASHTABLE ##########")
hashtable.tabledados()

print("\n########## REMOVENDO REGISTROS ##########")
hashtable.remove('NEX-0196')
hashtable.remove('JFS-7272')
hashtable.remove('NAL-7556')
hashtable.remove('ANX-1565')
hashtable.remove('IAL-0831')

print("\n########## SITUAÇÃO DA HASHTABLE ##########")
hashtable.tabledados()

print("\n########## INSERINDO REGISTROS ##########")
veiculo11 = Veiculo('NDI-5992', 2019, 'renault', 'branco')
hashtable.__setitem__(veiculo11.placa, veiculo11.__str__())

veiculo12 = Veiculo('IEY-2538', 2022, 'peugeot', 'branco')
hashtable.__setitem__(veiculo12.placa, veiculo12.__str__())

veiculo13 = Veiculo('BST-5572', 2009, 'fiat', 'preto')
hashtable.__setitem__(veiculo13.placa, veiculo13.__str__())

print("\n########## SITUAÇÃO DA HASHTABLE ##########")
hashtable.tabledados()