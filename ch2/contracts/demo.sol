// SPDX-License-Identifier: MIT

pragma solidity ^0.8.6;

contract Demo{
    uint public a;

    function setA(uint _a) public {
        a = _a;
    }

    function getA() public view returns(uint){
        return a;
    }

}