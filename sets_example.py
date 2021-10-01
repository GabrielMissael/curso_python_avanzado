def main():
    set1 = {1, 2, 3.5, True, "Juan", "María"}
    set2 = {0, 2, 3.1, False, "Juan", "Missael"}

    print(f"set1 = {set1}")
    print(f"set2 = {set2}")

    # union
    print(f"set1 + set2 = {set1 | set2}")

    # difference
    print(f"set2 - set1 = {set2 - set1}")
    print(f"set1 - set2 = {set1.difference(set2)}")

    # symmetric difference
    print(f"set1 ^ set2 = {set1 ^ set2}")

    # intersection
    print(f"set1 & set2 = {set1 & set2}")


if __name__=='__main__':
    main()