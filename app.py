from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import widgets, SelectMultipleField
import grafana.dashboard_editor_via_api as gfapi

SECRET_KEY = 'development'
app = Flask(__name__)
app.config.from_object(__name__)

# GLOBAL VARIABLES

# Grafana configs
GF_DASHBOARD_UID = '1MB0c91Vz'

# Grafana host details
GF_USERNAME = 'admin'
GF_PASSWORD = 'qwerty'
GF_IP_ADDR = 'grafana'  # with docker compose, the ip_addr is just the name of the service
GF_PORT = '3000'


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


class TaskFrom(FlaskForm):
    string_of_tasks = ['Data_Centric_Security_Approach\r\nConformance_Testing\r\n'
                              'De-risking_Coalition_Operations\r\nCross-Domain_Solutions\r\nData_and_Analytics\r\n'
                              'Connecting_sensor_-_decision_maker_-_effector\r\nFederated_Mission_Networking\r\n'
                              'Multi-Domain_Operations\r\nStandards_Validation\r\n']
    list_of_tasks = string_of_tasks[0].split()
    # create a list of value/description tuples
    files = [(x, x) for x in list_of_tasks]
    capabilityResult = MultiCheckboxField('Label', choices=files)


class ExersiceFrom(FlaskForm):
    string_of_exersices = ['CWIX_2021\r\nCWIX_2022\r\n']
    list_of_exersices = string_of_exersices[0].split()
    # create a list of value/description tuples
    files = [(x, x) for x in list_of_exersices]
    exersiceResult = MultiCheckboxField('Label', choices=files)


def underscore_replacer(capability):
    capability = ''.join(capability)
    print(capability)
    return capability.replace('_', ' ')


def change_Nation_Mapping(nation_list):
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
    nation_list = ''.join(nation_list)
    return str(nation_mapping[nation_list])


def nation_form_validation(nation_form, nation_form_result, exercise_form, exersice_form_result, html_page_received, query, query2, query3, panel_title_prefix):
    if nation_form.validate_on_submit() and exercise_form.validate_on_submit():
        selected_nation = nation_form_result
        selected_exersise = exersice_form_result
        selected_nation = change_Nation_Mapping(selected_nation)
        selected_exersise = underscore_replacer(selected_exersise)
        complete_query = query + selected_nation + query2 + selected_exersise + query3

        # Create new panel in the grafana dashboard
        panel_title = "{} {}".format(panel_title_prefix, selected_nation)
        gfapi.create_panel_on_grafana(GF_USERNAME, GF_PASSWORD, GF_IP_ADDR, GF_PORT, GF_DASHBOARD_UID, complete_query, panel_title)

        return render_template("by_nation_result.html", completeQuery=complete_query)
    else:
        print("Validation Failed")
        print("Form Errors ", nation_form.errors)

    return render_template(html_page_received, nationForm=nation_form, exersiceForm=exercise_form)


@app.route('/', methods=['post', 'get'])
def init_state():
    return render_template('index.html')


@app.route('/see_nation_capabilitie_by_exersise.html', methods=['post', 'get'])
def see_nation_capabilitie_by_exersise():
    # Generate Form
    nation_form = NationForm()
    task_form = TaskFrom()
    exersise_form = ExersiceFrom()
    # Initial Query
    query = "select c.name AS CAPABILITY_NAME, t2.name, n.name AS NATION_NAME, tp.exercise_cycle from" \
            " test_participants tp  inner join testcases t on t.id = tp.capability_id " \
            "inner join capability_tasks ct on t.id = ct.task_id  inner join tasks t2 on t2.id = ct.task_id  " \
            "inner join capabilities c on c.id = ct.capability_id  " \
            "inner join nations n on n.id = c.nation_id " \
            "where tp.exercise_cycle = '"
    query2 = "' and n.id = "
    query3 = " and t2.name = '"
    query4 = "'"
    # Form Validation and automatic generation of user query
    if nation_form.validate_on_submit():
        selected_nation = nation_form.nationResult.data
        selected_capability = task_form.capabilityResult.data
        selected_exercise = exersise_form.exersiceResult.data
        selected_nation = change_Nation_Mapping(selected_nation)
        selected_capability = underscore_replacer(selected_capability)
        selected_exercise = underscore_replacer(selected_exercise)
        complete_query = query + selected_exercise + query2 + selected_nation + query3 + selected_capability + query4
        
        # Create new panel in the grafana dashboard
        panel_title = 'Multidomain Operation Capability <{}> for Nation {}'.format(selected_capability, selected_nation)
        gfapi.create_panel_on_grafana(GF_USERNAME, GF_PASSWORD, GF_IP_ADDR, GF_PORT, GF_DASHBOARD_UID, complete_query, panel_title)

        print(complete_query)

        return render_template("by_nation_result.html", completeQuery=complete_query)
    else:
        print("Validation Failed")
        print("Nation Form Errors ", nation_form.errors)

    return render_template('see_nation_capabilitie_by_exersise.html', nationForm=nation_form, capabilityForm=task_form,
                           exersiceForm=exersise_form)


