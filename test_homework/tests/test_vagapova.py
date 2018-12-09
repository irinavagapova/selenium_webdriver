
def test_example(app):

    app.open_page("https://qa-engineer.herokuapp.com")
    app.code_page()
    app.verify_list_total()






