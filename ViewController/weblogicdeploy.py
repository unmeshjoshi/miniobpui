import re
 
warPath = 'target/dist/miniobpui.ear'
appName = 'miniobpui'

weblogicUrl = 't3://127.0.0.1:7001'
userName = 'weblogic'
password = 'weblogic1'

connect(userName, password, weblogicUrl)
 
appList = re.findall(appName, ls('/AppDeployments'))
if len(appList) >= 1:
    print 'undeploying application'
    undeploy(appName)
 
deploy(appName, path = warPath, retireTimeout = -1, upload = 'True')
 
exit()
