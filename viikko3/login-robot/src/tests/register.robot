*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
	Input New Command
	Input Credentials  kaaleppi  12345678
	Output Should Contain  New user registered
