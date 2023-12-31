import matplotlib.pyplot as plt


def generate_bar_chart(name, labels: list, values: list):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'./imgs/{name}.png')
    plt.close()

def generate_pie_chart(labels: list, values: list):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig('chart_pie_final_este_si.png')
    plt.close()


if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [10, 400, 800]
    # generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)
