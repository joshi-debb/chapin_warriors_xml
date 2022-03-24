from xml.dom import minidom

import os 
import webbrowser

#----------------------------------------------------------------------------
class Boxes_List():   #lista doblemente enlazada
    def __init__(self) -> None:
        self.boxes_head : Box = None #cabecera
        self.boxes_bottom = None #final
        self.boxes_size = 0

    def add_to_end(self,box,box_posX,box_posY,box_color,font_color):
        new_boxes = Box(box,box_posX,box_posY,box_color,font_color)
        self.boxes_size += 1
        if self.boxes_head is None:
            self.boxes_head = new_boxes
            self.boxes_bottom = new_boxes
        else:
            self.boxes_bottom.setNext_Box(new_boxes)
            new_boxes.setPrevius_Box(self.boxes_bottom)
            self.boxes_bottom = new_boxes
        return new_boxes

    def get_Boxs(self, box):
        tmp = self.boxes_head
        while tmp != None:
            if tmp.get_Box() == box:
                return tmp
            tmp = tmp.getNext_Box()
    
    def get_Boxs_By_Pos(self, pos_x, pos_y):
        tmp = self.boxes_head
        while tmp != None:
            if tmp.getPosX_Box() == pos_x and tmp.getPosY_Box() == pos_y:
                return tmp
            tmp = tmp.getNext_Box()

    def slide_Derecha(self):
        tmp =  self.boxes_head
        while tmp != None:
            tmp = tmp.getColor_Box()

    def show_Boxes2(self):
        tmp = self.boxes_head
        while tmp != None:
            print('Color:', tmp.get_Box(), 'Pos X: ', tmp.getPosX_Box(), 'Pos Y: ' , tmp.getPosY_Box())
            tmp = tmp.getNext_Box()
    
    def show_Boxes(self, name , code):
        tmp = self.boxes_head

        strGrafica = 'digraph G { \n graph [pad="1" bgcolor="purple:pink" style="filled" margin="0"  penwidth="3"] \n'
        strGrafica += 'label = "Nombre Piso: {} Codigo Piso: {}" fontname="Arial Black" fontsize="20pt" \n'.format(name,code)
        strGrafica += 'node [style = filled shape = box height="1" width="1"] \n'
        #strGrafica += 'edge [dir="both" arrowsize = "0.3"] \n'

        while tmp != None:
            strGrafica += '{}[fillcolor= "{}" fontcolor = "{}" pos="{},-{}!"] \n'.format(tmp.get_Box(),tmp.getColor_Box(),tmp.getFont_Box(),tmp.getPosX_Box(),tmp.getPosY_Box())
            tmp = tmp.getNext_Box()

        tmp = self.boxes_head
        while tmp != None:
            if tmp.getNext_Box() is None:
                None
            else: 
                strGrafica += '{}->{};\n'.format(tmp.get_Box(),tmp.getNext_Box().get_Box())
            tmp = tmp.getNext_Box()
        
        strGrafica += ' } '
        documentotxt = 'textoplano.txt'
        with open(documentotxt,'w') as grafica: 
            grafica.write(strGrafica)
        pdf = 'G{}{}.pdf'.format(name,code)
        os.system( 'neato -Tpdf ' + documentotxt + ' -o ' + pdf )
        webbrowser.open(pdf)
#----------------------------------------------------------------------------
class Box():
    def __init__(self, box,box_posX,box_posY,box_color,font_color) -> None:
        self.box_font: str = font_color
        self.box_color: str = box_color
        self.box_posX: int = box_posX
        self.box_posY: int = box_posY
        self.box =  box
        self.next_box = None
        self.previus = None
        self.up_box = None
        self.down_box = None

    def get_Box(self):
        return self.box

    def set_Box(self, box):
        self.box = box

    def getPosX_Box(self):
        return self.box_posX

    def setPosX_Box(self, box_posX):
        self.box_posX = box_posX

    def getPosY_Box(self):
        return self.box_posY

    def setPosY_Box(self, box_posY):
        self.box_posY = box_posY

    def getColor_Box(self):
        return self.box_color

    def setColor_Box(self, box_color):
        self.box_color = box_color

    def getFont_Box(self):
        return self.box_font

    def setFont_Box(self, box_font):
        self.box_font = box_font

    def getNext_Box(self):
        return self.next_box

    def setNext_Box(self, next_box):
        self.next_box = next_box
    
    def getPrevius_Box(self):
        return self.previus

    def setPrevius_Box(self, previus):
        self.previus = previus

    def getUp_Box(self):
        return self.up_box

    def setUp_Box(self, up):
        self.up_box = up
    
    def getDown_Box(self):
        return self.down_box

    def setDown_Box(self, down):
        self.down_box = down
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
class Linked_list():
    def __init__(self) -> None:
        self.head : Node = None #cabecera
        self.bottom = None #final
        self.size = 0

    def add_to_end(self, city_name, char, index):
        new = Node (city_name, char, index)
        self.size += 1
        if self.head is None:
            self.head = new
            self.bottom = new
        else:
            self.bottom.setNext_Char(new)
            self.bottom = new
        return new

    def get_size(self):
        count = 0
        node = self.head
        while node != None:
            node = node.getNext_Char()
            count = count + 1
        return count

    def get_chars(self, city_name):
        tmp = self.head
        while tmp != None:
            if tmp.getCity_Name() == city_name:
                return tmp
            tmp = tmp.getNext_Char()
    
    def get_next_in_list(self, index):
        tmp = self.head
        while tmp != None:
            if tmp.getIndex() == index:
                return tmp.getChar()
            tmp = tmp.getNext_Index()

    def show_chars(self):
        tmp = self.head
        for i in range(self.size):
            print(tmp.getChar())
            tmp = tmp.getNext_Char()
