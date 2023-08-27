from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.route("/")
def index():
    background_color = (211, 208, 206)

    options1 = [
        {"label": "Art", "value": "art"},
        {"label": "Biology", "value": "bio"},
        {"label": "Business", "value": "business"},
        {"label": "Chemistry", "value": "chem"},
        {"label": "Computer Science", "value": "comp sci"},
        {"label": "Construction", "value": "construction"},
        {"label": "Drama", "value": "drama"},
        {"label": "Engineering", "value": "engineering"},
        {"label": "English", "value": "english"},
        {"label": "Geography", "value": "geo"},
        {"label": "History", "value": "history"},
        {"label": "Kinesiology", "value": "kinesiology"},
        {"label": "Law", "value": "law"},
        {"label": "Math", "value": "math"},
        {"label": "Nutrition", "value": "nutrition"},
        {"label": "Physical Education", "value": "phys ed"},
        {"label": "Physics", "value": "physics"},
    ]

    options2 = [
        {"label": "Art", "value": "art"},
        {"label": "Biology", "value": "bio"},
        {"label": "Business", "value": "business"},
        {"label": "Chemistry", "value": "chem"},
        {"label": "Computer Science", "value": "comp sci"},
        {"label": "Construction", "value": "construction"},
        {"label": "Drama", "value": "drama"},
        {"label": "Engineering", "value": "engineering"},
        {"label": "English", "value": "english"},
        {"label": "Geography", "value": "geo"},
        {"label": "History", "value": "history"},
        {"label": "Kinesiology", "value": "kinesiology"},
        {"label": "Law", "value": "law"},
        {"label": "Math", "value": "math"},
        {"label": "Nutrition", "value": "nutrition"},
        {"label": "Physical Education", "value": "phys ed"},
        {"label": "Physics", "value": "physics"},
    ]
    return render_template(
        "index.html",
        options1=options1,
        options2=options2,
        background_color=background_color,
    )


@app.route("/page2")
def page2():
    suggestion = request.args.get("suggestion")
    suggestion2 = request.args.get("suggestion2")
    suggestion3 = request.args.get("suggestion3")
    gr1 = request.args.get("grade")
    gr2 = request.args.get("grade2")
    gr3 = request.args.get("grade3")
    req1 = request.args.get("req1")
    req2 = request.args.get("req2")
    req3 = request.args.get("req3")

    background_color = (211, 208, 206)
    return render_template(
        "page2.html",
        background_color=background_color,
        suggestion=suggestion,
        suggestion2=suggestion2,
        suggestion3=suggestion3,
        req1=req1,
        gr1=gr1,
        req2=req2,
        req3=req3,
        gr2=gr2,
        gr3=gr3,
    )


