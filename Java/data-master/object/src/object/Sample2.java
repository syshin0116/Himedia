package object;

import java.util.Date;

class Animal{
	String name;
	
	void setName(String name) {
		this.name = name;
	}
}

class Dog extends Animal{
	void sleep() {
		System.out.println(this.name+"는 잔다.");
	}
}
class HouseDog extends Dog{
	
	//생성자 오버로딩
	HouseDog(){
		
	}
	
	HouseDog(String nmae){
		this.setName(name);
	}
	
	//메소드 오버라이딩(Method overriding)
	//부모 함수를 재정의해서 기능을 추가
	void sleep() {
		System.out.println(this.name+"는 집에서 잔다.");
	}
	//메소드 오버로딩(Method overloading)
	//같은 이름의 다른 파라미터나 리턴값의 기능을 추가하는 경우
	void sleep(int hour) {
		System.out.println(this.name+"는 "+hour+"시에 집에서 잔다.");
	}
}

public class Sample2 {
	
	Date date = new Date();
	//자바는 다중 상속 되지 않는다.
	public static void main(String[] args) {
		Dog dog = new Dog();
		dog.setName("멍멍이");
		System.out.println(dog.name);
		dog.sleep();
		// IS - A관계
		// 개는 동물이다.
		Animal dog2 = new Dog();
		
		//Object java 최상위 객체(class)
		Object obj = new Dog();
		
		HouseDog houseDog = new HouseDog("돌돌이");
		houseDog.setName("집돌이");
		houseDog.sleep();
		houseDog.sleep(5);
	}

}
