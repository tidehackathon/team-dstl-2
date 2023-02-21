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
    string_of_nations = [
        'Nation_1\r\nNation_2\r\nNation_3\r\nNation_4\r\nNation_5\r\nNation_6\r\nNation_7\r\nNation_8\r\nNation_9\r\n'
        'Nation_10\r\nNation_11\r\nNation_12\r\nNation_13\r\nNation_14\r\nNation_15\r\nNation_16\r\nNation_17\r\n'
        'Nation_18\r\nNation_19\r\nNation_20\r\nNation_21\r\nNation_22\r\nNation_23\r\nNation_24\r\nNation_25\r\n'
        'Nation_26\r\nNation_27\r\nNation_28\r\nNation_29\r\nNation_30\r\nNation_31\r\nNation_32\r\nNation_33\r\n'
        'Nation_34\r\nNation_35\r\nNation_36\r\nNation_37\r\nNation_38\r\nNation_39\r\nNation_40\r\nNation_41\r\n'
        'Nation_42\r\nNation_43\r\nNation_44\r\nNation_45\r\nNation_46\r\n']
    list_of_nations = string_of_nations[0].split()
    # create a list of value/description tuples
    files = [(x, x) for x in list_of_nations]
    nationResult = MultiCheckboxField('Label', choices=files)


# class ExersiceFrom(FlaskForm):
#     string_of_exersices = ['CWIX_2021\r\nCWIX_2022\r\n']
#     list_of_exersices = string_of_exersices[0].split()
#     # create a list of value/description tuples
#     files = [(x, x) for x in list_of_exersices]
#     exersiceResult = MultiCheckboxField('Label', choices=files)
#
#
# class TaskFrom(FlaskForm):
#     string_of_tasks = ['Data_Centric_Security_Approach\r\nConformance_Testing\r\nDe-Risking_Coalition_Operations\r\n'
#                        'Data_Analytics\r\nConnecting_sensor_-_decision_maker_effector\r\n'
#                        'Federated_Mission_Networking\r\nMulti-Domain_Operations\r\nStandards_Violation\r\n']
#     list_of_tasks = string_of_tasks[0].split()
#     # create a list of value/description tuples
#     files = [(x, x) for x in list_of_tasks]
#     taskResult = MultiCheckboxField('Label', choices=files)
#
#
# class DomainFrom(FlaskForm):
#     string_of_domains = ['Air\nLand\r\nMaritime\r\nCyberspace\r\nSpace\r\nOther_Support_Services\r\n']
#     list_of_domains = string_of_domains[0].split()
#     # create a list of value/description tuples
#     files = [(x, x) for x in list_of_domains]
#     domainResult = MultiCheckboxField('Label', choices=files)
#
#
# class WarfareFrom(FlaskForm):
#     string_of_warfare = ['Strategic\nOperational\r\nDeployed\r\n']
#     list_of_warfare = string_of_warfare[0].split()
#     # create a list of value/description tuples
#     files = [(x, x) for x in list_of_warfare]
#     warfareResult = MultiCheckboxField('Label', choices=files)
#
#
# class TableForm(FlaskForm):
#     string_of_tables = ['Capabilities\r\n']
#     list_of_tables = string_of_tables[0].split()
#     # create a list of value/description tuples
#     files = [(x, x) for x in list_of_tables]
#     tableResult = MultiCheckboxField('Label', choices=files)


