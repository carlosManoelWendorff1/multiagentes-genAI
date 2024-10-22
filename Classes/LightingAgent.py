from Classes.Agent import Agent

class LightingAgent(Agent):
    def communicate(self, task, agents=[]):
        for agent in agents:
            if agent.name == 'Security Agent' and task == 'motion_detected':
                print(f"{self.name} turns on the lights due to motion detection by {agent.name}")
                return "Lights On"
        return "No action"