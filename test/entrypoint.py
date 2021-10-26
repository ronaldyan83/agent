from probe import MyProbe

test_telnet = MyProbe()
data_test = test_telnet.check_input()
result = test_telnet.execute(data_test)
test_telnet.parse(result)
print(str(result))
print("Process Completed!")
