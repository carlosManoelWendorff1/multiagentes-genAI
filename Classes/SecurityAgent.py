from Classes.Agent import Agent

class SecurityAgent(Agent):
    def communicate(self, task, agents=[]):
        if task == 'check_motion':
            print(f"{self.name} detected motion.")
            return "motion_detected"
        else:
            return "No motion"
