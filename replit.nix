k{ pkgs }: {
  repl = {
    language = "python";
    run = "python manage.py runserver 0.0.0.0:$PORT";
  };
}