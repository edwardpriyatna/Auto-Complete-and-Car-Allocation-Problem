# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def ford_fulkerson(my_graph):
    flow=0 #initialize flow
    residual_network=residual_network(my_graph) #initialize the residual network
    while residual_network.has_AugmentingPath():
        path= residual_network.get_AugmentingPath()#take the path
        flow+=path.residual_capacity #augment the flow to residual capacity
        residual_network.augment_flow(path) #updating the residual network
    return flow





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(13//5+1)

