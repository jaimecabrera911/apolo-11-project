from datetime import datetime


class Report:
    def __init__(self, mission: str, device: str, state: str):
        self.date = f"{datetime.now().strftime('%Y%m%d%H%M%S')}"
        self.mission = mission
        self.device = device
        self.state = state
        self.hash = self.__hash__()

    def __hash__(self) -> int:
        if self.mission != "Unknown":
            return hash((self.date, self.mission, self.device, self.state))
        else:
            return 0

    def to_dict(self):
        return {
            'date': self.date,
            'mission': self.mission,
            'device': self.device,
            'state': self.state,
            'hash': self.hash
        }
