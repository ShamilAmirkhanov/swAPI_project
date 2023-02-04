*** Settings ***
Library  RequestsLibrary

*** Variables ***
${base_url}  http://127.0.0.1:8000
${person}  4
${starship}  4
${planet}  4

*** Test Cases ***
People
    create session  myssion  ${base_url}
    ${response}=  GET On Session  myssion  /people/${person}
    log to console   ${response.status_code}
    log to console   ${response.content}
Starships
    create session  myssion  ${base_url}
    ${response}=  GET On Session  myssion  /starships/${starship}
    log to console   ${response.status_code}
    log to console   ${response.content}
Planets
    create session  myssion  ${base_url}
    ${response}=  GET On Session  myssion  /planets/${planet}
    log to console   ${response.status_code}
    log to console   ${response.content}

# robot -d results Robot.robot