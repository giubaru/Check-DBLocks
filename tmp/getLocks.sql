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
AND lo.session_id = s.SID and owner in ('TFADB77','TFADBO77'));
