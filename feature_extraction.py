from skimage import measure
import scipy.stats as ss

def features_set1(image_segmented,original_image):
	regions = measure.regionprops(image_segmented, intensity_image = original_image)
	print([r.label for r in regions])
	print([r.mean_intensity for r in regions])

def flattenArray(twodimage):
    arra = flattened_list = [y for x in twodimage for y in x]
    return arra

def statistics_features(image_data):
	image_data = flattenArray(image_data)
	skewness = ss.skew(image_data)
	print(skewness)
	Kurtosis = ss.kurtosis(image_data)
	print(Kurtosis)
	Entropy = ss.entropy(image_data)
	print(Entropy)




