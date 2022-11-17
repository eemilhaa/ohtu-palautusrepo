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

Register With Too Short Username And Valid Password
	Input New Command
	Input Credentials  k  12345678
	Output Should Contain  Username must be at least 3 letters long

Register With Valid Username And Too Short Password
	Input New Command
	Input Credentials  kaaleppi  1
	Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
	Input New Command
	Input Credentials  kaaleppi  qwertyuiop
	Output Should Contain  Password cannot only contain letters
