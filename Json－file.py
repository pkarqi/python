
import json
import time
import requests
import simplejson
response1 = requests.get("http://xx.xx.xx.158:9200/_nodes/stats?pretty&filter_path=**.host,**.jvm.mem")
new_dic = response1.text
ret_dict = simplejson.loads(response1.text)
ret = {ret_dict['nodes'][key]['host']: ret_dict['nodes'][key]['jvm']['mem']['pools']['old']['used_in_bytes'] for key in ret_dict['nodes'].keys()}
print ret
#for v  in ret_dict['nodes'].values():
#    print v
#for k in ret_dict['nodes'].keys():
#    print k
print ret.keys()
print  ret.values()
#print ret


#for key in ret_dict['nodes'].keys():
#    print key
