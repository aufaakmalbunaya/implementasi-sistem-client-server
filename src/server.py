import socket
import random
import threading
import logging
from datetime import datetime

HOST = "0.0.0.0"
PORT = 5012

logging.basicConfig(
    filename="server.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def handle_client(client_socket: socket.socket, addr):
    ip, port = addr
    logging.info(f"CONNECT | {ip}:{port}")

    # gunakan file-like object supaya bisa readline() dan newline-based protocol
    f = client_socket.makefile("rwb")

    def send_line(text: str):
        f.write((text + "\n").encode("utf-8"))
        f.flush()

    try:
        send_line("Selamat datang di Quiz Kalkulator!")
        send_line("Ketik 'exit' untuk keluar.")

        while True:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            question = f"Soal: {a} + {b} = ?"
            send_line(question)

            raw = f.readline()
            if not raw:
                logging.info(f"DISCONNECT (EOF) | {ip}:{port}")
                break

            answer = raw.decode("utf-8").strip()
            logging.info(f"RECV | {ip}:{port} | answer='{answer}' | question='{question}'")

            if answer.lower() == "exit":
                send_line("Terima kasih sudah bermain!")
                logging.info(f"EXIT | {ip}:{port}")
                break

            try:
                if int(answer) == a + b:
                    response = "BENAR"
                else:
                    response = f"SALAH. Jawaban benar: {a+b}"
            except ValueError:
                response = "Input tidak valid"

            send_line(response)
            logging.info(f"SEND | {ip}:{port} | response='{response}'")

    except Exception as e:
        logging.exception(f"ERROR | {ip}:{port} | {e}")
    finally:
        try:
            f.close()
        except:
            pass
        client_socket.close()
        logging.info(f"CLOSE | {ip}:{port}")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print(f"Server listening on port {PORT}...")
    logging.info(f"SERVER_START | {HOST}:{PORT}")

    while True:
        client_socket, addr = server_socket.accept()
        print("Connected by", addr)

        t = threading.Thread(target=handle_client, args=(client_socket, addr), daemon=True)
        t.start()

if __name__ == "__main__":
    main()