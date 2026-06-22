import pygame
from src.Coin import Coin
from src.Obstacle import Obstacle

class EntityMediator:

    @staticmethod
    def check_collisions(entity_list, player, level_instance):
        
        coin_sound = pygame.mixer.Sound('asset/coin.wav')
        collision_sound = pygame.mixer.Sound('asset/collision.wav')
        
        player_hitbox = pygame.Rect(0, 0, 60, 90)

        player_hitbox.centerx = player.rect.centerx
        player_hitbox.bottom = player.rect.bottom - 15

        for ent in entity_list[:]:
            
            if isinstance(ent, Coin) and player_hitbox.colliderect(ent.rect):
                coin_sound.play()
                level_instance.collected_coins += 1
                entity_list.remove(ent)
                continue

            if isinstance(ent, Obstacle) and player_hitbox.colliderect(ent.rect):
                obstacle_hitbox = pygame.Rect(0, 0, 120, 90)
                obstacle_hitbox.centerx = ent.rect.centerx
                obstacle_hitbox.bottom = ent.rect.bottom

                if not hasattr(ent, 'has_collided'):
                    ent.has_collided = False

                if player_hitbox.colliderect(obstacle_hitbox) and not ent.has_collided:
                    collision_sound.play()
                    ent.has_collided = True

            if (isinstance(ent, Obstacle) or isinstance(ent, Coin)) and ent.rect.right < 0:
                entity_list.remove(ent)