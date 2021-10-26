from probe import MyProbe

#creazione oggetto prove
test_telnet = MyProbe()
#prima test dati input sonda
data_test = test_telnet.check_input()
#eseguo la vera e propria "sonda"
result = test_telnet.execute(data_test)
#parso i risultati della sonda nel file di output json
test_telnet.parse(result)

print(str(result))
print("Process Completed!")
