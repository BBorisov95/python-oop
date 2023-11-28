from typing import List, Union
from project.robots.male_robot import MaleRobot
from project.robots.female_robot import FemaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:

    VALID_SERVICES = {'MainService': MainService,
                      'SecondaryService': SecondaryService}

    VALID_ROBOTS = {'MaleRobot': MaleRobot,
                    'FemaleRobot': FemaleRobot}

    def __init__(self):
        self.robots: List[Union[MaleRobot, FemaleRobot]] = []
        self.services: List[Union[MainService, SecondaryService]] = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICES:
            raise Exception('Invalid service type!')
        service_to_add = self.VALID_SERVICES[service_type](name)
        self.services.append(service_to_add)
        return f'{service_type} is successfully added.'

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOTS:
            raise Exception('Invalid robot type!')
        robot_to_add = self.VALID_ROBOTS[robot_type](name, kind, price)
        self.robots.append(robot_to_add)
        return f'{robot_type} is successfully added.'

    def add_robot_to_service(self, robot_name: str, service_name: str):
        service = self._get_service_by_name(service_name)
        robot_to_add = self._get_robot_by_name(robot_name)
        if service.capacity <= len(service.robots):
            raise Exception('Not enough capacity for this robot!')
        return self._add_robot_to_service(robot_to_add, service)

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self._get_service_by_name(service_name)
        robot_to_remove = self._get_specific_robot_from_service(robot_name, service)
        if not robot_to_remove:
            raise Exception("No such robot in this service!")
        service.robots.remove(robot_to_remove)
        self.robots.append(robot_to_remove)
        return f'Successfully removed {robot_name} from {service_name}.'

    def feed_all_robots_from_service(self, service_name: str):
        service_robots = self._get_all_robots_from_service(service_name)
        for robot in service_robots:
            robot.eating()
        return f'Robots fed: {len(service_robots)}.'

    def service_price(self, service_name: str):
        service_robots = self._get_all_robots_from_service(service_name)
        total_cost = sum([r.price for r in service_robots])
        return f'The value of service {service_name} is {total_cost:.2f}.'

    def _get_service_by_name(self, service_name):
        service = next((s for s in self.services if s.name == service_name), None)
        return service

    def _get_robot_by_name(self, robot_name):

        robot = next((r for r in self.robots if r.name == robot_name), None)
        return robot

    def _add_robot_to_service(self, robot, service):

        if robot.POSSIBLE_SERVICE == service.__class__.__name__:
            service.robots.append(robot)
            self.robots.remove(robot)
            return f'Successfully added {robot.name} to {service.name}.'
        return f'Unsuitable service.'

    def _get_all_robots_from_service(self, service_name):
        service_name = self._get_service_by_name(service_name)
        return service_name.robots

    @staticmethod
    def _get_specific_robot_from_service(robot_name, service):
        specific_robot = next((r for r in service.robots if r.name == robot_name), None)
        return specific_robot

    def __str__(self):
        result = []
        for service in self.services:
            result.append(service.details())
        return '\n'.join(result)
