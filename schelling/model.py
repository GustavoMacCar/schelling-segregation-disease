from mesa import Model, Agent
from mesa.time import RandomActivation
from mesa.space import SingleGrid
from mesa.datacollection import DataCollector


class SchellingAgent(Agent):
    """
    Schelling segregation agent
    """

    def __init__(self, pos, model, agent_type, sick, spread_probability):
        """
        Create a new Schelling agent.

        Args:
           unique_id: Unique identifier for the agent.
           x, y: Agent initial location.
           agent_type: Indicator for the agent's type (minority=1, majority=0)
        """
        super().__init__(pos, model)
        self.pos = pos
        self.type = agent_type
        self.sick = {'status': sick , 'time': 3}
        self.spread_probability = spread_probability


    def step(self):
        similar = 0
        sick_neighbor =  False
        spread_disease = [True, False]
        weights = [self.spread_probability, 1-self.spread_probability]

        for neighbor in self.model.grid.neighbor_iter(self.pos):
            if neighbor.type == self.type:
                similar += 1

            if self.sick['status'][0]:
                spread = self.random.choices(spread_disease, weights)
                if spread[0]:
                    neighbor.sick['status'][0] = spread[0] 
                     

        for neighbor in self.model.grid.neighbor_iter(self.pos):
            if neighbor.sick['status'][0]:
                similar = 0
                sick_neighbor = True
                break

        if self.sick['status'][0]:
            self.model.sick_count += 1

        if self.sick['status'][0]:
            self.sick['time'] -= 1
            if self.sick['time'] <= 0:
                self.sick['status'][0] = False
                self.sick['time'] = 3
                self.model.sick_count -= 1

        # If unhappy, move:
        if similar < self.model.homophily or sick_neighbor:
            self.model.grid.move_to_empty(self)
        else:
            self.model.happy += 1


class Schelling(Model):
    """
    Model class for the Schelling segregation model.
    """

    def __init__(self, width=20, height=20, density=0.8, minority_pc=0.2, homophily=3, disease_probability=0, spread_probability=0):
        """ """

        self.width = width
        self.height = height
        self.density = density
        self.minority_pc = minority_pc
        self.homophily = homophily
        self.disease_probability = disease_probability / 100
        self.spread_probability = spread_probability / 100
        self.sick_count = 0
        self.running = True

        self.schedule = RandomActivation(self)
        self.grid = SingleGrid(width, height, torus=True)

        self.happy = 0
        self.datacollector = DataCollector(
            model_reporters=
            {"happy": "happy",
            "sick": "sick_count"},  # Model-level count of happy agents
            # For testing purposes, agent's individual x and y
            #{"x": lambda a: a.pos[0], "y": lambda a: a.pos[1]},
                        
        )


        sick = [True, False]
        weights = [self.disease_probability, 1 - self.disease_probability]

        # Set up agents
        # We use a grid iterator that returns
        # the coordinates of a cell as well as
        # its contents. (coord_iter)
        for cell in self.grid.coord_iter():
            x = cell[1]
            y = cell[2]

            disease = self.random.choices(sick, weights)

            if self.random.random() < self.density:
                if disease[0]:
                    self.sick_count += 1
                if self.random.random() < self.minority_pc:
                    agent_type = 1
                else:
                    agent_type = 0

                agent = SchellingAgent((x, y), self, agent_type, disease, self.spread_probability)
                self.grid.position_agent(agent, (x, y))
                self.schedule.add(agent)

        self.running = True
        self.datacollector.collect(self)

    def step(self):
        """
        Run one step of the model. If All agents are happy, halt the model.
        """
        self.happy = 0  # Reset counter of happy agents
        self.sick_count = 0
        self.schedule.step()
        # collect data
        self.datacollector.collect(self)

        if self.happy == self.schedule.get_agent_count():
            self.running = False
