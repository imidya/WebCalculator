Feature: Calculator Functions
	Test basic function of web calculator.

	Scenario: Test basic plus formula
	Given A web calculator
	When enter 1 + 2
	Then get the result is 3

    Scenario: Test basic plus formula and some questions
    Given A web calculator again
    When enter <augend> + <addend>
        | augend | addend |
        |  8     |  4     |
        |  5     |  9     |

    Then get the sum is <sum>
        | sum |
        |  14 |