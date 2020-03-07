import pyaudio

# import simpleaudio.functionchecks as fc

def main():
    texto = []
    arq = open('input.txt', 'r')
    texto = arq.read()  # Lê a mensagem do arquivo e armazena str na var 'texto'
    arq.close()
    print('-- mensagem:', texto, '   -- formato:', type(texto))
    string_utf = texto.encode('utf-16be')  # Conversão para bytes - utf-8

    print('-- mensagem:', string_utf, '-- formato:', type(string_utf))
    #fc.LeftRightCheck.run() #Check-in

    sample_stream = []
    high_note = (b'\xFF' * 100 + b'\0' * 100) * 50
    low_note = (b'\xFF' * 50 + b'\0' * 50) * 100
    for bit in string_utf[2:]:
        if bit == '1':
            sample_stream.extend(high_note)
        else:
            sample_stream.extend(low_note)

    sample_buffer = b''.join(sample_stream)

    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(16),
                    channels=1,
                    rate=44100,
                    output=True)
    stream.write(sample_buffer)


main()
