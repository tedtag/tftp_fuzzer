# TFTP Fuzzer Tool
A simple fuzzer tool to explore and exploit buffer overflow vulnerabilities for the TFTP protocol.
This tool is based off the specifications outlined in [RFC 1350](https://tools.ietf.org/html/rfc1350).

## Usage
```bash
python tftp_fuzzer.py
    -t 192.168.100.1 #[target]
    -p 69 #[port - default is 69]
    -i 1000 #[iterations - default is 1000]
    -f filename #[field - default is filename]
