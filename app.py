from flask import Flask, render_template, request
from ctg_api import ClinicalTrialsAPI, visualize_trial_locations_interactive

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_expr = request.form.get('search_expr', '')
        title = request.form.get('title', '')
        max_studies = int(request.form.get('max_studies', 50))
        
        api = ClinicalTrialsAPI()
        fig = visualize_trial_locations_interactive(
            api=api,
            search_expr=search_expr,
            title=title,
            max_studies=max_studies
        )
        
        # Get the HTML representation of the plot
        plot_html = fig.to_html(full_html=False, include_plotlyjs='cdn')
        return render_template('index.html', plot_html=plot_html)
    
    return render_template('index.html', plot_html=None)

if __name__ == '__main__':
    app.run(debug=True)
