# 2. In a sequence of n integers 𝑎1, 𝑎2, … , 𝑎𝑛 , an inversion is a pair (𝑎𝑖, 𝑎𝑗) with i < j but 𝑎𝑖 > 𝑎𝑗.
# Give an algorithm for computing the number of inversions in a sequence of n integers,
# that runs in time O(n log n). To get full credit, you need to provide the efficiency analysis.

# Merge Sort + Inversion Sayacı (n logn === merge sort [divide-and-conquer]):

def count_inversions(arr):
    # Merge ile hem sıralama hem inversion sayma
    def merge_count(left, right):
        i = j = 0
        inv = 0
        merged = []

        while i < len(left) and j < len(right):
            # Sıralı merge
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                # left[i] > right[j] ise
                # left'in geri kalan tüm elemanları right[j]'den büyük
                inv += len(left) - i

        # Kalanları ekle
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv

    # Divide-and-conquer kısmı
    def sort_count(a):
        if len(a) <= 1:
            return a, 0  # tek eleman → sıralı ve 0 inversion

        mid = len(a) // 2
        left, inv_left = sort_count(a[:mid])
        right, inv_right = sort_count(a[mid:])

        merged, inv_split = merge_count(left, right)

        total_inv = inv_left + inv_right + inv_split
        return merged, total_inv

    _, total = sort_count(arr)
    return total
