class parameter:
	GETLOCKS = 'getLocks.sql'
	KILLLOCKS = 'killLocks.sql'
	SCRIPT_PATH = './tmp/'
	DB_USERS = ['TFADB77','TFADBO77']
	STR_CONN = 'AIM_DBA/AIM_DBA@EPCMABP2'
	SQLCOMMAND = 'sqlplus -s %s @%s' %(STR_CONN,SCRIPT_PATH)