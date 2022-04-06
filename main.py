from platform import node
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from xml.dom import minidom

import os 
import webbrowser


#GLOBALES

#Auxiliares
city_name = ''
type_of_mision = ''
selection_robot = ''
mision_result = ''

capacidad_incial = ''
capacidad_final = ''

codes = ''
citys = ''
Civil = ''
Recurso = ''

robot = ''

#Colores
Withe = '#FFFFFF'
Black = '#000000'
Green = '#00FF00'
Blue = '#0066FF'
Gray = '#AEB6BF'
Red = '#C62828'
Path = 'Cyan'



#----------------------------------------------------------------------------
class Linked_list_military():
    def __init__(self) -> None:
        self.military_head : Node_military = None #cabecera
        self.military_last = None #final
        self.military_size = 0

    def add_to_end(self, pos_x, pos_y, capacity):
        new_military = Node_military(pos_x, pos_y, capacity)
        self.military_size += 1
        if self.military_head is None:
            self.military_head = new_military
            self.military_last = new_military
        else:
            self.military_last.setNext_Military(new_military)
            self.military_last = new_military
        return new_military

    def get_Militarys(self, pos_X, pos_y):
        tmp = self.military_head
        while tmp != None:
            if tmp.getPos_X() == pos_X and tmp.getPos_Y == pos_y:
                return tmp
            tmp = tmp.getNext_Military()

    def get_size(self):
        count = 0
        node = self.military_head
        while node != None:
            node = node.getNext_Military()
            count = count + 1
        return count

    def show_Militarys(self):
        tmp = self.military_head
        for i in range(self.military_size):
            print('Pos X:', tmp.getPos_X(), 'Pos Y:', tmp.getPos_Y(), 'Capacidad: ', tmp.getCapacity_Military())
            tmp = tmp.getNext_Military()
#----------------------------------------------------------------------------
class Node_military():
    def __init__(self, pos_x, pos_y, capacity) -> None:
        self.pos_x: int = pos_x
        self.pos_y: int = pos_y
        self.capacity: int = capacity
        self.next_military = None

    def getPos_X(self):
        return self.pos_x
            
    def getPos_Y(self):
        return self.pos_y
            
    def getCapacity_Military(self):
        return self.capacity
        
    def getNext_Military(self):
        return self.next_military

    def setNext_Military(self, military):
        self.next_military = military
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
class Linked_list_robot():
    def __init__(self) -> None:
        self.robot_head : Node_robot = None #cabecera
        self.robot_last = None #final
        self.robot_size = 0

    def add_to_end(self,robot_name, robot_type, robot_capacity):
        new_robot = Node_robot(robot_name, robot_type, robot_capacity)
        self.robot_size += 1
        if self.robot_head is None:
            self.robot_head = new_robot
            self.robot_last = new_robot
        else:
            self.robot_last.setNext_Robot(new_robot)
            self.robot_last = new_robot
        return new_robot

    def get_Robots_by_type(self, robot_type):
        tmp = self.robot_head
        while tmp != None:
            if tmp.getType_Robot() == robot_type:
                return tmp
            tmp = tmp.getNext_Robot()
    
    def get_Robots_by_name(self, robot_name):
        tmp = self.robot_head
        while tmp != None:
            if tmp.getName_Robot() == robot_name:
                return tmp
            tmp = tmp.getNext_Robot()

    def get_size(self):
        count = 0
        node = self.robot_head
        while node != None:
            node = node.getNext_Robot()
            count = count + 1
        return count

    def clear(self):
        self.robot_head = None
        self.robot_last = None
        self.robot_size = 0
        return

    def show_Robots(self):
        tmp = self.robot_head
        for i in range(self.robot_size):
            print('Nombre:', tmp.getName_Robot(), 'Tipo:', tmp.getType_Robot(), 'Capacidad: ', tmp.getCapacity_Robot())
            tmp = tmp.getNext_Robot()
    
    def show_Robots_by_type(self, robot_type):
        tmp = self.robot_head
        while tmp != None:
            if tmp.getType_Robot() == robot_type:
                print(' > Nombre:', tmp.getName_Robot(), 'Capacidad: ', tmp.getCapacity_Robot())
            tmp = tmp.getNext_Robot()
