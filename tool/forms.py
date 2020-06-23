from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, FloatField, RadioField
from wtforms.validators import  Optional, NumberRange, Regexp

class QueryForm(FlaskForm):
    '''
    QueryForm class
    Used to generate a form with various fields that work as filters for searching the WDS-GAIA dataset
    Prevents users from entering invalid number ranges
    Also uses a regex to validate the wds_name field
    '''
    # Wds_name: ex: '12345+1234'
    WDS_name = StringField('WDS_name', validators=[Optional(), Regexp('[0-9]{5}[+,-]{1}[0-9]{4}', message='Invalid format.')])
    min_mag = FloatField('Min primary component magnitude', validators=[Optional(), NumberRange(0, 50, message='Mag invalid')])
    max_mag = FloatField('Max primary component magnitude', validators=[Optional(), NumberRange(0, 50, message='Mag invalid')])
    # ex: 120000 (HHMMSS)
    min_ra = FloatField('Min RA', validators=[Optional(), NumberRange(0, 240000, message='RA invalid')])
    max_ra = FloatField('Max RA', validators=[Optional(), NumberRange(0, 240000, message='RA invalid')])
    # ex: -75
    min_dec = FloatField('Min DEC', validators=[Optional(), NumberRange(-90, 90, message='Dec invalid')])
    max_dec = FloatField('Max DEC', validators=[Optional(), NumberRange(-90, 90, message='Dec invalid')])
    # ex: 8
    min_sep = FloatField('Min Separation', validators=[Optional(), NumberRange(0, 100, message='Sep invalid')])
    max_sep = FloatField('Max Separation', validators=[Optional(), NumberRange(0, 100, message='Sep invalid')])
    max_delta_mag = FloatField('Max Delta Mag', validators=[Optional(), NumberRange(0, 12, message='Delta Mag invalid')])
    # change all nobs to max_nobs and add a min_nobs
    min_nobs = FloatField('Minimum Number Observations', validators=[Optional(), NumberRange(0,100, message ='Number observations invalid')])
    nobs = FloatField('Number Observations', validators=[Optional(), NumberRange(0,100, message='Number observations invalid')])
    last_obs = FloatField('Last Observation', validators=[Optional(), NumberRange(1782, 2030, message='Last observation invalid')])
    # add delta separation min and max
    min_d_sep = FloatField('Minimum Delta Separation', validators=[Optional(), NumberRange(-10,10, message='Delta separation invalid')])
    max_d_sep = FloatField('Maximum Delta Separation', validators=[Optional(), NumberRange(-10,10, message='Delta separation invalid')])
    submit = SubmitField('Search')
