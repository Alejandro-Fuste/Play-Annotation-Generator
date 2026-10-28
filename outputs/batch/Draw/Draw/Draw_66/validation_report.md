# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_66`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_66/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Resolved action overlap for track '6' (C): higher_priority='Action_BallSnap' [34–48], lower_priority='Action_PassBlock' annotated_start=37, effective_Action_PassBlock_start=49.
> - Action 'Action_None' range [34-323] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [327-329] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-339] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-127] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-176] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-94] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-145] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [37-64] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [74-83] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-258] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [34-197] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-286] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-75] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-79] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-188] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [37-73] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [76-96] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-114] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-159] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [164-177] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-197] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-262] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-128] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-182] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-156] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-125] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-149] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-183] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [34-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-83] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-188] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-194] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-115] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [119-170] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-223] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-246] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [248-254] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-262] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-389] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-211] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-237] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [240-241] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-268] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-342] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-325] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-355] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [366-389] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-323] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-373] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-351] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-362] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-368] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-326] for track '24' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.