#----------------------------------------------------------------------------
class Node_robot():
    def __init__(self, robot_name, robot_type, robot_capacity) -> None:
        self.robot_name: str = robot_name
        self.robot_type: str = robot_type
        self.robot_capacity: int = robot_capacity
        self.next_robot = None

    def getName_Robot(self):
        return self.robot_name
            
    def getType_Robot(self):
        return self.robot_type
            
    def getCapacity_Robot(self):
        return self.robot_capacity
    
    def setCapacity_Robot(self, capacity):
        self.robot_capacity = capacity
        
    def getNext_Robot(self):
        return self.next_robot

    def setNext_Robot(self, robot):
        self.next_robot = robot
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
class Boxes_List():   #lista doblemente enlazada
    def __init__(self):
        self.boxes_head : Box = None #cabecera
        self.boxes_last = None #final
        self.boxes_size = 0

    def add_to_end(self,box,box_posX,box_posY,box_color,font_color):
        new_boxes = Box(box,box_posX,box_posY,box_color,font_color)
        self.boxes_size += 1
        if self.boxes_head is None:
            self.boxes_head = new_boxes
            self.boxes_last = new_boxes
        else:
            self.boxes_last.setNext_Box(new_boxes)
            new_boxes.setPrevius_Box(self.boxes_last)
            self.boxes_last = new_boxes
        return new_boxes
        

    def insert_in_pos(self,box_posX,box_posY,box_color,font_color):
        tmp = self.boxes_head
        while tmp != None:
            if tmp.getPosX_Box() == box_posX and tmp.getPosY_Box() == box_posY:
                tmp.setColor_Box(box_color)
                tmp.setFont_Box(font_color)
            tmp = tmp.getNext_Box()

    def get_size(self):
        count = 0
        node = self.boxes_head
        while node != None:
            node = node.getNext_Box()
            count = count + 1
        return count
    
    def get_Boxs(self, box):
        tmp = self.boxes_head
        while tmp != None:
            if tmp.getColor_Box() == box:
                return tmp
            tmp = tmp.getNext_Box()
    
    def get_Boxs_By_Pos(self, pos_x, pos_y):
        tmp = self.boxes_head
        while tmp != None:
            if tmp.getPosX_Box() == pos_x and tmp.getPosY_Box() == pos_y:
                return tmp
            tmp = tmp.getNext_Box()
        
    def show_Boxes(self):
        tmp = self.boxes_head
        while tmp != None:
            print('Color:', tmp.get_Box(), 'Pos X: ', tmp.getPosX_Box(), 'Pos Y: ' , tmp.getPosY_Box() ,'Index: ' , tmp.get_Index())
            tmp = tmp.getNext_Box()
    
    def show_Boxes1(self, name):
        tmp = self.boxes_head

        strGrafica = 'digraph G { \n graph [pad="1" bgcolor="yellow:orange" style="filled" margin="0"  penwidth="3"] \n'
        strGrafica += 'label = "\n \n Ciudad: {}" fontname="times-bold" fontsize="20pt" \n'.format(name)
        strGrafica += 'node [style = filled shape = box height="1" width="1"] \n'

        while tmp != None:
            strGrafica += '{}[fillcolor= "{}" fontcolor = "{}" pos="{},-{}!"] \n'.format(tmp.get_Box(),tmp.getColor_Box(),tmp.getFont_Box(),tmp.getPosX_Box(),tmp.getPosY_Box())
            tmp = tmp.getNext_Box()
        
        tmp2 = self.boxes_last
        strGrafica += 'node2 [shape = "none", image="AuxFiles\\leyenda.png", label="" pos = "{},-{}!"] \n'.format(int(tmp2.getPosX_Box())/2,int(tmp2.getPosY_Box())+3)

        strGrafica += ' } '
        documentotxt = 'textoplano.txt'
        with open(documentotxt,'w') as grafica: 
            grafica.write(strGrafica)
        pdf = '{}.pdf'.format(name)
        os.system( 'neato -Tpdf ' + documentotxt + ' -o ' + pdf )
        webbrowser.open(pdf)
    
    def show_Boxes2(self,nombre_ciudad,civil, nombre_robot, resultado):
        tmp = self.boxes_head

        strGrafica = 'digraph G { \n graph [pad="1" bgcolor="yellow:orange" style="filled" margin="0"  penwidth="3"] \n'
        strGrafica += 'label = "\n \n Resultado de la mision: {}! \n \n Ciudad: {} \n Tipo de mision: Rescate \n Unidad Civil Rescatada: ({},{}) \n Robot Utilizado: {}" \
            fontname="times-bold" fontsize="20pt" '.format(resultado,nombre_ciudad,civil.getPosX_Box(),civil.getPosY_Box(),nombre_robot)

        strGrafica += 'node [style = filled shape = box height="1" width="1"] \n'

        while tmp != None:
            strGrafica += '{}[fillcolor= "{}" fontcolor = "{}" pos="{},-{}!"] \n'.format(tmp.get_Box(),tmp.getColor_Box(),tmp.getFont_Box(),tmp.getPosX_Box(),tmp.getPosY_Box())
            tmp = tmp.getNext_Box()
        
        tmp2 = self.boxes_last
        strGrafica += 'node2 [shape = "none", image="AuxFiles\\leyenda.png", label="" pos = "{},-{}!"] \n'.format(int(tmp2.getPosX_Box())/2,int(tmp2.getPosY_Box())+3)

        
        strGrafica += ' } '
        documentotxt = 'textoplano.txt'
        with open(documentotxt,'w') as grafica: 
            grafica.write(strGrafica)
        pdf = '{}_{}.pdf'.format(nombre_ciudad,'Rescate')
        os.system( 'neato -Tpdf ' + documentotxt + ' -o ' + pdf )
        webbrowser.open(pdf)
    
    def show_Boxes3(self, nombre_ciudad, recurso, nombre_robot, capacidad_inicial, capacidad_final, resultado):
        tmp = self.boxes_head

        strGrafica = 'digraph G { \n graph [pad="1" bgcolor="yellow:orange" style="filled" margin="0"  penwidth="3"] \n'
        strGrafica += ' label = "\n \n Resultado de la mision: {}! \n \n Ciudad: {} \n Tipo de mision: Extraccion de Recursos \n Recurso Extraido: ({},{}) \n Robot Utilizado: {} \n (Capacidad Inicial: {}, Capacidad Final: {})" \
                        fontname="times-bold" fontsize="20pt" '.format(resultado,nombre_ciudad,recurso.getPosX_Box(),recurso.getPosY_Box(),nombre_robot,capacidad_inicial,capacidad_final)

        strGrafica += 'node [style = filled shape = box height="1" width="1"] \n'

        while tmp != None:
            strGrafica += '{}[fillcolor= "{}" fontcolor = "{}" pos="{},-{}!"] \n'.format(tmp.get_Box(),tmp.getColor_Box(),tmp.getFont_Box(),tmp.getPosX_Box(),tmp.getPosY_Box())
            tmp = tmp.getNext_Box()
        
        tmp2 = self.boxes_last
        strGrafica += 'node2 [shape = "none", image="AuxFiles\\leyenda.png", label="" pos = "{},-{}!"] \n'.format(int(tmp2.getPosX_Box())/2,int(tmp2.getPosY_Box())+3)


        strGrafica += ' } '
        documentotxt = 'textoplano.txt'
        with open(documentotxt,'w') as grafica: 
            grafica.write(strGrafica)
        pdf = '{}_{}.pdf'.format(nombre_ciudad,'Rescate')
        os.system( 'neato -Tpdf ' + documentotxt + ' -o ' + pdf )
        webbrowser.open(pdf)
