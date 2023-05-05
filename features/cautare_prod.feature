Feature: Searching a product

  Background:
    Given Login Page: I am on the shein boutique login page

  @T1 @existentProduct @regressionTesting
  Scenario: Search for an existent product
    When I click the search bar
    When I enter product "pantofi fete"
    When I click the search button
    Then I select the product "pantofi fete"
    Then I select the number "27 - 16.6 cm"
    Then I click on the add to cart button
    Then I click on complete order button
    Then I see a successful message displayed

  @T2 @nonexistentProduct @regressionTesting
  Scenario Outline: Search for a nonexistent product
    Given I am on the Search Page
    When I click the search bar
    And I enter nonexistent_product "excavator"
    And I click the search button
    Then I see a message indicating that no products were found

    Examples:
      | product   | error_message                                |
      | excavator | Căutarea dvs. nu a returnat niciun rezultat. |