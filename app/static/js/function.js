$(function(){
    $.ajax({
        url: 'http://127.0.0.1:5000/api/token', // FlaskサーバーのURL
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            client_id: '492514a8-6ea5-443b-8bb7-90a48f7d90a6',
            client_secret: 'sxGXlLA3cZ9totYKosMn1OIdZ3Wb1LaLuINlMMBl_oY'
        }),
        success: function(response) {
            var accessToken = response.access_token;

            window.Genesys = new GenesysCloudClientApp({
                clientId: '492514a8-6ea5-443b-8bb7-90a48f7d90a6',
                redirectUri: 'http://127.0.0.1:5000',
                environment: 'mypurecloud.jp' // Set to your specific Genesys Cloud environment
              });
          
            // 認証トークンを取得した後にAPIリクエストを送信
            getUsers(accessToken);
            getCalls(accessToken);
        },
        error: function(xhr, status, error) {
            console.error('Error obtaining token:', error);
        }
    });
});

$('#call').click(function() {
    clickToDial()
})

// APIリクエストの送信
function getUsers(accessToken) {
    $.ajax({
        url: 'http://127.0.0.1:5000/api/users', // FlaskサーバーのURL
        type: 'GET',
        headers: {
            'Authorization': 'Bearer ' + accessToken
        },
        success: function(response) {
            console.log('User data:', response);
        },
        error: function(xhr, status, error) {
            console.error('Error fetching users:', xhr.responseText);
        }
    });
}

// APIリクエストの送信
function getCalls(accessToken) {
    $.ajax({
        url: 'https://api.mypurecloud.jp/api/v2/conversations/calls',
        method: 'GET',
        headers: {
          'Authorization': 'Bearer ' + accessToken
        },
        success: function(response) {
          const callHistory = response.entities;
          // Update CRM records with call history
          console.log('callHistory data:', callHistory);
        },                  
        error: function(error) {
          console.error('Error fetching call history', error);
        }
      });
}


function clickToDial() {
    console.log('process click to dial');
    document.getElementById("softphone").contentWindow.postMessage(JSON.stringify({
        type: 'clickToDial',
        data: { number: "09057435528", autoPlace: true }
    }), "*");
}

$(document).ready(function() {
    // 詳細表示ボタンがクリックされたとき
    $('#show-details-btn').on('click', function() {
        $('#details').addClass('show'); // 詳細をぬるっと表示
        $('#show-details-btn').hide();  // 詳細表示ボタンを非表示
        $('#hide-details-btn').show();  // 隠すボタンを表示
    });

    // 隠すボタンがクリックされたとき
    $('#hide-details-btn').on('click', function() {
        $('#details').removeClass('show');  // 詳細をぬるっと非表示
        $('#show-details-btn').show();  // 詳細表示ボタンを再表示
        $('#hide-details-btn').hide();  // 隠すボタンを非表示
    });
});
