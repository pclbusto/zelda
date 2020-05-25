import pygame

RIGHT_FACING = 0
LEFT_FACING = 1
FACTOR_SCALADO = 2


def add_image_pair(imagen, x1, y1, x2, y2):
    img1 = pygame.Surface((x2 - x1 + 1, y2 - y1 + 1))
    #img2 = pygame.Surface((x2 - x1 + 1, y2 - y1 + 1))
    img1.blit(imagen, (0, 0), (x1, y1, x2 - x1 + 1, y2 - y1 + 1))
    img1.set_colorkey((0, 255, 0))
    img1 = img1.convert_alpha()
    img2 = pygame.transform.flip(img1, True, False)
    img1 = pygame.transform.scale(img1, (img1.get_width() * FACTOR_SCALADO, img1.get_height() * FACTOR_SCALADO))
    img2 = pygame.transform.scale(img2, (img2.get_width() * FACTOR_SCALADO, img2.get_height() * FACTOR_SCALADO))
    return (img1, img2)


class Toad(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.character_face_direction = RIGHT_FACING
        # Track out state
        self.jumping = False
        self.walking = False
        self.running = False
        self.swimming = False
        self.standup = True
        self.hanging = False
        self.climbing = False
        self.is_on_ladder = False
        self.FRAMES_OJOS_ABIERTO = 100
        self.MAX_ACELERACION = 4
        self.INERCIA = 0.3
        self.ACELERACION = 0.03
        self.FRAMES_PARPADEO = 20
        self.index_textura_parado = 0
        self.index_textura_walking = 0
        self.timer_parpadeo = 0
        self.vel_salto = 1
        self.aceleracion = 0
        self.vel = 0
        self.pos = (100, 100)
        self.sensibilidad_doble_presionado = 30
        self.cantidad_ticks_desde_posible_doble = 0
        self.cur_texture = None
        self.lista_movimientos = []
        megaman = pygame.image.load("Megaman/sprites battletoad.png").convert_alpha()
        self.list_stand = []
        self.list_walk = []
        self.list_jump = []
        self.teclas_prsionadas = {pygame.K_j: False, pygame.K_l: False}

        self.list_stand.append(add_image_pair(megaman, 439, 0, 490, 71))
        self.list_stand.append(add_image_pair(megaman, 505, 0, 556, 71))

        self.list_walk.append(add_image_pair(megaman, 0, 0, 52, 71))
        self.list_walk.append(add_image_pair(megaman, 60, 0, 108, 71))
        self.list_walk.append(add_image_pair(megaman, 123, 0, 189, 71))
        self.list_walk.append(add_image_pair(megaman, 197, 0, 239, 71))
        self.list_walk.append(add_image_pair(megaman, 246, 0, 314, 71))
        self.cur_texture = self.cur_texture = self.list_walk[0][self.character_face_direction]

    def update_walking(self):
        index = 0
        self.index_textura_walking += 1
        index = self.index_textura_walking // 8
        index %= 5
        self.pos = (self.pos[0] + self.vel, self.pos[1])
        # self.texture = self.list_walk[self.index_textura_walking][self.character_face_direction]
        self.cur_texture = self.list_walk[index][self.character_face_direction]

    def update_standup(self):
        # ojos abiertos
        if self.index_textura_parado == 0:
            if self.timer_parpadeo <= self.FRAMES_OJOS_ABIERTO:
                self.timer_parpadeo += 1
            else:
                # se produce un parpadeo
                self.timer_parpadeo = 0
                self.index_textura_parado += 1
                print("parpadeo")

        elif self.index_textura_parado == 1:
            if self.timer_parpadeo <= self.FRAMES_PARPADEO:
                self.timer_parpadeo += 1
            else:
                # se termina el parpadeo o de tener los ojos cerrados
                self.index_textura_parado = 0
                self.timer_parpadeo = 0
                print("abre ojos")

        self.cur_texture = self.list_stand[self.index_textura_parado][self.character_face_direction]

    def update(self, evento) -> None:
        # keys = pygame.key.get_pressed()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_j:
                self.teclas_prsionadas[pygame.K_j] = True
                self.aceleracion = 0
            elif evento.key == pygame.K_l:
                self.teclas_prsionadas[pygame.K_l] = True
                self.aceleracion = 0
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_j:
                self.teclas_prsionadas[pygame.K_j] = False
                self.standup = True
                self.aceleracion = 0
                self.walking = False
            elif evento.key == pygame.K_l:
                self.teclas_prsionadas[pygame.K_l] = False
                self.standup = True
                self.aceleracion = 0
                self.walking = False


        if self.teclas_prsionadas[pygame.K_j]:
            self.character_face_direction = LEFT_FACING
            #self.aceleracion = 0
            self.standup = False
            self.walking = True
            self.acelerar()
            print(self.aceleracion)
            self.vel = -self.aceleracion + self.INERCIA
        elif self.teclas_prsionadas[pygame.K_l]:
            self.character_face_direction = RIGHT_FACING
            self.standup = False
            self.walking = True
            self.acelerar()
            print(self.aceleracion)
            self.vel = self.aceleracion - self.INERCIA

        if self.standup:
            self.update_standup()
        if self.walking:
            self.update_walking()

        # for evento in pygame.event.get():
        #     evento.key = 0
        #
        #     if evento.type == pygame.KEYUP:
        #         if evento.key == pygame.K_j or evento.key == pygame.K_l:
        #             self.walking = False
        #             self.running = False
        #             self.standup = True
        #             delta = 0.15
        #
        #     # if evento.type == pygame.JOYAXISMOTION:
        #     #     evento.key = 0
        #     #     if joy.get_axis(2) > 0:
        #     #         evento.key = KEY_DERECHA
        #     #         # lista[KEY_DERECHA] = 1
        #     #     elif joy.get_axis(2) < 0:
        #     #         evento.key = KEY_IZQUIERDA
        #     #         # lista[KEY_IZQUIERDA] = 1
        #
        #         if self.walking:
        #             if self.cantidad_ticks_desde_posible_doble < self.sensibilidad_doble_presionado:
        #                 self.lista_movimientos.clear()
        #                 cantidad_ticks_desde_posible_doble = 0
        #             self.lista_movimientos.append(evento.key)
        #             if len(self.lista_movimientos) > 10:
        #                 del (self.lista_movimientos[0])
        #             if len(self.lista_movimientos) > 2:
        #                 print(self.lista_movimientos[-2:-1][0], self.lista_movimientos[-3:-2][0])
        #                 if self.lista_movimientos[-2:-1][0] == self.lista_movimientos[-3:-2][0]:
        #                     self.running = True
        #                     self.walking = False
        #                     delta = 0.25
        #
        #         # if self.running and self.direccion == RIGHT_FACING and evento.key == KEY_IZQUIERDA:
        #         #     CORRIENDO = 1
        #         #     delta = 0.15
        #         # elif CORRIENDO == 2 and direccion == DIRECCION_IZQUIERDA and evento.key == KEY_DERECHA:
        #         #     CORRIENDO = 1
        #         #     delta = 0.15
        #
        #         # print(joy.get_numaxes())
        #         # help(evento)
        #         print(evento)
        #         # print(evento.key)
        #     if evento.type == pygame.JOYBUTTONDOWN:
        #         pass
        #
        #     if evento.type == pygame.KEYDOWN:
        #         if CORRIENDO == 1:
        #             if cantidad_ticks_desde_posible_doble < self.sensibilidad_doble_presionado:
        #                 self.lista_movimientos.clear()
        #                 self.cantidad_ticks_desde_posible_doble = 0
        #             self.lista_movimientos.append(evento.key)
        #
        #     if len(self.lista_movimientos) > 10:
        #         del (self.lista_movimientos[0])
        #     if len(self.lista_movimientos) > 2:
        #         print(self.lista_movimientos[-2:-1][0], self.lista_movimientos[-3:-2][0])
        #         if self.lista_movimientos[-2:-1][0] == self.lista_movimientos[-3:-2][0]:
        #             CORRIENDO = 2
        #             delta = 0.25
        #
        #     if CORRIENDO == 2 and self.direccion == DIRECCION_DERECHA and evento.key == KEY_IZQUIERDA:
        #         CORRIENDO = 1
        #         delta = 0.15
        #     elif CORRIENDO == 2 and self.direccion == DIRECCION_IZQUIERDA and evento.key == KEY_DERECHA:
        #         CORRIENDO = 1
        #         delta = 0.15
        #
        #         # print("KEYDOWN {}".format(evento.key))
        #     cantidad_ticks_desde_posible_doble += 1
        #
        # if CORRIENDO == 1:
        #     pass
        #     # print("ESTADO CAMINANDO")
        # else:
        #     print("ESTADO CORRIENDO")
        #
        # lista = pygame.key.get_pressed()
        #
        # incremento = (VEL_CORRER_X * CORRIENDO)
        #
        # if lista[KEY_IZQUIERDA] == 1 or evento.key == KEY_IZQUIERDA:
        #     index_frame_corriendo = int(delta_acumulado) % len(list_left_run)
        #     delta_acumulado -= delta
        #     x -= incremento
        #     direccion = DIRECCION_IZQUIERDA
        #     if estado == STATE_PARADO:
        #         estado = STATE_CORRIENDO
        #
        #
        # if lista[KEY_DERECHA] == 1 or evento.key == KEY_DERECHA:
        #     index_frame_corriendo = int(delta_acumulado) % len(list_left_run)
        #     delta_acumulado += delta
        #     x += incremento
        #     direccion = DIRECCION_DERECHA
        #     if estado == STATE_PARADO:
        #         estado = STATE_CORRIENDO
        #
        # if lista[KEY_DERECHA] == 0 and lista[KEY_IZQUIERDA] == 0 and estado == STATE_CORRIENDO:
        #     estado = STATE_PARADO
        #     timer_parpadeo = 0
        #
        # if estado == STATE_PARADO and index_parado == 0 and timer_parpadeo <= FRAMES_OJOS_ABIERTO:
        #     timer_parpadeo += 1
        # if estado == STATE_PARADO and index_parado == 1 and timer_parpadeo <= FRAMES_PARPADEO:
        #     timer_parpadeo += 1
        # if estado == STATE_PARADO and index_parado == 0 and timer_parpadeo == FRAMES_OJOS_ABIERTO:
        #     index_parado = 1
        #     timer_parpadeo = 0
        # if estado == STATE_PARADO and index_parado == 1 and timer_parpadeo == FRAMES_PARPADEO:
        #     index_parado = 0
        #     timer_parpadeo = 0
        #
        # if lista[pygame.K_a] == 1:
        #     if estado == STATE_CORRIENDO or estado == STATE_PARADO:
        #         estado = STATE_SALTANDO_UP
        #         y -= vel_salto
        #         vel_salto -= DESACEL_Y
        #     elif estado == STATE_SALTANDO_UP:
        #         y -= vel_salto
        #         vel_salto -= DESACEL_Y
        #
        # elif lista[pygame.K_a] == 0 and estado in [STATE_SALTANDO_DOWN, STATE_SALTANDO_UP]:
        #     # print("index salto: {} stado {}".format(index_porcentaje_salto, estado))
        #     if vel_salto >= LIM_ACEL_SIN_SALTO_PRECIONADO:
        #         vel_salto = 1
        #
        # # print("tecla A {} estado {} porcentaje {}".format(lista[pygame.K_a], estado,index_porcentaje_salto))
        # # print("index: {} estado {} direccion {} pos salto {}".format(index_porcentaje_salto, estado, direccion,
        # #                                                 150 - (110 * porcentaje_salto[index_porcentaje_salto])))
        #
        # # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ
        #
        # # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ
        #
        # # Primero, limpia la pantalla con blanco. No vayas a poner otros comandos de dibujo encima
        # # de esto, de otra forma serán borrados por este comando:
        # pantalla.fill(ROJO)
        # # pantalla.blit(fondo,(0,0))
        # # index = int(i)%len(list_left_run)
        # if direccion == DIRECCION_DERECHA and estado == STATE_CORRIENDO:
        #     pantalla.blit(list_right_run[index_frame_corriendo], (x, y))
        # elif direccion == DIRECCION_IZQUIERDA and estado == STATE_CORRIENDO:
        #     pantalla.blit(list_left_run[index_frame_corriendo], (x, y))
        # elif direccion == DIRECCION_DERECHA and estado in [STATE_SALTANDO_UP, STATE_SALTANDO_DOWN]:
        #     pantalla.blit(list_jump_right[0], (x, y))
        # elif direccion == DIRECCION_IZQUIERDA and estado in [STATE_SALTANDO_UP, STATE_SALTANDO_DOWN]:
        #     pantalla.blit(list_jump_left[0], (x, y))
        # elif direccion == DIRECCION_DERECHA and estado == STATE_PARADO:
        #     pantalla.blit(list_right_stand[index_parado], (x, y))
        # elif direccion == DIRECCION_IZQUIERDA and estado == STATE_PARADO:
        #     pantalla.blit(list_left_stand[index_parado], (x, y))

    def acelerar(self):
        if self.aceleracion < self.MAX_ACELERACION:
            self.aceleracion += self.ACELERACION
        else:
            self.aceleracion = self.MAX_ACELERACION
