# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_26`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_26/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 54: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_Handoff' range [76-80] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [83-86] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [88-108] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-155] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-108] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [109-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-99] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-94] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-90] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-98] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-175] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-179] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-142] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-152] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [52-92] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [47-150] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-123] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-154] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [52-64] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [66-88] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [100-124] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-100] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-104] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-142] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [52-72] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [74-78] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [89-93] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [95-104] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [108-111] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-62] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-130] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-203] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-37] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-49] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-147] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-162] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-167] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-145] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-152] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-170] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-179] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-163] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [165-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-201] for track '29' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.