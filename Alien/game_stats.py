class GameStats:
    """Collecting statistics for the game"""

    def __init__(self, ai_game):
        """Initialising statistics"""
        self.settings = ai_game.settings
        self.reset_stats() #Başlangıçta sıfırlamak için kullanılır.

        # Game starts in non-active state
        self.game_active = False
      # Bu satır, "high_score.txt" adlı bir dosyayı okuma-yazma modunda açar.
        with open("high_score.txt", "w+") as file_object:
            high_score = file_object.read() #Dosyadan okur
            if high_score == "":
                high_score = 0

        self.high_score = int(high_score)

    def reset_stats(self): #Statları sıfırlamak için kullanırız.
        """Initialising statistics, changing in game process"""
        self.ships_left = self.settings.ship_limit #Gemi limitini gösterir
        self.score = 0
        self.level = 1
