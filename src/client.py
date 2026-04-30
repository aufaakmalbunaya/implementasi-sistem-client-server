import socket

HOST = "10.6.6.41"
PORT = 5020

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    f = client_socket.makefile("rwb")

    def recv_line() -> str:
        data = f.readline()
        if not data:
            return ""
        return data.decode("utf-8").rstrip("\n")

    def send_line(text: str):
        f.write((text + "\n").encode("utf-8"))
        f.flush()

    # baca 2 baris sambutan
    print(recv_line())
    print(recv_line())

    while True:
        question = recv_line()
        if question == "":
            print("Koneksi ditutup oleh server.")
            break

        print(question)
        answer = input("Jawaban: ")
        send_line(answer)

        response = recv_line()
        if response == "":
            print("Koneksi ditutup oleh server.")
            break
        print(response)

        if answer.lower() == "exit":
            break

    f.close()
    client_socket.close()

if __name__ == "__main__":
    main()