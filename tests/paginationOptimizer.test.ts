import { PaginationOptimizer } from "../src/paginationOptimizer";
import { CursorManager } from "../src/cursorManager";

describe("API response pagination optimizer", () => {
    test("should process valid input", () => {
        const obj = new PaginationOptimizer();
        expect(obj.process({ key: "val" })).not.toBeNull();
    });
    test("should handle null", () => {
        const obj = new PaginationOptimizer();
        expect(obj.process(null)).toBeNull();
    });
    test("should track stats", () => {
        const obj = new PaginationOptimizer();
        obj.process({ x: 1 });
        expect(obj.getStats().processed).toBe(1);
    });
    test("support should work", () => {
        const obj = new CursorManager();
        expect(obj.process({ data: "test" })).not.toBeNull();
    });
});
