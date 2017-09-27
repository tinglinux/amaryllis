KindEditor.ready(function(K) {
    window.editor = K.create('textarea[name="content"]',
        {
            'width':'800px',
            'height':'500px',
            'uploadJson':'/admin/upload/kindeditor',
            extraFileUploadParams:{
                "csrfmiddlewaretoken":"{{ csrf_token }}"
        }
        });
});