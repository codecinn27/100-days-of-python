import random

arr= [
  [
    "[-----]",
    "[     ]",
    "[  0  ]",
    "[     ]",
    "[-----]"
  ],
  [
    "[-----]",
    "[0    ]",
    "[     ]",
    "[    0]",
    "[-----]"
  ],
  [
    "[-----]",
    "[0    ]",
    "[  0  ]",
    "[    0]",
    "[-----]"
  ],
  [
    "[-----]",
    "[0   0]",
    "[     ]",
    "[0   0]",
    "[-----]"
  ],
  [
    "[-----]",
    "[0   0]",
    "[  0  ]",
    "[0   0]",
    "[-----]"
  ],
  [
    "[-----]",
    "[0   0]",
    "[0   0]",
    "[0   0]",
    "[-----]"
  ]
  
  
]
def dice(arr):
  while True:
    random_number = random.randint(0,5)
    for line in arr[random_number]:
      print(line)
    
    choice = input("Press any key to roll again and n to exit: ").lower()
    print()
    if choice == "n":
      print("Thanks for playing")
      break
      
    
dice(arr)