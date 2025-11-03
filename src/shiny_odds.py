import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import seaborn as sb

plt.rcParams.update({
    'text.usetex':False,
    'font.family':'sans-serif'
})

def exp_analytical(mean, a, b):
    rate = 1/mean

    return np.exp(-rate*a) - np.exp(-rate*b)

def numerical(func,mean, a, b):
    ans = quad(func, a, b, args=mean)[0]

    return ans

def PDF(x, mean):
    rate = 1/mean

    return rate*np.exp(-rate*x)

def plot(x, func, mean, a, b):
    sb.set_style('darkgrid')
    plt.figure()
    plt.xlabel('# of encounters', size = 15)
    plt.ylabel('PDF', size = 15)
    y = func(x, mean)
    plt.plot(x, y, color = 'black')

    if b==np.inf:
        plt.fill_between(x, y, 0, where=(x>a), color='grey')
        plt.title(f'P(x > {a}) = '
                  f'{np.mean([exp_analytical(mean, a, b), numerical(func, mean, a, b)]) * 100:.2f} %'
                  , size = 15)

    else:
        plt.fill_between(x, y, 0, where=(x>=a) & (x<=b), color = 'grey')
        plt.title(f'P({a} < x < {b}) = '
                  f'{np.mean([exp_analytical(mean, a, b), numerical(func, mean, a, b)]) * 100:.2f} %'
                  , size=15)


    plt.tight_layout()
    plt.show()

def main():

    # CHANGE ACCORDING TO GAME
    mean = 8192

    x = np.linspace(0, 50000, 1000000)

    while True:
        try:
            a = int(input('\nPlease input the lower value: '))

            break
        except ValueError:
            print('\nInvalid entry, please try again')

    while True:
        try:
            b = input('\nPlease input upper value ("inf" for infinity): ')

            b = int(b)

            if b>a:
                break
            else:
                print('b must be greater than a. Try again.')

        except ValueError:
            if b=='inf':
                b = np.inf

                break
            else:
                print('\nInvalid entry, Please try again')

    analytical_prob = exp_analytical(mean, a, b)

    numerical_prob = numerical(PDF, mean, a, b)
    
    print(f'\nMean shiny encounters: {mean}\n')
	
    print('\n{0:^25}|'.format(''),
          '{0:^25}|'.format('analytical (%)'),
          '{0:^25}'.format('numerical (%)'))

    print('{0:^25}|'.format(f'P({a} < x < {b})'),
          '{0:^25.2f}|'.format(analytical_prob*100),
          '{0:^25.2f}\n'.format(numerical_prob*100))

    layman_probability = 1/(np.mean([analytical_prob, numerical_prob]))

    if layman_probability<2:
        pass
    else:
        print(f"In layman's terms: the probability of encountering a shiny is 1 "
              f"in {int(np.round(layman_probability))}\n")


    plot(x, PDF, mean, a, b)

if __name__ == '__main__':
    main()
