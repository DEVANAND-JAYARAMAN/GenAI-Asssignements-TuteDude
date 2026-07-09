prices = [100, 250, 400, 1200, 50]
gst = lambda x : x +(x *18/100)
prices_with_gst = list(map(gst, prices))
print("Original prices :", prices)
print("Prices after GST :", prices_with_gst)