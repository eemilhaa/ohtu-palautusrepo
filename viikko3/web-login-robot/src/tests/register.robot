*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page

*** Test Cases ***
Register With Valid Username And Password
    Click Link  Register new user
    Set Username  kaaleppi
    Set Password  kaaleppi123
    Set Password Confirmation  kaaleppi123
    Submit Credentials
	Registration Should Succeed

Register With Too Short Username And Valid Password
    Click Link  Register new user
    Set Username  k
    Set Password  kaaleppi123
    Set Password Confirmation  kaaleppi123
    Submit Credentials
	Registration Should Fail With Message  Username must be at least 3 letters long

Register With Valid Username And Too Short Password
    Click Link  Register new user
    Set Username  uolevi
    Set Password  123
    Set Password Confirmation  123
    Submit Credentials
	Registration Should Fail With Message  Password must be at least 8 characters long

Register With Nonmatching Password And Password Confirmation
    Click Link  Register new user
    Set Username  uolevi
    Set Password  12345678
    Set Password Confirmation  01234567
    Submit Credentials
	Registration Should Fail With Message  Password confirmation does not match

*** Keywords ***
Registration Should Succeed
    Page Should Contain  Welcome to Ohtu Application!

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register
