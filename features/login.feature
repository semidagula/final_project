Feature: Check the functionality of the login page
  As a user
  I want to can make an account
  So that I can enter my details

  Background:
    Given Login Page: I am on the shein boutique login page

    """
    Background = daca o sa consider ca un pas given este valabil pentru toate scenariile sau mai multe scenarii, atunci pentru
    a economisi cod voi putea trece acel pas la inceputul unui feature file sub keyword-ul  Background care inseamna
    ca se da un context general pentru testele care ne intereseaza
    """

  @T1 @loginSuccessful @regressionTesting
  Scenario:  Check that you can login into the application when providing correct credentials
    When Login Page: I insert  email "sem.gula@gmail.com" and I insert password "mypass1234"
    When Login Page: I click the login button
    Then I can login into the application and see the list of product

      """
      Scenario outline este o modalitate prin care putem sa executam acelasi test de mai multe ori folosindu-ne de un
      tabel de examples
      Pentru scenario outline vom parametriza elementele dinamice (adica cele care isi schimba valoarea la fiecare test)
      si vom rula testul de atatea ori cate randuri avem in tabelul de exemple
      Pentru a rula testele in mod individual putem sa ne folosim de conceptul de tag-uri
      Tag-urile incep cu @ si sunt urmate de un text la alegerea utilizatorului
      Un test poate sa fie reprezentat de mai multe tag-uri
      """


  @T2 @invalidLogin @regressionTesting
  Scenario Outline:  Check that you cannot login into the application when providing incorrect email and password
    When Login Page: I insert email "email"
    When I insert  password "password"
    When Login Page: I click the login button
    Then Login Page: I cannot login into the application and I receive error message "error_message"


    Examples:
      | email         | password | error_message                                                             |  |  |
      | s.g.gmail@com | 123abc   | Introduceți o adresă de e-mail corectă. De exemplu ionpopescu@domeniu.ro. |  |  |

    Examples:
      | email              | password           | error_message                                                             |  |  |
      | sem.gula@gmail.com | incorrect_password | Please enter more characters or clean leading or trailing spaces.         |  |  |
      | standard_email     | mypass1234         | Introduceți o adresă de e-mail corectă. De exemplu ionpopescu@domeniu.ro. |  |  |

