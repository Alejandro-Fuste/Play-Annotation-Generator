# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_352`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_352/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 66 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_BallCarry' range [110-158] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [67-140] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [143-144] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-161] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-175] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-93] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-161] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [67-115] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-197] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [86-104] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-196] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-208] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-95] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [64-128] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-92] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-104] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-127] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-91] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-104] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-127] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-128] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-167] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-193] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-210] for track '24' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.