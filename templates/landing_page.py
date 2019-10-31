from flask import (
    Flask,
    render_template
)

# application instance
app = Flask(__name__, template_folder="templates") 
# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

@app.route('/')
def home(): 
    return render_template('landing_page.html') 

if __name__ =='__main__': 
    app.run(host='0.0.0.0', port=5000, debug=True)