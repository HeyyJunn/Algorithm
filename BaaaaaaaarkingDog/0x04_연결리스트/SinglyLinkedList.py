class Node:
  def __init__(self, value):
    self.value = value
    self.next = None 

class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  # Node 맨 앞 삽입
  def push_front(self, value):
    new_node = Node(value)
    new_node.next = self.head
    self.head = new_node

    if self.size == 0:
      self.tail = new_node
    
    self.size += 1

  # Node 를 맨 뒤 삽입
  def push_back(self, value):
    new_node = Node(value)
    
    if self.size == 0:
      self.head = new_node
      self.tail = new_node 
    else:
      self.tail.next = new_node
      self.tail = new_node

    self.size += 1

  # 맨 앞 Node 삭제, 값 반환
  def pop_front(self):
    if self.size == 0:
      raise IndexError("pop from empty list")
    
    removed = self.head
    self.head = self.head.next
    self.size -= 1

    if self.size == 0:
      self.tail = None
    
    return removed.value
  # 탐색 value가 있으면 True, 없으면 False
  def find(self, value):
    cur = self.head

    while cur is not None:
      if cur.value == value:
        return True
      cur = cur.next
    return False
  # index번째 값 가져오기 (0-index)
  def get(self, index):
    if index < 0 or index >= self.size:
      raise IndexError("index out of range")
    
    cur = self.head

    for _ in range(index):
      cur = cur.next
    return cur.value
  
  def debug_print(self):
    cur = self.head
    parts = []
    while cur is not None:
      parts.append(str(cur.value))
      cur = cur.next

    print(" -> ".join(parts) if parts else "(empty)")
    print(f"size={self.size}, head={self.head.value if self.head else None}, tail={self.tail.value if self.tail else None}")
    print("-" * 40)



def main():
    ll = SinglyLinkedList()

    print("[1] 빈 리스트 상태")
    ll.debug_print()

    print("[2] push_back 10, 20, 30")
    ll.push_back(10)
    ll.push_back(20)
    ll.push_back(30)
    ll.debug_print()

    print("[3] push_front 5")
    ll.push_front(5)
    ll.debug_print()

    print("[4] get 테스트")
    print("get(0) =", ll.get(0))  # 5
    print("get(2) =", ll.get(2))  # 20
    print("get(3) =", ll.get(3))  # 30
    print("-" * 40)

    print("[5] find 테스트")
    print("find(20) =", ll.find(20))  # True
    print("find(99) =", ll.find(99))  # False
    print("-" * 40)

    print("[6] pop_front 테스트")
    print("pop_front() =", ll.pop_front())  # 5
    ll.debug_print()

    print("[7] pop_front 여러 번 해서 빈 리스트 만들기")
    print("pop_front() =", ll.pop_front())  # 10
    print("pop_front() =", ll.pop_front())  # 20
    print("pop_front() =", ll.pop_front())  # 30
    ll.debug_print()

    print("[8] 빈 리스트에서 pop_front 예외 확인")
    try:
        ll.pop_front()
    except IndexError as e:
        print("예외 발생 확인:", e)
        print("-" * 40)

    print("[9] 다시 값 넣고 head/tail 정상인지 확인")
    ll.push_back(100)
    ll.debug_print()
    ll.push_front(50)
    ll.debug_print()

if __name__ == "__main__":
    main()
