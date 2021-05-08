document.ready();
const wdBtn = document.getElementById("wdBtn");
const depBtn = document.getElementById("depBtn");
const wdAmount = document.getElementById("wdAmount");
const accTotal = document.getElementById("accTotal");
const depAmount = document.getElementById("depAmount");

class Bank {
    constructor(accTotal, depAmount, wdAmount){
        this._accTotal = accTotal;
        this._depAmount = depAmount;
        this._wdAmount = wdAmount;
    }
    get accTotal(){
        return this._accTotal;
    }
    get depAmount() {
        return this._depAmount;
    }
    get wdAmount(){
        return this._wdAmount;
    }
    set accTotal(value){
        if (accTotal <= 0){
            const warning = function warning(){
                document.createElement("p"["Please ensure you have funds above 0"]);
            };
            return warning ;
        } else {
            document.element.append("accTotal",value);
            };
        };
    };

    class Withdraw extends Bank {
        constructor(accTotal, depAmount, wdAmount){
            super(accTotal, depAmount, wdAmount);
            this._withdrawl = withdrawal;
        }
        get withdrawal() {
            return this._withdrawl;
        }
    }