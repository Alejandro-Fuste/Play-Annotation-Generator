# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_362`
- **Input XML**: `outputs/batch/Power/Power/Power_362/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [14-111] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-171] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-192] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-140] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-162] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-172] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-206] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-112] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-126] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-129] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-210] for track '3' has 9 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-126] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-130] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-210] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-172] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-203] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-206] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-109] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [110-136] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-109] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [110-114] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [119-128] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '8' starts at frame 172, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [172-172] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-114] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-134] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-157] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-147] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-28] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-45] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-23] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-107] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-139] for track '12' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-152] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-157] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-15] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [110-139] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [172-197] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-79] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-154] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-173] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-209] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-192] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-208] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-176] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-183] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-184] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-200] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-209] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-193] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-204] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-210] for track '23' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.