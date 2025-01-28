use borsh::{BorshDeserialize, BorshSerialize};

#[derive(BorshSerialize, BorshDeserialize)]
pub struct Trade {
    pub amount: u64,
    pub price: u64,
    pub timestamp: i64,
}

#[derive(BorshSerialize, BorshDeserialize)]
pub struct Model {
    pub version: u32,
    pub data: Vec<u8>,
}
