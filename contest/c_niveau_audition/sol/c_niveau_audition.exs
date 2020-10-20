# Solution by Thomas Lacroix

read_int_list = fn ->
  IO.read(:stdio, :line) |> String.trim() |> String.split(" ") |> Stream.map(&String.to_integer/1)
end

_nb_rows = IO.read(:stdio, :line)
row_capacities = read_int_list.() |> Stream.with_index()
_nb_spectators = IO.read(:stdio, :line)
hearing_levels = read_int_list.() |> Enum.frequencies()

case Enum.reduce_while(
       row_capacities,
       {hearing_levels, 0},
       fn {row_capacity, i}, {hearing_levels, remaining_seats} = _acc ->
         row = i + 1
         {nb_persons, new_levels} = Map.pop(hearing_levels, row, 0)

         if row_capacity + remaining_seats >= nb_persons do
           {:cont, {new_levels, remaining_seats + (row_capacity - nb_persons)}}
         else
           {:halt, :impossible}
         end
       end
     ) do
  :impossible ->
    IO.puts("IMPOSSIBLE")

  {hearing_levels, remaining_seats} ->
    remaining_people = Map.values(hearing_levels) |> Enum.sum()
    IO.puts(if remaining_seats >= remaining_people, do: "POSSIBLE", else: "IMPOSSIBLE")
end
