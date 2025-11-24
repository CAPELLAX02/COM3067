# 1. You are given two sorted sequences which consist of distinct elements. Design an
# algorithm that finds the k-th smallest element in the union of both sequences. The running
# time of your algorithm should be O(log n + log m) in the worst case where n and m are the
# sizes of the sequences. To get full credit, you need to provide the efficiency analysis.

def kth_smallest(A, B, k):
    n = len(A)
    m = len(B)

    # Her zaman daha kısa dizide çalışıcak BS
    if n > m:
        return kth_smallest(B, A, k)

    # olası "i" aralıkları
    left = max(0, k - m)
    right = min(k, n)

    # BS
    while left <= right:
        i = (left + right) // 2   # A'dan alınan eleman sayısı
        j = k - i                 # B'den alınan eleman sayısı

        # Sınırlar: (taşmaması için +-sonsuzlar var)
        # Sol tarafın en büyük elemanı, sağ tarafın en küçük elemanından büyük olmamalı

        # A_left hesapla
        if i > 0:
            A_left = A[i - 1]
        else:
            A_left = float('-inf')

        # A_right hesapla
        if i < n:
            A_right = A[i]
        else:
            A_right = float('inf')

        # B_left hesapla
        if j > 0:
            B_left = B[j - 1]
        else:
            B_left = float('-inf')

        # B_right hesapla
        if j < m:
            B_right = B[j]
        else:
            B_right = float('inf')

        # Doğru partition mu?
        if A_left <= B_right and B_left <= A_right:
            # k'ıncı eleman = sol tarafın en büyüğü
            return max(A_left, B_left)

        # Çok fazla A'dan aldık → i'yi azalt
        elif A_left > B_right:
            right = i - 1

        # A'dan az aldık → i'yi artır
        else:
            left = i + 1

    # Normalde buraya gelmemeli
    return None
