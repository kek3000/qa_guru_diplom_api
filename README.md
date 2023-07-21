## Autotests API Project
### Technologies used
<p  align="center">
<code><img width="5%" title="Python" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/1024px-Python.svg.png"></code>
<code><img width="5%" title="Pycharm" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/PyCharm_Icon.svg/1200px-PyCharm_Icon.svg.png"></code>
<code><img width="5%" title="Pytest" src="https://upload.wikimedia.org/wikipedia/commons/b/ba/Pytest_logo.svg"></code>
<code><img width="5%" title="Selene" src="https://fs.getcourse.ru/fileservice/file/download/a/159627/sc/264/h/e0cabcb69a2df1e6b1086292c020a4a7.png"></code>
<code><img width="5%" title="Requests" src="https://upload.wikimedia.org/wikipedia/commons/a/aa/Requests_Python_Logo.png"></code>
<code><img width="5%" title="Allure Report" src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4"></code>
<code><img width="5%" title="Allure TestOps" src="https://marketplace-cdn.atlassian.com/files/92e2d8c3-2a30-46c0-bf21-2453a4a270d3?fileType=image&mode=full-fit"></code>
<code><img width="5%" title="Jira" src="https://www.svgrepo.com/show/353935/jira.svg"></code>
<code><img width="5%" title="Selenoid" src="https://diginomica.com/sites/default/files/images/2017-09/docker-container.jpg"></code>
<code><img width="5%" title="Jenkins" src="https://avatars.githubusercontent.com/u/2520748?v=4"></code>
<code><img width="5%" title="GitHub" src="https://cdn-icons-png.flaticon.com/512/25/25231.png"></code>
</p>
<br> 

### The project consists of two groups of tests:
<details><summary><b>reqres.in - only api api</b></summary>
<ul>
  <li>Create user</li>
  <li>Update user by put</li>
  <li>Update user by patch</li>
  <li>Delete user</li>
  <li>Successful registration</li>
  <li>Unsuccessful registration</li>
</ul>

</details>
<details><summary><b>demowebshop - ui\api tests</b></summary>
<br> 
<ul>
  <li>Successful auth</li>
  <li>Removing a product from the wishlist</li>
  <li>Removing an item from the cart</li>
  <li>Logout</li>
</ul>
</details>
<br>

### <img width="3%" title="Jenkins" src="https://avatars.githubusercontent.com/u/2520748?v=4"> [Running a project in Jenkins](https://jenkins.autotests.cloud/job/qa_guru_diplom_api_Nikita/)
##### Clicking on "Build Now" will start building the tests and running them on the Jenkins server.

![Jenkins_run](images/jenkins%20api.png)


### <img width="3%" title="Allure Report" src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4"> [Allure report](https://jenkins.autotests.cloud/job/qa_guru_diplom_api_Nikita/2/allure/)
##### After passing the tests, the results can be viewed in the Allure report.

![Overview](images/allure%20report.png)


##### ВOn the Behaviors tab, there are collected test cases, which describe the steps. Attachments are implemented for api methods. For combined tests, at the end of the test, a screenshot is taken and a video recording of the test is saved.

![Behaviors](images/allure%20api.png)


##### Video of the test Removing goods from the cart, adding is done by api, deleting through ui.

https://selenoid.autotests.cloud/video/88edc5171ccaae2a7e01d5cb4605f4f8.mp4


### <img width="3%" title="Allure TestOps" src="https://marketplace-cdn.atlassian.com/files/92e2d8c3-2a30-46c0-bf21-2453a4a270d3?fileType=image&mode=full-fit">  [Integration with Allure TestOps](https://allure.autotests.cloud/project/3532/dashboards)

##### Also, all reporting is saved in Allure TestOps, where similar graphs are built.

![Graf](images/testops.png)

#### In the suites tab, we can:
- Manage all test cases or each separately
- Rerun each test separately from all tests
- Set up integration with Jira
- Add manual tests, etc.

![tests](images/Testops_cases_api.png)

### <img width="3%" title="Jira" src="https://www.svgrepo.com/show/353935/jira.svg"> [Jira integration](https://jira.autotests.cloud/browse/HOMEWORK-798)
##### By setting up integration with Jira through Allure TestOps, you can forward the result of passing tests and a list of test cases from Allure to a ticket

![Jira](images/jira%20api.png)

