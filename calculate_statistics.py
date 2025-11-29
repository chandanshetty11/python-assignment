def calculate_statistics(numbers):
    total = sum(numbers)
    mean = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    
    return {
        "sum": total,
        "mean": mean,
        "min": minimum,
        "max": maximum
    }

if __name__ == "__main__":
    print(calculate_statistics([10,20,30,40,50]))
