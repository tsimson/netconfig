from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, BooleanField
from wtforms.fields import HiddenField, SelectField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, IPAddress


class LoginForm(FlaskForm):
    """User login form."""

    user = StringField('Username', validators=[DataRequired()])
    pw = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class AddHostForm(FlaskForm):
    """Add new device to local database form."""

    hostname = StringField('Hostname', validators=[DataRequired()])
    ipv4_addr = StringField('IPv4 Address', validators=[DataRequired(), IPAddress()])
    hosttype_choices = [('', ''),
                        ('Switch', 'Switch'),
                        ('Router', 'Router'),
                        ('Firewall', 'Firewall')]
    hosttype = SelectField('Host Type', choices=hosttype_choices, validators=[DataRequired()])
    ios_type_choices = [('cisco_ios', 'IOS'),
                        ('cisco_asa', 'ASA'),
                        ('cisco_nxos', 'NX-OS'),
                        ('cisco_xe', 'IOS-XE')]
    ios_type = SelectField('IOS Type', choices=ios_type_choices, validators=[DataRequired()])


class ImportHostsForm(FlaskForm):
    """Import devices into local database using CSV format."""

    csvimport = StringField('Devices to Import via CSV format', widget=TextArea())


class EditInterfaceForm(FlaskForm):
    """Edit device interface form."""

    datavlan = StringField('Data Vlan')
    voicevlan = StringField('Voice Vlan')
    other = StringField('Other', widget=TextArea())
    host = HiddenField('Host')
    interface = HiddenField('Interface')


class EditHostForm(FlaskForm):
    """Edit device in local database form."""

    hostname = StringField('Hostname', validators=[DataRequired()])
    ipv4_addr = StringField('IPv4 Address', validators=[DataRequired()])
    hosttype_choices = [('', ''),
                        ('Switch', 'Switch'),
                        ('Router', 'Router'),
                        ('Firewall', 'Firewall')]
    hosttype = SelectField('Host Type', choices=hosttype_choices, validators=[DataRequired()])
    ios_type_choices = [('', ''),
                        ('cisco_ios', 'IOS'),
                        ('cisco_asa', 'ASA'),
                        ('cisco_nxos', 'NX-OS'),
                        ('cisco_xe', 'IOS-XE'),
                        ('cisco_wlc_ssh', 'WLC')]
    ios_type = SelectField('IOS Type', choices=ios_type_choices, validators=[DataRequired()])


class CustomCommandsForm(FlaskForm):
    """Bulk commands form."""

    hostname = StringField('Hostname', validators=[DataRequired()])
    command = StringField('Commands', widget=TextArea())


class CustomCfgCommandsForm(FlaskForm):
    """Bulk configuration commands form."""

    hostname = StringField('Hostname', validators=[DataRequired()])
    command = StringField('Commands', widget=TextArea())
