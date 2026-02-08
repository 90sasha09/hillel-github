name1 = "днів"
seconds = int(input("Введіть число: "))

days = seconds // (24 * 60 * 60)
seconds = seconds % (24 * 60 * 60)
hours = seconds // 3600
seconds %= 3600

minutes = seconds // 60
seconds %= 60

print(f"{days} днів {str(hours).zfill(2)}:"
      f"{str(minutes).zfill(2)}:"
      f"{str(seconds).zfill(2)}")

