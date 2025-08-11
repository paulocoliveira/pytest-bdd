Feature: Login
  Scenario: Logging in with correct credentials
    Given the user is on the login screen
    When they enter valid login details
    Then the my account dashboard should appear

  Scenario Outline: Logging in with different credentials
    Given the user is on the login screen
    When the user logs in with "<username>" and "<password>"
    Then the my account dashboard should appear

    Examples:
      | username                    | password    |
      | lambdatestblogs@gmail.com   | test123@    |
      | lambdatestblogs2@gmail.com  | 123456@test |
  
  Scenario: Logging in with specific username and password
    Given the user is on the login screen
    When the user logs in with "lambdatestblogs@gmail.com" and "test123@"
    Then the my account dashboard should appear