import os

""" this is a scrip that make all file that needed 
    to start flask website application
    for that to work must install flask
    run this comonad in your terminal(pip/3 install flask)
    all you need to do is give the main Directory 
    the scrip continue homepage ready with css and bootstrap 
    just run the scrip then the wsgi file and open the  website 
    if you see (welcome Developer!!!!fell free to use it and edit ♦♥!!!!')
    :)
    
"""


# name me
main_directory = 'website'
# you can name if you want
app = 'app'

# the path of the Directory
location = os.getcwd()

os.path.isdir(main_directory)
os.mkdir('{}/{}'.format(location, main_directory))
os.mkdir('{}/{}/{}'.format(location, main_directory,app))

# wsgi file
wsgi = open('{}/{}/wsgi.py'.format(location, main_directory), 'w')
wsgi.write('from {} import app\n\n'
           'if __name__ == "__main__":\n'
           '\tapp.run(port=5000)'.format(app))

# the init file
init = open('{}/{}/{}/__init__.py'.format(location, main_directory, app), 'w')
init.write('import flask\n\n\n\n'
           'app = flask.Flask(__name__)\n\n'
           'from {} import routes\n'.format(app))

# routes file with homepage ready
routes = open('{}/{}/{}/routes.py'.format(location, main_directory, app), 'w')
routes.write('from {} import app\n'
             'import flask\n\n\n\n'
             '@app.route("/")\n'
             'def homepage():\n'
             '\t return flask.render_template("homepage.html")'.format(app))

# the static folder put all the Css the img etc in this folder
os.mkdir('{}/{}/{}/static'.format(location, main_directory, app))

# the static folder have one css file that change the body
home_css = open('{}/{}/{}/static/home.css'.format(location, main_directory, app),'w')
home_css.write("body{background:linear-gradient(10deg,  #ffffff 30%, #38caff 25%);}")

# this for all html,Jania files
os.mkdir('{}/{}/{}/templates'.format(location, main_directory, app))
# ready html page
html = open('{}/{}/{}/templates/homepage.html'.format(location, main_directory,app), 'w')

s = "{{url_for('static',filename='home.css')}}"
css_loc = '<link rel="stylesheet" type="text/css" href="{}">'.format(s)
html.write('<!DOCTYPE html>\n'
           '<html lang="en">\n'
           '<head>\n'
           '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">\n'
           '{}\n'
           '<meta charset="UTF-8">\n'
           '<title>Title</title>\n'
            '</head>\n'
            '<body>\n\n'
           '<h2>welcome Developer!!!!</h2>\n\n'
           '<h5>fell free to use it and edit ♦♥!!!!</h5>\n\n'
            '</body>\n'
            '</html>\n'.format(css_loc))