#----------------------------------------------------------------------------
class Box():
    def __init__(self, box,box_posX,box_posY,box_color,font_color):
        self.box_font: str = font_color
        self.box_color: str = box_color
        self.box_posX: int = int(box_posX)
        self.box_posY: int = int(box_posY)
        self.next_box = None
        self.previus = None
        self.box =  box

        self.up_box = None
        self.down_box = None
        self.rigth_box = None
        self.left_box = None

        self.blocked = False

    def getUp_Box(self):
        return self.up_box

    def setUp_Box(self, up):
        self.up_box = up
    
    def getDown_Box(self):
        return self.down_box

    def setDown_Box(self, down):
        self.down_box = down

    def getRigth_Box(self):
        return self.rigth_box

    def setRigth_Box(self, rigth):
        self.rigth_box = rigth

    def getLeft_Box(self):
        return self.left_box

    def setLeft_Box(self, left):
        self.left_box = left

    def get_Box(self):
        return self.box

    def set_Box(self, box):
        self.box = box

    def getPosX_Box(self):
        return self.box_posX

    def setPosX_Box(self, pos_x):
        self.box_posX = pos_x

    def getPosY_Box(self):
        return self.box_posY

    def setPosY_Box(self, pos_y):
        self.box_posY = pos_y

    def getColor_Box(self):
        return self.box_color

    def setColor_Box(self, color):
        self.box_color = color

    def getFont_Box(self):
        return self.box_font

    def setFont_Box(self, font):
        self.box_font = font
    
    def getStatus_Box(self):
        return self.blocked

    def setStatus_Box(self, status):
        self.blocked = status

    def getNext_Box(self):
        return self.next_box

    def setNext_Box(self, next):
        self.next_box = next  

    def getPrevius_Box(self):
        return self.previus

    def setPrevius_Box(self, prev):
        self.previus = prev
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
class Patterns_List():
    def __init__(self) -> None:
        self.patterns_head : Pattern = None #cabecera
        self.patterns_last = None #final
        self.patterns_size = 0

    def add_to_end(self, pattern_code, patterns):
        new_patterns = Pattern(pattern_code, patterns)
        self.patterns_size += 1
        if self.patterns_head is None:
            self.patterns_head = new_patterns
            self.patterns_last = new_patterns
        else:
            self.patterns_last.setNext_Pattern(new_patterns)
            self.patterns_last = new_patterns
        return new_patterns
        
    def get_Patterns(self, Pattern_Code):
        tmp = self.patterns_head
        while tmp != None:
            if tmp.getCode_Pattern() == Pattern_Code:
                return tmp
            tmp = tmp.getNext_Pattern()

    def show_Patterns(self):
        tmp = self.patterns_head
        for i in range(self.patterns_size):
            print('Codigo Patron: ', tmp.getCode_Pattern(), 'Patron: ' , tmp.get_Pattern())
            tmp = tmp.getNext_Pattern()
