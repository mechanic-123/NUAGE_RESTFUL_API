# NUAGE_RESTFUL_API

  HTTP METHOD         URL                 PAYLOAD FORMAT                                       RESPONSE WITHOUT PAYLOAD               RESPONSE WITH PAYLOAD                                         
.  GET                 /users/             {"users":["name of user"]}                           List of all User objects           List of Userobjects for<users>
                                                                                                                                   (sorted byname)

.  POST               /add/                {"user":<name of newuser (unique)>}                  N/A                                <user> acount is created.
  
.  POST               /iou/                 {"lender":<name oflender>,                          N/A                                updated Userobjects for<lender> and<borrower> 
                                            "borrower":<name ofborrower>,"amount": x}



for running the Unit Testcases use commands ->Python manage.py test
