#!/usr/bin/python2.7

DOCUMENTATION = ''' 
--- 
module: my_monitoring_module 
short_description: This is my server cpu-memory monitoring module. 
version_added: "2.4" 
description: 
- "This is my cpu-memory monitoring module to show 'n' peak processes at the time of module call." 
options: 
pid: 
description: 
- This is the value same as pid denoting process id. 
required: true 
ppid: 
description: 
- This is the value same as ppid denoting parent process id. 
required: true 
cmd: 
description: 
- This is the value same as cmd denoting the command in process. 
required: false 
mem: 
description: 
- This is the value same as mem denoting the memory in percent for a process. 
required: true 
alias: memory 
cpu: 
description: 
- This is the value same as cpu denoting the cpu usage in percent for a process. 
required: true 
sort: 
description: 
- This is the value as either cpu or mem to sort by the order of cpu usage or memory usage. 
required: true 
num: 
description: 
- This is the value to output the number of peak processes. 
required: true 
author: 
- Nitin (@4hathacker) 
'''

from ansible.module_utils.basic import * 
import subprocess

def main(): 
   # defining the available arguments/parameters 
   # the user must pass to module 
   module = AnsibleModule( 
      argument_spec = dict( 
         pid = dict(required=True, type='str'), 
         ppid = dict(required=True, type='str'), 
         cmd = dict(required=False, type='str'), 
         mem = dict(aliases=['memory'], required=True, type='str'), 
         cpu = dict(required=True, type='str'), 
         sort = dict(required=True, type='str'), 
         num = dict(required=True, type='str') 
      ), 
      # module supports check_mode 
      # but value at exit remain unchanged 
      # as its for monitoring pusrpose only 
      supports_check_mode=True 
   )

   if module.check_mode: 
      module.exit_json(changed=False) 
      params = module.params 
      # passing the params to a shell command 
      # command = 'ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head -n num' 
      # passing the command in subprocess module 

   if module.params['cmd'] is None: 
      process = subprocess.Popen("ps -eo" +  \
                module.params['pid'] + "," + \
                module.params['ppid'] + ",%" + \
                module.params['mem'] + ",%" + \
                module.params['cpu'] + " \
                --sort=-%" + \
                module.params['sort'] + \
                " | head -n " + module.params['num'],\
                shell=True, \
                stdout=subprocess.PIPE, \
                close_fds=True) 
   else: 
      process = subprocess.Popen("ps -eo" + \
                module.params['pid'] + "," + \
                module.params['cmd'] + "," + \
                module.params['ppid'] + ",%" + \
                module.params['mem'] + ",%" + \
                module.params['cpu'] + " \
                --sort=-%" + \
                module.params['sort'] + \
                " | head -n " + module.params['num'], \
                shell=True, \
                stdout=subprocess.PIPE, \
                close_fds=True) 

   exists = process.communicate()[0] # getting result if process is not None 
   if exists: 
      result = exists.split('\n') 
      module.exit_json(changed=True, meminfo=result) 
   else: 
      err_info = "Error Occured: Not able to get peak cpu info" 
      module.fail_json(msg=err_info)

if __name__ == '__main__': 
   main()


