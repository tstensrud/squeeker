use crate::users;

pub struct Squeek<'a> {
    pub id: u32,
    pub owner: users::User<'a>,
    pub content: &'a str,
    pub comments: Vec<Comment>,
}

impl Squeek<'_> {
    pub fn get_id(&self) -> u32 {
        return self.id;
    }
    
    pub fn get_owner(&self) -> &users::User {
        return &self.owner;
    }

    pub fn get_content(&self) -> &str {
        return self.content;
    }

    pub fn get_comments(&self) {
        println!("Comments");
        for comment in &self.comments {
            println!("{}", comment.get_comment());
        }
    }

    pub fn new_comment(&mut self, id: u32, text: String) {
        let new_comment = Comment{id: id, comment: text};
        self.comments.push(new_comment);
    }
}

pub struct Comment{
    id: u32,
    comment: String,
}

impl Comment {
    pub fn get_comment(&self) -> String{
        let output: String = format!( "ID: {} -- {}", self.id, &self.comment);
        output
    }
}