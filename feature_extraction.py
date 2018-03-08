def features(image_segmented , original_image):
  	regions = measure.regionprops(i, intensity_image=image)
    print([r.label for r in regions])
    print([r.mean_intensity for r in regions])