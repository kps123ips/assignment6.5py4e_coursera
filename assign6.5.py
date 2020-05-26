str='X-DSPM-Confidence: 0.847'
st= str.find(':')
print(st)
out=str[st+1:]
print(out)
val=float(out)
print(val)
