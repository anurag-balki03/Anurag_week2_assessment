class logger:
    def log(self, message : int) -> int:
        print("the log message : ERROR")
    def log(self, message : float) -> float:
        print("the log message : WARNING")
    def log(self, message : str) -> str:
        print("the log message : INFO")
def main():
    LOG=logger()
    msg=int(input("enter message"))
    LOG.log(msg)
    msg=float(input("enter message"))
    LOG.log(msg)
    LOG.log("message")
    
main()