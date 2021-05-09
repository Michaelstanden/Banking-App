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
        if (value <= 0){
            const warning = function warning(){
                document.createElement("p"["Please ensure you have funds above 0"]);
            };
            return warning ;
        } else {
            document.element.append("accTotal",value);
            };
        };
    set wdAmount(input){
        const withdrawal = document.getElementById("wdAmount", input);
    } 
    set depAmount(input){
        const depositedAmount = document.getElementById("depAmount", input);
    }   
    };

    class Withdraw extends Bank {
        constructor(accTotal, depAmount, wdAmount){
            super(accTotal, depAmount, wdAmount);
            this._withdrawal = withdrawl;
        }
        withdraw() {
            this.accTotal - this.withdrawal;
            return this.accTotal;
        }
    };

    class Deposit extends Bank {
        constructor(accTotal, depAmount, wdAmount){
            super(accTotal, depAmount, wdAmount);
            this._deposit = deposit;
        }
        get deposit(){
            return this._deposit;
        }
        deposited() {
            this.depositedAmount + this.accTotal;
            return this.accTotal;
        }
    };

    function mwdBtnClick() {
        document.getElementById("wdBtn").click(withdrawal);
      };
    
    
    function mwdBtnClick() {
        document.getElementById("depBtn").click(deposited);
      };