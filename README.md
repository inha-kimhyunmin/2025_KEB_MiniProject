마이데이터 테스트베드 api를 사용하려고 했는데 쓸려면 기업인증을 해야 쓸수있다고 하네요?
그래서 임의로 결제내역을 db에 저장하는 코드를 짜봤습니다

FastAPI를 이용해서 제작했고 
register에서 email과 password를 등록하고
login에서는 email과 password가 register에서 등록한거랑 일치하는지 확인합니다

그리고 payments 등록에서 결제일시, 결제금액, 상호명을 등록하고
read payments에서 userid를 입력하면 거기에 맞는 결제내역을 불러옵니다.

GPT 선생님의 도움을 받아서 만들었습니다, Mysql 사용한거로 만들었는데 db가 로컬에 있는 서버에 저장되게 해놨습니다.

![image](https://github.com/user-attachments/assets/7c09294d-b411-406f-a1e3-d5457bd30447)

users table은 id, email, password로 되어있고 password는 암호화해서 저장되어 있습니다
payments table은 id(순번), user_id, amount(금액), date(날짜), merchant_name(상호명) 으로 되어있습니다.