#----------------------------------------------------------------------------
class Node():
    def __init__(self, city_name,char, index) -> None:
        self.char = char
        self.index = index
        self.city_name = city_name
        self.colors = Boxes_List()
        self.next = None
    
    def getCity_Name(self):
        return self.name

    def getChar(self):
        return self.char
    
    def getIndex(self):
        return self.index

    
    def getNext_Index(self):
        return self.next

    def setNext_Index(self, index):
        self.next = index

    def getNext_Char(self):
        return self.next

    def setNext_Char(self, char):
        self.next = char
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
class Linked_list_military():
    def __init__(self) -> None:
        self.military_head : Node_military = None #cabecera
        self.military_bottom = None #final
        self.military_size = 0

    def add_to_end(self, pos_x, pos_y, capacity):
        new_military = Node_military(pos_x, pos_y, capacity)
        self.military_size += 1
        if self.military_head is None:
            self.military_head = new_military
            self.military_bottom = new_military
        else:
            self.military_bottom.setNext_Military(new_military)
            self.military_bottom = new_military
        return new_military

    def get_Militarys(self, capacity):
        tmp = self.military_head
        while tmp != None:
            if tmp.getCapacity_Military() == capacity:
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
        self.robot_bottom = None #final
        self.robot_size = 0

    def add_to_end(self,robot_name, robot_type, robot_capacity):
        new_robot = Node_robot(robot_name, robot_type, robot_capacity)
        self.robot_size += 1
        if self.robot_head is None:
            self.robot_head = new_robot
            self.robot_bottom = new_robot
        else:
            self.robot_bottom.setNext_Robot(new_robot)
            self.robot_bottom = new_robot
        return new_robot

    def get_Decks(self, robot_name):
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

    def show_Robots(self):
        tmp = self.robot_head
        for i in range(self.robot_size):
            print('Nombre:', tmp.getName_Robot(), 'Tipo:', tmp.getType_Robot(), 'Capacidad: ', tmp.getCapacity_Robot())
            tmp = tmp.getNext_Robot()
#----------------------------------------------------------------------------
class Node_robot():
    def __init__(self, robot_name, robot_type, robot_capacity) -> None:
        self.robot_name: str = robot_name
        self.robot_type: str = robot_type
        self.robot_capacity: int = robot_capacity
        #self.code_patterns = Patterns_List()
        self.next_robot = None

    def getName_Robot(self):
        return self.robot_name
            
    def getType_Robot(self):
        return self.robot_type
            
    def getCapacity_Robot(self):
        return self.robot_capacity
        
    def getNext_Robot(self):
        return self.next_robot

    def setNext_Robot(self, robot):
        self.next_robot = robot
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
class Linked_list_city():
    def __init__(self) -> None:
        self.city_head : Node_city = None #cabecera
        self.city_bottom = None #final
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

    def get_size(self):
        count = 0
        node = self.city_head
        while node != None:
            node = node.getNext_City()
            count = count + 1
        return count

    def show_Citys(self):
        tmp = self.city_head
        for i in range(self.city_size):
            print('Nombre:', tmp.getName_City(), 'Filas:', tmp.getRow_City(), 'Columnas: ', tmp.getColumn_City())
            tmp = tmp.getNext_City()
