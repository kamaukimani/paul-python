// class Human {
//   constructor() {
//     console.log("The consturctor was called");
//   }
//   anotherone() {
//     console.log("Another one");
//   }
// }

// let date=n
// let alpha = new Human();
// alpha.anotherone();
// // function name()

class Human {
  constructor(gender, name) {
    this.gender = gender;
    this.name = name;

    if (gender === "Male") {
      this.ribs = 24;
      this.curse = "Suffer";
    } else {
      this.ribs = 23;
      this.curse = "Pain";
    }
  }

  print_self() {
    console.log("----------------------");
    console.log("name", this.name);
    console.log("gender", this.gender);
    console.log("ribs", this.ribs);
    console.log("curse", this.curse);
    console.log("---------------------");
  }
}

let adam = new Human("Male", "Adam");
adam.print_self();

let eve = new Human("Female", "Eve");
eve.print_self();

