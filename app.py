import subprocess
from flask import Flask, render_template, request, make_response, send_file

app = Flask(__name__)

@app.route('/')
def form():
    # Display the input form
    return render_template('index.html')

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    # Receive data from the form
    setup = request.form['setup']
    sub = request.form['sub']
    madap = request.form['madap']
    madaf = request.form['madaf']
    visap = request.form['visap']
    visaf = request.form['visaf']
    mcp = request.form['mcp']
    mcf = request.form['mcf']
    app = request.form['app']
    apf = request.form['apf']
    aep = request.form['aep']
    aef = request.form['aef']
    urp = request.form['urp']
    urf = request.form['urf']
    stcp = request.form['stcp']
    stcf = request.form['stcf']
    tabbyp = request.form['tabbyp']
    tabbyf = request.form['tabbyf']
    tamarap = request.form['tamarap']
    tamaraf = request.form['tamaraf']
    sadp = request.form['sadp']
    sadf = request.form['sadf']


    # Generate HTML content based on the inputs
    rendered_html = render_template('proposal_template.html', setup=setup, sub=sub,
    madap=madap, madaf=madaf,
    visap=visap, visaf=visaf,
    mcp=mcp,mcf=mcf,app=app,apf=apf,aep=aep,aef=aef,urp=urp,urf=urf,stcp=stcp,stcf=stcf,tabbyp=tabbyp,
                                    tabbyf=tabbyf,tamarap=tamarap,tamaraf=tamaraf,sadp=sadp,sadf=sadf
                                    )

    # Create a temporary HTML file
    with open("proposal.html", "w") as file:
        file.write(rendered_html)

    # Convert HTML to PDF using wkhtmltopdf
    process = subprocess.Popen(['/usr/local/bin/wkhtmltopdf', 'proposal.html', 'proposal.pdf'], stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

    process.communicate()

    # Send the generated PDF back to the client
    return send_file('proposal.pdf')


if __name__ == '__main__':
    app.run(debug=True)
