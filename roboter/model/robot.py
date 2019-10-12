from roboter.models import ranking
from roboter.views import console

DEFAULT_ROBOT_NAME = 'Roboko'

class Robot(object):
    """Base model for Robot."""

    def __init__(self, name=DEFAULT_ROBOT_NAME, user_name='', speak_color='green'):
        self.name = name
        self.user_name = user_name
        self.speak_color = speak_color

    def hello(self):
        """Returns words to the user that the robot speaks at the beginning"""
        while True:
            template = console.get_template('hello.txt', self.speak_color)
            user_name = input(template.substitute({
                'robot_name' : self.name}))

            if user_name:
                self.user_name = user_name.title()
                break



class RestaurantRobot(Robot):
    """Handle data model on restaurant."""

    def __init__(self, name = DEFAULT_ROBOT_NAME):
        super().__init__(name=name)
        self.ranking_model = ranking.RankingModel()

    def _hello_decorator(func):
        """Decorator to say a greeting if you are not greeting the user."""
        def wrapper(self):
            if not self.user_name:
                self.hello()
            return func(self)
        return wrapper

    @_hello_decorator
    def recommend_restaurant(self):
        """Show restaurant recommended restaurant to the user."""
        new_recommended_restaurant = self.ranking_model.get_most_popular()
        if not new_recommended_restaurant:
            return None