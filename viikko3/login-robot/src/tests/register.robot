*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
	Input New Command
	Input Credentials  kaaleppi  12345678
	Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
	Input New Command
	Input Credentials  kaaleppi  12345678
	Input New Command
	Input Credentials  kaaleppi  12345678
	Output Should Contain  Username already taken
