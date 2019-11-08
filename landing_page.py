from flask import render_template, Flask
import connexion

# application instance
app = connexion.App(__name__, specification_dir='./')
# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

@app.route('/')
def home(): 
    return render_template('landing_page.html') 

if __name__ =='__main__': 
    app.run(host='0.0.0.0', port=5000, debug=True)


#So, connect to http://localhost:5000/api/products to see list of data. Successful API Created.