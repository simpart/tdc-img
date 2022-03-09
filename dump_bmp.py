#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    try:
        bmp_fmt = {
        	### File Header ###
        	'file-type': None,       # 2 byte (2)
        	'file-size': None,       # 4 byte (6)
        	'reserved-1': None,      # 2 byte (8)
        	'reserved-2': None,      # 2 byte (10)
        	'offset': None,          # 4 byte (14)
        	
        	### Information Header ###
        	'info-size': None,       # 4 byte (18)   (4)
        	'width': None,           # 4 byte (22)   (8)
        	'height': None,          # 4 byte (26)   (12)
        	'planes': None,          # 2 byte (28)   (14)
        	'bit-count': None,       # 2 byte (30)   (16)
        	'compression': None,     # 4 byte (34)   (20)
        	'image-size': None,      # 4 byte (38)   (24)
        	'xpixper-meter': None,   # 4 byte (42)   (28)
        	'ypixper-meter': None,   # 4 byte (46)   (32)
        	'color-used': None,      # 4 byte (50)   (36)
        	'color-important': None, # 4 byte (54)   (40)
        	
        	### Palette Data ###
        	'blue': None,            # 1 byte (55)
        	'green': None,           # 1 byte (56)
        	'red': None,             # 1 byte (57)
        	'reserved-3': None       # 1 byte (56)
        	
        	# 4 byte
    	}
    
    	with open('./test_epd.bmp', 'rb') as bmp:
        	#print(type(bmp))
        	
        	# File Header
        	bmp_fmt['file-type']  = bmp.read(2).decode('utf-8')
        	bmp_fmt['file-size']  = str(int.from_bytes(bmp.read(4),byteorder='little')) + ' byte'
        	bmp_fmt['reserved-1'] = int.from_bytes(bmp.read(2),byteorder='little')
        	bmp_fmt['reserved-2'] = int.from_bytes(bmp.read(2),byteorder='little')
        	bmp_fmt['offset']     = str(int.from_bytes(bmp.read(4),byteorder='little')) + ' byte'
        	
        	# Information Header
        	bmp_fmt['info-size']       = str(int.from_bytes(bmp.read(4),byteorder='little')) + ' byte'
        	bmp_fmt['width']           = str(int.from_bytes(bmp.read(4),byteorder='little')) + ' px'
        	bmp_fmt['height']          = str(int.from_bytes(bmp.read(4),byteorder='little')) + ' px'
        	bmp_fmt['planes']          = int.from_bytes(bmp.read(2),byteorder='little')
        	bmp_fmt['bit-count']       = int.from_bytes(bmp.read(2),byteorder='little')
        	bmp_fmt['compression']     = int.from_bytes(bmp.read(4),byteorder='little')
        	bmp_fmt['image-size']      = str(int.from_bytes(bmp.read(4),byteorder='little')) + ' byte'
        	bmp_fmt['xpixper-meter']   = int.from_bytes(bmp.read(4),byteorder='little')
        	bmp_fmt['ypixper-meter']   = int.from_bytes(bmp.read(4),byteorder='little')
        	bmp_fmt['color-used']      = int.from_bytes(bmp.read(4),byteorder='little')
        	bmp_fmt['color-important'] = int.from_bytes(bmp.read(4),byteorder='little')
        	
        	# Palette Data
        	bmp_fmt['blue']       = int.from_bytes(bmp.read(1),byteorder='little')
        	bmp_fmt['green']      = int.from_bytes(bmp.read(1),byteorder='little')
        	bmp_fmt['red']        = int.from_bytes(bmp.read(1),byteorder='little')
        	bmp_fmt['reserved-3'] = int.from_bytes(bmp.read(1),byteorder='little')
        	
        	#print(bmp.read(4))  # pallete data
        	#print(bmp.read(2))  # pallete data
        	
    	#print(bmp_fmt)
    	
    	# dump format data
    	for bmp_key in bmp_fmt.keys():
    	    print(bmp_key + ":" + str(bmp_fmt[bmp_key]))
		
    except:
        import traceback
        traceback.print_exc()