@app.route('/ineroperability_issues_by_nation_search.html', methods=['post', 'get'])
def interoperability_issue_by_nation():
    # Generate Form
    nation_form = NationForm()
    exercise_form = ExersiceFrom()
    # Initial Query
    query = "select n.name as Nation_Name, t.tc_number as testcase_number, t.exercise_cycle, t.overall_result from" \
            " testcases t inner join test_participants tp on t.id = tp.testcase_id " \
            "inner join capabilities c on c.id = tp.capability_id  " \
            "inner join nations n on n.id = c.nation_id " \
            "where t.overall_result = 'Interoperability Issue' and n.id = "
    query2 = " and t.exercise_cycle = '"
    query3 = "'"
    # Form Validation and automatic generation of user query
    panel_title_prefix = 'Interoperability Issues for Specified Country: '
    return nation_form_validation(nation_form, nation_form.nationResult.data, exercise_form, exercise_form.exersiceResult.data,
                                  'ineroperability_issues_by_nation_search.html', query, query2, query3, panel_title_prefix)


@app.route('/multi_lateral_interoperability_program_by_nation_search.html', methods=['post', 'get'])
def multi_lateral_interoperablility_program_by_nation():
    # Generate Form
    nation_form = NationForm()
    exercise_form = ExersiceFrom()
    # Initial Query
    query = "select n.name as Nation_Name, fa.name as focus_area_name, o.name as objective_name, t.exercise_cycle " \
            "from focus_areas fa inner join objectives o on o.focus_area_id = fa.id inner join test_objectives to2" \
            " on to2.objective_id  = o.id inner join testcases t on t.id = to2.testcase_id inner join" \
            " test_participants tp on tp.testcase_id  = t.id inner join capabilities c on c.id = tp.capability_id" \
            " inner join nations n on n.id = c.nation_id where fa.name = 'Multilateral Interoperability Programme'" \
            " and n.id = "
    query2 = " and t.exercise_cycle = '"
    query3 = "'"
    # Form Validation and automatic generation of user query
    panel_title_prefix = 'Multilateral Interoperability Programmes for Nation: '
    return nation_form_validation(nation_form, nation_form.nationResult.data, exercise_form, exercise_form.exersiceResult.data,
                                  'multi_lateral_interoperability_program_by_nation_search.html', query, query2, query3, panel_title_prefix)


@app.route('/cross_domain_solution_by_nation_search.html', methods=['post', 'get'])
def cross_domain_solution_by_nation():
    # Generate Form
    nation_form = NationForm()
    exercise_form = ExersiceFrom()
    # Initial Query
    query = "select c.name AS CAPABILITY_NAME, t2.name, n.name AS NATION_NAME, tp.exercise_cycle from " \
            "test_participants tp inner join testcases t on t.id = tp.capability_id " \
            "inner join capability_tasks ct on t.id = ct.task_id " \
            "inner join tasks t2 on t2.id = ct.task_id " \
            "inner join capabilities c on c.id = ct.capability_id inner join nations n on n.id = c.nation_id " \
            "where t2.name = 'Cross-Domain Solutions' and n.id = "
    query2 = " and tp.exercise_cycle = '"
    query3 = "'"
    # Form Validation and automatic generation of user query
    panel_title_prefix = 'Multilateral Interoperability Programmes for Nation: '
    return nation_form_validation(nation_form, nation_form.nationResult.data, exercise_form, exercise_form.exersiceResult.data,
                                  'cross_domain_solution_by_nation_search.html', query, query2, query3, panel_title_prefix)


