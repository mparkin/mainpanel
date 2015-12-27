import json

settings_json = json.dumps([
#	{'type': 'title',
#	 'title': 'Pump System Settings v0.5A'},

        {'type' : 'bool',
         'title': 'A boolean setting',
         'desc' : 'Boolean description text',
         'section' : 'operation',
         'key' : 'boolexample'},

        {'type': 'string',
         'title' : 'Flow Rate',
         'section' : 'operation',
         'key'   : 'flowRate'},

        {'type' : 'options',
         'title': 'Mode',
         'desc' : 'Operational Mode of Pump',
         'section' : 'operation',
         'key'  : 'Mode',
         'options' : ['Run', 'Timed', 'Sequenced']},

        {'type'  : 'string',
         'title' : 'Pump Address',
         'desc'  : 'IP Address of Pump',
         'section': 'operation',
         'key'   : 'PumpAddress'},

        {'type' : 'path',
         'title': 'A path setting',
         'desc' : 'Path description text',
         'section' : 'operation',
         'key' : 'pathexample'}])

