# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_35`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_35/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 102 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 388 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 72: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 72: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 388 as fallback play end.
> - Action 'Action_PreSnap' range [0-358] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-288] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-226] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-308] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-351] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-77] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-81] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-265] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-93] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-105] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-185] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-248] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-251] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-77] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-81] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-198] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [199-219] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [231-363] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-310] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-343] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [345-372] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-371] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-171] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-175] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-185] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-193] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-233] for track '12' has 7 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-320] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [328-355] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-180] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-195] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-198] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-209] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-221] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-241] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-192] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-249] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-276] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-279] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-290] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-295] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-334] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-388] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [164-192] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [200-206] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [216-223] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-235] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-388] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-189] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-251] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-205] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-267] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-319] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-14] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-73] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-97] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-100] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-105] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-109] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-137] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-140] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-154] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-157] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-163] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [164-166] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [168-169] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-340] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-277] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-304] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [276-343] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [346-363] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [370-371] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [376-377] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-288] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-293] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-314] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-322] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-333] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-337] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [321-323] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [331-387] for track '29' has 2 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.