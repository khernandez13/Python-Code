text = "X-DSPAM-Confidence:    0.8475"
fpos = text.find('0')
begin = int(fpos)
epos = text.find('5')
end = int(epos)
answer=float(text[begin:end+1])
print(answer)
