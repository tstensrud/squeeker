slint::include_modules!();

fn main() -> Result<(), slint::PlatformError> {
    let ui = AppWindow::new()?;

    ui.on_request_increase_value({
        let ui_handle = ui.as_weak();
        move || {
            let ui = ui_handle.unwrap();
            ui.set_counter(ui.get_counter() + 1);
        }
    });

    ui.run()
}


    
/* let mut user = users::User{id:1, name:"Torbjørn", email:"torbjorn.stensrud@gmail.com", age:39, squeeks: vec![]};
let mut mysqueek = squeek::Squeek{id:1, owner:user, content:"This is my first squeek", comments: vec![]};

println!("id: {}", mysqueek.get_id());
println!("owner: {}, @ {}", mysqueek.get_owner().get_name(), mysqueek.get_owner().get_email());
println!("content: {}", mysqueek.get_content());


mysqueek.new_comment(0001, "This is the comment :-)".to_string());
mysqueek.new_comment(0002, "This is a different comment :-)".to_string());
mysqueek.get_comments();
 */