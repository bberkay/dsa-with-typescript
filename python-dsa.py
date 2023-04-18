"""

    ALGORİTMA - CODE COMPLEXITY
    UDEMY: https://www.udemy.com/course/algorithms-data-structures-and-real-life-python-problems/

"""


def square_sum1(n):
    """
        Take an input of n and return the sum of the squares of numbers from 0 to n
    """
    total = 0
    for x in range(1, n + 1):
        total += x ** 2
    return total


# print(square_sum1(5))
# return -> 55

def square_sum2(n):
    """
        Take an input of n and return the sum of the squares of numbers from 0 to n with formula
    """
    return (n * (n + 1) * (2 * n + 1)) / 6


# print(square_sum2(5))
# return -> 55

############################################################################################################

"""

    Big-O Notation(Asymptotic Analysis)
    - Algoritmaların hızlarını ölçmek için kullanılan sistem.
    - Çoğu Big-O fonksiyonu inputların büyüklüğüne göre ölçülür.
        - Örn: Big-O       | Name         | Complexity
             : 1             Constant       Excellent
             : log(n)        Logarithmic    Good
             : n             Linear         Fair
             : nlog(n)       Log Linear     Bad
             : n^2           Quadratic      Bad
             : n^3           Cubic          Horrible
             : 2^n           Exponential    Horrible
             
"""

############################################################################################################

"""

    Big O | Omega | Theta
    - Big O : yazdığımız kodun en kötü durumda nasıl çalıştığını test etmek için kullanılır
    - Omega : yazdığımız kodun en iyi durumda nasıl çalıştığını test etmek için kullanılır.
    - Theta : mid case senaryo
    
"""

############################################################################################################

"""
    Big-O Notation Örnekleri
"""

"""

    O(1) Constant
    - Constant çünkü input size'dan bağımsız.
    - Eğer input size çok büyük olsaydı yine sonuç değişmeyecekti.

"""


def constant_big_o(liste):
    print(liste[0])


# constant_big_o([0,1,2,3,4,5,6,7,8,9])
# return -> 0

"""

    O(n) Linear
    - Bu fonksiyon linear zamanda çalışır. Yani algoritma içerisinde ki operasyon sayısı input size ile doğru orantılı.
    - Mesela input size 5 olsaydı, 5 kez print fonksiyonu çağırılacaktı. Yani input size ile doğru orantılı
    - Ya da input size 2 olsaydı, 2 kez print fonksiyonu çağırılacaktı.

"""


def linear_big_o(liste):
    for i in liste:
        print(i)


# linear_big_o([1,2,3,4,5,6,7,8,9])
# return -> 1 \n 2 \n 3 \n .... \n 9

"""

    O(n^3) Cubic
    - Nested loop'lardan oluşan 3 tane for döngüsü kullanacağız.
    - Yani n^3 işlem yapacağız.
    - Mesela input size = 3 için, 27 tane işlem yapacağız.

"""


def cubic_big_o(liste):
    for item_1 in liste:
        for item_2 in liste:
            for item_3 in liste:
                print(item_1, item_2, item_3)


# cubic_big_o([1,2,3])
# return -> 1 1 1 \n 1 1 2 \n 1 1 3 \n 2 1 1 \n .... \n 3 3 3

############################################################################################################

"""

    Calculating Scale of Big-O 
    
"""

"""

    - Insignificant Constant
    - Linear Big-O input size ile doğru orantılı
    - İlk örneğimde big-O = O(n)
    - İkinci örneğimde big-O = O(2n)
    - 2 burada insignificant constant olarak geçer ve bu sabit sayısı ihmal edebiliriz.
    - Yani her iki durum içinde big-O = O(n)
    
"""


def linear_big_o(liste):
    for i in liste:
        print(i)


# linear_big_o([1,2,3]) -> O(n)
# return -> 1 \n 2 \n 3

def linear_big_o_2(liste):
    for i in liste:
        print(i)
    for i in liste:
        print(i)


