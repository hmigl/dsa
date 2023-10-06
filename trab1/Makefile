SHELL := /bin/sh

OBJDIR   := objdir

CXXFLAGS += -I./include -Wall -Wextra -std=c++17
LDFLAGS  +=
LDLIBS   +=
CXX      := g++
LINK.cpp := $(filter-out $(CXXFLAGS), $(LINK.cpp))

SRCS     := main.cpp Node.cpp LinkedList.cpp CommandHandler.cpp
OBJS     := $(addprefix $(OBJDIR)/, $(SRCS:.cpp=.o))
DEPS     := $(OBJS:.o=.d)
NAME     := trab1

vpath %.cpp src

.PHONY: all clean fclean re options

all: $(NAME)

$(NAME): $(OBJS)
	$(LINK.cpp) $(LDLIBS) $(OUTPUT_OPTION) $^

$(OBJDIR)/%.o: %.cpp Makefile | $(OBJDIR)
	$(COMPILE.cpp) $(OUTPUT_OPTION) -MMD -MP $<

-include $(DEPS)

$(OBJDIR):
	mkdir $@

clean:
	$(RM) $(OBJS) $(DEPS)

fclean: clean
	$(RM) $(NAME)

re: fclean all

options:
	@echo "$(NAME) build options:"
	@echo "CXXFLAGS      = $(CXXFLAGS)"
	@echo "LDFLAGS       = $(LDFLAGS)"
	@echo "LDLIBS        = $(LDLIBS)"
	@echo "CXX           = $(CXX)"
