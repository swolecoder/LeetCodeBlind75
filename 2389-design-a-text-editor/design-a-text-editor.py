from threading import Lock

class TextEditor:
    def __init__(self):
        self.left = []
        self.right = []
        self.lock = Lock()  # A lock to ensure thread-safe operations

    def addText(self, text: str) -> None:
        with self.lock:  # Acquire the lock before modifying the state
            for char in text:
                self.left.append(char)

    def deleteText(self, k: int) -> int:
        with self.lock:  # Acquire the lock before modifying the state
            count = 0
            while self.left and k > 0:
                self.left.pop()
                k -= 1
                count += 1
            return count

    def cursorLeft(self, k: int) -> str:
        with self.lock:  # Acquire the lock before modifying the state
            while self.left and k > 0:
                self.right.append(self.left.pop())
                k -= 1
            return "".join(self.left[-10:])

    def cursorRight(self, k: int) -> str:
        with self.lock:  # Acquire the lock before modifying the state
            while self.right and k > 0:
                self.left.append(self.right.pop())
                k -= 1
            return "".join(self.left[-10:])


        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)