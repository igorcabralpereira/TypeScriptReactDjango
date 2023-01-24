import * as C from './styles';
import { Item } from '../../types/Item'
import { TableItem } from '../TableItem'


// quando preciso receber uma Propriedade de uma lista(Props da lista)
// em um componente(C.Table e C.TableHeadColumn), é preciso criar um type para ele.
type Props = {
    list: Item[];
    //setItem: Dispatch<SetStateAction<Item[]>>;
}

// Aqui é onde eu pego minha Lista do tipo Props
export const TableArea = ({ list }: Props) => {

    return (
        <C.Table>
            {/* C.Table e C.TableHeadColumn é um componente criado */}
            <thead>
                <tr>
                    <C.TableHeadColumn width={100}>Data</C.TableHeadColumn>
                    <C.TableHeadColumn width={180}>Categoria</C.TableHeadColumn>
                    <C.TableHeadColumn width={100}>Título</C.TableHeadColumn>
                    <C.TableHeadColumn width={180}>Valor</C.TableHeadColumn>
                </tr>

            </thead>
            <tbody>
                {/*  Props da lista */}
                {list.map((item, index) => (

                    <TableItem key={index} item={item} />

                ))}

            </tbody>

        </C.Table>
    );
}