@app.route('/', methods=['post', 'get'])
def multi_Domain_Operations_By_Nation():
    # Initiate Program
    # Nation Mapping Dictionary
    nation_mapping = {
        'Nation_1': 1,
        'Nation_2': 2,
        'Nation_3': 3,
        'Nation_4': 4,
        'Nation_5': 5,
        'Nation_6': 6,
        'Nation_7': 7,
        'Nation_8': 8,
        'Nation_9': 9,
        'Nation_10': 10,
        'Nation_11': 11,
        'Nation_12': 12,
        'Nation_13': 13,
        'Nation_14': 14,
        'Nation_15': 15,
        'Nation_16': 16,
        'Nation_17': 17,
        'Nation_18': 18,
        'Nation_19': 19,
        'Nation_20': 20,
        'Nation_21': 21,
        'Nation_22': 22,
        'Nation_23': 23,
        'Nation_24': 24,
        'Nation_25': 25,
        'Nation_26': 26,
        'Nation_27': 27,
        'Nation_28': 28,
        'Nation_29': 29,
        'Nation_30': 30,
        'Nation_31': 31,
        'Nation_32': 32,
        'Nation_33': 33,
        'Nation_34': 34,
        'Nation_35': 35,
        'Nation_36': 36,
        'Nation_37': 37,
        'Nation_38': 38,
        'Nation_39': 39,
        'Nation_40': 40,
        'Nation_41': 41,
        'Nation_42': 42,
        'Nation_43': 43,
        'Nation_44': 44,
        'Nation_45': 45,
        'Nation_46': 46,
        'Nation_47': 47,
        'Nation_48': 48,
        'Nation_49': 49,
        'Nation_50': 50,
        'Nation_51': 51,
        'Nation_52': 52,
        'Nation_53': 53,
        'Nation_54': 54,
        'Nation_55': 55,
        'Nation_56': 56,
        'Nation_57': 57,
        'Nation_58': 58,
        'Nation_59': 59,
        'Nation_60': 60,
        'Nation_61': 61,
        'Nation_62': 62,
        'Nation_63': 63,
        'Nation_64': 64,
        'Nation_65': 65,
        'Nation_66': 66,
        'Nation_67': 67,
        'Nation_68': 68,
        'Nation_69': 69,
        'Nation_70': 70,
    }
    # Generate Form
    nation_form = NationForm()
    # Initial Query
    query = "select t.name, c.name AS CAPABILITY_NAME, n.name AS NATION_NAME from tasks t inner join capability_tasks "\
            "ct on t.id = ct.task_id inner join capabilities c on c.id = ct.capability_id inner join nations n on "\
            "n.id = c.nation_id where t.id = 8 and n.id = "
    # Form Validation and automatic generation of user query
    if nation_form.validate_on_submit():
        print(nation_form.nationResult.data)
        selected_nation = nation_form.nationResult.data
        str_selected_nation = ''.join(selected_nation)
        print(str_selected_nation)
        complete_query = query + str(nation_mapping[str_selected_nation])

        return render_template("multi_Domain_Operations_By_Nation_result.html", nationData=nation_form.nationResult.data, completeQuery=complete_query)
    else:
        print("Validation Failed")
        print("Nation Form Errors ", nation_form.errors)

    return render_template('multi_Domain_Operations_By_Nation_search.html', nationForm=nation_form)

# @app.route('/', methods=['post', 'get'])
# def hello_world():
#     # Initiate Program
#     nation_form = NationForm()
#     exersice_form = ExersiceFrom()
#     task_form = TaskFrom()
#     domain_form = DomainFrom()
#     warfare_form = WarfareFrom()
#
#     # Form Validation
#     if nation_form.validate_on_submit() & exersice_form.validate_on_submit() & task_form.validate_on_submit() & \
#             domain_form.validate_on_submit() & warfare_form.validate_on_submit():
#         print(nation_form.nationResult.data)
#         print(exersice_form.exersiceResult.data)
#         print(task_form.taskResult.data)
#         print(domain_form.domainResult.data)
#         print(warfare_form.warfareResult.data)
#         return render_template("multi_Domain_Operations_By_Nation_result.html", nationData=nation_form.nationResult.data,
#                                exersiceData=exersice_form.exersiceResult.data, taskData=task_form.taskResult.data,
#                                domainData=domain_form.domainResult.data, warfareData=warfare_form.warfareResult.data)
#     else:
#         print("Validation Failed")
#         print("Nation Form Errors ", nation_form.errors)
#         print("Exersice Form Errors ", exersice_form.errors)
#         print("Task Form Errors ", task_form.errors)
#         print("Domain Form Errors ", domain_form.errors)
#         print("Warfare Form Errors ", warfare_form.errors)
#     return render_template('multi_Domain_Operations_By_Nation_search.html', nationForm=nation_form, exersiceForm=exersice_form, taskForm=task_form,
#                            domainForm=domain_form, warfareForm=warfare_form)


if __name__ == '__main__':
    app.run(debug=True)
