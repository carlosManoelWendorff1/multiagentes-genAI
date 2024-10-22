from Classes.ApplianceAgent import ApplianceAgent
from Classes.LightingAgent import LightingAgent
from Classes.SecurityAgent import SecurityAgent

# Instantiate agents
lighting_agent = LightingAgent('Lighting Agent')
security_agent = SecurityAgent('Security Agent')
appliance_agent = ApplianceAgent('Appliance Agent')

# Simulate interaction
task_from_security = security_agent.communicate('check_motion')
lighting_agent.communicate(task_from_security, [security_agent])
appliance_agent.communicate('no_one_home', [security_agent])
