import argparse
from datetime import date

from . import storage

TOKEN_VALUE = 20

def add_machine(args):
    data = storage.load_data()
    next_id = max([m['id'] for m in data['machines']], default=0) + 1
    machine = {'id': next_id, 'name': args.name}
    data['machines'].append(machine)
    storage.save_data(data)
    print(f"Added machine {next_id}: {args.name}")


def cash_in(args):
    data = storage.load_data()
    promos = data.get('promotions', {})
    tokens = promos.get(str(args.amount))
    if tokens is None:
        tokens = args.amount // TOKEN_VALUE
    record = {
        'date': str(date.today()),
        'cash': args.amount,
        'tokens': tokens
    }
    data['cash_ins'].append(record)
    storage.save_data(data)
    print(f"Cash in {args.amount} -> {tokens} tokens")


def stock(args):
    data = storage.load_data()
    entry = {
        'machine_id': args.machine_id,
        'date': str(date.today()),
        'quantity': args.quantity,
        'cost_per_unit': args.cost
    }
    data['stock_entries'].append(entry)
    storage.save_data(data)
    print(
        f"Stocked machine {args.machine_id} with {args.quantity} units at {args.cost} each"
    )


def play(args):
    data = storage.load_data()
    record = {
        'machine_id': args.machine_id,
        'date': str(date.today()),
        'tokens_used': args.tokens,
        'rewards_taken': args.rewards
    }
    data['plays'].append(record)
    storage.save_data(data)
    baht_value = args.tokens * TOKEN_VALUE
    if args.rewards:
        avg_price = baht_value / args.rewards
        print(
            f"Recorded play: {args.tokens} tokens ({baht_value} baht) -> {args.rewards} rewards (~{avg_price:.2f} baht each)"
        )
    else:
        print(
            f"Recorded play: {args.tokens} tokens ({baht_value} baht) -> no rewards"
        )


def report_cash(args):
    data = storage.load_data()
    total = sum(
        r['cash'] for r in data['cash_ins'] if r['date'] == args.date
    )
    print(f"Cash in on {args.date}: {total} baht")


def main(argv=None):
    parser = argparse.ArgumentParser(description='Claw machine backend CLI')
    sub = parser.add_subparsers()

    m_add = sub.add_parser('add-machine', help='Add a new machine')
    m_add.add_argument('name')
    m_add.set_defaults(func=add_machine)

    cash = sub.add_parser('cash-in', help='Record cash exchange for tokens')
    cash.add_argument('amount', type=int)
    cash.set_defaults(func=cash_in)

    st = sub.add_parser('stock', help='Stock a machine with rewards')
    st.add_argument('machine_id', type=int)
    st.add_argument('quantity', type=int)
    st.add_argument('cost', type=float)
    st.set_defaults(func=stock)

    pl = sub.add_parser('play', help='Record a play result')
    pl.add_argument('machine_id', type=int)
    pl.add_argument('tokens', type=int)
    pl.add_argument('rewards', type=int)
    pl.set_defaults(func=play)

    rc = sub.add_parser('report-cash', help='Report cash-in for a date')
    rc.add_argument('date', help='YYYY-MM-DD')
    rc.set_defaults(func=report_cash)

    args = parser.parse_args(argv)
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
