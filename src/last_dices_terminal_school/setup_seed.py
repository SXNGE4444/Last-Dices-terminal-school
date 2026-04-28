from last_dices_terminal_school.services.seed_setup import SeedSetupService


def main() -> None:
    counts = SeedSetupService().run()
    print("[LAST DICES] seed setup complete")
    for k, v in counts.items():
        print(f"- {k}: {v}")


if __name__ == "__main__":
    main()
