package object2;

interface MainAnimal{
	String getFood();
}
interface Sound{
	void sound();
}
class Animal{
	String name;
	
	void setname(String name) {
		this.name=name;
	}
}

class Tiger extends Animal implements MainAnimal, Sound{

	@Override
	public String getFood() {
		// TODO Auto-generated method stub
		return "닭고기";
	}
	public void sound() {
		System.out.println("어흥");
	}
}

class Lion extends Animal implements MainAnimal, Sound{

	@Override
	public String getFood() {
		// TODO Auto-generated method stub
		return "돼지고기";
	}
	public void sound() {
		System.out.println("크헝");
	}
}
class Giraffe extends Animal implements MainAnimal, Sound{

	@Override
	public String getFood() {
		// TODO Auto-generated method stub
		return "사과";
	}
	public void sound() {
		System.out.println("히히힝");
	}
}

class Zookeeper{
//	void feed(Tiger tiger) {
//		System.out.println("닭고기를 먹이로 줍니다.");
//	}
//	void feed(Lion lion) {
//		System.out.println("돼지고기를 먹이로 줍니다.");
//	}
//	void feed(Giraffe giraffe) {
//		System.out.println("사과를 먹이로 줍니다.");
//	}
	
	void feed(MainAnimal mainAnimal) {
		System.out.println(mainAnimal.getFood() + "를 먹이로 줍니다.");
	}
	
}
class Bouncer{
	void soundAnimal(Sound animal) {
		animal.sound();
	}
}
public class Sample {

	public static void main(String[] args) {
		Zookeeper zookeeper = new Zookeeper();
		Tiger tiger = new Tiger();
		Lion  lion  = new Lion();
		Giraffe giraffe = new Giraffe();
		
		zookeeper.feed(lion);
		zookeeper.feed(tiger);
		zookeeper.feed(giraffe);
		
		Bouncer bouncer = new Bouncer();
		bouncer.soundAnimal(tiger);
		bouncer.soundAnimal(lion);
		bouncer.soundAnimal(giraffe);
	}

}