@app.route("/process_form", methods=["POST"])
def process_form():
    selected_option1 = request.form.get("selected_option1")
    selected_option2 = request.form.get("selected_option2")
    suggestion = "No suggestions available."
    req1 = ""
    gr1 = ""
    suggestion2 = "No suggestions available"
    req2 = ""
    gr2 = ""
    suggestion3 = "No suggestions available"
    req3 = ""
    gr3 = ""

    if selected_option1 == "engineering" or selected_option2 == "engineering":
        suggestion = "Engineering with specialization (i.e. Chemical Engineering) - Offered at all Ontario Universities"
        req1 = "ENG4U, MCV4U, MHF4U, SPH4U, SCH4U"
        gr1 = "mid 80s to mid 90s"

    elif selected_option1 == "comp sci" or selected_option2 == "comp sci":
        suggestion = "Computer Science - University of Waterloo"
        req1 = "ENG4U, MCV4U, MHF4U"
        gr1 = "98+ (competitive average)"
        suggestion2 = "Computer Science - University of Toronto"
        req2 = "ENG4U, MCV4U"
        gr2 = "Low 90s"
        suggestion3 = "Computer Science - McMaster University"
        req3 = "ENG4U, MCV4U, 2 of SBI4U, SCH4U, SPH4U, SES4U, ICS4U, TEJ4M"
        gr3 = "95+ (competitive average)"

    elif selected_option1 == "business" or selected_option2 == "business":
        suggestion = "Business with a specialization (i.e. Business and Comupters) - Offered at Trent University and Brock University"
        req1 = "ENG4U, MCV4U or MHF4U"
        gr1 = "mid to high 70s"

    elif (
        selected_option1 == "physics"
        or (selected_option1 == "physics" and selected_option2 == "chem")
        or (selected_option1 == "chem" and selected_option2 == "physics")
    ):
        suggestion = "Chemical and Physical Sciences - McMaster"
        req1 = "ENG4U, SPH4U, SCH4U, MCV4U, MHF4U"
        gr1 = "low to mid 80s"
        suggestion2 = "Engineering I - McMaster University"
        req2 = "ENG4U, SPH4U, SCH4U, MCV4U"
        gr2 = "mid to high nineties (competitive average)"

    elif selected_option1 == "law" or selected_option2 == "law":
        suggestion = "Social Sciences - Offered at most Ontario Universities"
        req1 = "ENG4U (SBI4U or MCV4U/MHF4U depending on specialization)"
        gr1 = "varies low 70s to mid 80s"
        suggestion2 = "Any kind of undergrad should get you into law school"

    elif selected_option1 == "nutritiion" or selected_option2 == "nutrition":
        suggestion = "Life Sciences - Offered at most Ontario Universities"
        req1 = "ENG4U, SCH4U, SBI4U, MCV4U or MHF4U or MDM4U"
        gr1 = "low to mid 90s"
        suggestion3 = "Social Sciences - Offered at most Ontario Universities"
        req3 = "ENG4U (SBI4U or MCV4U/MHF4U depending on specialization)"
        gr3 = "varies low 70s to mid 80s"

    elif selected_option1 == "phys ed" or selected_option2 == "phys ed":
        suggestion = "Physical Education - Brock University"
        req1 = "ENG4U, SBI4U, MCV4U or MHF4U or MDM4U, PSE4U or PSK4U"
        gr1 = "mid 70s"

    elif selected_option1 == "geo" or selected_option2 == "geo":
        suggestion = "Geography and Aviation - University of Waterloo"
        req1 = "ENG4U, MCV4U or MHF4U or MDM4U"
        gr1 = "mid 80s"
        suggestion2 = "Geography (BA or BSc) - Offered at most Ontario Universities"
        req2 = "ENG4U, MCV4U or MHF4U, 1 from SBI4U, SPH4U, SCH4U, or SES4U"
        gr2 = "mid 70s to mid 80s"

    elif selected_option1 == "history" or selected_option2 == "history":
        suggestion = "History - Offered at most Ontario Universities"
        req1 = "ENG4U"
        gr1 = "low 70s to high 80s"
        suggestion2 = "Humanities - McMaster Universities"
        req2 = "ENG4U"
        gr2 = "high 70s"
        suggestion3 = "Social Sciences - Offered at most Ontario Universities"
        req3 = "ENG4U (SBI4U or MCV4U/MHF4U depending on specialization)"
        gr3 = "varies low 70s to mid 80s"

    elif selected_option1 == "kinesiology" or selected_option2 == "kinesiology":
        suggestion = "Kinesiology - Offered at most Ontario Universities"
        req1 = "ENG4U, SBI4U, MCV4U"
        gr1 = "high 80s to high 90s"
        suggestion2 = "Health Sciences - Offered at most Ontario Universities"
        req2 = "ENG4U, SCH4U, SBI4U, MCV4U or MHF4U or MDM4U"
        gr2 = "high 80s to high 90s"
        suggestion3 = "Life Sciences - Offered at most Ontario Universities"
        req3 = "ENG4U, SCH4U, SBI4U, MCV4U or MHF4U or MDM4U"
        gr3 = "low to mid 90s"

    elif selected_option1 == "chem" or selected_option2 == "chem":
        suggestion = "Chemical and Physical Sciences - McMaster University"
        req1 = "ENG4U, SPH4U, SCH4U, MCV4U, MHF4U"
        gr1 = "low to mid 80s"
        suggestion2 = "Life Sciences - Queen's University"
        req2 = "ENG4U, SCH4U, SBI4U, MCV4U or MHF4U or MDM4U"
        gr2 = "low 90s"
        suggestion3 = "Pharmaceutial Chemistry - Ontario Tech University"
        req3 = "ENG4U, SCH4U, MHF4U, SBI4U or MCV4U or SPH4U"
        gr3 = "low 70s"

    elif selected_option1 == "math" or selected_option2 == "math":
        suggestion = "Mathematics and Statistics - Offered at most Ontario Universities"
        req1 = "ENG4U, MCV4U, MHF4U"
        gr1 = "varies from low 70s to high nineties"
        suggestion2 = "Physical and Mathematical Sciences"
        req2 = "ENG4U, MCV4U"
        gr2 = "mid to high 80s"
        suggestion3 = "Pharmaceutial Chemistry - Ontario Tech University"
        req3 = "ENG4U, SCH4U, MHF4U, SBI4U or MCV4U or SPH4U"
        gr3 = "low 70s"

    elif selected_option1 == "bio" or selected_option2 == "bio":
        suggestion = "Biology with your choice of specialization (i.e. Marine Biology) - Offered at all Ontario Universities"
        req1 = "ENG4U, SCH4U, MHF4U, SBI4U"
        gr1 = "varies from low 80s to low 90s"

    elif selected_option1 == "drama" or selected_option2 == "drama":
        suggestion = "Dramatic Arts at Brock University"
        req1 = "ENG4U, ADA4M"
        gr1 = "mid to high 70s"

    elif (selected_option1 == "art" and selected_option2 != "drama") or (
        selected_option2 == "art" and selected_option1 != "drama"
    ):
        suggestion = "Fine Arts - University of Waterloo"
        req1 = "ENG4U, ADA4M"
        gr1 = "mid to high 70s"
        suggestion2 = "Visual Arts - University of Ottawa"
        req2 = "ENG4U, or FRA4U"
        gr2 = "mid 70s"
        suggestion3 = "Arts Honours - University of Guelph"
        req3 = "ENG4U"
        gr3 = "mid 70s to low 80s"

    elif selected_option1 == "english" or selected_option2 == "english":
        suggestion = "English Literature - Offered at most Ontario Universities"
        req1 = "ENG4U"
        gr1 = "mid 70s to mid 80s"
        suggestion2 = "Humanities - McMaster Universities"
        req2 = "ENG4U"
        gr2 = "high 70s"
        suggestion3 = "Social Sciences - Offered at most Ontario Universities"
        req3 = "ENG4U (SBI4U or MCV4U/MHF4U depending on specialization)"
        gr3 = "varies low 70s to mid 80s"

    elif selected_option1 == "construction" or selected_option2 == "construction":
        suggestion = "Civil Engineering - Offered at most Ontario Universities"
        req1 = "ENG4U, MCV4U, MHF4U, SPH4U, SCH4U"
        gr1 = "mid 80s to mid 90s"

    return redirect(
        f"/page2?suggestion={suggestion}&suggestion2={suggestion2}&suggestion3={suggestion3}&req1={req1}&req2={req2}&req3={req3}&grade={gr1}&grade2={gr2}&grade3={gr3}"
    )


if __name__ == "__main__":
    app.run()
