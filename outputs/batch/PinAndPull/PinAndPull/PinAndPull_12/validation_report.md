# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PinAndPull_12`
- **Input XML**: `outputs/batch/PinAndPull/PinAndPull/PinAndPull_12/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PinAndPull.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 127 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 479 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 26: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - Row 26: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 479 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '8' (LG) duration 229 frames exceeds threshold 90 frames [start=21, end=249].
> - Action 'Action_None' range [201-362] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [201-301] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-331] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-286] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-479] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-284] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-347] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-356] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-336] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-369] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-373] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [21-224] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [228-235] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [238-240] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [248-249] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-362] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-406] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-234] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-297] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-282] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-389] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-251] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [209-255] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-287] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [321-407] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [421-423] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-336] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [339-340] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-365] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-479] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-367] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [209-282] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-288] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-341] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-345] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-360] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [373-392] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [396-479] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-315] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [238-295] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-200] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-222] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-228] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-341] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [343-345] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-360] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-479] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-53] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-85] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-260] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-360] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-282] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [284-296] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-303] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-307] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-315] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [317-341] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [343-358] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [371-422] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-362] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-381] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [383-394] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [396-398] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [400-403] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [415-477] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [292-388] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-394] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [402-407] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [410-413] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-330] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [333-365] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [368-409] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [413-467] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [321-388] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-407] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [410-425] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-479] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [408-409] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [432-433] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [448-450] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [453-454] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [470-473] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [464-477] for track '37' has 3 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.