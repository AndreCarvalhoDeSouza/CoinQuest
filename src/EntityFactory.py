from src.Background import Background
from src.Const import WIN_WIDTH


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'level1_background':
                list_level1_bg = []
                for i in range(5):
                    list_level1_bg.append(Background(f'level1_background{i}', (0, 0)))
                    list_level1_bg.append(Background(f'level1_background{i}', (WIN_WIDTH, 0)))
                return list_level1_bg