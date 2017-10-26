import matplotlib.pyplot as plt
import matplotlib as mpl
from tkinter import *


def print_gist(ages):
    fig = plt.figure("Гистограмма")
    plt.hist(ages)
    plt.title("Распределение возрастов")
    plt.ylabel("Количество людей, шт")
    plt.xlabel("Возраст, лет")
    plt.grid(True)
    plt.show()
