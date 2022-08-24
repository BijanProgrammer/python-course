from manager import Manager
from ui import Ui

if __name__ == "__main__":
    manager = Manager()
    ui = Ui(manager)
    
    while True:
        result = ui.main_menu()
        if result == -1:
            break
    
    manager.save_data()
