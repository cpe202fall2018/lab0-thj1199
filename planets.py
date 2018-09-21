def weight_on_planets():
    weight = int(input("What do you weigh on earth? "))
    mars = weight * 0.38
    jupiter = weight * 2.34
    print("\nOn Mars you would weigh " + str(mars) + " pounds.")
    print("On Jupiter you would weigh " + str(jupiter) + " pounds.")

if __name__ == '__main__':
    weight_on_planets()
