class Solution:
	def reverse_string(self, s):
		s = s.strip()
		words = s.split(' ')
		l = []
		for word in words:
			l.append(word)
		return ' '.join(l[::-1])

def main():
	s = Solution()
	print s.reverse_string('Today is a great day')
main()