@app.route('/multi_domain_solution_by_nation_search.html', methods=['post', 'get'])
def multi_domain_solution_by_nation():
    # Generate Form
    nation_form = NationForm()
    # Initial Query
    query = "select n.name AS NATION_NAME, t.name as task_type, c.name AS CAPABILITY_NAME  from tasks t inner join" \
            " capability_tasks ct on t.id = ct.task_id inner join capabilities c on c.id = ct.capability_id inner" \
            " join nations n on n.id = c.nation_id where t.name = 'Multi-Domain Operations' and n.id = "
    # Form Validation and automatic generation of user query
    panel_title_prefix = 'Multidomain Solutions for Nation: '
    return nation_form_validation(nation_form, nation_form.nationResult.data,
                                  'multi_domain_solution_by_nation_search.html', query, panel_title_prefix)


@app.route('/cross_dom_solution_&_multi_dom_ops_by_nation_search.html', methods=['post', 'get'])
def multi_domain_solution_and_cross_dom_sol_by_nation():
    # Generate Form
    nation_form = NationForm()
    # Initial Query
    query = "select n.name AS NATION_NAME, t.name as task_type, c.name AS CAPABILITY_NAME  from tasks t inner join " \
            "capability_tasks ct on t.id = ct.task_id inner join capabilities c on c.id = ct.capability_id inner " \
            "join nations n on n.id = c.nation_id where (t.name = 'Multi-Domain Operations' or t.name = " \
            "'Cross-Domain Solutions') and n.id = "
    # Form Validation and automatic generation of user query
    panel_title_prefix = 'Cross Domain and Multi Domain Operations for Nation: '
    return nation_form_validation(nation_form, nation_form.nationResult.data,
                                  'cross_dom_solution_&_multi_dom_ops_by_nation_search.html', query)


@app.route('/compare_two_nations_capabilities.html', methods=['post', 'get'])
def measure_cap_between_two_nations():
    # Generate Form
    nation1_form = NationForm()
    nation2_form = NationForm()
    capability_form = TaskFrom()
    # Initial Query
    query = "select new_table.NATION_NAME, count(new_table.CAPABILITY_NAME) from" \
            " (	" \
            "select n.name AS NATION_NAME, t.name as task_type, c.name AS CAPABILITY_NAME  from tasks t " \
            "inner join capability_tasks ct on t.id = ct.task_id " \
            "inner join capabilities c on c.id = ct.capability_id " \
            "inner join nations n on n.id = c.nation_id where t.name = '"
    query2 = "' and n.id = "
    query3 = " union	" \
             "select n.name AS NATION_NAME, t.name as task_type, c.name AS CAPABILITY_NAME  from tasks t " \
             "inner join capability_tasks ct on t.id = ct.task_id " \
             "inner join capabilities c on c.id = ct.capability_id " \
             "inner join nations n on n.id = c.nation_id where t.name = '"
    query4 = "' and n.id = "
    query5 = " ) as new_table group by new_table.NATION_NAME"
    # Form Validation and automatic generation of user query
    if nation1_form.validate_on_submit() and nation2_form.validate_on_submit() and capability_form.validate_on_submit():
        selected_nation1 = nation1_form.nationResult.data[0]
        selected_nation2 = nation2_form.nationResult.data[1]
        selected_capability = capability_form.capabilityResult.data
        underscore_replacer(selected_capability)
        selected_nation1 = change_Nation_Mapping(selected_nation1)
        selected_nation2 = change_Nation_Mapping(selected_nation2)
        selected_capability = underscore_replacer(selected_capability[0])
        complete_query = query + selected_capability + query2 + selected_nation1 + query3 + selected_capability + query4 + selected_nation2 + query5
        # Create new panel in the grafana dashboard
        panel_title = 'Compare Capability <{}> for Nations: {}, {}'.format(selected_capability, selected_nation1, selected_nation2)
        gfapi.create_panel_on_grafana(GF_USERNAME, GF_PASSWORD, GF_IP_ADDR, GF_PORT, GF_DASHBOARD_UID, complete_query, panel_title)

        return render_template("compare_nation_results.html",
                               nation1Data=selected_nation1, nation2Data=selected_nation2,
                               capabilityData=selected_capability, completeQuery=complete_query)

    else:
        print("Validation Failed")
        print("Nation 1 Form Errors ", nation1_form.errors)
        print("Nation 2 Form Errors ", nation1_form.errors)
        print("Capability Form Errors ", capability_form.errors)

        return render_template('compare_two_nations_capabilities.html', nation1Form=nation1_form,
                               nation2Form=nation2_form, capabilityForm=capability_form)


