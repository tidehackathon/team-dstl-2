from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import widgets, SelectMultipleField

SECRET_KEY = 'development'
app = Flask(__name__)
app.config.from_object(__name__)


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class NationForm(FlaskForm):
    string_of_files = ['Nation_1\r\nNation_2\r\nNation_3\r\nNation_4\r\nNation_5\r\nNation_6\r\nNation_7\r\nNation_8\r'
                       '\nNation_9\r\nNation_10\r\nNation_11\r\nNation_12\r\nNation_13\r\nNation_14\r\nNation_15\r'
                       '\nNation_16\r\nNation_17\r\nNation_18\r\nNation_19\r\nNation_20\r\nNation_21\r\nNation_22\r'
                       '\nNation_23\r\nNation_24\r\nNation_25\r\nNation_26\r\nNation_27\r\nNation_28\r\nNation_29\r'
                       '\nNation_30\r\nNation_31\r\nNation_32\r\nNation_33\r\nNation_34\r\nNation_35\r\nNation_36\r'
                       '\nNation_37\r\nNation_38\r\nNation_39\r\nNation_40\r\nNation_41\r\nNation_42\r\nNation_43\r'
                       '\nNation_44\r\nNation_45\r\nNation_46\r\n']
    list_of_files = string_of_files[0].split()
    # create a list of value/description tuples
    files = [(x, x) for x in list_of_files]
    example = MultiCheckboxField('Label', choices=files)


class ExersiceFrom(FlaskForm):
    string_of_files = ['CWIX_2021\r\nCWIX_2022\r\n']
    list_of_files = string_of_files[0].split()
    # create a list of value/description tuples
    files = [(x, x) for x in list_of_files]
    example = MultiCheckboxField('Label', choices=files)


class TaskFrom(FlaskForm):
    string_of_files = ['Data_Centric_Security_Approach\r\nConformance_Testing\r\nDe-Risking_Coalition_Operations\r\n'
                       'Data_Analytics\r\nConnecting_sensor_-_decision_maker_effector\r\n'
                       'Federated_Mission_Networking\r\nMulti-Domain_Operations\r\nStandards_Violation\r\n']
    list_of_files = string_of_files[0].split()
    # create a list of value/description tuples
    files = [(x, x) for x in list_of_files]
    example = MultiCheckboxField('Label', choices=files)


class DomainFrom(FlaskForm):
    string_of_files = ['Air\nLand\r\nMaritime\r\nCyberspace\r\nSpace\r\nOther_Support_Services\r\n']
    list_of_files = string_of_files[0].split()
    # create a list of value/description tuples
    files = [(x, x) for x in list_of_files]
    example = MultiCheckboxField('Label', choices=files)


class WarfareFrom(FlaskForm):
    string_of_files = ['Strategic\nOperational\r\nDeployed\r\n']
    list_of_files = string_of_files[0].split()
    # create a list of value/description tuples
    files = [(x, x) for x in list_of_files]
    example = MultiCheckboxField('Label', choices=files)


@app.route('/', methods=['post', 'get'])
def hello_world():
    nation_form = NationForm()
    exersice_form = ExersiceFrom()
    task_form = TaskFrom()
    domain_form = DomainFrom()
    warfare_form = WarfareFrom()
    if nation_form.validate_on_submit() & exersice_form.validate_on_submit() & task_form.validate_on_submit() & \
            domain_form.validate_on_submit() & warfare_form.validate_on_submit():
        print(nation_form.example.data)
        print(exersice_form.example.data)
        print(task_form.example.data)
        print(domain_form.example.data)
        print(warfare_form.example.data)
        return render_template("result.html", nationData=nation_form.example.data,
                               exersiceData=exersice_form.example.data, taskData=task_form.example.data,
                               domainData=domain_form.example.data, warfareData=warfare_form.example.data)
    else:
        print("Validation Failed")
        print("Nation Form Errors ", nation_form.errors)
        print("Exersice Form Errors ", exersice_form.errors)
        print("Task Form Errors ", task_form.errors)
        print("Domain Form Errors ", domain_form.errors)
        print("Warfare Form Errors ", warfare_form.errors)
    return render_template('search.html', nationForm=nation_form, exersiceForm=exersice_form, taskForm=task_form,
                           domainForm=domain_form, warfareForm=warfare_form)


if __name__ == '__main__':
    app.run(debug=True)
