
$(function() {
    $(".edit-button").click(function() {
            // TODO: ajax call to submit an edit
            var $item = $(this).parents('.item')
            var quote_id = $item.attr('quote_id');

            var $quote_container = $(".quote-container", $item);
            var $quote_id_container = $(".quote_id", $item);
            var $author_container = $(".author-container", $item);
            var $save_container = $(".save-container", $item);
            var $cancel_container = $(".cancel-container", $item);

            var quote_container_height = parseInt($quote_container.css('height'),10) + 30;
            var quote_text = $quote_container.text().trim();
            var author = $author_container.text().trim();
            author = author.slice(2,author.length); // to account for the "- "

            var $qt = $(".quote_template").clone(); // qt = quote template
            var $qt_id = $qt.find('.quote_id');
            var $qt_quote = $qt.find('.quote_quote');
            var $qt_author = $qt.find('.quote_author');
            var $qt_comment = $qt.find('.quote_comment');
            var $save_button = $qt.find('.edit-save-button');
            var $cancel_button = $qt.find('.edit-cancel-button');


            $qt_quote.val(quote_text.slice(1,quote_text.length-1));
            console.log(quote_container_height);
            $qt_quote.css('height',quote_container_height);

            $qt_id.val(quote_id);

            $qt_author.val(author);
            $qt_author.css('float','right');
            $qt_author.css('text-align','right');

            $quote_container.html($qt_quote);
            $quote_container.append($qt_id);
            $author_container.html($qt_author);
            $save_container.html($save_button);
            $cancel_container.html($cancel_button);

            $author_container.append('<div class="clear"></div>');

            $(".edit-save-button").click(function(e) {
                // e.preventDefault();
                // TODO: code here for sending an AJAX request to edit info.
            });

            // Remove the edit button until the edit is canceled/submitted
            $(this).css('opacity','0');
        });

        $(".edit-save-button").click(function() {
            $(this).parents(".edit-button").css('opacity','0');
        })
        $(".edit-cancel-button").click(function() {
            $(this).parents(".edit-button").css('opacity','0');
        })

        $(".delete-button").click(function() {
            var $item = $(this).parents('.item')
            var quote_id = $item.attr('quote_id');
            console.log(quote_id);
            $.ajax({
                type: 'POST',
                url: '{% url delete_quote %}',
                data: {
                    'quote_id': quote_id,
                },
                success: function(data) {
                    console.log(data);
                    $item.hide();
                },
                error: function(xhr, text_status, error_thrown) {
                    console.log(xhr.responseText.slice(0,500));
                    alert(xhr.responseText.slice(0,1900));
                    console.log(text_status);
                    console.log(error_thrown);
                },
            });
        });
})