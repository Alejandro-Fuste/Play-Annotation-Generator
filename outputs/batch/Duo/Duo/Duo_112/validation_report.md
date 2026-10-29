# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_112`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_112/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 268 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 226: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 268 as fallback play end.
> - Segment 'Action_BlockSecondLevel' for track '21' has invalid range: start=156, end=127. Clamping end to start.
> - Action 'Action_PreSnap' range [0-244] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-152] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-169] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-243] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-267] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-152] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-245] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-251] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-156] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-167] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-122] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-195] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-240] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-152] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-268] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-169] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-177] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-190] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-201] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-268] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-45] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-94] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-100] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-112] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-243] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-18] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-22] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [140-200] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-215] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-221] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-231] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-89] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-139] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [140-159] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-53] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-135] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-251] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-259] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-268] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-76] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [201-268] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-123] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-127] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-120] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-123] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-127] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-185] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-193] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-222] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-226] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-143] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-258] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-232] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-175] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-178] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-221] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-236] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-258] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-268] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-221] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-228] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [231-237] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-241] for track '26' has 1 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.