#----------------------------------------------------------------------------
class Pattern():
    def __init__(self, pattern_code, pattern) -> None:
        self.pattern_code: str = pattern_code
        self.pattern: str = pattern
        self.color_patterns = Boxes_List()                 
        self.next_pattern = None

    def getNext_Pattern(self):
        return self.next_pattern

    def setNext_Pattern(self, next_pattern):
        self.next_pattern = next_pattern

    def setCode_Pattern(self, pattern_code):
        self.pattern_code = pattern_code

    def getCode_Pattern(self):
        return self.pattern_code

    def set_Pattern(self, pattern):
        self.pattern = pattern

    def get_Pattern(self):
        return self.pattern
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
class Linked_list_city():
    def __init__(self) -> None:
        self.city_head : Node_city = None #cabecera
        self.city_last = None #final
        self.city_size = 0

    def add_to_end(self, city_name, city_rows, city_column):
        new_city = Node_city(city_name, city_rows, city_column)
        self.city_size += 1
        if self.city_head is None:
            self.city_head = new_city
            self.city_bottom = new_city
        else:
            self.city_bottom.setNext_City(new_city)
            self.city_bottom = new_city
        return new_city

    def get_Citys(self, city_name):
        tmp = self.city_head
        while tmp != None:
            if tmp.getName_City() == city_name:
                return tmp
            tmp = tmp.getNext_City()
        return None

    def get_size(self):
        count = 0
        node = self.city_head
        while node != None:
            node = node.getNext_City()
            count = count + 1
        return count

    def clear(self):
        self.city_head = None
        self.city_last = None
        self.city_size = 0
        return

    def show_Citys(self):
        tmp = self.city_head
        for i in range(self.city_size):
            print(' > Nombre:', tmp.getName_City(), 'Filas:', tmp.getRow_City(), 'Columnas: ', tmp.getColumn_City())
            tmp = tmp.getNext_City()
