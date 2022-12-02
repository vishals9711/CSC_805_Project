from interface import BreastCancerInterface


def index():
    return "Hello World"

if __name__ == "__main__":
    breastCancer = BreastCancerInterface()
    breastCancer.get_violion_plot("headers")