var clientModal = $("#clientModal");
    $(function () {

        //JSON data by API call
        $.get(show_fullListApiUrl, function (response) {
            if(response) {
                var table = '';
                $.each(response, function(index, show_full) {
                    table += '<tr data-id="'+ show_full.client_id +'" data-name="'+ client_name.name +'" client_amount_30_days="'+ show_full.client_amount_30_days +'" job="'+ show_full.job +'"joined_date"'+ show_full.joined_date + '"end_date"' + show_full.end_date + '"due_date"' + show_full.due_date + '"staff_id"' + show_full.staff_id + '"staff_name"' + show_full.staff_name + '"staff_salary_28_days"' + show_full.staff_salary_28_days + '"staff_advance_amount"' + show_full.staff_advance_amount + '"staff_salary_left"' + show_full.staff_salary_left +'">' +
                        '<td>'+ show_full.client_name +'</td>'+
                        '<td>'+ show_full.client_amount_30_days +'</td>'+
                        '<td>'+ show_full.job +'</td>'+
                        '<td>'+ show_full.staff_id +'</td>'+
                        '<td>'+ show_full.staff_name +'</td>'+
                        '<td>'+ show_full.staff_salary_28_days +'</td>'+
                        '<td>'+ show_full.staff_advance_amount +'</td>'+
                        '<td>'+ show_full.staff_salary_left +'</td>'+
                        '<td>'+ show_full.end_date +'</td>'+
                        '<td>'+ show_full.joined_date +'</td>'+
                        '<td>'+ show_full.end_date +'</td>'+
                        '<td>'+ show_full.due_date +'</td>'+
                        

                        '<td><span class="btn btn-xs btn-danger delete-show_full">Delete</span></td></tr>';
                });
                $("table").find('tbody').empty().html(table);
            }
        });
    });

    const requestPayload = {};

    
    callApi("POST",clientSaveApiUrl, {
        'data': JSON.stringify(requestPayload)
    });



    // Save client
    $("#saveclient").on("click", function () {
        // If we found id value in form then update product detail
        var data = $("#clientForm").serializeArray();
        var requestPayload = {
            client_name: null,
            client_amount_30_days: null,
            job: null,
            joined_date: null,
            end_date: null,
            due_date: null

        };
        for (var i=0;i<data.length;++i) {
            var element = data[i];
            switch(element.name) {
                case 'client_name':
                    requestPayload.client_name = element.value;
                    break;
                case 'client_amount_30_days':
                    requestPayload.client_amount_30_days = element.value;
                    break;
                case 'job':
                    requestPayload.job = element.value;
                    break;
                 case 'joined_date':
                    requestPayload.joined_date = element.value;
                    break;
                case 'end_date':
                    requestPayload.end_date = element.value;
                    break;
                case 'due_date':
                    requestPayload.due_date = element.value;
                    break;
            }
        }
        callApi("POST",staffSaveApiUrl, {
            'data': JSON.stringify(requestPayload)
        });
    });



    // Save staff
    $("#savestaff").on("click", function () {
        // If we found id value in form then update product detail
        var data = $("#staffForm").serializeArray();
        var requestPayload = {
            staff_name: null,
            staff_amount_28_days: null,
            job: null,
            staff_advance_amount: null,
            staff_salary_left: null,
            joined_date: null,
            end_date: null,

        };
        for (var i=0;i<data.length;++i) {
            var element = data[i];
            switch(element.name) {
                case 'staff_name':
                    requestPayload.staff_name = element.value;
                    break;
                case 'staff_amount_28_days':
                    requestPayload.staff_amount_28_days = element.value;
                    break;
                case 'job':
                    requestPayload.job = element.value;
                    break;
                case 'staff_advance_amount':
                    requestPayload.staff_advance_amount = element.value;
                    break;
                case 'staff_salary_left':
                    requestPayload.staff_salary_left = element.value;
                    break;
                 case 'joined_date':
                    requestPayload.joined_date = element.value;
                    break;
                case 'end_date':
                    requestPayload.end_date = element.value;
                    break;
                
            }
        }
        callApi("POST", productSaveApiUrl, {
            'data': JSON.stringify(requestPayload)
        });
    });



    $(document).on("click", ".delete_client", function (){
        var tr = $(this).closest('tr');
        var data = {
            client_id : tr.data('id')
        };
        var isDelete = confirm("Are you sure to delete "+ tr.data('name') +" item?");
        if (isDelete) {
            callApi("POST", clientDeleteApiUrl, data);
        }
    });



    $(document).on("click", ".delete_staff", function (){
        var tr = $(this).closest('tr');
        var data = {
            staff_id : tr.data('id')
        };
        var isDelete = confirm("Are you sure to delete "+ tr.data('name') +" item?");
        if (isDelete) {
            callApi("POST", staffDeleteApiUrl, data);
        }
    });



    clientModal.on('hide.bs.modal', function(){

        $("#client_id").val('0');
        $("#client_name, #client_amount_30_days, #job, #joined_date, #end_date, #due_date").val('');
        clientModal.find('.modal-title').text('Add New client');
    });

    // staffModal.on('hide.bs.modal', function(){
    //     $("#staff_id").val('0');
    //     $("#staff_name, #job, #staff_salary_28_days, #staff_advance_amount, #staff_salary_left, #joined_date, #end_date").val('');
    //     staffModal.find('.modal-title').text('Add New staff');
    // });


    // productModal.on('show.bs.modal', function(){
    //     //JSON data by API call
    //     $.get(uomListApiUrl, function (response) {
    //         if(response) {
    //             var options = '<option value="">--Select--</option>';
    //             $.each(response, function(index, uom) {
    //                 options += '<option value="'+ uom.uom_id +'">'+ uom.uom_name +'</option>';
    //             });
    //             $("#uoms").empty().html(options);
    //         }
    //     });
    // });