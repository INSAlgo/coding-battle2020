readInt = fn -> IO.read(:stdio, :line) |> String.trim() |> String.to_integer() end

nbbillets = readInt.()
prix1 = readInt.()
prix2 = readInt.()
prix3 = readInt.()

cond do
  nbbillets > 200 ->
    nbbillets = nbbillets - 200
    IO.puts(nbbillets * prix3 + 100 * prix2 + 100 * prix1)

  nbbillets > 100 ->
    nbbillets = nbbillets - 100
    IO.puts(nbbillets * prix2 + 100 * prix1)

  true ->
    IO.puts(nbbillets * prix1)
end
