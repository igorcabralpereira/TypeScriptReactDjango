import styled from 'styled-components';

export const TableLine = styled.tr`
    background-color: #f8f8f8;
    border: 1px solid #ddd;
    padding: .35em;

`;

export const TableColumn = styled.td`

`;

export const Title = styled.div`

`;



export const Category = styled.div<{ color: string }>`
    display: inline-block;
    padding: 5px 10px;
    border-radius: 5px;
    color: #FFF;
    background-color: ${props => props.color};

`;

export const Value = styled.div<{ color: string }>`
    color: ${props => props.color};
    font-weight: bold;
    text-align: center;


`;

export const ButtonUpdate = styled.button`
    width: 100%;
    height: 30px;
    border: 1px solid lightblue;
    border-radius: 5px;
    background-color: lightblue;
    color: black;
    cursor: pointer;

    &:hover {
        background-color: blue;
        color: white;
    }
`;

export const ButtonDelete = styled.button`
    width: 100%;
    height: 30px;
    border: 1px solid #bd111c;
    border-radius: 5px;
    background-color: #bd111c;
    color: white;
    cursor: pointer;

    &:hover {
        background-color: red;
        color: white;
    }
`;

export const InputTitle = styled.div`
    font-weight: bold;
    margin-bottom: 5px;
`;