from PIL import Image,ImageDraw


im1=Image.open("/root/Downloads/lemur_ed66878c338e662d3473f0d98eedbd0d.png")
im2=Image.open("/root/Downloads/flag_7ae18c704272532658c10b5faad06d74.png")


im=Image.new('RGB',(582,327))
draw=ImageDraw.Draw(im)

for i in range(0,582):
	for j in range(0,327):
		num1=im1.getpixel((i,j))
		num2=im2.getpixel((i,j))
		r=num1[0]^num2[0]
		g=num1[1]^num2[1]
		b=num1[2]^num2[2]
		draw.point((i,j),fill=(r,g,b))

im.show()