@app.route('/interoperability_issues_between_two_nations.html', methods=['post', 'get'])
def interops_issue_between_two_nations():
    # Generate Form
    nation1_form = NationForm()
    nation2_form = NationForm()
    # Initial Query
    query = "select new_table.NATION_NAME, count(new_table.overall_result) from" \
            "	( select n.name as Nation_Name, t.tc_number as testcase_number, t.exercise_cycle, t.overall_result from" \
            " testcases t	inner join test_participants tp on t.id = tp.testcase_id " \
            "inner join capabilities c on c.id = tp.capability_id " \
            "inner join nations n on n.id = c.nation_id " \
            "where t.overall_result = 'Interoperability Issue' and n.id = "
    query2 = "union select n.name as Nation_Name, t.tc_number as testcase_number, t.exercise_cycle, t.overall_result " \
             "from testcases t inner join test_participants tp on t.id = tp.testcase_id " \
             "inner join capabilities c on c.id = tp.capability_id " \
             "inner join nations n on n.id = c.nation_id where t.overall_result = 'Interoperability Issue' and n.id = "
    query3 = " ) as new_table group by new_table.NATION_NAME"
    # Form Validation and automatic generation of user query
    if nation1_form.validate_on_submit() and nation2_form.validate_on_submit():
        selected_nation1 = nation1_form.nationResult.data[0]
        selected_nation2 = nation2_form.nationResult.data[1]
        selected_nation1 = change_Nation_Mapping(selected_nation1)
        selected_nation2 = change_Nation_Mapping(selected_nation2)
        complete_query = query + selected_nation1 + query2 + selected_nation2 + query3
        # Create new panel in the grafana dashboard
        panel_title = 'Interoperability issues between 2 nations: {}, {}'.format(selected_nation1, selected_nation2)
        gfapi.create_panel_on_grafana(GF_USERNAME, GF_PASSWORD, GF_IP_ADDR, GF_PORT, GF_DASHBOARD_UID, complete_query, panel_title)

        return render_template("compare_nation_results.html",
                               nation1Data=selected_nation1, nation2Data=selected_nation2, completeQuery=complete_query)

    else:
        print("Validation Failed")
        print("Nation 1 Form Errors ", nation1_form.errors)
        print("Nation 2 Form Errors ", nation1_form.errors)

        return render_template('interoperability_issues_between_two_nations.html', nation1Form=nation1_form,
                               nation2Form=nation2_form)


@app.route('/measure_two_capabilities_between_two_nations.html', methods=['post', 'get'])
def measure_two_cap_between_two_nations():
    # Generate Form
    nation1_form = NationForm()
    nation2_form = NationForm()
    capability_form = TaskFrom()
    capability2_form = TaskFrom()
    # Initial Query
    query = "select new_table.NATION_NAME, count(new_table.capability_name) from " \
            "( select n.name AS NATION_NAME, t.name as task_type, c.name AS CAPABILITY_NAME  " \
            "from tasks t inner join capability_tasks ct on t.id = ct.task_id " \
            "inner join capabilities c on c.id = ct.capability_id " \
            "inner join nations n on n.id = c.nation_id where (t.name = '"
    query2 = "' or t.name = '"
    query3 = "') and n.id = "
    query4 = "6 union select n.name AS NATION_NAME, t.name as task_type, c.name AS CAPABILITY_NAME" \
             "  from tasks t inner join capability_tasks ct on t.id = ct.task_id " \
             "inner join capabilities c on c.id = ct.capability_id inner join nations n on n.id = c.nation_id " \
             "where (t.name = '"
    query5 = "' or t.name = '"
    query6 = "') and n.id = "
    query7 = "as new_table group by new_table.NATION_NAME"
    # Form Validation and automatic generation of user query
    if nation1_form.validate_on_submit() and nation2_form.validate_on_submit() and capability_form.validate_on_submit():
        selected_nation1 = nation1_form.nationResult.data[0]
        selected_nation2 = nation2_form.nationResult.data[1]
        selected_capability1 = capability_form.capabilityResult.data[0]
        selected_capability2 = capability_form.capabilityResult.data[1]
        selected_capability1 = underscore_replacer(selected_capability1)
        selected_capability2 = underscore_replacer(selected_capability2)
        selected_nation1 = change_Nation_Mapping(selected_nation1)
        selected_nation2 = change_Nation_Mapping(selected_nation2)
        complete_query = query + selected_capability1 + query2 + selected_capability2 + query3 + selected_nation1 + query4 + selected_capability1 + query5 + selected_capability2 + query6 + selected_nation2 + query7
        # Create new panel in the grafana dashboard
        panel_title = 'Measure 2 Capabilities between 2 Nations: {}, {}, {}, {}'.format(selected_capability1, selected_capability2, selected_nation1, selected_nation2)
        gfapi.create_panel_on_grafana(GF_USERNAME, GF_PASSWORD, GF_IP_ADDR, GF_PORT, GF_DASHBOARD_UID, complete_query, panel_title)

        return render_template("compare_nation_results.html",
                               nation1Data=selected_nation1, nation2Data=selected_nation2,
                               capabilityData=selected_capability1, completeQuery=complete_query)

    else:
        print("Validation Failed")
        print("Nation 1 Form Errors ", nation1_form.errors)
        print("Nation 2 Form Errors ", nation1_form.errors)
        print("Capability Form Errors ", capability_form.errors)
        print("Capability 2 From Errors ", capability2_form.errors)

        return render_template('measure_two_capabilities_between_two_nations.html', nation1Form=nation1_form,
                               nation2Form=nation2_form, capabilityForm=capability_form,
                               capability2Form=capability2_form)


