use solana_program::program_error::ProgramError;

pub enum SaitInstruction {
    ExecuteTrade { amount: u64, price: u64 },
    UpdateModel { model_data: Vec<u8> },
}

impl SaitInstruction {
    pub fn unpack(input: &[u8]) -> Result<Self, ProgramError> {
        let (&tag, rest) = input.split_first().ok_or(ProgramError::InvalidInstructionData)?;
        match tag {
            0 => {
                let (amount, price) = rest.split_at(8);
                Ok(Self::ExecuteTrade {
                    amount: u64::from_le_bytes(amount.try_into().unwrap()),
                    price: u64::from_le_bytes(price.try_into().unwrap()),
                })
            }
            1 => Ok(Self::UpdateModel {
                model_data: rest.to_vec(),
            }),
            _ => Err(ProgramError::InvalidInstructionData),
        }
    }
}
