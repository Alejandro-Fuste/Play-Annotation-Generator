# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_16`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_16/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 66 |
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
> - Action 'Action_None' range [20-88] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-139] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-295] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-304] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' for track '3' starts at frame 90, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [90-147] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [154-166] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-75] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [71-123] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [125-170] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [24-132] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-114] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-129] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-160] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-329] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [195-308] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-329] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-57] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-329] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-19] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-194] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-140] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-146] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-166] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-182] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-196] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-188] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-258] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [298-304] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-329] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.