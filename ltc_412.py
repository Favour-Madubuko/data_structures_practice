#FizzBuzz
def fizzBuzz(self, n: int):
    answer = []
    for integer in range(1,n+1):
        if integer % 3 == 0 and integer % 5 == 0:
            answer.append("FizzBuzz")
        elif integer % 3 == 0:
            answer.append("Fizz")
        elif integer % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(str(integer))
    return answer
'''
#JAVA EQUIVALENT
public List<String> fizzBuzz(int n) {
    List<String> answer = new ArrayList<>();
    //answer = []
    for (int i = 1; i<=n; i++){
        if(i % 3 == 0 && i % 5 == 0){
            answer.add("FizzBuzz");
        }else if( i % 3 == 0){
            answer.add("Fizz");
        }else if( i % 5 == 0){
            answer.add("Buzz");
        }else{
            answer.add(Integer.toString(i));
        }
    }
    return answer;
    }
'''