import zlib

s = b'witch which has which witches wrist watch'
print(len(s))

t = zlib.compress(s)	# data compress
print(t, len(t))

d = zlib.decompress(t)
print(d)

print(zlib.crc32(s))