#----------------------------------------------------------------------------
class Node_city():
    def __init__(self, city_name, city_rows, city_column) -> None:
        self.city_name: str = city_name
        self.city_rows: int = city_rows
        self.city_column: int = city_column
        self.military_units = Linked_list_military()
        self.code_patterns = Patterns_List()
        self.next_city = None

    def getName_City(self):
        return self.city_name
            
    def setName_City(self, name):
        self.city_name = name

    def getRow_City(self):
        return self.city_rows
            
    def getColumn_City(self):
        return self.city_column
        
    def getNext_City(self):
        return self.next_city

    def setNext_City(self, city):
        self.next_city = city
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
def MiniDom(datas, linked_list: Linked_list_city, linked_robots: Linked_list_robot):

    global Withe
    global Black
    global Green
    global Blue
    global Gray
    global Red
    global Path

    linked_list.clear()
    linked_robots.clear()

    mydoc = minidom.parse(datas)
    #Extraer Ciudades
    citys = mydoc.getElementsByTagName('ciudad')
    for city in citys:
        city_name = city.getElementsByTagName('nombre')
        rowses = city.getElementsByTagName('fila')
        military_unit = city.getElementsByTagName('unidadMilitar')

        for attribs in city_name:
            name = attribs.firstChild.data
            rows = attribs.attributes['filas'].value
            columns = attribs.attributes['columnas'].value

        cityses = linked_list.add_to_end(name,rows,columns)
        #linked_list.show_Citys()

        pattern = ''
        for lista in rowses:
            lista.attributes['numero'].value
            node = lista.firstChild.data
            for nodes in node:
                pattern += nodes
        
        codes = cityses.code_patterns.add_to_end(name,pattern)
        
        pos_x = 0
        pos_y = 0
        contador = 1 

        for color in pattern:
            count_rows = 0
            while int(rows) > count_rows:
                count_cols = 0
                if color == ' ':
                    color = 'W{}'.format(str(contador))
                    codes.color_patterns.add_to_end(color,pos_x,pos_y,Withe,Withe)
                    contador += 1 
                    pos_x += 1 
                elif color == '*':
                    color = 'B{}'.format(str(contador))
                    codes.color_patterns.add_to_end(color,pos_x,pos_y,Black,Black)
                    contador += 1
                    pos_x += 1
                elif color == 'E':
                    color = 'E{}'.format(str(contador))
                    codes.color_patterns.add_to_end(color,pos_x,pos_y,Green,Green)
                    contador += 1
                    pos_x += 1
                elif color == 'C':
                    color = 'C{}'.format(str(contador))
                    codes.color_patterns.add_to_end(color,pos_x,pos_y,Blue,Blue)
                    contador += 1
                    pos_x += 1
                elif color == 'R':
                    color = 'R{}'.format(str(contador))
                    codes.color_patterns.add_to_end(color,pos_x,pos_y,Gray,Gray)
                    contador += 1
                    pos_x += 1
                while int(columns) > count_cols:
                    count_cols += 1
                count_rows += 1
                if pos_x >= int(columns):
                    pos_y += 1
                    pos_x = 0


        for military in military_unit:
            combat_capacity = military.firstChild.data
            military_pos_x = int(military.attributes['columna'].value)-1 
            military_pos_y = int(military.attributes['fila'].value)-1
            cityses.military_units.add_to_end(military_pos_x,military_pos_y,combat_capacity)
            codes.color_patterns.insert_in_pos(military_pos_x,military_pos_y,Red,Red)

        #cityses.military_units.show_Militarys()
        #print(pattern)
        #cityses.row_list.show_chars()
        #codes.color_patterns.show_Boxes1('nombre','codigo')
        #codes.color_patterns.show_Boxes()
    
    #Extraer Robots
    robots = mydoc.getElementsByTagName('robot')
    for robot in robots:
        robot_name = robot.getElementsByTagName('nombre')
        for attribs in robot_name:
            robots_names = attribs.firstChild.data
            type_robot = attribs.attributes['tipo'].value
            if type_robot == 'ChapinFighter':
                capacity = attribs.attributes['capacidad'].value
            elif type_robot == 'ChapinRescue':
                capacity = None
            linked_robots.add_to_end(robots_names,type_robot,capacity)     
    #linked_robots.show_Robots()
#---------------------------------------------------------------------------- 

