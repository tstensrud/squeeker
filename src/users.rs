use crate::squeek;

pub struct User<'a> {
    pub id: u32,
    pub name: &'a str,
    pub email: &'a str,
    pub age: u8,
    pub squeeks: Vec<squeek::Squeek<'a>>,
}

impl<'a> User<'a> {
    pub fn get_id(&self) -> u32{
        return self.id;
    }
    
    pub fn get_name(&self) -> &str {
        return &self.name;
    }

    pub fn get_email(&self) -> &str {
        return self.email;
    }

    pub fn get_age(&self) -> u8 {
        return self.age;
    }

    pub fn get_squeeks(&self) -> &Vec<squeek::Squeek> {
        return &self.squeeks;
    }
}
