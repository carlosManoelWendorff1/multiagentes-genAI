from Classes.Agent import Agent

class ApplianceAgent(Agent):
    def communicate(self, task, agents=[]):
        for agent in agents:
            if agent.name == 'Security Agent' and task == 'no_one_home':
                print(f"{self.name} pauses appliances because {agent.name} confirmed no one is home.")
                return "Appliances Paused"
        return "No action"