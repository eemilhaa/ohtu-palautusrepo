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
