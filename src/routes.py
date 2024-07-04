from flask import redirect, render_template, url_for, request, flash
from flask_wtf import FlaskForm
from wtforms import SubmitField, DateField, ValidationError
from wtforms.validators import DataRequired
from src.charts import get_charts
from src.data import prepare_data, get_filtered_data, get_records_replace_nan
import pandas as pd
import logging

columns = [
    "ID",
    "Name",
    "Status",
    "Original German",
    "Founding year",
    "Founder",
    "Linkedin-Account Founder",
    "Legal Name",
    "Legal form",
    "Street",
    "Postal code",
    "City",
    "Country",
    "Register Number/ Company ID/ LEI",
    "Segment",
    "Subsegment",
    "Bank Cooperation",
    "Homepage",
    "E-Mail",
    "Insolvency",
    "Liquidation",
    "Date of inactivity",
    "Local court",
    "Former name",
]


def validate_date(form, field):
    if form.todate.data < form.fromdate.data:
        raise ValidationError("Recycled waste can't be larger than generated waste!")


class FilterForm(FlaskForm):
    fromdate = DateField("From", validators=[DataRequired(), validate_date])
    todate = DateField("To", validators=[DataRequired(), validate_date])
    submit = SubmitField("Apply Filter")


class Routes:

    def __init__(self, app, session) -> None:
        self.app = app
        self.session = session
        self.df = []

    def initRoutes(self):
        try:
            dataFrames = pd.read_csv("src/data/German_FinTechCompanies.csv")
            self.df = prepare_data(dataFrames)
        except Exception as ex:
            logging.error("Error occurred", exc_info = ex)
            return redirect(url_for("error"))

        # Home Page
        @self.app.route("/")
        def index():
            self.session.clear()  # clear session while starting the app
            return render_template("home.html")

        @self.app.route("/data", methods=["GET"])
        def data():
            try:
                records = get_records_replace_nan(self.df)
                return render_template(
                    "data.html",
                    columns=columns,
                    tableData=records,
                    number_of_columns=len(columns),
                    total_records=len(records),
                )
            except Exception as ex:
                logging.error("Error occurred", exc_info = ex)
                return redirect(url_for("error"))

        @self.app.route("/error", methods=["GET"])
        def error():
            return render_template("error.html")

        @self.app.route("/dashboard", methods=["POST", "GET"])
        def chart():
            try:
                form = FilterForm()
                dashboard_df = self.df
                if request.method == "POST":
                    if form.validate_on_submit():
                        dashboard_df = get_filtered_data(
                            self.df, form.fromdate.data, form.todate.data
                        )
                        if len(dashboard_df) == 0:
                            flash(
                                "Currently, we have data up to January 1, 2021. Please try an earlier date."
                            )
                    else:
                        dashboard_df = []
                        flash("Invalid Dates! From date should be less than to date. ")

                return render_template(
                    "chart.html", chart_properties=get_charts(dashboard_df), form=form
                )
            except Exception as ex:
                logging.error("Error occurred", exc_info = ex)
                return redirect(url_for("error"))
