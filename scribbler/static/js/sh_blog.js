<script>
    function get_comments(blog_id){
      $.ajax({
      url: "/home/comments?id="+blog_id,
      }).done(function(response){
          $('#comments_'+blog_id).html(response.comments);
          $('#comment_'+blog_id).html(response.comment_count)
      });
    }

    function post_comment(blog_id){
        var content = $("#new_comment_"+blog_id).val();
        console.log(content);
        if(content){
          $.ajax({
        url: "/home/post_comments?id="+blog_id+'&content='+content,
        }).done(function(response){
          get_comments(blog_id);
        });
    }
    }

    function like(blog_id){
      $.ajax({
      url: "/like?id="+blog_id,
      }).done(function(response){
          $('#like_'+blog_id).html(response.like_count)
      });
    }
  </script>