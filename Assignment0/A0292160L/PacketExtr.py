import sys

def main():
    buffer = b""
    while True:
        tempRead = sys.stdin.buffer.read1(1000)
        if not tempRead:
            break
        buffer = buffer + tempRead
        while True:
            headerEnd = buffer.find(b"B")
            if headerEnd == -1:
                break
            header = buffer[:headerEnd+1].decode("ascii")
            payloadSize = int(header[6:-1])
            if len(buffer) < payloadSize + headerEnd + 1:
                break
            payload = buffer[headerEnd + 1 : payloadSize + headerEnd + 1]
            sys.stdout.buffer.write(payload)
            sys.stdout.buffer.flush()
            buffer = buffer[payloadSize + headerEnd + 1:]

if __name__ == "__main__":
    main()

