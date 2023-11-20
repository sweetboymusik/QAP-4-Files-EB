// Program to inject customer info into HTML
// Using a customer object and template literals
// Date written: November 19, 2023
// Authro: Elliott Butt

// define customer object
const customer = {
  firstName: "John",
  lastName: "Doe",
  birthDate: new Date(1991, 0, 1),
  gender: "male",
  phoneNum: "123-456-7890",
  payMethod: "Visa",

  cardNum: "4567543245679876",
  licenceNum: "B1029839827CD",
  SIN: "123 456 789",
  addGuests: 3,

  addGuestInfo: [
    {
      guestFirstName: "Jane",
      relation: "spouse",
      minor: "no",
    },
    {
      guestFirstName: "Jack",
      relation: "son",
      minor: "yes",
    },
    {
      guestFirstName: "Jessica",
      relation: "sister",
      minor: "yes",
    },
  ],

  roomPrefs: [
    "two queen-sized beds",
    "window view",
    "pool access",
    "working A/C",
    "pullout couch",
  ],

  mailAddress: {
    street: "1 New Lane",
    city: "New Town",
    province: "Alberta",
    postal: "A1B 1C1",
    country: "Canada",
  },

  checkDates: {
    checkIn: new Date(2023, 9, 10),
    checkOut: new Date(2023, 9, 12),
  },

  getAge: function () {
    const today = new Date();
    return today.getFullYear() - this.birthDate.getFullYear();
  },

  getStayDuration: function () {
    duration_ms = this.checkDates.checkOut - this.checkDates.checkIn;
    return duration_ms / 86400000;
  },

  getPronoun: function () {
    let pronoun = "";
    if (customer.gender == "male") {
      pronoun = "He";
    } else if (customer.gender == "female") {
      pronoun = "She";
    } else if (customer.gender == "non-binary" || customer.gender == "other") {
      pronoun = "They";
    }

    return pronoun;
  },

  checkDiscount: function () {
    minorCounter = 0;
    discount = false;

    if (this.addGuests > 0) {
      this.addGuestInfo.forEach((element) => {
        if (element.minor == "yes") {
          minorCounter += 1;
        }
      });
    }

    minorCounter >= (this.addGuests + 1) / 2
      ? (discount = true)
      : (discount = false);

    return discount;
  },
};

// determine variables (only really necessary if you have different customer objects with different values)
let prefs_html = "";
customer.roomPrefs.forEach((element) => {
  prefs_html += `<li>${element}</li>`;
});

let guests_html = "";
customer.addGuestInfo.forEach((element, index) => {
  index < customer.addGuestInfo.length - 1
    ? (guests_html += `${element.guestFirstName} (${element.relation}), `)
    : (guests_html += `and ${element.guestFirstName} (${element.relation}).`);
});

let discount_html = "";
customer.checkDiscount()
  ? (discount_html = `eligible for a discount (50% or more of guests are minors)`)
  : (discount_html = `not eligible for a discount (less than 50% of guests are minors).`);

let cardNumDsp = "XXXX XXXX XXXX " + customer.cardNum.slice(12);

// create html to inject
html_insert = `
    <h1>Motel Customer Info</h1>

    <p>${customer.firstName} ${customer.lastName} is a 
       ${customer.getAge()} year old ${customer.gender.toLowerCase()},
       born on <i>${customer.birthDate.toLocaleDateString("en-us", {
         year: "numeric",
         month: "long",
         day: "numeric",
       })}</i>. 
       The customer provided two pieces of goverment ID: 
       SIN ending in ${customer.SIN.slice(8)} 
       and licence number starting with ${customer.licenceNum.slice(0, 5)}.
    </p>

    <p>${customer.firstName} will be checking in on 
       <i>${customer.checkDates.checkIn.toLocaleDateString("en-us", {
         year: "numeric",
         month: "long",
         day: "numeric",
       })}</i>
       and will be checking out on
       <i>${customer.checkDates.checkOut.toLocaleDateString("en-us", {
         year: "numeric",
         month: "long",
         day: "numeric",
       })}</i>.
       ${customer.getPronoun()} will be joined by ${customer.addGuests} 
       additional guests: ${guests_html}
       They will be staying a total of <b>${customer.getStayDuration()}</b> days.
       ${customer.getPronoun()} has already paid for thier booking 
       using ${customer.payMethod},
       with card number ${cardNumDsp}.
       ${customer.firstName} is ${discount_html}.
    </p>

    <h3><u>Room Preferences:</u></h3>
    <ol>${prefs_html}</ol>

    <h3><u>Contact Info</u></h3>
    <p>
       <b>Phone Number</b>: ${customer.phoneNum} <br>
       <br>
       <b>Mailing address</b>: <br>
          ${customer.firstName} ${customer.lastName} <br>
          ${customer.mailAddress.street} <br>
          ${customer.mailAddress.city} <br>
          ${customer.mailAddress.province} ${customer.mailAddress.postal} <br>
          ${customer.mailAddress.country} <br>
    </p>
`;

// inject html into DOM
document.body.innerHTML = html_insert;