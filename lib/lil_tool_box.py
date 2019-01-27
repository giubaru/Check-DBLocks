def create_query_check_lock(users):
	return  '''\
set pages 200 lines 200
col ORACLE_USERNAME format a16
col OS_USER_NAME format a15
col OWNER format a10
col OBJECT_NAME format a30
col PROGRAM format a50
col OBJECT_TYPE format a15
select count(1) from (
SELECT session_id, s.serial#, oracle_username, os_user_name, owner, object_name, object_type,
s.PROGRAM, s.PROCESS FROM v$locked_object lo, all_objects ao, v$session s
WHERE lo.object_id = ao.object_id
AND lo.session_id = s.SID and owner in (%s));
exit;
''' % users

def create_query_kill_session(users):
	return """\
set pages 200 lines 200
SELECT distinct 'ALTER SYSTEM KILL SESSION ''' || SESSION_ID || ',' || SERIAL# || ''';' EXCECUTE_THIS_AS_DBA from 
(
SELECT session_id,s.serial#,s.sid, oracle_username, os_user_name, owner, object_name, object_type,
s.PROGRAM, s.PROCESS FROM v$locked_object lo, all_objects ao, v$session s
WHERE LO.OBJECT_ID = AO.OBJECT_ID
AND LO.SESSION_ID = S.SID and owner in (%s));
exit;
""" % users

def edit_fetched_alter_session(path):
	file = open(path, 'rt')
	fetch = file.readlines()[3:-1]
	fetch[-1] = 'exit;'
	fetch = ''.join(fetch) 
	file.close()
	file = open(path, 'wt')
	file.write(fetch)
	file.close()
