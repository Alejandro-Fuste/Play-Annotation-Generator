# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_65`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_65/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 42 |
| Player Tracks | 42 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 123 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Segment 'Action_BlockPunt' for track '11' has invalid range: start=74, end=35. Clamping end to start.
> - Action 'Action_None' range [8-268] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-137] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-137] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [8-32] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [34-35] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-54] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-93] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-101] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-121] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-160] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-166] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-329] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-63] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-134] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-199] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [207-211] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-329] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-199] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-224] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-154] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_SecureRecovery' range [155-162] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-54] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-329] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-55] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-35] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-213] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [60-80] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [85-117] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [120-203] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-45] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-323] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-40] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-107] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-171] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-186] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-254] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [257-295] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [297-304] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [8-37] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-99] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-109] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [8-74] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-98] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-208] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [63-65] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-137] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-89] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-242] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [104-249] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-133] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-147] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-162] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-177] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-244] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-249] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-270] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-124] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-127] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-182] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-203] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-132] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-149] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-222] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-175] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-169] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-173] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-208] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-192] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-216] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [218-232] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-242] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-252] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-270] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-300] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [314-317] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-198] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-264] for track '35' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [266-279] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-213] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-215] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-320] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-295] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-314] for track '41' has 1 frames without a visible bounding box.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.