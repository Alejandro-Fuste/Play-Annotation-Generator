# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_45`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_45/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 136 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [128–144], lower_priority='Action_ZoneBlock' annotated_start=130, effective_Action_ZoneBlock_start=145.
> - Action 'Action_None' range [128-200] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-292] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [296-311] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [128-153] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-162] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-336] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-449] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [128-144] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [145-153] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [157-161] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [167-195] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [197-207] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-325] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-374] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [128-362] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [367-374] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [378-387] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [390-398] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-433] for track '7' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [438-442] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [130-135] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [138-162] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [169-178] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [181-182] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [184-207] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-312] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-329] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-341] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [347-365] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-382] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-133] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-153] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-162] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-197] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-437] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [440-447] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-267] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-360] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [128-345] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-392] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [177-195] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-202] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-449] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-163] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [177-309] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [130-135] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [138-152] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [157-162] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [167-181] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [184-189] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-329] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-363] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [365-368] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-383] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-133] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-153] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-162] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-178] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-262] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-351] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [130-133] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [141-153] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [155-162] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [165-180] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [185-190] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-268] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [270-324] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-340] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [346-445] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [130-135] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [138-153] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [155-162] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [168-173] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-127] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-133] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-153] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [155-162] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-189] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [192-195] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-219] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-449] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [210-361] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [365-368] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [372-376] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-218] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-365] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-279] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-314] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-322] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [331-337] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [342-345] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-363] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [374-392] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [399-403] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [420-422] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [430-431] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [437-440] for track '28' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.