from constantes import *

data = {
    'frog_skin': "frog26",
    'last_unlocked_lvl': 1
}

try:
    # the file already exists
    with open('save.txt') as load_file:
        data = json.load(load_file)
except:
    # create the file and store initial values
    with open('save.txt', 'w') as store_file:
        json.dump(data, store_file)

clock = pygame.time.Clock()

frog_skin = "frog26"
menu_skin = "images/skin_menu/skin_background.png"
taille_skin = 100

skins = []
for image in range(30):
    skin = pygame.image.load("images/skin_menu/frogs/frog" + str(image) + ".png")
    skin = pygame.transform.scale(skin, (taille_skin, taille_skin))
    skins.append(skin)

skin_dict = {}


def grid():
    menu_background = pygame.image.load(menu_skin).convert()
    menu_background = pygame.transform.scale(menu_background, (1920, 1080))
    screen.blit(menu_background, (0, 0))
    pygame.display.flip()

    x_coord = 50
    y_coord = 50
    for image in range(len(skins)):
        if image % 5 == 0 and image != 0:
            x_coord = 50
            y_coord += taille_skin + 50
        screen.blit(skins[image], (x_coord, y_coord))
        skin_dict["frog" + str(image)] = (x_coord, y_coord, x_coord + taille_skin, y_coord + taille_skin)
        x_coord += taille_skin + 100


def creation_fenetre():
    grid()
    pygame.display.flip()

    running = True  # Variable pour contrôler la boucle principale
    while running:

        pygame.display.flip()
        clock.tick(20)
        for event in pygame.event.get():
            if (event.type == KEYDOWN and event.key == K_ESCAPE) or event.type == pygame.QUIT:
                running = False  # Quitter la boucle principale si l'utilisateur ferme la fenêtre
                pygame.quit()
            if event.type == KEYDOWN and event.key == K_RETURN:  # Quitter la boucle principale si l'utilisateur ferme la fenêtre
                running = False  # Quitter la boucle principale si l'utilisateur ferme la fenêtre
                import select_lvl
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:  # Vérifier le clic de souris
                # Récupérer les coordonnées du clic
                clic_x, clic_y = event.pos
                for key, value in skin_dict.items():
                    if value[0] < clic_x < value[2]:
                        if value[1] < clic_y < value[3]:
                            data['frog_skin'] = key
                            with open('save.txt', 'w') as store_data:
                                json.dump(data, store_data)
                            frog_skin = key
                            grid()
                            skin = pygame.image.load("images/skin_menu/frogs/" + frog_skin + ".png")
                            skin = pygame.transform.scale(skin, (taille_skin * 2.5, taille_skin * 2.5))
                            screen.blit(skin, (1000, 500))

    pygame.quit()


creation_fenetre()