@app.route('/capability_maturity_by_nation.html', methods=['post', 'get'])
def cap_mat_by_nation():
    # Generate Form
    nation_form = NationForm()
    capability_form = TaskFrom()
    # Initial Query
    query = "select table1.capability_maturity, count(capability_maturity) as cap_mat from " \
            "( select n.name as nation_name, c.name as capability_name, c.maturity as capability_maturity, " \
            "t.name as task_name from nations n inner join capabilities c on c.nation_id = n.id " \
            "inner join capability_tasks ct on ct.capability_id = c.id inner join tasks t on t.id = ct.task_id " \
            "where n.id = "
    query2 = " and t.name = '"
    query3 = "' and c.maturity = 'Near-Fielded' ) as table1 group by table1.capability_maturity " \
             "union select table2.capability_maturity, count(capability_maturity) as cap_mat " \
             " from ( select n.name as nation_name, c.name as capability_name, c.maturity as capability_maturity," \
             " t.name as task_name from nations n inner join capabilities c on c.nation_id = n.id " \
             "inner join capability_tasks ct on ct.capability_id = c.id inner join tasks t on t.id = ct.task_id" \
             " where n.id = "
    query4 = " and t.name= '"
    query5 = "'  and c.maturity = 'Fielded' ) as table2 group by table2.capability_maturity union " \
             "select table3.capability_maturity, count(capability_maturity) as cap_mat  " \
             "from ( select n.name as nation_name, c.name as capability_name, c.maturity as " \
             "capability_maturity, t.name as task_name from nations n inner join capabilities c on" \
             " c.nation_id = n.id inner join capability_tasks ct on ct.capability_id = c.id " \
             "inner join tasks t on t.id = ct.task_id where n.id = "
    query6 = " and t.name = '"
    query7 = "' and c.maturity = 'Developmental' ) as table3 group by table3.capability_maturity union" \
             " select table4.capability_maturity, count(capability_maturity) as cap_mat  from" \
             " ( select n.name as nation_name, c.name as capability_name, c.maturity as capability_maturity," \
             " t.name as task_name from nations n inner join capabilities c on c.nation_id = n.id " \
             "inner join capability_tasks ct on ct.capability_id = c.id " \
             "inner join tasks t on t.id = ct.task_id where n.id = "
    query8 = " and t.name = '"
    query9 = "' and c.maturity = 'Experimental' ) as table4 group by table4.capability_maturity"
    if nation_form.validate_on_submit() and capability_form.validate_on_submit():
        selected_nation = nation_form.nationResult.data
        selected_nation = change_Nation_Mapping(selected_nation)
        selected_capability = capability_form.capabilityResult.data
        selected_capability = underscore_replacer(selected_capability)
        complete_query = query + selected_nation + query2 + selected_capability + query3 + selected_nation + query4 + selected_capability + query5 + selected_nation + query6 + selected_capability + query7 + selected_nation + query8 + selected_capability + query9
        # Create new panel in the grafana dashboard
        panel_title = "Capability Maturity for Nation {} for Capabilities <{}>".format(selected_nation, selected_capability)
        gfapi.create_panel_on_grafana(GF_USERNAME, GF_PASSWORD, GF_IP_ADDR, GF_PORT, GF_DASHBOARD_UID, complete_query, panel_title)
        return render_template('compare_nation_results.html', nation1data=selected_nation, capabilityData=selected_capability)
    else:
        print("Validation Failed")
        print("Nation Form Errors ", nation_form.errors)
        print("Capability Form Errors ", capability_form.errors)

        return render_template('capability_maturity_by_nation.html', nationForm=nation_form,
                               capabilityForm=capability_form)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
