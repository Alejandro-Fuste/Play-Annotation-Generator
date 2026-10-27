# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_60`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_60/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 59 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 122: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [18-150] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [50-131] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-49] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-145] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-99] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-74] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [18-40] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-55] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-46] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-50] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-61] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-51] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-82] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [21-40] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-150] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-28] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-36] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-150] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [28-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-37] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-42] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-150] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-97] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-100] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-150] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-128] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-115] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-150] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '26' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
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