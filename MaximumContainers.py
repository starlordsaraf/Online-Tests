def maximumContainers(scenarios):
    answer = []
    for scene in scenarios:
        scene = scene.split()
        budget = int(scene[0])
        price_per_container = int(scene[1])
        exchange_price = int(scene[2])

        total = 0

        containers_bought = budget//price_per_container

        total+=containers_bought
        new_containers= 1000000000000

        while(new_containers>0):
            new_containers = containers_bought//exchange_price
            total+=new_containers
            containers_bought = new_containers + containers_bought%exchange_price
        
        answer.append(total)

    return(answer)

print(maximumContainers(["10 2 5","12 4 4","6 2 2"]))