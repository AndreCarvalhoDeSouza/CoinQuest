from src.Background import Background
from src.Coin import Coin
from src.Const import WIN_WIDTH, WIN_HEIGHT
from src.Obstacle import Obstacle
from src.Player import Player


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position:tuple = (0,0)):

        ground_y = WIN_HEIGHT

        match entity_name:
            case 'level1_background':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'level1_background{i}',
                                              (0, 0)))
                    list_bg.append(Background(f'level1_background{i}',
                                              (WIN_WIDTH, 0)))
                return list_bg
            case 'level2_background':
                        list_bg = []
                        for i in range(7):
                            list_bg.append(Background(f'level2_background{i}',
                                                      (0, 0)))
                            list_bg.append(Background(f'level2_background{i}',
                                                      (WIN_WIDTH, 0)))
                        return list_bg
            case 'player':
                walk_sprite = Player.load_player('asset/player_walk.png',
                                                 64, 64, 3, 2)
                run_sprite = Player.load_player('asset/player_run.png',
                                                64, 64, 4, 2)
                hurt_sprite = Player.load_player('asset/player_hurt.png',
                                                 64, 64, 3, 2)
                death_sprite = Player.load_player('asset/player_death.png', 64, 64, 4, 2)
                current_player = Player('player', (100, ground_y + 10),
                                        walk_sprite, run_sprite, hurt_sprite, death_sprite)
                return current_player
            case 'obstacle1_level_1' | 'obstacle2_level_1' | 'obstacle1_level_2' |\
                 'obstacle2_level_2' | 'obstacle3_level_2':
                position_y = ground_y - 200
                return Obstacle(entity_name, (WIN_WIDTH, position_y))
            case 'coin_level_1'  | 'coin_level_2':
                return Coin(entity_name, position)