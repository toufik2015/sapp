



<div class="row">

	<div class="col-md-4"></div>

	<div class="col-md-12">

		<div class="card card-body">

			
			
			<!-- Data Table -->
			<table class="table table-dark">
			  <thead>
			    <tr>
			      <th scope="col">Full Name</th>
			      <th scope="col">Phone Number</th>

			    </tr>
			  </thead>
			  <tbody id="tests-table">

			  </tbody>
			</table>

		</div>

	</div>

	<div class="col-md-4"></div>
</div>


<script>

	$('#add-test').on('click', function(){
	})


	
	$('#create-test').on('click', function(){

	})

	var tests = [
		{'name':'Distillation 50%', 'id':'1', 'result':"43"},
	    {'name':'Flah Point', 'id':'2', 'result':"61"},
	    {'name':'Water By Karl Fischer', 'id':'3', 'result':"24"},
	]


	for (var i in tests){
		addRow(tests[i])
	}

	function addRow(obj){
		var row = `<tr scope="row" class="test-row-${obj.id}">
	    			   <td>${obj.name}</td>
	                   <td>${obj.result}</td>
	                   <td>
	                   		<button class="btn btn-sm btn-danger" data-testid="${obj.id}" id="delete-${obj.id}">Absent</button>
	                   		<button class="btn btn-sm btn-info"  data-testid="${obj.id}" id="save-${obj.id}">Present</button> 
	                   </td>
	    		   </tr>`
		$('#tests-table').append(row)

		$(`#save-${obj.id}`).on('click',saveUpdate)
		$(`#delete-${obj.id}`).on('click',deleteTest)

	}

	

	function saveUpdate(){

		var testid = $(this).data('testid')

		var saveBtn = $(`#save-${testid}`)
		var deleteBtn = $(`#delete-${testid}`)

		saveBtn.addClass('disabled')
		deleteBtn.addClass('hidden')
	}



	function deleteTest(){

		var testid = $(this).data('testid')

		var saveBtn = $(`#save-${testid}`)
		var deleteBtn = $(`#delete-${testid}`)

		saveBtn.addClass('hidden')
		deleteBtn.addClass('disabled')

	}