#---------------------------------------------------------------------------- 
def second_menu(linked_list,linked_robots: Linked_list_robot):

    flag = True
    while flag:
        print()
        print('=======================')
        print('Menu Secundario')
        print('=======================')
        print('1. Buscar ciudad por nombre')
        print('2. Mostrar Ciudad')
        print('3. Configurar Misiones')
        print('4. Inciar Misiones')
        print('=======================')
        print()
        option = input('> ')
        
        global city_name
        global type_of_mision
        global selection_robot
        global mision_result
        global capacidad_incial
        global capacidad_final

        global citys
        global codes
        global Civil
        global Recurso

        global robot

        global Withe
        global Black
        global Green
        global Blue
        global Gray
        global Red
        global Path
        
        
        mision_type = ''

        if option == '1':
            print()
            try:
                city_name =  input(' > Ingrese el nombre de la ciudad que desea seleccionar: ')
                #citys: Node_city = linked_list.get_Citys(city_name)
                citys = linked_list.get_Citys(city_name)
                
                

                if citys is None:
                    print(' > Nombre incorrecto')
                else:
                    print(' > Se ha seleccionado la ciudad: ', citys.getName_City())
            except:
                print(' > Asegurese de haber cargado la data')
        elif option == '2':
            try:
                codes = citys.code_patterns.get_Patterns(citys.getName_City())
                codes.color_patterns.show_Boxes1(citys.getName_City())

                color: Box =  codes.color_patterns.boxes_head

                while color != None:

                    x = int(color.getPosX_Box())
                    y = int(color.getPosY_Box())

                    left: Box = codes.color_patterns.get_Boxs_By_Pos(x-1,y)
                    right: Box = codes.color_patterns.get_Boxs_By_Pos(x+1,y)
                    up: Box = codes.color_patterns.get_Boxs_By_Pos(x,y-1)
                    down: Box = codes.color_patterns.get_Boxs_By_Pos(x,y+1)

                    if right != None:
                        if color.getColor_Box() != Black and right.getColor_Box() == Withe:
                            color.setRigth_Box(right)
                    if left != None:
                        if color.getColor_Box() != Black and left.getColor_Box() == Withe:
                            color.setLeft_Box(left)
                    if up != None:
                        if color.getColor_Box() != Black and up.getColor_Box() == Withe:
                            color.setUp_Box(up)
                    if down != None:
                        if color.getColor_Box() != Black and down.getColor_Box() == Withe:
                            color.setDown_Box(down)

                    color = color.getNext_Box()

                #codes1.color_patterns.show_Boxes()
            except:
                print(' > Asegurese de haber seleccionado una ciudad')
        elif option == '3':
            print()
            print(' > 1. Mision de Rescate')
            print(' > 2. Mision de Extraccion')
            print()
            mision_type =  input('> ')

            if mision_type == '1':
                try:

                    type_of_mision = 'Mision de Rescate'

                    color =  codes.color_patterns.boxes_head
                    color1 =  codes.color_patterns.boxes_head 

                    #Mision de Rescate
                    print()
                    print('> Robots disponibles para esta mision:')
                    linked_robots.show_Robots_by_type('ChapinRescue')
                    #Seleccionar Robot
                    print()
                    selection_robot =  input('> Ingrese el nombre del Robot que desea seleccionar: ')
                    robot = linked_robots.get_Robots_by_name(selection_robot)
                    if robot is None:
                        print(' > Nombre incorrecto')
                    else:
                        print(' > Se ha seleccionado el robot: ', robot.getName_Robot())

                    #Mostrar Ubicacion de Puntos de entrada y civiles
                    print()
                    print('> Puntos de Entrada: ')
                    while color != None:
                        if color.getColor_Box() == Green:
                            print(' > Punto de Entrada: (X:{},Y:{})'.format(color.getPosX_Box(),color.getPosY_Box()))
                        color = color.getNext_Box()
                    print()
                    print('> Ubicacion de Civiles: ')
                    while color1 != None:
                        if color1.getColor_Box() == Blue:
                            print(' > Ubicacion de Civil: (X:{},Y:{})'.format(color1.getPosX_Box(),color1.getPosY_Box()))
                        color1 = color1.getNext_Box()
                    print()
                    entrada_x =  input('> Ingrese coordenada X del punto de Entrada: ')
                    entrada_y =  input('> Ingrese coordenada Y del punto de Entrada: ')

                    Entrada = codes.color_patterns.get_Boxs_By_Pos(int(entrada_x),int(entrada_y))

                    if Entrada.getColor_Box() != Green:
                        print(' > Coordenadas De Entrada Incorrectas') 
                    print()

                    civil_x =  input('> Ingrese coordenada X del punto del Civil: ')
                    civil_y =  input('> Ingrese coordenada Y del punto del Civil: ')

                    Civil = codes.color_patterns.get_Boxs_By_Pos(int(civil_x),int(civil_y))

                    if Civil.getColor_Box() != Blue:
                        print(' > Coordenadas De Civil Incorrectas')
                    print()

                except:
                    print('Datos Invalidos')
                

            elif mision_type == '2':
                try:

                    type_of_mision = 'Mision de Extraccion'

                    color =  codes.color_patterns.boxes_head
                    color1 =  codes.color_patterns.boxes_head   

                    #Mision de Extraccion
                    print()
                    print('> Robots disponibles para esta mision:')
                    linked_robots.show_Robots_by_type('ChapinFighter')
                    
                    #Seleccionar Robot
                    print()
                    selection_robot =  input(' > Ingrese el nombre del Robot que desea seleccionar: ')
                    robot = linked_robots.get_Robots_by_name(selection_robot)
                    
                    

                    if robot is None:
                        print(' > Nombre incorrecto')
                    else:
                        print(' > Se ha seleccionado el robot: ', robot.getName_Robot())

                    #Mostrar Ubicacion de Puntos de entrada y Rercursos
                    print()
                    print('> Puntos de Entrada: ')
                    while color != None:
                        if color.getColor_Box() == Green:
                            print(' > Punto de Entrada: (X:{},Y:{})'.format(color.getPosX_Box(),color.getPosY_Box()))
                        color = color.getNext_Box()
                    print()
                    print('> Ubicacion de Recursos: ')
                    while color1 != None:
                        if color1.getColor_Box() == Gray:
                            print(' > Ubicacion de Recurso: (X:{},Y:{})'.format(color1.getPosX_Box(),color1.getPosY_Box()))
                        color1 = color1.getNext_Box()
                    print()
                    entrada_x =  input('> Ingrese coordenada X del punto de Entrada: ')
                    entrada_y =  input('> Ingrese coordenada Y del punto de Entrada: ')

                    Entrada = codes.color_patterns.get_Boxs_By_Pos(int(entrada_x),int(entrada_y))
                    if Entrada.getColor_Box() != Green:
                        print(' > Coordenadas De Entrada Incorrectas')               

                    print()
                    recurso_x =  input('> Ingrese coordenada X del punto del Recurso: ')
                    recurso_y =  input('> Ingrese coordenada Y del punto del Recurso: ')

                    Recurso = codes.color_patterns.get_Boxs_By_Pos(int(recurso_x),int(recurso_y))
                    if Recurso.getColor_Box() != Gray:
                        print(' > Coordenadas De Recurso Incorrectas') 
                    print()

                except:
                    print('Datos Invalidos')

            else:
                print(' > Opcion Invalida!')

        elif option == '4':

            if type_of_mision == 'Mision de Rescate':

                print()
                print('Mision Realizada!')
                print('Ciudad Utilizada: {}'.format(city_name))
                print('Tipo de mision: {}'.format(type_of_mision))
                print('Robot Utilizado: {}, Capacidad de combate inicial: {}'.format(selection_robot,robot.getCapacity_Robot()))
                print('Punto Entrada: (X:{},Y:{})'.format(Entrada.getPosX_Box(),Entrada.getPosY_Box()))
                print('Civil Rescatado: (X:{},Y:{})'.format(Civil.getPosX_Box(),Civil.getPosY_Box()))
                
                Coin = codes.color_patterns.get_Boxs_By_Pos(Entrada.getPosX_Box(),Entrada.getPosY_Box())

                coin_x = int(Coin.getPosX_Box())
                coin_y = int(Coin.getPosY_Box())

                if find_path_Rescue(coin_x,coin_y) == True:
                    mision_result = 'Mision Exitosa'

                    color: Box =  codes.color_patterns.boxes_head
                    while color != None:
                        if color.getFont_Box() == Blue:
                            color.setColor_Box(Blue)
                        if color.getFont_Box() == Red:
                            color.setColor_Box(Red)
                        if color.getFont_Box() == Green:
                            color.setColor_Box(Green)
                        if color.getFont_Box() == Gray:
                            color.setColor_Box(Gray)

                        if color.getColor_Box() == Path:
                            color.setFont_Box(Path)                   
        
                        color = color.getNext_Box()

                    codes.color_patterns.show_Boxes2(city_name,Civil,selection_robot,mision_result)

                else:
                    print(' > Ha fracasado la mision :[ ')
                    mision_result = 'Mision Fallida'

                    color: Box =  codes.color_patterns.boxes_head
                    while color != None:
                        if color.getFont_Box() == Blue:
                            color.setColor_Box(Blue)
                        if color.getFont_Box() == Red:
                            color.setColor_Box(Red)
                        if color.getFont_Box() == Green:
                            color.setColor_Box(Green)
                        if color.getFont_Box() == Gray:
                            color.setColor_Box(Gray)

                        if color.getColor_Box() == Path:
                            color.setFont_Box(Path)                   
        
                        color = color.getNext_Box()

                    codes.color_patterns.show_Boxes2(city_name,Civil,selection_robot,mision_result)


            elif type_of_mision == 'Mision de Extraccion':

                mision_result = 'Mision Exitosa'
                
                capacidad_incial = robot.getCapacity_Robot()
                capacidad_final = None

                print()
                print('Mision Realizada!')
                print('Ciudad Utilizada: {}'.format(city_name))
                print('Tipo de mision: {}'.format(type_of_mision))
                print('Robot Utilizado: {}, Capacidad de combate inicial: {}'.format(selection_robot,capacidad_incial))
                print('Punto Entrada: (X:{},Y:{})'.format(Entrada.getPosX_Box(),Entrada.getPosY_Box()))
                print('Recurso Extraido: (X:{},Y:{})'.format(Recurso.getPosX_Box(),Recurso.getPosY_Box()))
            
                Coin = codes.color_patterns.get_Boxs_By_Pos(Entrada.getPosX_Box(),Entrada.getPosY_Box())

                coin_x = int(Coin.getPosX_Box())
                coin_y = int(Coin.getPosY_Box())

                if find_path_Extract(coin_x,coin_y) == True:
                    mision_result = 'Mision Exitosa'

                    color: Box =  codes.color_patterns.boxes_head
                    while color != None:
                        if color.getFont_Box() == Blue:
                            color.setColor_Box(Blue)
                        if color.getFont_Box() == Red:
                            color.setColor_Box(Red)
                        if color.getFont_Box() == Green:
                            color.setColor_Box(Green)
                        if color.getFont_Box() == Gray:
                            color.setColor_Box(Gray)

                        if color.getColor_Box() == Path:
                            color.setFont_Box(Path)                   
        
                        color = color.getNext_Box()

                    codes.color_patterns.show_Boxes3(city_name,Recurso,selection_robot,capacidad_incial,capacidad_final,mision_result)

                else:
                    print(' > Ha fracasado la mision :[ ')
                    mision_result = 'Mision Fallida'

                    color: Box =  codes.color_patterns.boxes_head
                    while color != None:
                        if color.getFont_Box() == Blue:
                            color.setColor_Box(Blue)
                        if color.getFont_Box() == Red:
                            color.setColor_Box(Red)
                        if color.getFont_Box() == Green:
                            color.setColor_Box(Green)
                        if color.getFont_Box() == Gray:
                            color.setColor_Box(Gray)

                        if color.getColor_Box() == Path:
                            color.setFont_Box(Path)                   
        
                        color = color.getNext_Box()

                    codes.color_patterns.show_Boxes3(city_name,Recurso,selection_robot,capacidad_incial,capacidad_final,mision_result)
            #Devolver al menu principal imediatamente despues de realizar la mision
            #Devolver los colores estandar a las ciudades
            main_menu(linked_list,linked_robots)

            break
        else:
            print('Opcion Invalida!')
