def computeLps(inputString):
    lps = [-1 for _ in range(len(inputString) + 1)]
    lps[0] = -1
    i = 0
    j = -1
    while i < len(inputString):
        while j >= 0 and inputString[i] != inputString[j]:
            j = lps[j]
        lps[i + 1] = j + 1
        j += 1
        i += 1
    lps[0] = 0
    return lps


def kmpAlgorithm(text, pattern):
    if len(pattern) > len(text):
        return []
    ans = []
    currMatchCount = 0
    currIndex = 0
    lps = computeLps(pattern)
    while currIndex < len(text) - len(pattern) + 1:
        if currIndex + currMatchCount >= len(text):
            currMatchCount = 0
            continue
        if text[currIndex + currMatchCount] == pattern[currMatchCount]:
            currMatchCount += 1
            if currMatchCount == len(pattern):
                ans.append(currIndex)
                currIndex += currMatchCount - lps[currMatchCount]
                currMatchCount = lps[currMatchCount]
                continue
            else:
                continue
        else:
            if currMatchCount - lps[currMatchCount] <= 0:
                currIndex = currIndex + 1
            else:
                currIndex += currMatchCount - lps[currMatchCount]
            currMatchCount = lps[currMatchCount]
    return ans


if __name__ == "__main__":
    print(computeLps("ccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacf"))
    print(kmpAlgorithm("eccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacfbccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacfijbccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacfdccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacfgccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacfjccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacfgcccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacfjcccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacfaccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacfgccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacfdccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacfdccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacfijccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacfjccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacfeaccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacfgcjccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacffjccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacfaccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacffccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacfbdbccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacfidccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacfcbccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacfdhccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacffccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacfbccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacfdjijccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacfdccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacfeccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacffccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacfcba", "ccjhdhcabhbceeaeggahbafcgbacifichfidcfbjfaijabacf"))
