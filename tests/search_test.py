from pages.homepage import HomePage

def test_basic(browser):

    searchTerm = "test"

    home_page = HomePage(browser)

    home_page.load()

    home_page.search(searchTerm)

    assert searchTerm in browser.title