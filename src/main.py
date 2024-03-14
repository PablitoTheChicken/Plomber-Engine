from engine import *

def main():
    engine = Engine()
    engine.createWindow((800,800))
    
    while True:
        deltaTime = engine.tick(60)
        
        # Base Engine Loop
        engine.registerEvents()
        engine.physicsStep(deltaTime)
        engine.render(deltaTime)
        
    
if __name__ == "__main__":
    main()