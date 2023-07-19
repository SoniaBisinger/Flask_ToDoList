from website import create_app

#website is a python package now

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
