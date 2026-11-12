# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_46`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_46/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [85–97], lower_priority='Action_ZoneBlock' annotated_start=88, effective_Action_ZoneBlock_start=98.
> - Action 'Action_None' range [85-151] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-157] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [88-105] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-167] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-171] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-122] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-159] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-171] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-91] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-174] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [109-123] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [127-130] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-175] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-228] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-265] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-139] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-137] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-169] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [94-103] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-106] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-144] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-182] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-235] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-152] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-186] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-209] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-201] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-244] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-249] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-202] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-214] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '31' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.