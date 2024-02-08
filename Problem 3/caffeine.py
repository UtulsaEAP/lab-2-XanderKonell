
def caffeine():
    caffeine_mg = float(input())
    ''' Type your code here. '''
    half_life = 6
    
    caffeine_6_hours = caffeine_mg * (0.5 ** (6 / half_life))
    
    caffeine_12_hours = caffeine_mg * (0.5 ** (12 / half_life))
    
    caffeine_24_hours = caffeine_mg * (0.5 ** (24 / half_life))
    
    print(f"After 6 hours: {caffeine_6_hours:.2f} mg")
    print(f"After 12 hours: {caffeine_12_hours:.2f} mg")
    print(f"After 24 hours: {caffeine_24_hours:.2f} mg")
    
if __name__ == "__main__":
    caffeine()