#---------------------------------------------------------------------------- 
 
#---------------------------------------------------------------------------- 
def find_path_Rescue(x,y):

    global citys
    global codes
    global Civil
    global Recurso

    global Black
    global Withe
    global Path
    global Gray 
    global Red
    global Green

    try:
        nodo: Box = codes.color_patterns.get_Boxs_By_Pos(int(x),int(y))

        if x < 0 or y < 0 or nodo.getColor_Box() == Black \
            or nodo.getColor_Box() == Path or nodo.getColor_Box() == Gray or nodo.getColor_Box() == Red:
            return False

        if (nodo.getPosX_Box() == Civil.getPosX_Box()) and (nodo.getPosY_Box() == Civil.getPosY_Box()):
            return True

        nodo.setColor_Box(Path)

        if find_path_Rescue(x,y+1) or find_path_Rescue(x,y-1) or find_path_Rescue(x+1,y) or find_path_Rescue(x-1,y):
            return True
        
        nodo.setColor_Box(Withe)

        # if find_path_Rescue(x,y) == False:
        #     nodo.setColor_Box(Path)

        return False

    except:
        print('Cambiando Ruta')
#---------------------------------------------------------------------------- 
#---------------------------------------------------------------------------- 

def find_path_Extract(x,y):

    global citys
    global codes
    global Civil
    global Recurso
    global capacidad_final

    global robot

    global Black
    global Withe
    global Path
    global Gray 
    global Red
    global Green

    try:
        nodo: Box = codes.color_patterns.get_Boxs_By_Pos(int(x),int(y))

        if x < 0 or y < 0 or nodo.getColor_Box() == Black \
            or nodo.getColor_Box() == Path or nodo.getColor_Box() == Blue:
            return False

        if (nodo.getPosX_Box() == Recurso.getPosX_Box()) and (nodo.getPosY_Box() == Recurso.getPosY_Box()):
            return True
  
        nodo.setColor_Box(Path)

        if find_path_Extract(x,y+1) or find_path_Extract(x,y-1) or find_path_Extract(x+1,y) or find_path_Extract(x-1,y):
            return True

        nodo.setColor_Box(Withe)
    
        # if find_path_Extract(x,y) == False:
        #     nodo.setColor_Box(Path)

        return False

    except:
        print('Cambiando Ruta')
