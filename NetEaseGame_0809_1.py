import sys

# 算个税

class TaxCalculator:
    def __init__(self):
        self.degree_array = [0, 3000, 12000, 25000, 35000, 55000, 80000]
        self.tax_rate_array = [0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45]

    def calculate_tax(self, salary):
        if salary <= 5000:
            return 0
        else:
            tax_value = 0
            tax_part = salary - 5000
            for index in range(len(self.degree_array)):
                if tax_part <= self.degree_array[index]:
                    tax_value += (tax_part-self.degree_array[index-1]) * self.tax_rate_array[index-1]
                    for i in range(1, index):
                        tax_value += (self.degree_array[i]-self.degree_array[i-1])*self.tax_rate_array[i-1]
                    return tax_value
                else:
                    if index == len(self.degree_array)-1:
                        tax_value += (tax_part-self.degree_array[-1])*self.tax_rate_array[-1]
                        for i in range(1, index+1):
                            tax_value += (self.degree_array[i] - self.degree_array[i-1]) * self.tax_rate_array[i-1]
                        return tax_value

    def down_4_up_5(self, num):
        if (num - 0.5) >= int(num):
            return num + 1
        else:
            return num

if __name__ == "__main__":
    # 读取第一行的n
    tax_calc = TaxCalculator()
    res = []
    n = int(sys.stdin.readline().strip())

    for i in range(n):
        line = sys.stdin.readline()
        salary = int(line)
        tax = int(tax_calc.down_4_up_5(tax_calc.calculate_tax(salary)))
        res.append(tax)
    for tax in res:
        print(tax)