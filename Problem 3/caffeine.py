
def caffeine():
    caffeine_mg = float(input())
    
    after_6 = caffeine_mg * .50
    after_12 = caffeine_mg * .50 ** 2
    after_24 = caffeine_mg * .50 ** 4

    print(f'After 6 hours: {after_6:.2f} mg')
    print(f'After 12 hours: {after_12:.2f} mg')
    print(f'After 24 hours: {after_24:.2f} mg')
    ''' Type your code here. '''
    
if __name__ == "__main__":
    caffeine()