#---------------------------------------------------------------------------- 
#---------------------------------------------------------------------------- 
  
def main_menu(linked_list: Linked_list_city,linked_robots: Linked_list_robot):
    flag = True
    while flag:
        print()
        print('=======================')
        print('Menu Principal')
        print('=======================')
        print('1. Cargar Data')
        print('2. Mostrar Ciudadaes Cargadas')
        print('3. Seleccionar Una Ciudad')
        print('4. Salir')
        print('=======================')

        option = input('> ')

        if option == '1':
            Tk().withdraw()
            filename = askopenfilename(initialdir="./",filetypes = [('Files','*.xml')])
            datas = open(filename, 'r+', encoding='utf-8')
            MiniDom(datas, linked_list,linked_robots)
            #MiniDom('./Files/ArchivoPruebas.xml', linked_list,linked_robots)
            print('> La data se ha cargado!')
        elif option == '2':
            print()
            print('> Ciudades Cargadas: ')
            linked_list.show_Citys()
        elif option == '3':
            second_menu(linked_list,linked_robots)
            break
        elif option == '4':
            flag = False
            print('=======================')
            print('=>Ejecucion Terminada<=')
            print('=======================')
        else:
            print(' > Opcion Invalida!')
#---------------------------------------------------------------------------- 

#----------------------------------------------------------------------------
if __name__ == '__main__':
    linked_city = Linked_list_city()
    linked_robots = Linked_list_robot()
    main_menu(linked_city,linked_robots)