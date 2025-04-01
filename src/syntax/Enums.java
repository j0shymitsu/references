package syntax;

import java.util.ArrayList;

public class Enums
{
    static ArrayList<ClothingItem> allClothes = new ArrayList<>();

    public static void main(String[] args)
    {
        ClothingItem tShirt = new ClothingItem("black T-shirt", Category.MENS, 1599);
        ClothingItem skirt = new ClothingItem("blue skirt", Category.WOMENS, 2599);
        ClothingItem tights = new ClothingItem("grey tights", Category.WOMENS, 499);
        ClothingItem dress = new ClothingItem("red dress", Category.WOMENS, 3499);
        ClothingItem jeans = new ClothingItem("kids jeans", Category.CHILDRENS, 699);

        allClothes.add(tShirt);
        allClothes.add(skirt);
        allClothes.add(tights);
        allClothes.add(dress);

        ArrayList<ClothingItem> womensClothes = womensClothes();
        for (ClothingItem item : womensClothes)
        {
            System.out.println(item.getName() + ": " + item.getPrice());
        }
    }

    static class ClothingItem
    {
        // ivar
        final private String name;
        final private Category category;
        private int price;

        // constructor
        public ClothingItem(String name, Category category, int price)
        {
            this.name = name;
            this.category = category;
            this.price = price;
        }

        // getters
        public String getName()
        {
            return name;
        }

        public Category getCategory()
        {
            return category;
        }

        public int getPrice()
        {
            return price;
        }
    }

    static ArrayList<ClothingItem> womensClothes()
    {
        ArrayList<ClothingItem> womens = new ArrayList<>();

        for (ClothingItem clothingItem : allClothes)
        {
            if (clothingItem.getCategory() == Category.WOMENS)
            {
                womens.add(clothingItem);
            }
        }

        return womens;
    }
}





