from flask import Flask, render_template

app = Flask(__name__)
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    project_list = [
        {
            "title": "Book Design",
            "description": "The design challenge was to create a book that is print-ready and includes both the cover as well as the content pages. It should have proper layout and all contents should be styled.",
            "images": ["Book.jpg"], # put these in /static/images
            "link": "#",
            "colors": ["#e38025", "#000000"],
            "font": ["Elephant Regular", "Lucida Sans Regular"],

            "title": "Flyer Design",
            "description": "The design challenge was to create a flyer advertising a specific event or something for a company. Its goal was to be something eye catching that would encourage someone to engage in whatever the flyer is for and be consistent in its elements such as fonts, colors, images, and so forth.",
            "images": ["Flyer.jpg"], # put these in /static/images
            "link": "#",
            "colors":["#fdf7d3", "#868f55"],
            "font": ["Botanica Script","Roboto Black"],

            "title": "Brochure Design",
            "description": "The design challenge was to create a trifold brochure that is professional and print-ready. It should be consistent across each page and have proper hierarchy. I solved this by creating a travel brochure for a fictitious European tour. I used natural colors and images to portray tourist attractions.",
            "images": ["Trifold.jpg"], # put these in /static/images
            "link": "#",
            "colors": ["#40432d", "#72491e"],
            "font": ["Brittanic Bold", "Dubai Regular"],

            "title": "Menu Design",
            "description": "The design challenge was to create a multi-page document for a restaurant menu that is professional and well organized. It should include all typical information that a traditional menu would have and be consistent.",
            "images": ["Menu.jpg"], # put these in /static/images
            "link": "#",
            "colors": ["#5a1720", "#ddbc9b", "#f3bc19"],
            "font": ["Montserrat Alternates Black", "Lato Bold"],

            "title": "Logo Design",
            "description": "The design challenge was to create a sizable logo with multiple color versions that is both print and web ready. The logo should communicate the purpose of the business and be both eye-catching yet simple.",
            "images": ["Shirt.jpg"], # put these in /static/images
            "link": "#",
            "colors": ["#5F6C7B", "#D9E6F6", "#ECBAB9"],
            "font": ["Gluten Semibold", "Lato Bold Italic"],

            "title": "Photography",
            "description": "Photography became a large interest of mine alongside graphic design. In the beginning I didn\’t see much in it, but over time I\’ve grown to see how diverse the photography industry is and the importance of it in different workplaces. I\’ve used a variety of techniques to create multiple series that explore topics such as still life, portraiture, shutter speed, etc. I used Photoshop to edit the images by adjusting the colors, details, removing items, and to overall finalize them.",
            "images": ["Sarah_A_01.jpg"], # put these in /static/images
            "link": "#"

        }
    ]
    return render_template("project.html", projects=project_list)

@app.route('/photography')
def photography():
    return render_template('photography.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        flash('Message sent successfully!')
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
