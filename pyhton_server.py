from flask_cors import CORS
from flask import Flask,jsonify

app = Flask(__name__)
CORS(app)

opportunities = {
    "internships": {
        "1st_year": [
            {
                "title": "Google STEP Internship",
                "desc": "Early internship for 1st/2nd year undergrads. Big resume booster.",
                "timeline": "Applications open in September",
                "applyLink": "https://buildyourfuture.withgoogle.com/programs/step/",
                "finalMonth": "September"
            },
            {
                "title": "Microsoft Engage Program",
                "desc": "Mentorship + project program leading to Microsoft internships.",
                "timeline": "Applications open in May",
                "applyLink": "https://microsoft.acehacker.com/engage2025/",
                "finalMonth": "May"
            }
        ],
        "2nd_year": [
            {
                "title": "Amazon WOW",
                "desc": "Women-only tech program with mentorship and possible internship offers.",
                "timeline": "Opens in April-May",
                "applyLink": "https://amazonwowindia.splashthat.com/",
                "finalMonth": "April"
            }
        ]
    },
    "open_source": {
        "1st_year": [
            {
                "title": "Google Summer of Code (GSoC)",
                "desc": "Work on open source projects with stipends. Internationally recognized.",
                "timeline": "Applications open in March",
                "applyLink": "https://summerofcode.withgoogle.com/",
                "finalMonth": "March"
            },
            {
                "title": "MLH Fellowship",
                "desc": "Remote global fellowship for open-source contributions. Great for networking.",
                "timeline": "Spring, Summer, Fall",
                "applyLink": "https://fellowship.mlh.io/",
                "finalMonth": "February"
            }
        ]
    },
    "research": {
        "1st_year": [
            {
                "title": "MITACS Globalink Research",
                "desc": "Fully funded summer research internship in Canada.",
                "timeline": "Applications open in July-August",
                "applyLink": "https://www.mitacs.ca/en/programs/globalink",
                "finalMonth": "August"
            }
        ]
    }
}

# API to fetch all opportunities
@app.route("/api/all")
def get_all():
    return jsonify(opportunities)

# API to fetch by category
@app.route("/api/<category>")
def get_by_category(category):
    data = opportunities.get(category, {})
    return jsonify(data)

# API to fetch by category and year
@app.route("/api/<category>/<year>")
def get_by_category_year(category, year):
    category_data = opportunities.get(category, {})
    year_data = category_data.get(year, [])
    return jsonify(year_data)

if __name__ == "__main__":
    app.run(debug=True)