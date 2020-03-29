# HooHacks Project Backend API

### Database Models
**User**  
&nbsp;&nbsp;ID: `Int`  
&nbsp;&nbsp;Email: `String`  
&nbsp;&nbsp;Phone: `String`  
&nbsp;&nbsp;FirstName: `String`  
&nbsp;&nbsp;LastName: `String`  
&nbsp;&nbsp;Password: `Encrypted String`  
&nbsp;&nbsp;MonthlyIncome: `Float`  
&nbsp;&nbsp;Created: `Date`  

**Category**  
&nbsp;&nbsp;ID: `Int`  
&nbsp;&nbsp;Name: `String`  
&nbsp;&nbsp;Amount: `Float`  
&nbsp;&nbsp;Created: `Date`  
&nbsp;&nbsp;SpendingType: `String` (`ACTUAL` or `EXPECTED`)  
&nbsp;&nbsp;UserID: `User.ID`  

**Transaction**  
&nbsp;&nbsp;ID: `Int`  
&nbsp;&nbsp;Name: `String`  
&nbsp;&nbsp;Amount: `Float`  
&nbsp;&nbsp;Created: `Date`  
&nbsp;&nbsp;UserID: `User.ID`  
&nbsp;&nbsp;CategoryID: `Category.ID`  

<hr>

### Default Error/Success Responses  
```json
{
    "error": true,
    "message": "Reason for error."
}
```
```json
{
    "error": false,
    "message": "Reason for success."
}
```  

<hr>

### API Endpoints
***Base URL: https://hoohacksproject.appspot.com***  

`POST` [/api/login]()  

Expected Data
```json
{
    "email": "useremail@swizard.tech",
    "password": "plaintextpassword"
}
```  

Response
```json
{
    "error": false,
    "created": "Sat, 28 Mar 2020 20:47:13 GMT",
    "email": "useremail@swizard.tech",
    "fname": "First",
    "user_id": 1,
    "lname": "Last",
    "monthly_income": 10000.0,
    "phone": "1234567890"
}
```  
<br>

`POST` [/api/register]()  
Expected Data
```json
{
    "fname": "First",
    "lname": "Last",
    "email": "user@swizard.tech",
    "password": "mypassword",
    "monthly_income": 10000.00,
    "phone": "1234567890"
}
```  

Response  
```json
{
    "error": false,
    "message": "User successfully created"
}
```  
<br>

`POST` [/api/]()  
Expected Data
```json
{

}
```  

Response  
```json
{

}
```  
<br>