# linear_big_o_2([1,2,3]) -> O(2n) '2' ihmal edilebilir. n = sonsuz ise sonsuz * 2 gene sonsuzdur.
# return -> 1 \n 2 \n 3 \n 1 \n 2 \n 3

"""

    - Bu örnekte insignificant term 1 sayısıdır. Bu nedenle ihmal edebiliriz.
    - Insignificant olup olmadığını anlamak içinde n değerine sonsuz verip deneyelim.
    - Sonuç olarak example metodunun O(n)'dir.
 
"""


def example(liste):
    print(liste[0])  # O(1) constant

    for each in liste:  # O(n) linear
        print(each)


# example([1,2,3,4])
# return -> 1 \n 1 \n 2 \n 3 \n \ 4

############################################################################################################

"""
    
    - ALGORİTMA ÖRNEKLERİ
    
"""


# Faktoriyel
def factorial(num):
    return num * factorial(num - 1) if num > 1 else 1


# factorial(5)
# return -> 120


# Kelimenin Tersi
def reverseStr(txt):
    return txt[::-1]


# reverseStr("istanbul")
# return -> "lubnatsi"


# Saat çevirme
def convertMinToHour(min):
    return str(min // 60) + "." + str(min % 60)


# convertMinToHour(128)
# return -> 2.8 Saat


# Baş Harf Büyütme
def upFirstLetter(txt):
    txt = ""
    for i in txt.split(" "):
        txt = txt + " " + i[0].upper() + i[1:]
    return txt


# upFirstLetter("hello world")
# return -> "Hello World"


# Kelime Karıştırma
def mixWord(txt1, txt2):
    for i in txt1:
        if i not in txt2:
            return False
    return True


# mixWord("ankara", "kaarna")
# return -> True


# Sıklık Bulma
def findDuplicate(txt):
    liste = {}
    result = ""
    for i in txt:
        if i not in liste:
            liste.update({i: 1})
        else:
            liste.update({i: liste[i] + 1})
    for i, k in liste.items():
        result += str(k) + k * i
    return result


# findDuplicate("kkwcccddee"))
# return -> 2kk1w3ccc2dd2ee


# Array Rotasyonu
def arrayRotation(val):
    result_left = ""
    result_right = ""
    index = val[0]
    i = 0
    while i < len(val):
        if index <= i:
            result_left += str(val[i])
        if index > i:
            result_right += str(val[i])
        i += 1
    return result_left + result_right


# arrayRotation([4,5,6,7,8,9,10,11,12,13])
# return -> 89101112134567


# Array Pairs
def arrayPairs(val):
    i = 0
    while i < len(val):
        if i % 2 != 0:
            if val[i] == val[i - 1]:
                return str(val[i]) + "," + str(val[i - 1])
        i += 1
    return "ok"


# arrayPairs([5,6,6,5,3,3])
# return -> 3,3


############################################################################################################

"""

    - STACKS - QUEUES - DEQUES

"""

"""
    
    STACKS
    - Ekleme ve çıkarma işlemlerinin her zaman aynı yerden yapıldığı stack(yığın) denir.
    - Bu ekleme çıkarma işlemi "top" kısmından yapılır.
    - Top'ın tersi olan kısma da "base" denir.
    - İlk giren son çıkar LIFO(Last in First Out) mantığı ile çalışır.
    - Karakteristik özelliği Push ve Pop işlemleridir. Yığına veri atılması işlemine push işlemi denir. Yığından veri çekilmesi işlemine de pop denir.
    - Üç ana fonksiyonu vardır
        - Push: Stack içerisine eleman koyma
        - Pop: Stack içerisindne eleman alma
        - Top: Stack'in en tepesindeki elemanı gösterme

"""


# Stack With Python
class Stack:
    def __init__(self):
        """
        initialize(constructor)
        """
        self.items = []

    def isEmpty(self):
        """
        Boş olup olmadığını kontrol eder.
        :return: boolean
        """
        return self.items == []

    def push(self, item):
        """
        Stack'e item ekler.
        """
        self.items.append(item)

    def pop(self):
        """
        Stack'ten item çıkartır.
        """
        return self.items.pop()

    def top(self):
        """
        Stack içerisindeki son item'i gösterir.
        """
        return self.items[len(self.items) - 1]

    def size(self):
        """
        Stack'in boyutunu döner.
        :return: int
        """
        return len(self.items)


# stack = Stack()
# print(stack.isEmpty()) -> "True"
# stack.push("ankara") -> " En sona item ekliyor"
# stack.push("istanbul") -> " En sona item ekliyor"
# print(stack.top()) -> "istanbul"
# print(stack.size()) -> 2
# stack.pop() -> "En sondaki itemi çıkartıyor(istanbul)"
# print(stack.top()) -> "ankara"


"""

    QUEUES
    - "rear" kısmından veri ekleriz. "front" kısmından veri çıkartırız.
    - İlk giren ilk çıkar. (FIFO, first in first out ya da first come first served)
    - Enqueue item eklemek. Dequeue item çıkarmak.

"""


# Queues with Python
class Queue:
    def __init__(self):
        """
        initialize(constructor)
        """
        self.items = []

    def isEmpty(self):
        """
        Boş olup olmadığını kontrol eder.
        :return: boolean
        """
        return self.items == []

    def enqueue(self, item):
        """
        Queue' ya item ekler.
        """
        self.items.insert(0, item)

    def dequeue(self):
        """
        Queue' dan item çıkartır.
        """
        return self.items.pop()

    def size(self):
        """
        Queue'nun uzunluğu
        :return: int
        """
        return len(self.items)


# queue = Queue()
# print(queue.isEmpty()) -> "True"
# queue.enqueue("ankara") -> "En başa item ekliyor"
# queue.enqueue("istanbul") -> "En başa item ekliyor"
# print(queue.size()) -> 2
# queue.dequeue() -> "sondaki itemi çıkartıyor(ankara)"
# print(queue.size()) -> 1


"""

    DEQUEUE
    - Double ended queue olarak bilinir.
    - İki tane "end", "front" ve "rear" a sahip
    - Üstten ve alttan eklemek ve çıkarmalar yapılabilir.

"""


# Dequeue with Python
class Dequeue:
    def __init__(self):
        """
        initalize(constructor)
        """
        self.items = []

    def isEmpty(self):
        """
        Boş olup olmadığını kontrol eder.
        :return: boolean
        """
        return self.items == []

    def addFront(self, item):
        """
        Deque'ya front kısmından item ekler.
        """
        self.items.append(item)

    def addRear(self, item):
        """
        Deque'ya rear kısmından item ekler.
        """
        self.items.insert(0, item)

    def removeFront(self):
        """
        Deque front kısmından item çıkartır.
        """
        return self.items.pop()

    def removeRear(self):
        """
        Deque rear kısmından item çıkartır.
        """
        return self.items.pop(0)

    def size(self):
        """
        Deque uzunluğunu döner.
        :return: int
        """
        return len(self.items)


# dequeue = Dequeue()
# print(dequeue.isEmpty()) -> True
# dequeue.addFront("deep") -> front kısmına "deep" ekler.
# dequeue.addRear("learning") -> rear kısmına "learning" ekler.
# print(dequeue.size()) -> 2
# dequeue.removeFront() -> front kısmından "deep'i" çıkartır.
# dequeue.removeRear() -> rear kısmından "learning'i" çıkartır.
# print(dequeue.isEmpty()) -> True

"""

    ÖRNEKLER

"""

# Reverse String With Stack
def reverseWithStack(txt: str):
    global stack

    new_string = ""
    n = len(txt)
    for i in range(n):
        stack.push(txt[i])
        new_string += stack.pop()

    return new_string

# reverseWithStack("datai team")
# return -> maet iatad


############################################################################################################


"""

    - Linked List

"""

"""

    Linked List
    - Singly Linked list, linked listing en basit formudur.
    - Single linked list node'ların toplanıldığı bir linear yapıdır.
    - Her bir node hem veri depolar hem de diğer node'a ulaşmak için pointer'a(adres) sahiptir.
    - Head: link list'te ki ilk node
    - Tail: link list'te ki son node
    - Link list içerisinde bir node'dan bir node'a dolaşmaya 'traversing' denir.
    - Link listin önemli özelliklerinden bir tanesi predetermined fixed bir size'a sahip olmaması. Yani
    linked list boyutu önceden belirlenmiyor.
    - Linked list'in başına yeni bir elemen eklemek istersek
        1- Yeni node yarat
        2- Node içerisinde ki veriyi belirle
        3- Node'un adresinin(pointer) önceki head olarak belirle.
        4- Yaratılan yeni node'u head olarak belirle.
    - Linked list'in sonuna yeni bir eleman eklemek istersek
        1- Yeni node yarat
        2- Next referansı None olarak ayarla
        3- Tail'in next reference'ini bu yeni node olarak ayarla
        4- Yeni eklenen node'u tail olarak ayarla
    - Linked list'te baştan eleman çıkarmak istersek
        1- Çıkartacağımız node'dan sonraki node'u head reference yaparız. Yani head pointing çıkartılan
        node'un adresini
    - Linked list'te sondan eleman çıkarmak istersek
        1- Singly Linked list'in son elemanını çıkarmak için listemizi doubly linked list yapmamız lazım!
        
"""

# Linked List with Python
class Node():
    def __init__(self, value):
        """
        Node yarat: node has value and next pointer
        """
        self.value = value
        self.nextnode = None

    def setNextNode(self, node):
        """
        next node'un ne olduğunu set eder
        """
        self.nextnode = node

    def getNextNode(self):
        """
        bir sonraki node'u return eder.
        """
        return self.nextnode

    def getNodeValue(self):
        """
        node içerisinde depolanan değeri return eder.
        """
        return self.value


#ankara = Node("06")
#bolu = Node("14")
#istanbul = Node("34")
#ankara.setNextNode(bolu)
#print(ankara.getNextNode().getNodeValue()) -> 14
#bolu.setNextNode(istanbul)
#print(bolu.getNextNode().getNodeValue()) -> 34
#print(ankara.getNextNode().getNextNode().getNodeValue()) -> 34



"""

    Doubly Linked List
    - Doubly linked list'de her bir node kendisinden önceki ve sonraki node'un pointer'ını(adresini) 
    tutar.
    - Bir önceki node reference'ı için 'prev' keyword'ü kullanılır.
    - Listenin başında ve sonunda özel node'lar vardır.
        - Header node: listenin başında bulunan sentinel(guard) diye bilinen node'dur
        - Trailer node: listenin sonunda bulunan sentinel(guard) diye bilinen node'dur
    
"""

# Doubly Linked List with Python
class DoublyLinkedListNode(object):
    def __init__(self, value):
        """
        Node yarat: node has value, pointer and prev pointer
        """
        self.value = value
        self.nextnode = None
        self.prevnode = None

    def setNextNode(self, node):
        """
        Next node'un ne olduğunu set eder.
        """
        self.nextnode = node

    def setPrevNode(self, node):
        """
        Prev node'un ne olduğunu set eder.
        """
        self.prevnode = node

    def getNextNode(self):
        """
        Bir sonraki node'u döndür.
        """
        return self.nextnode

    def getPrevNode(self):
        """
        Bir önceki node'u döndür.
        """
        return self.prevnode

    def getNodeValue(self):
        """
        Node içerisinde depolanan veriyi return eder.
        """
        return self.value


#ankara = DoublyLinkedListNode("06")
#bolu = DoublyLinkedListNode("14")
#istanbul = DoublyLinkedListNode("34")
#ankara.setNextNode(bolu)
#bolu.setPrevNode(ankara)
#print(bolu.getPrevNode().getNodeValue()) -> 06
#bolu.setNextNode(istanbul)
#print(istanbul.getPrevNode()) -> None
#istanbul.setPrevNode(bolu)
#print(istanbul.getPrevNode().getNodeValue()) -> 14
#print(istanbul.getPrevNode().getPrevNode().getNodeValue()) -> 06



############################################################################################################


"""
   - Searching Algorithims
"""

"""
    Sequential(Linear) Search with Unordered List
    - Sequential search sıralı arama demektir.
    - Unordered list ise bir listenin içerisinde ki değerin sırasız bir şekilde bulunduğu listelerdir.
        - [5, 7, 2, 3, 15, 8, 100, 12]
    - Sequential Search de aranan sayı listenin içinde baştan başlayarak sırayla aranır.
    - Mesela 8 sayısını yukarıda tanımlı listenin içerisinde aramak istiyoruz. Aramaya baştan başlanır ve sırasıyla
    bulana kadar devam edilir. Eğer aranan sayı bulunamaz ise arama listenin sonuna kadar devam eder.
    - En iyi durumda aranan değer bulunur ise complexity of algoritma O(1)
    - Diğer durumlarda ise complexity of algoritma O(n)
"""

# Sequential Search Unordered List
def sequentialSearchUnorderedList(liste, value):
    index = 0
    found = False

    while index < len(liste) and not found:
        if liste[index] == value:
            found = True
        else:
            index += 1
    return (found, index)

#liste = [5, 7, 2, 3, 15, 8, 100, 12]
#found, index = sequentialSearchUnorderedList(liste, 15)
#print(found) -> False
#print(index) -> 8



"""
    Sequential(Linear) Search with Ordered List
    - Sequential search sıralı arama demektir.
    - Unordered list ise bir listenin içerisinde ki değerin sırasız bir şekilde bulunduğu listelerdir.
        - [2, 3, 5, 7, 8, 12, 15, 100]
    - Mesela 8 sayısını yukarıda tanımlı listenin içerisinden aramak istiyoruz. Aramaya baştan başlanır ve sırasıyla
    bulana kadar devam edilir. Eğer aranan sayı bulunamaz ise liste ordered olduğu için aranan sayıdan daha büyük bir
    sayı ile karşılaşıldığında arama sona erer.
    - Başka bir örnek vermek gerekirse. Yukarıda ki liste içerisinde 6 sayısını arıyoruz. Baştan başlayıp aramaya
    devam ederken 7 sayısı ile karşılaştığımızda arama sona erer.
    - En iyi durumda complexity of algoritma O(1)
    - En kötü durumda ise complexity of algoritma O(n)
"""

# Sequential Search Ordered List
def sequentialSearchOrderedList(liste, value):
    index = 0
    found = False
    stop = False
    
    while index < len(liste) and not found and not stop:
        if liste[index] ==  value:
            found = True
        else:
            if value < liste[index]:
                stop = True
            else:
                index += 1
    return (found, index)

#liste = [2, 3, 5, 7, 9, 12, 15, 100]
#found, index = sequentialSearchUnorderedList(liste, 15)
#print(found) -> False
#print(index) -> 8



"""
    Binary Search
    - Sequential search aksine binary search sıralı arama yapmaz.
    - Binary search ordered yani sıralı listelerde çok avantajlıdır.
    - Binary search aramaya ortadan başlar. Eğer aradığı değer ortadaki değerden büyük ise bir sonraki arama adımını
    listenin upper half kısmında yapar. Bu process böyle tekrar eder.
    - Binary search divide and conquer mantığı ile çalışır.
    - Binary search complexity of algorithm logarithmic big O yani O(log n) n bir listedeki eleman sayısı
"""

# Binary Search Sorted List
def binarySearch(liste, value):
    first_index = 0
    last_index = len(liste) - 1
    found = False

    while first_index <= last_index and not found:
        middle_index = int((first_index + last_index) / 2)

        if liste[middle_index] == value:
            found = True
        else:
            # lower half
            if value < liste[middle_index]:
                last_index = middle_index - 1
                print("lower half")
            # upper half
            else:
                first_index = middle_index + 1
                print("upper half")
        
    return found

#liste = [3, 6, 11, 12, 18, 21, 34]
#binarySearch(liste, 18) -> "upper half" \n "lower half" \n True



"""
    Hashing ve Hash Table
    - Diper searching algoritmalarından farklı olarak complexity of algorithm O(1) olan bir data structure elde edebiliriz.
    Bu konsept hashing diye adlandırılır.
    - Hash table değerlerin daha sonra kolay bulunabilmesini sağlayan bir data structure yapısıdır.
    - Hash table üzerindeki her biz pozisyon slots olarak adlandırılır.
    - Bunu boş bir liste olarak düşünebiliriz.
    - 10 tane boş slotu olan bir hash table.
    - Hash function: slotlar ve bu slotlarda ki itemler arasında bağlantı(mapping) kurmaya yarayan fonksiyondur.
    - Hash fonksiyonu item değerini alır ve bu item'in hangi slotta olduğunu return eder.
    - Hash function remainder method: item'i hangi slot'a koyacağımızı remainder yöntemi ile bulmak.
    - Mesela bir hash table'ımız var. n = 8 yani empty hash table size.
    - Bir listemiz var. [44, 36, 83, 27, 67, 41]
    - h(item) = item % n => hash value
    - collusion: birden fazla linked listing bir slot'a bağlanması.
"""



"""
    - Algoritma ne demektir ?
        - Algoritma, girdi olarak bir değer ya da değer kümesi alan ve çıktı olarak bir değer ya da değer kümesi üreten
        iyi tanımlanmış bir hesaplama prosedürüdür. Bir algoritma, girişi çıktıya dönüştüren bir hesaplama adımı dizisidir.
    - Binary Search'ü açıklayın.
        - İlk önce arrayin ortasındaki değere bakarız.
        - Aradığımız değer bu ortadaki değerden büyükse upper half'ın ortasındaki değere bakarız ve lower half'ı iptal ederiz.
        - Daha sonra aradığımız değer lower half'ın ortasında ki değerden büyükse bu seferde upper half'ın upper half'ına bakarız.
        - Arama bu süreçleri tekrar ederek sürer.
    - Binary Search time complexity (Big O) nedir?
        - Binary search recursion ile çözülebiliyor. Recursion ile implement edildiği zaman O(Log n)dir.
    - Binary Search ile Linked list de arama yapılır mı?
        - Hayır. Binary search de arama ortadan başladığı için linked listte bir anda(yani O(1) sürede) ortaya gidemez.
    - Hash algorithm nerelede kullanılır?
        - Şifre doğrulama
    - Algoritmada best case ve worst case senaryolarının tanımı nedir?
        - Best case: en hızlı mesela binary search de aranan değerin arrayin ortasında olması.
        - Worst case: en yavaş
"""



############################################################################################################    



"""
    Sorting Algorithms
"""

"""
    Bubble Sort
    - Bir listede birbirine ardışık duran iki değeri sıralama yapar ve bu süreci tüm liste sıralı
    hale gelene kadar devam eder.
"""

# Bubble Sort
def bubbleSortAlgorithm(arr):
    for n in range(len(arr)-1, 0, -1):
        for k in range(n):
            if arr[k] > arr[k+1]:
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp

    return arr

#print(bubbleSortAlgorithm([3, 2, 13, 4, 6, 5, 7, 8, 20])) -> [2, 3, 4, 5, 6, 7, 8, 13, 20]



"""
    Insertion Sort
    - Sub list kullanır.
    - İlk value bir sub list elemanıdır ve zaten tek bir değere sahip olduğu için sıralıdır. Bu sub listenin
    içerisinde kalan değerler karlılaştırılarak eklenir.
"""

# Insertion Sort
def insertionSortAlgorithm(arr):
    for i in range(i, len(arr)):
        current_value = arr[i]
        position = i

        while position > 0 and arr[position-1] > current_value:
            arr[position] = arr[position-1]
            position -= 1
        arr[position] = current_value
    return arr

#print(insertionSortAlgorithm([3, 2, 13, 4, 6, 5, 7, 8, 1, 20])) -> [1, 2, 3, 4, 5, 6, 7, 8, 13, 20]


   
"""
    Selection Sort
    - Sıralı olmayan bir listem var.
    - Bu listenin içerisinde en küçük değeri bulup index 0'a atarım.
    - Daha sonra bir sonraki en küçük değeri bularak aramama devam ederim.
"""

# Selection Sort
def selectionSortAlgorithm(arr):
    for i in range(len(arr)-1, 0, -1):
        position_of_max = 0

        for location in range(1, i + 1):
            if arr[location] > arr[position_of_max]:
                position_of_max = location
        temp = arr[i]
        arr[i] = arr[position_of_max]
        arr[position_of_max] = temp
    return arr

#print(selectionSortAlgorithm([3, 2, 13, 4, 6, 5, 7, 8, 1, 20]))



############################################################################################################    



"""
    Tree Theory
"""

"""
    Tree
    - Trees bir data structure'dır. Aynı zamanda belirli özellikleri taşıyan bir graph'dır.
    - Trees yapısı array, linked list ve queue gibi linear data structure'ların aksine hierarchical data structure'dır.
    - Root, Parent, Child, Leaves/Leaf ve Siblings gibi terimler vardır.
        - Root, en üst eleman
        - Parent, altında eleman bulunan eleman
        - Child, parentın altında bulunan eleman
        - Leaves, altında eleman bulunmayan eleman
        - Siblings aynı parentın altında bulunan elemanlar
    - Tree'lerin kullanım alanlarından ilki hierarchy olması durumudur. Mesela bilgisayarlarımızda bulunan dosya yapısı.
    - Trees bazı durumlarda hem arama yapmada hem de node ekleme ve çıkarmada diğer data structure'lardan hızlıdır.
    Bu nedenle hierarchy söz konusu ise avantaj sağlar.
"""



"""
    Binary Tree
    - Node'larında en fazla 2 children olan yapılara denir.
    - Children sayısı maksimum 2 olacağı için isimleri left ve right olarak adlandırılmıştır.
    - Left child ve right child gibi.
    - Belirli bir levelde ki maksimum node sayısı -> 2^L
    - Mesela 3.levelde maksimum node sayısı 2^3 = 8
    - Height = istenilen node'dan en aşağıda bir yaprağa doğru olan path'lerin toplam sayısı
    - Root height = 3 = height of tree
    - leaves height = 0
    - Bazı önemli tree tipleri
        - Full Binary Tree: Her bir node 0 ya da 2 çocuğa sahip olan yapılar.
        - Complete Binary Tree: Ya tüm level'ları dolu olacak ya da en azından son level'ında nodelar olabildiğince sol tarafta olacak.
        - Perfect Binary Tree: Tüm node'lar 2 children'a sahip olacak ayrıca tüm leaves aynı level'da olacak.
        - A degenerate (or pathological) tree: Her node 1 child'a sahipse.
"""

# Binary Tree
class Node:
    def __init__(self, key):
        self.val = key
        self.right = None
        self.light = None

#root = Node("A")
#root.left = Node("B")
#root.left.left = Node("D")
#root.right = Node("C")



"""
    Binary Search Tree
    - Her node'a solundaki kolundan ulaşabilecek bütün değerlerin node'un değerinden küçük, sağ kolundan ulaşılabilecek
    bütün değerlerin o node'un değerinden büyük olmasını şart koşar.
    - Ve tabii ki ayrıca binary tree olmak zorunda
    - BST'de ordering olmasından dolayı search hızlı yapılır.
    - En kötü durumda(worst case) searching ve inserting operation'ların time complexity'si O(h)dır. h = height
"""

# Binary Search Tree
class Node:
    def __init__(self, key):
        self.val = key
        self.right = None
        self.light = None

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
                
#r = Node(41)
#insert(r, Node(65))
#insert(r, Node(99))
#insert(r, Node(11))

def inorder(root):
    if root:
        inorder(root.left)
        inorder(root.right)
        print(root.val)
    else:
        return None

#inorder(r) -> 11 \n 65 \n 99



############################################################################################################    



"""
    Graph Theory
"""

"""
    Graph Theory
    - Graph'lar tree'lerden daha genel data structure'lardır.
    - Trees özel graph çeşididir.
    - Gerçek hayatta karşılaşılan problemleri graph theory kullanarak ifade edebiliriz.
    - Mesela bir ülkede ki hava trafiği, ya da internet bağlantısı
    - Yani graph theory gerçek hayatta karşılaşılan problemleri çözmek için sıklıkla kullanılır.
    - Graphs iki temel bileşenden oluşur.
        - Node(vertex)
        - Edge(E): connection between two nodes(vertices).
        - Edge iki yönlü olabilir.
            - Eğer edge tek yönlü ise directed graph ya da diagraph denir.
            - Eğer yönü yok ise un-directed graph denir.
    - Vertices = V = (Ankara, Burdur, Antalya, Konya)
    - E = {(Ankara, Burdur, 300), (Burdur, Antalya, 200)}
    - Formal graph gösterimi => G = (V, E)
    - Path: edge'ler ile birbirine bağlanan node sırası
        - Path form Ankara to Antalya: (Ankara, Burdur, Antalya)
        - Path is sequence of vertices that are connected by edges.
    - Cycle graph: bir path'in bir node'dan başlayıp aynı node'da bitmesi
"""

"""
    Adjacency Matrix and Adjacency List
    - Graph'ı ifade etmenin en kolay yollarından bir tanesi 2 boyutlu matrix kullanmaktır.
    - Her bir row and column graph'ın node'larıdır.
    - Adjacent komşu demek. Tanımı ise 2 tane node'un bir edge ile bağlanması sonucu ortaya çıkan yapıya adjacent denir.
    - Küçük graph'lar için adjaceny matrix kullanmak görme açısından kolaylık sağlar.
    - Ama gördüğüüz gibi matrix içerisinde çok fazla sayıda boş cell var. Yani boşuna yer kaplıyor. Bu boşlukları azaltmanın yolu
    graph'da edge sayısını arttırmak. Bu nedenle eğer bir graph da edge sayısı fazla ise adjaceny matrix kullanmak avantajlıdır.
    - Eğer çok graph da çok sayıda edge oksa adjaceny matrix yerine adjaceny list kullanmayı tercih etmeliyiz. 
"""

# Adjacency List
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, neighbor, weight = 0):
        self.connectedTo[neighbor] = weight

    def __str__(self):
        return str(self.id) + " connected to: " + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()
        
    def getId(self):
        return self.id

    def getWeight(self, neighbor):
        return self.connectedTo[neighbor]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        numVertex = Vertex(key)    
        self.vertList[key] = newVertex()

    def getVertex(self, n):
        if n is self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost = 0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
    
#g = Graph()
#g.addVertex(1)
#g.addVertex(2)
#g.addEdge(1, 2)


    
############################################################################################################    



"""
    Dynamic Programming
"""

"""
     Dynamic Programming
     - Dynamic programming büyük bir problemi küçük problemlere bölerek çözmek ve bu küçük problemlerin sonuçlarını
     depolayarak aynı sonuçların tekrar hesaplanmasını önler.
     - Her bir küçük problem birleşerek büyük problem için çözüm yolu oluşturur.
     - Dynamic programming'in en güzel örneği fibonachi sayılarıdır.
     - Fibonachi sayılarında pek çok repeated operation çalışır.
     - Divide big problem to the small problem and one solution will contribute to other solution.
     - Time complexity: T(n) = T(n-1) + T(n-2) which is exponential.
     - Bu metod çok fazla repeated work yapıyor bu nedenle fibonacci number n için uygun bir yöntem değil.
"""
    
























































