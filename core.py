import lib.lil_tool_box as Box
import lib.parameters as parameters
import lib.bcolors as colors
import commands

def generate_script(script, body):
	p_file = parameters.parameter.SCRIPT_PATH + script
	file = open(p_file, 'w')
	file.write(body)
	file.close()

def run_command(script):
	command = parameters.parameter.SQLCOMMAND + script
	state, out = commands.getstatusoutput(command)
	return out

DB_USERS = ','.join([ "'%s'" % i for i in parameters.parameter.DB_USERS])

generate_script(parameters.parameter.GETLOCKS, Box.create_query_check_lock(DB_USERS))

fetch = run_command(parameters.parameter.GETLOCKS)
fetch = fetch.split()[2]

if fetch != '0':
	print colors.color.BOLD + colors.color.FAIL + 'Hay lockeos en la base: %s sesiones lockeadas.' + colors.color.ENDC % fetch
	msg = colors.color.WARNING + "Limpiar lockeos? (Y/N): " + colors.color.ENDC
	var = str(raw_input(msg))
	if var.upper() == "Y":
    	generate_script(parameters.parameter.KILLLOCKS, Box.create_query_kill_session(DB_USERS))
    	a = run_command(parameters.parameter.KILLLOCKS)
    	generate_script(parameters.parameter.ALTERSESSION, a)
    	Box.edit_fetched_alter_session(parameters.parameter.SCRIPT_PATH + parameters.parameter.ALTERSESSION)
    	run_command(parameters.parameter.ALTERSESSION)

else:
	print colors.color.BOLD + colors.color.OKGREEN + 'No hay lockeos.' + colors.color.ENDC