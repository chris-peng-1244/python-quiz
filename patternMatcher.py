from collections import defaultdict

def patternMatcher(pattern, string):
    # Write your code here.
	isPatternFlipped = False
	if pattern.startswith('y'):
		pattern = normalizePattern(pattern)
		isPatternFlipped = True
	firstYIndex = pattern.find('y')
	patternCount = getPatternCount(pattern)
	
	xPatternLength = 1
	while xPatternLengthCanExpand(string, xPatternLength, patternCount):
		yPattern = getYPattern(string, firstYIndex, xPatternLength, patternCount)
		if yPattern == None:
			xPatternLength += 1
			continue
		xPattern = string[:xPatternLength]
		if patternMatchesString(xPattern, yPattern, pattern, string):
			return [xPattern, yPattern] if not isPatternFlipped else [yPattern, xPattern]
		xPatternLength += 1
	return []

def normalizePattern(pattern):
	newPattern = ''
	for char in pattern:
		if char == 'x':
			newPattern += 'y'
		else:
			newPattern += 'x'
	return newPattern

def getPatternCount(pattern):
	count = defaultdict(int)
	for char in pattern:
		count[char] += 1
	return count

def xPatternLengthCanExpand(string, xPatternLength, patternCount):
	return (xPatternLength * patternCount['x'] + patternCount['y']) <= len(string)

def getYPattern(string, firstYIndexInPattern, xPatternLength, patternCount):
	if firstYIndexInPattern == -1:
		return ""
	yPatternTotalLength = len(string) - patternCount['x']*xPatternLength
	if yPatternTotalLength % patternCount['y'] != 0:
		return None
	yPatternLength = yPatternTotalLength // patternCount['y']
	startIndex = firstYIndexInPattern * xPatternLength
	endIndex = startIndex + yPatternLength
	return string[startIndex:endIndex]

def patternMatchesString(xPattern, yPattern, pattern, string):
	stringFromPattern = ''
	for char in pattern:
		if char == 'x':
			stringFromPattern += xPattern
		else:
			stringFromPattern += yPattern
	return stringFromPattern == string