#----------------------------------------------------------------------------
class Node_city():
    def __init__(self, city_name, city_rows, city_column) -> None:
        self.city_name: str = city_name
        self.city_rows: int = city_rows
        self.city_column: int = city_column
        self.military_units = Linked_list_military()
        self.row_list = Linked_list()
        self.next_city = None

    def getName_City(self):
        return self.city_name
            
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
#Globals
name = ''
rows = 0
columns = 0
pattern_code = ''
pattern = ''


#----------------------------------------------------------------------------
def MiniDom(ruta, linked_list: Linked_list_city, linked_robots: Linked_list_robot):
    mydoc = minidom.parse(ruta)

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
        count = 0
        for row_list in rowses:
            row_list.attributes['numero'].value
            node = row_list.firstChild.data
            for nodes in node:
                nodeses = cityses.row_list.add_to_end(name,nodes,count)
                count += 1
            
                pos_x = 0
                pos_y = 0
                contador = 1

                Withe = '#FFFFFF'
                Black = '#000000'
                Green = '#008000'
                Red = '#FF0000'
                Blue = '#0000FF'
                Gray = '#808080'
                Font_W = 'white'
                Font_B = 'black'
                Font_G = 'green'
                Font_R = 'red'
                Font_Bu = 'blue'
                Font_Gr = 'gray'
                
                for i in range(cityses.row_list.get_size()):
                    color = cityses.row_list.get_next_in_list(i)
                    count_rows = 0
                    while int(rows) > count_rows:
                        count_cols = 0
                        if color == ' ':
                            color = 'W{}'.format(str(contador))
                            nodeses.colors.add_to_end(color,pos_x,pos_y,Withe,Font_W)
                            contador += 1 
                            pos_x += 1 
                        elif color == '*':
                            color = 'B{}'.format(str(contador))
                            nodeses.colors.add_to_end(color,pos_x,pos_y,Black,Font_B)
                            contador = contador +1
                            pos_x += 1
                        elif color == 'E':
                            color = 'E{}'.format(str(contador))
                            nodeses.colors.add_to_end(color,pos_x,pos_y,Green,Font_G)
                            contador = contador +1
                            pos_x += 1
                        elif color == 'C':
                            color = 'C{}'.format(str(contador))
                            nodeses.colors.add_to_end(color,pos_x,pos_y,Blue,Font_Bu)
                            contador = contador +1
                            pos_x += 1
                        elif color == 'R':
                            color = 'R{}'.format(str(contador))
                            nodeses.colors.add_to_end(color,pos_x,pos_y,Gray,Font_Gr)
                            contador = contador +1
                            pos_x += 1
                        while int(columns) > count_cols:
                            count_cols += 1
                        if color == ' ':
                            color = 'W{}'.format(str(contador))
                            nodeses.colors.add_to_end(color,pos_x,pos_y,Withe,Font_W)
                            contador += 1 
                            pos_x += 1 
                        elif color == '*':
                            color = 'B{}'.format(str(contador))
                            nodeses.colors.add_to_end(color,pos_x,pos_y,Black,Font_B)
                            contador = contador +1
                            pos_x += 1
                        elif color == 'E':
                            color = 'E{}'.format(str(contador))
                            nodeses.colors.add_to_end(color,pos_x,pos_y,Green,Font_G)
                            contador = contador +1
                            pos_x += 1
                        elif color == 'C':
                            color = 'C{}'.format(str(contador))
                            nodeses.colors.add_to_end(color,pos_x,pos_y,Blue,Font_Bu)
                            contador = contador +1
                            pos_x += 1
                        elif color == 'R':
                            color = 'R{}'.format(str(contador))
                            nodeses.colors.add_to_end(color,pos_x,pos_y,Gray,Font_Gr)
                            contador = contador +1
                            pos_x += 1
                        count_rows = count_rows + 1
                        if pos_x >= int(columns):
                            pos_y += 1
                            pos_x = 0
                #print(color)
        #cityses.row_list.show_chars()
        #nodeses.colors.show_Boxes('nombre','codigo')

        for military in military_unit:
            combat_capacity = military.firstChild.data
            military_pos_x = military.attributes['fila'].value
            military_pos_y = military.attributes['columna'].value
            cityses.military_units.add_to_end(military_pos_x,military_pos_y,combat_capacity)
            #cityses.military_units.show_Militarys()
    
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






def main_menu(linked_list: Linked_list_city,linked_robots: Linked_list_robot):
    flag = True
    while flag:
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
            MiniDom('./Files/ArchivoPrueba.xml', linked_list,linked_robots)
            print(' > La data se ha cargado!')
        elif option == '2':
            print(' > Ciudades Cargadas: ')
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

linked_city = Linked_list_city()
linked_robots = Linked_list_robot()
if __name__ == '__main__':
    main_menu(linked_city,linked_robots)